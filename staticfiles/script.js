// Toggle Menu
const menuToggle = document.getElementById('menu-toggle');
const navList = document.getElementById('nav-list'); // corrigido

menuToggle.addEventListener('click', () => {
  navList.classList.toggle('show');
});

document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scrolling for Navigation Links
    document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            const headerOffset = document.querySelector('header').offsetHeight; // Get header height
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset; // Adjust for sticky header

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        });
    });

    // Back to Top Button
    const backToTopButton = document.getElementById('back-to-top');

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) { // Show button after scrolling 300px
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Dynamic Header Shadow on Scroll
    const mainHeader = document.getElementById('main-header');

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 50) { // Add shadow after scrolling 50px
            mainHeader.classList.add('scrolled');
        } else {
            mainHeader.classList.remove('scrolled');
        }
    });

    // Scroll Reveal Animations
    const revealElements = document.querySelectorAll('.reveal-on-scroll');

    const observerOptions = {
        root: null, // viewport
        rootMargin: '0px',
        threshold: 0.1 // 10% of the element must be visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Stop observing once revealed
            }
        });
    }, observerOptions);

    revealElements.forEach(el => {
        observer.observe(el);
    });

    // Active Navigation Link on Scroll
    const sections = document.querySelectorAll('main section');
    const navLinks = document.querySelectorAll('nav a');

    const highlightNavLink = () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            // Adjust for header height to make activation more accurate
            if (pageYOffset >= sectionTop - mainHeader.offsetHeight - 50) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active-link');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active-link');
            }
        });
    };

    window.addEventListener('scroll', highlightNavLink);
    // Call on load to set initial active link
    highlightNavLink();
});
