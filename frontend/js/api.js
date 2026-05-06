const API_BASE = 'http://localhost:8000';

function getToken() { return localStorage.getItem('access_token'); }
function getRole() { return localStorage.getItem('role'); }
function getUserId() { return localStorage.getItem('user_id'); }
function getUsername() { return localStorage.getItem('username'); }

function saveAuth(data) {
  localStorage.setItem('access_token', data.access_token);
  localStorage.setItem('role', data.role);
  localStorage.setItem('user_id', String(data.user_id));
  localStorage.setItem('account_id', String(data.account_id));
}

function clearAuth() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('role');
  localStorage.removeItem('user_id');
  localStorage.removeItem('account_id');
  localStorage.removeItem('username');
}

function requireAuth() {
  if (!getToken()) { window.location.href = 'index.html'; return false; }
  return true;
}

async function apiFetch(endpoint, options = {}) {
  const headers = { 'Content-Type': 'application/json', ...options.headers };
  const token = getToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const res = await fetch(`${API_BASE}${endpoint}`, { ...options, headers });

  if (res.status === 401) { clearAuth(); window.location.href = 'index.html'; return; }

  const text = await res.text();
  let data;
  try { data = JSON.parse(text); } catch { data = text; }

  if (!res.ok) {
    const msg = data?.detail || data?.message || 'Terjadi kesalahan';
    throw new Error(typeof msg === 'string' ? msg : JSON.stringify(msg));
  }
  return data;
}

/* Toast */
function showToast(message, type = 'success') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = message;
  container.appendChild(toast);
  setTimeout(() => { toast.style.opacity = '0'; toast.style.transform = 'translateX(40px)'; setTimeout(() => toast.remove(), 300); }, 3500);
}

function formatDate(d) {
  if (!d) return '-';
  const dt = new Date(d);
  return dt.toLocaleDateString('id-ID', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' });
}
