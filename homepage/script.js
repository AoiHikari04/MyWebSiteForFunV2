// Tailwind CSS configuration
tailwind.config = {
    theme: {
        extend: {
            colors: {
                "n8n-pink": "#EA4B71",
                "sd-blue": "#4A90E2",
                "video-green": "#34D399"
            },
            backdropBlur: {
                'xs': '2px',
            }
        }
    }
}

// Define data at the beginning
const toolCards = [
    { "id": "n8n", "name": "n8n Workflow Automation", "url": "https://n8n.aoihikari.my" },
    { "id": "a1111", "name": "Automatic1111", "url": "https://a1111.example.com", "outputsUrl": "https://a1111.example.com/outputs" },
    { "id": "video", "name": "Video Generation", "url": "https://runwayml.com" }
];

// Function to handle navigation with JS
function navigateTo(url) {
    window.location.href = url;
}

// Event listeners
document.getElementById('open-workflows').addEventListener('click', function(e) {
    e.preventDefault();
    navigateTo(toolCards[0].url);
});

document.getElementById('launch-webui').addEventListener('click', function(e) {
    e.preventDefault();
    navigateTo(toolCards[1].url);
});

document.getElementById('outputs-link').addEventListener('click', function(e) {
    e.preventDefault();
    navigateTo(toolCards[1].outputsUrl);
});

document.getElementById('generate-video').addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('exit-modal').classList.remove('hidden');
});

document.getElementById('cancel-exit').addEventListener('click', function() {
    document.getElementById('exit-modal').classList.add('hidden');
});

document.getElementById('confirm-exit').addEventListener('click', function() {
    navigateTo(toolCards[2].url);
});