const API_BASE_URL = 'http://localhost:8000/api';

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "save_finding") {
        chrome.storage.local.get(['token', 'activeSession'], async (result) => {
            if (!result.token || !result.activeSession) {
                sendResponse({ success: false, error: 'Not authenticated or no active session' });
                return;
            }

            const payload = {
                testing_session: result.activeSession,
                title: request.data.title || 'Quick Note',
                description: request.data.description,
                category: request.data.category,
                severity: request.data.severity,
                page_url: request.data.page_url,
                page_title: request.data.page_title,
                element_text: request.data.element_text,
                element_tag: request.data.element_tag,
                element_selector: request.data.element_selector,
                annotation: {
                    page_url: request.data.page_url,
                    page_title: request.data.page_title,
                    selector: request.data.element_selector,
                    element_tag: request.data.element_tag,
                    element_text: request.data.element_text,
                    x: request.data.x,
                    y: request.data.y,
                    width: request.data.width,
                    height: request.data.height,
                    viewport_width: request.data.viewport_width,
                    viewport_height: request.data.viewport_height,
                    scroll_x: request.data.scroll_x,
                    scroll_y: request.data.scroll_y
                }
            };

            try {
                const response = await fetch(`${API_BASE_URL}/findings/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Token ${result.token}`
                    },
                    body: JSON.stringify(payload)
                });
                
                const data = await response.json();
                if (response.ok) {
                    sendResponse({ success: true, findingId: data.id });
                } else {
                    sendResponse({ success: false, error: JSON.stringify(data) });
                }
            } catch (err) {
                sendResponse({ success: false, error: err.toString() });
            }
        });
        return true; // async response
    } else if (request.action === "capture_screenshot") {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            if (tabs && tabs.length > 0) {
                chrome.tabs.captureVisibleTab(tabs[0].windowId, {format: "png"}, (dataUrl) => {
                    if (chrome.runtime.lastError) {
                        console.error("Screenshot error:", chrome.runtime.lastError.message);
                        sendResponse({ dataUrl: null, error: chrome.runtime.lastError.message });
                    } else {
                        sendResponse({ dataUrl: dataUrl });
                    }
                });
            } else {
                sendResponse({ dataUrl: null, error: "No active tab found" });
            }
        });
        return true;
    }
});
