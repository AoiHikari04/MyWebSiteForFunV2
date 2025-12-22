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

// Global variable to store tool data
let toolCards = [];

// Function to handle navigation with JS
function navigateTo(url) {
    window.location.href = url;
}

// Fetch tool data from API
async function loadToolData() {
    try {
        const response = await fetch('/api/tools');
        toolCards = await response.json();
        console.log('Tool data loaded:', toolCards);
    } catch (error) {
        console.error('Failed to load tool data:', error);
        // Fallback to default data if API fails
        toolCards = [
            { "id": "n8n", "name": "n8n Workflow Automation", "url": "https://n8n.aoihikari.my" },
            { "id": "a1111", "name": "Automatic1111", "url": "https://a1111.example.com", "outputsUrl": "https://a1111.example.com/outputs" },
            { "id": "video", "name": "Video Generation", "url": "https://runwayml.com" }
        ];
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', async function() {
    await loadToolData();
    
    // Event listeners
    document.getElementById('open-workflows').addEventListener('click', function(e) {
        e.preventDefault();
        const n8nTool = toolCards.find(tool => tool.id === 'n8n');
        if (n8nTool) {
            navigateTo(n8nTool.url);
        }
    });

    document.getElementById('launch-webui').addEventListener('click', function(e) {
        e.preventDefault();
        const a1111Tool = toolCards.find(tool => tool.id === 'a1111');
        if (a1111Tool) {
            navigateTo(a1111Tool.url);
        }
    });

    document.getElementById('outputs-link').addEventListener('click', function(e) {
        e.preventDefault();
        const a1111Tool = toolCards.find(tool => tool.id === 'a1111');
        if (a1111Tool && a1111Tool.outputsUrl) {
            navigateTo(a1111Tool.outputsUrl);
        }
    });

    document.getElementById('generate-video').addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('exit-modal').classList.remove('hidden');
    });

    document.getElementById('cancel-exit').addEventListener('click', function() {
        document.getElementById('exit-modal').classList.add('hidden');
    });

    document.getElementById('confirm-exit').addEventListener('click', function() {
        const videoTool = toolCards.find(tool => tool.id === 'video');
        if (videoTool) {
            navigateTo(videoTool.url);
        }
    });
});