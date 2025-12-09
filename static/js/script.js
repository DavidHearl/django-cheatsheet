window.onscroll = function() {
    const button = document.getElementById("backToTop");
    if (document.documentElement.scrollTop > 200) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
};

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Copy functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        // Success notification could be added here
    }, (err) => {
        console.error('Could not copy text: ', err);
    });
}

// Initialize copy buttons for code blocks
function initializeCopyButtons() {
    // Remove existing copy buttons first
    const existingButtons = document.querySelectorAll('.copy-button');
    existingButtons.forEach(button => button.remove());
    
    // Regular code blocks - line by line copy buttons
    const regularCodeBlocks = document.querySelectorAll('pre:not(.file-content) code');
    
    regularCodeBlocks.forEach(function(codeBlock) {
        const lines = codeBlock.textContent.trim().split('\n');
        codeBlock.innerHTML = '';
        
        lines.forEach(function(line, index) {
            if (line.trim() === '' && index === lines.length - 1) return;
            
            const lineDiv = document.createElement('span');
            lineDiv.className = 'code-line';
            lineDiv.textContent = line;
            
            if (line.trim() !== '') {
                const copyButton = document.createElement('button');
                copyButton.className = 'copy-button';
                copyButton.textContent = 'Copy';
                copyButton.onclick = function() {
                    copyToClipboard(line.trim());
                    copyButton.textContent = 'Copied!';
                    setTimeout(() => {
                        copyButton.textContent = 'Copy';
                    }, 1000);
                };
                lineDiv.appendChild(copyButton);
            }
            
            codeBlock.appendChild(lineDiv);
            
            if (index < lines.length - 1) {
                codeBlock.appendChild(document.createElement('br'));
            }
        });
    });
    
    // File content blocks - one copy button for the entire block
    const fileContentBlocks = document.querySelectorAll('pre.file-content');
    
    fileContentBlocks.forEach(function(pre) {
        const codeElement = pre.querySelector('code');
        if (!codeElement) return;
        
        // Create a single copy button for the entire block
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button file-content-copy';
        copyButton.textContent = 'Copy';
        
        // Get the entire text content
        const textToCopy = codeElement.textContent.trim();
        
        // Add click event
        copyButton.onclick = function() {
            copyToClipboard(textToCopy);
            copyButton.textContent = 'Copied!';
            setTimeout(() => {
                copyButton.textContent = 'Copy';
            }, 1000);
        };
        
        pre.appendChild(copyButton);
    });
}


document.addEventListener('DOMContentLoaded', function() {
    initializeCopyButtons();
});