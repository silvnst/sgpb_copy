document.addEventListener('DOMContentLoaded', () => {
    
    if ( !document.cookie.split(';').some((item) => item.includes('noInfo=true')) ) {
        document.querySelector('#header-alert').classList.remove('d-none');
    }

    // Highlight active section
    document.querySelectorAll('nav.navbar a').forEach( e => {
        if (e.href === location.href) {
            e.classList.add('active');
            e.ariaCurrent = 'page';
        }
    })

    // Header alert
    document.querySelectorAll('#header-alert').forEach( alertEl => {
        alertEl.querySelector('button.btn-close').addEventListener('click', () => {
            alertEl.addEventListener('animationend', () => {
                alertEl.remove();
                document.cookie = 'noInfo=true; max-age=60*60; Secure';
            })
            alertEl.style.animationPlayState = 'running';
        })
    }) 
})

