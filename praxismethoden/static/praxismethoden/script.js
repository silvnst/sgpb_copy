

document.addEventListener('DOMContentLoaded', () => {
        
    // Highlight active section
    document.querySelectorAll('.sidebar nav.nav a').forEach( e => {
        if (e.href === location.href) {
            e.classList.add('active');
        }
    })

})

