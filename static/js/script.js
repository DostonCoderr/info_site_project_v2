document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
        });
    }

    // Accessibility Panel Functionality
    const accessibilityPanel = document.querySelector('.accessibility-panel');
    const body = document.body;
    let currentFontSize = 16; // Asosiy font hajmi (px)

    if (accessibilityPanel) {
        accessibilityPanel.addEventListener('click', function(event) {
            const target = event.target.closest('.access-btn'); // Tugmani topish

            if (!target) return; // Agar tugma bo'lmasa, qaytish

            const buttonText = target.textContent.trim();
            const iconClass = target.querySelector('i')?.classList[1]; // Ikonka klassini olish

            if (buttonText === 'A+') {
                currentFontSize += 2;
                body.style.fontSize = currentFontSize + 'px';
            } else if (buttonText === 'A-') {
                currentFontSize -= 2;
                body.style.fontSize = currentFontSize + 'px';
            } else if (buttonText === 'Aa') {
                currentFontSize = 16; // Asl holatga qaytarish
                body.style.fontSize = currentFontSize + 'px';
                body.classList.remove('high-contrast'); // Ko'zi ojizlar rejimini o'chirish
                // Agar boshqa stil o'zgarishlari bo'lsa, bu yerda qaytarish
            } else if (iconClass === 'fa-volume-up') {
                // Matnni ovoz chiqarib o'qish funksiyasi (qiyinroq, bu yerda oddiy alert)
                alert("Matnni ovoz chiqarib o'qish funksiyasi (ishlamoqda deb hisoblang!)");
            } else if (iconClass === 'fa-eye-slash') {
                // Ko'zi ojizlar rejimi (yuqori kontrast)
                body.classList.toggle('high-contrast');
            }
        });
    }
});