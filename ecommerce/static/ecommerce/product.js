
// Quantity handling
const quantity = document.getElementById('quantity');
const decrease = document.getElementById('decrease');
const increase = document.getElementById('increase');

decrease.addEventListener('click', () => {
  let value = parseInt(quantity.value);
  if (value > 1) {
    quantity.value = value - 1;
  }
});

increase.addEventListener('click', () => {
  let value = parseInt(quantity.value);
  quantity.value = value + 1;
});

// Tab switching
function switchTab(tabId) {
  // Hide all tabs
  document.querySelectorAll('.tab-content > div').forEach(tab => {
    tab.classList.add('hidden');
    tab.classList.remove('block');
  });
  
  // Show selected tab
  const selectedTab = document.getElementById(tabId);
  selectedTab.classList.remove('hidden');
  selectedTab.classList.add('block');
  
  // Update tab buttons
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('text-indigo-600', 'border-b-2', 'border-indigo-600');
    btn.classList.add('text-gray-500');
  });
  
  document.getElementById(`${tabId}-tab`).classList.add('text-indigo-600', 'border-b-2', 'border-indigo-600');
  document.getElementById(`${tabId}-tab`).classList.remove('text-gray-500');
}
