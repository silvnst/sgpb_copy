document.addEventListener('DOMContentLoaded', () => {
    
    // Header alert
    
    //// Check if cookie
    if ( !document.cookie.split(';').some( (item) => item.includes('noInfo=true') ) ) {
        document.querySelector('#header-alert').classList.remove('d-none');
    }
    
    //// button and cookie setting
    document.querySelectorAll('#header-alert').forEach( alertEl => {
        alertEl.querySelector('button.btn-close').addEventListener('click', () => {
            alertEl.addEventListener('animationend', () => {
                alertEl.remove();
            })
            alertEl.style.animationPlayState = 'running';
            document.cookie = 'noInfo=true; Max-Age=10*5; Secure';
        })
    }) 

    // Highlight active section
    document.querySelectorAll('nav.navbar div.navbar-nav > a.nav-link').forEach( e => {
        if (e.href === location.href) {
            e.classList.add('active');
            e.ariaCurrent = 'page';
        }
    })

    
})

