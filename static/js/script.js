document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const mainNav = document.getElementById('mainNav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active'); // Toggles the 'active' class
        });
    }

    // Loader functionality - Bu qism o'chirildi, chunki sizga loader kerak emas dedingiz.
    // Agar loader kerak bo'lsa, HTMLdagi loader divini sharhdan oling
    // va bu yerda quyidagi kodni qayta yoqing:
    /*
    const loader = document.getElementById('loader');
    const mainContent = document.getElementById('main-content');

    if (loader && mainContent) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                loader.style.display = 'none';
                mainContent.style.display = 'block';
            }, 500);
        });
    }
    */


    // Accessibility Panel Functionality
    const accessibilityPanel = document.querySelector('.accessibility-panel');
    const body = document.body;
    let currentFontSize = 16; // Asosiy font hajmi (px)

    if (accessibilityPanel) {
        accessibilityPanel.addEventListener('click', function(event) {
            const target = event.target.closest('.access-btn');

            if (!target) return;

            const buttonText = target.textContent.trim();
            const iconElement = target.querySelector('i');
            const iconClass = iconElement ? iconElement.classList[1] : null;

            if (buttonText === 'A+') {
                currentFontSize += 2;
                body.style.fontSize = currentFontSize + 'px';
            } else if (buttonText === 'A-') {
                currentFontSize -= 2;
                body.style.fontSize = currentFontSize + 'px';
            } else if (buttonText === 'Aa') {
                currentFontSize = 16; // Reset to original font size
                body.style.fontSize = currentFontSize + 'px';
                body.classList.remove('high-contrast'); // Turn off high contrast mode
            } else if (iconClass === 'fa-volume-up') {
                alert("Matnni ovoz chiqarib o'qish funksiyasi (ishlamoqda deb hisoblang!)");
            } else if (iconClass === 'fa-eye-slash') {
                body.classList.toggle('high-contrast');
            }
        });
    }
}); 