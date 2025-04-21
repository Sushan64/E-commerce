const searchIcon = document.getElementById('search-icon');
    const searchBarContainer = document.getElementById('search-bar-container');
    const searchInput = document.getElementById('search-input');
    const toggleBtn = document.getElementById('search-toggle-btn');
    const toggleIcon = toggleBtn.querySelector('i');

    let isSearchVisible = false;

    function toggleSearchBar() {
      isSearchVisible = !isSearchVisible;
      if (isSearchVisible) {
        searchBarContainer.classList.remove('hidden');
        searchBarContainer.classList.add('flex');
        searchInput.focus();
      } else {
        searchBarContainer.classList.remove('flex');
        searchBarContainer.classList.add('hidden');
        searchInput.value = '';
        toggleIcon.className = 'bi bi-x';
      }
    }

    searchIcon.addEventListener('click', () => {
      toggleSearchBar();
    });

    toggleBtn.addEventListener('click', () => {
      if (searchInput.value.trim() === '') {
        toggleSearchBar();
      } else {
        alert('Searching for: ' + searchInput.value);
      }
    });

    searchInput.addEventListener('input', () => {
      toggleIcon.className = searchInput.value.trim() === '' ? 'bi bi-x' : 'bi bi-arrow-right';
    });