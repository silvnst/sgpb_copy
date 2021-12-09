document.addEventListener('DOMContentLoaded', () => {
        
    // Highlight active section
    document.querySelectorAll('nav.navbar a').forEach( e => {
        if (e.href === location.href) {
            e.classList.add('active');
            e.ariaCurrent = 'page';
        }
    })

})

