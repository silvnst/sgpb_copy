document.addEventListener('DOMContentLoaded', () => {
    
    // Highlight active section
    document.querySelectorAll('.sidebar nav.nav a').forEach( e => {
        if (e.href === location.href) {
            e.classList.add('active');
        }
    })

    // Detail ansicht
    document.querySelectorAll('.method-modal').forEach( c =>{
        c.addEventListener('click', () => {
            console.log(c.id);
            fetch(`/api/methoden/${c.id}`)
            .then(response => response.json())
            .then(content => {
            let mod = document.querySelector('#methodModal');
            pillsCat = '';
            content.category.forEach(catName =>{
                pillsCat += `<span class="badge rounded-pill bg-light shadow-sm text-dark mx-1" id="${catName.toLowerCase()}-modal">${catName}</span>`;
            });
            mod.innerHTML =
                `<div class="modal-dialog modal-lg modal-fullscreen-sm-down modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="">${content.titel}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">${content.content}</div>
                    <div class="modal-body">
                        <div class="d-flex justify-content-start">${pillsCat}
                        </div>
                    </div>
                    <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Schliessen</button>
                    <button type="button" class="btn btn-primary">Zur Favoriten hinzufügen</button>
                    </div>
                </div>
                </div>`;
            
            let methodModal = new bootstrap.Modal(mod);
            methodModal.toggle();
            })
            .catch(error => {
                console.log(error);
            })
        })
    })
})

