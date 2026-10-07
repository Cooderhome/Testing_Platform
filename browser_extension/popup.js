const API_BASE_URL = 'http://localhost:8000/api';

document.addEventListener('DOMContentLoaded', () => {
    chrome.storage.local.get(['token', 'username', 'criticModeActive'], (result) => {
        if (result.token) {
            showMainView(result.username);
            loadSessions(result.token);
            if (result.criticModeActive) {
                document.getElementById('start-critic-btn').style.display = 'none';
                document.getElementById('stop-critic-btn').style.display = 'block';
            }
        } else {
            document.getElementById('login-view').style.display = 'block';
        }
    });

    document.getElementById('login-btn').addEventListener('click', async () => {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        try {
            const response = await fetch(`${API_BASE_URL}/auth/login/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            const data = await response.json();
            
            if (response.ok) {
                chrome.storage.local.set({ token: data.token, username: data.username });
                document.getElementById('login-view').style.display = 'none';
                showMainView(data.username);
                loadSessions(data.token);
            } else {
                document.getElementById('login-error').innerText = data.error || 'Login failed';
            }
        } catch (err) {
            document.getElementById('login-error').innerText = 'Connection error';
        }
    });

    document.getElementById('logout-btn').addEventListener('click', () => {
        chrome.storage.local.clear();
        document.getElementById('main-view').style.display = 'none';
        document.getElementById('login-view').style.display = 'block';
        chrome.runtime.sendMessage({ action: "stop_critic_mode" });
    });

    document.getElementById('start-critic-btn').addEventListener('click', () => {
        const sessionId = document.getElementById('session-select').value;
        if (!sessionId) {
            alert('Please select a testing session');
            return;
        }

        chrome.permissions.request({
            origins: ['<all_urls>']
        }, (granted) => {
            if (granted) {
                chrome.storage.local.set({ activeSession: sessionId, criticModeActive: true });
                document.getElementById('start-critic-btn').style.display = 'none';
                document.getElementById('stop-critic-btn').style.display = 'block';
                
                chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
                    if (!tabs || !tabs.length) return;
                    chrome.tabs.sendMessage(tabs[0].id, { action: "enable_critic_mode" }, (response) => {
                        if (chrome.runtime.lastError) {
                            alert("Please hard-refresh the web page first! The extension was updated and needs the page to reload.");
                            chrome.storage.local.set({ criticModeActive: false });
                            document.getElementById('start-critic-btn').style.display = 'block';
                            document.getElementById('stop-critic-btn').style.display = 'none';
                        }
                    });
                });
            } else {
                alert("AppCritic requires universal site access to take screenshots! Please accept the prompt or enable it in Extension Settings.");
            }
        });
    });

    document.getElementById('stop-critic-btn').addEventListener('click', () => {
        chrome.storage.local.set({ criticModeActive: false });
        document.getElementById('start-critic-btn').style.display = 'block';
        document.getElementById('stop-critic-btn').style.display = 'none';
        
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            if (!tabs || !tabs.length) return;
            chrome.tabs.sendMessage(tabs[0].id, { action: "disable_critic_mode" }, (response) => {
                if (chrome.runtime.lastError) {
                    console.log("Content script not active or already disabled");
                }
            });
        });
    });
});

function showMainView(username) {
    document.getElementById('main-view').style.display = 'block';
    document.getElementById('user-display').innerText = username;
}

async function loadSessions(token) {
    try {
        const response = await fetch(`${API_BASE_URL}/sessions/`, {
            headers: { 'Authorization': `Token ${token}` }
        });
        if (response.ok) {
            const sessions = await response.json();
            const select = document.getElementById('session-select');
            sessions.forEach(s => {
                const opt = document.createElement('option');
                opt.value = s.id;
                opt.innerText = s.title;
                select.appendChild(opt);
            });
        }
    } catch (err) {
        console.error('Failed to load sessions', err);
    }
}
