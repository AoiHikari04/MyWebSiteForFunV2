import os
from dotenv import load_dotenv
import runpod
import base64
import time
from pathlib import Path
import json


load_dotenv()


payload = {
  "input": {
    "prompt": "Haruno Sakura from Naruto, cinematic anime illustration, ultra-detailed, masterpiece, best quality, 4k resolution, vibrant yet balanced colors, soft sakura pink palette, dynamic pose, expressive emerald eyes, detailed hair strands, flowing movement, ninja outfit with fine fabric texture, dramatic lighting, soft rim light, shallow depth of field, anime key visual style, studio-quality illustration, sharp focus, clean lineart, high detail background, cherry blossom petals floating, emotional and powerful atmosphere",
    "negative_prompt": "blurry, low quality, low resolution, pixelated, overexposed, underexposed, bad anatomy, bad hands, extra fingers, missing fingers, deformed face, distorted eyes, flat lighting, dull colors, oversaturated, jpeg artifacts, watermark, text, logo",
    "width": 512,
    "height": 512,
    "steps": 30,
    "sampler_name": "Euler a",
    "cfg_scale": 9
  }
}

runpod.api_key = os.getenv("API_KEY")
runpodEndpoint = os.getenv("ENDPOINT_ID")
endpoint = runpod.Endpoint(runpodEndpoint)

# Create output folder if it doesn't exist
output_folder = Path("generated_images")
output_folder.mkdir(exist_ok=True)

# Start the job
print("🚀 Requesting image...")
run_request = endpoint.run(payload)


# Initial check without blocking, useful for quick tasks
status = run_request.status()
print(f"Initial job status: {status}")

if status != "COMPLETED":
    # Polling with timeout for long-running tasks
    output = run_request.output(timeout=60)
else:
    output = run_request.output()

# Get the output
output = run_request.output()
print("✅ Job Completed!")
info = json.loads(output.get("info", "{}"))
print(f"Model used for this generation: {info.get('sd_model_name')}")

if output is None:
    print("❌ Job returned no output.")
    exit(1)

# Extract image data (RunPod endpoints may return different formats)
image_data = None

# Try different possible output formats
if isinstance(output, dict):
    image_data = output.get("image") or output.get("images", [None])[0]
elif isinstance(output, str):
    image_data = output
elif isinstance(output, list) and len(output) > 0:
    image_data = output[0]

if image_data:
    # Remove base64 prefix if present
    if isinstance(image_data, str):
        if image_data.startswith("data:image"):
            image_data = image_data.split(",")[1]
        
        # Decode and save the image
        try:
            image_bytes = base64.b64decode(image_data)
            timestamp = int(time.time())
            output_path = output_folder / f"image_{timestamp}.png"
            
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            
            print(f"✅ Image saved to: {output_path}")
        except Exception as e:
            print(f"❌ Error saving image: {e}")
else:
    print("❌ No image data found in output.")
    print(f"Output received: {output}")


