document.addEventListener('DOMContentLoaded', function() {
  const carousel = document.getElementById('carousel-container');
  const wrapper = document.getElementById('carousel-wrapper');
  const indicators = document.querySelectorAll('[data-carousel-indicator]');
  
  let currentSlide = 0;
  const slideCount = indicators.length;
  let autoPlayInterval;
  let touchStartX = 0;
  let touchEndX = 0;

  function updateSlide(index) {
    currentSlide = index;
    carousel.style.transform = `translateX(-${currentSlide * 100}%)`;
    
    indicators.forEach((indicator, i) => {
      indicator.classList.toggle('opacity-50', i !== currentSlide);
      indicator.classList.toggle('opacity-100', i === currentSlide);
    });
  }

  function nextSlide() {
    updateSlide((currentSlide + 1) % slideCount);
  }

  function startAutoPlay() {
    autoPlayInterval = setInterval(nextSlide, 3000); // Change slide every 3 seconds
  }

  function stopAutoPlay() {
    clearInterval(autoPlayInterval);
  }

  // Touch events
  wrapper.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
    stopAutoPlay();
  });

  wrapper.addEventListener('touchmove', (e) => {
    touchEndX = e.touches[0].clientX;
  });

  wrapper.addEventListener('touchend', () => {
    const difference = touchStartX - touchEndX;
    if (Math.abs(difference) > 50) {
      if (difference > 0) {
        updateSlide((currentSlide + 1) % slideCount);
      } else {
        updateSlide((currentSlide - 1 + slideCount) % slideCount);
      }
    }
    startAutoPlay();
  });

  // Indicator clicks
  indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
      updateSlide(index);
      stopAutoPlay();
      startAutoPlay();
    });
  });

  // Start autoplay
  startAutoPlay();
});