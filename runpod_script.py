import os
from dotenv import load_dotenv
import runpod
import base64
import time
from pathlib import Path
import json


load_dotenv()

prompt_text = "wide angle cinematic landscape, samurai battle, sword fight, cinematic battle shot, samurai holding katana, two samurai, insane lighting, high resolution, sunset lighting, sunset sky, sunset settings, under the cherry blossoms tree, epic stand off, high contrast, cinematic masterpiece, dramatic lighting, 8K wallpaper"


payload = {
  "input": {
  "prompt": prompt_text,
  "negative_prompt": "blurry, low quality, low resolution, pixelated, bad anatomy, bad hands, extra fingers, missing fingers, deformed face, distorted eyes, watermark, text, logo, (worst quality, low quality:2), monochrome, zombie, distorted, out of frame, cropped, duplicate, split image, double landscape",
  "seed": -1,
  "subseed": -1,
  "subseed_strength": 0,
  "batch_size": 1,
  "n_iter": 1,
  "steps": 35,
  "cfg_scale": 7,
  "width": 1344, 
  "height": 768,
  "sampler_name": "DPM++ 2M",
  "restore_faces": False,
  "tiling": False,
  "do_not_save_samples": False,
  "do_not_save_grid": False,
  "enable_hr": True,
  "hr_scale": 1.5,
  "hr_upscaler": "R-ESRGAN 4x+",
  "hr_second_pass_steps": 15,
  "hr_resize_x": 0,
  "hr_resize_y": 0,
  "denoising_strength": 0.4
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


