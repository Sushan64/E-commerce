
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
document.addEventListener('DOMContentLoaded', function() {
      const tabLinks = document.querySelectorAll('.tablinks');
      const tabContents = document.querySelectorAll('.tabcontent');

      function openItem(itemName, clickedButton) {
        tabContents.forEach(function(content) {
          content.classList.add('hidden');
        });

        tabLinks.forEach(function(link) {
          link.classList.remove('border-blue-500', 'text-blue-500');
          link.classList.add('text-gray-600', 'border-transparent');
        });

        const targetContent = document.getElementById(itemName);
        if (targetContent) {
          targetContent.classList.remove('hidden');
        }

        if (clickedButton) {
          clickedButton.classList.remove('text-gray-600', 'border-transparent');
          clickedButton.classList.add('border-blue-500', 'text-blue-500');
        }
      }

      tabLinks.forEach(function(link) {
        link.addEventListener('click', function() {
          const itemName = this.getAttribute('data-item');
          openItem(itemName, this);
        });
      });

      // Trigger the first tab on load
      if (tabLinks.length > 0) {
        const firstCity = tabLinks[0].getAttribute('data-item');
        openItem(firstCity, tabLinks[0]);
      }
    });