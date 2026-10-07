let isActive = false;
let overlay, hoverBox, toolbar;
let dialog;
let currentElement = null;

// Initialize on page load if active
chrome.storage.local.get(['criticModeActive'], (res) => {
    if (res.criticModeActive) {
        enableCriticMode();
    }
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "enable_critic_mode") {
        enableCriticMode();
    } else if (request.action === "disable_critic_mode") {
        disableCriticMode();
    }
});

function enableCriticMode() {
    if (isActive) return;
    isActive = true;
    
    // Create UI elements
    overlay = document.createElement('div');
    overlay.id = 'appcritic-overlay';
    
    hoverBox = document.createElement('div');
    hoverBox.className = 'appcritic-hover-box';
    overlay.appendChild(hoverBox);
    
    toolbar = document.createElement('div');
    toolbar.id = 'appcritic-toolbar';
    toolbar.innerHTML = `<span style="color:#ffc107">💡 Right-Click any element to report a bug</span> <button class="appcritic-btn" id="appcritic-stop-btn" style="margin-left:10px">STOP</button>`;
    
    document.body.appendChild(overlay);
    document.body.appendChild(toolbar);
    
    document.getElementById('appcritic-stop-btn').addEventListener('click', disableCriticMode);
    
    document.addEventListener('mousemove', onMouseMove, true);
    document.addEventListener('contextmenu', onContextMenu, true);
}

function disableCriticMode() {
    if (!isActive) return;
    isActive = false;
    chrome.storage.local.set({ criticModeActive: false });
    
    if (overlay) overlay.remove();
    if (toolbar) toolbar.remove();
    if (dialog) dialog.remove();
    
    document.removeEventListener('mousemove', onMouseMove, true);
    document.removeEventListener('contextmenu', onContextMenu, true);
}

function onMouseMove(e) {
    if (dialog && document.body.contains(dialog)) return; // Don't hover while dialog is open
    
    // We always show the hover box now to indicate what will be selected


    const target = e.target;
    // Ignore our own UI
    if (target.id === 'appcritic-overlay' || target.id === 'appcritic-toolbar' || target.closest('#appcritic-toolbar') || target.closest('#appcritic-dialog')) {
        hoverBox.style.display = 'none';
        return;
    }
    
    currentElement = target;
    const rect = target.getBoundingClientRect();
    
    hoverBox.style.display = 'block';
    hoverBox.style.top = `${rect.top}px`;
    hoverBox.style.left = `${rect.left}px`;
    hoverBox.style.width = `${rect.width}px`;
    hoverBox.style.height = `${rect.height}px`;
}

function onContextMenu(e) {
    // Ignore clicks on our UI
    if (e.target.closest('#appcritic-toolbar') || e.target.closest('#appcritic-dialog') || e.target.closest('#appcritic-overlay')) return;
    
    e.preventDefault(); // Prevent the browser's right-click menu
    e.stopPropagation();
    
    if (dialog && document.body.contains(dialog)) {
        document.body.removeChild(dialog);
    }
    
    if (toolbar) toolbar.style.display = 'none';
    const targetEl = currentElement || e.target;
    
    // Slight delay to allow UI to hide before screenshot
    setTimeout(() => {
        try {
            // Find the root element that contains the actual content
            const rootElement = document.getElementById('root') || document.documentElement;
            
            html2canvas(rootElement, { 
                useCORS: true, 
                logging: false,
                allowTaint: false,
                scale: 1, // Avoid massive images
                width: window.innerWidth,
                height: window.innerHeight,
                x: window.scrollX,
                y: window.scrollY
            }).then(canvas => {
                const screenshotDataUrl = canvas.toDataURL("image/jpeg", 0.7); // Use JPEG for smaller size
                if (toolbar) toolbar.style.display = 'flex';
                showFindingDialog(targetEl, screenshotDataUrl);
            }).catch(err => {
                console.error("html2canvas failed, falling back to native:", err);
                chrome.runtime.sendMessage({ action: "capture_screenshot" }, (response) => {
                    if (toolbar) toolbar.style.display = 'flex';
                    const screenshotDataUrl = (response && response.dataUrl) ? response.dataUrl : null;
                    showFindingDialog(targetEl, screenshotDataUrl);
                });
            });
        } catch (err) {
            console.error("Screenshot error, falling back to native:", err);
            chrome.runtime.sendMessage({ action: "capture_screenshot" }, (response) => {
                if (toolbar) toolbar.style.display = 'flex';
                const screenshotDataUrl = (response && response.dataUrl) ? response.dataUrl : null;
                showFindingDialog(targetEl, screenshotDataUrl);
            });
        }
    }, 150);
}

function getCssSelector(el) {
    if (el.id) return `#${el.id}`;
    if (el.className) return `.${el.className.trim().replace(/\s+/g, '.')}`;
    return el.tagName.toLowerCase();
}

function showFindingDialog(element, screenshotDataUrl) {
    if (dialog) dialog.remove();
    
    const rect = element.getBoundingClientRect();
    
    dialog = document.createElement('div');
    dialog.id = 'appcritic-dialog';
    dialog.innerHTML = `
        <h4 style="margin-top:0;">New Finding</h4>
        
        <label>Title</label>
        <input type="text" id="ac-title" placeholder="e.g. Button misaligned" required>

        <label>Category</label>
        <select id="ac-category">
            <option value="USABILITY">Usability</option>
            <option value="BUG">Bug</option>
            <option value="UI_UX">UI/UX</option>
            <option value="FUNCTIONAL">Functional</option>
        </select>
        
        <label>Severity</label>
        <select id="ac-severity">
            <option value="MEDIUM">Medium</option>
            <option value="HIGH">High</option>
            <option value="LOW">Low</option>
            <option value="CRITICAL">Critical</option>
        </select>
        
        <label>Observation</label>
        <textarea id="ac-description" placeholder="What did you notice?"></textarea>
        
        ${screenshotDataUrl ? `
            <label>Screenshot Attached</label>
            <div style="border:1px solid #ccc; border-radius:4px; margin-bottom:15px; max-height:120px; overflow:hidden;">
                <img src="${screenshotDataUrl}" style="width:100%; height:auto; display:block;" alt="Screenshot preview">
            </div>
        ` : `
            <div style="color:#dc3545; font-size:12px; margin-bottom:15px;">
                ⚠️ Screenshot could not be captured automatically.
            </div>
        `}
        
        <div class="actions">
            <button class="appcritic-btn" style="background:#6c757d" id="ac-cancel">Cancel</button>
            <button class="appcritic-btn" id="ac-save">Save Finding</button>
        </div>
    `;
    
    document.body.appendChild(dialog);
    
    document.getElementById('ac-cancel').addEventListener('click', () => dialog.remove());
    document.getElementById('ac-save').addEventListener('click', () => {
        const titleEl = document.getElementById('ac-title');
        const titleVal = titleEl ? titleEl.value : '';
        
        if (!titleVal) {
            alert('Please enter a title!');
            return;
        }

        const payload = {
            title: titleVal,
            description: document.getElementById('ac-description').value,
            category: document.getElementById('ac-category').value,
            severity: document.getElementById('ac-severity').value,
            page_url: window.location.href,
            page_title: document.title,
            element_text: element.innerText.substring(0, 200),
            element_tag: element.tagName.toLowerCase(),
            element_selector: getCssSelector(element),
            screenshot_data: screenshotDataUrl,
            x: rect.left,
            y: rect.top,
            width: rect.width,
            height: rect.height,
            viewport_width: window.innerWidth,
            viewport_height: window.innerHeight,
            scroll_x: window.scrollX,
            scroll_y: window.scrollY
        };
        
        document.getElementById('ac-save').innerText = 'Saving...';
        
        chrome.runtime.sendMessage({ action: "save_finding", data: payload }, (response) => {
            if (response && response.success) {
                dialog.remove();
                alert('Finding saved!');
            } else {
                alert('Error saving finding: ' + (response ? response.error : 'Unknown'));
                document.getElementById('ac-save').innerText = 'Save Finding';
            }
        });
    });
}
