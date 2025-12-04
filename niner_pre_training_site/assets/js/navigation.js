// Navigation and UI interactions for 365WineTrade QuickStart Guide

document.addEventListener('DOMContentLoaded', function() {

    // Highlight current page in sidebar navigation
    highlightCurrentPage();

    // Smooth scrolling for anchor links
    setupSmoothScrolling();

    // Mobile menu toggle
    setupMobileMenu();

    // Add copy buttons to code blocks
    setupCodeCopyButtons();
});

function highlightCurrentPage() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.sidebar .nav-link');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath ||
            currentPath.endsWith(link.getAttribute('href'))) {
            link.classList.add('active');

            // Scroll the active link into view in the sidebar
            link.scrollIntoView({ block: 'center', behavior: 'smooth' });
        }
    });
}

function setupSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Update URL without jumping
                history.pushState(null, null, targetId);
            }
        });
    });
}

function setupMobileMenu() {
    // Create mobile menu toggle button if it doesn't exist
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;

    const toggleBtn = document.createElement('button');
    toggleBtn.className = 'btn btn-primary d-md-none mb-3';
    toggleBtn.innerHTML = '☰ Menu';
    toggleBtn.onclick = function() {
        sidebar.style.display = sidebar.style.display === 'none' ? 'block' : 'none';
    };

    // Insert before sidebar on mobile
    if (window.innerWidth < 768) {
        sidebar.parentNode.insertBefore(toggleBtn, sidebar);
    }
}

function setupCodeCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');

    codeBlocks.forEach(block => {
        const pre = block.parentElement;
        const wrapper = document.createElement('div');
        wrapper.style.position = 'relative';

        const copyBtn = document.createElement('button');
        copyBtn.className = 'btn btn-sm btn-outline-secondary';
        copyBtn.style.position = 'absolute';
        copyBtn.style.top = '0.5rem';
        copyBtn.style.right = '0.5rem';
        copyBtn.innerHTML = 'Copy';

        copyBtn.onclick = function() {
            navigator.clipboard.writeText(block.textContent).then(() => {
                copyBtn.innerHTML = 'Copied!';
                setTimeout(() => {
                    copyBtn.innerHTML = 'Copy';
                }, 2000);
            });
        };

        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        wrapper.appendChild(copyBtn);
    });
}

// Add keyboard navigation
document.addEventListener('keydown', function(e) {
    // Alt + Left Arrow = Previous page
    if (e.altKey && e.key === 'ArrowLeft') {
        const prevBtn = document.querySelector('.nav-btn.prev');
        if (prevBtn) {
            window.location.href = prevBtn.href;
        }
    }

    // Alt + Right Arrow = Next page
    if (e.altKey && e.key === 'ArrowRight') {
        const nextBtn = document.querySelector('.nav-btn.next');
        if (nextBtn) {
            window.location.href = nextBtn.href;
        }
    }
});

// Add scroll progress indicator
function createScrollProgress() {
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, #722f37, #d4af37);
        z-index: 9999;
        transition: width 0.2s;
    `;
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = scrolled + '%';
    });
}

createScrollProgress();
