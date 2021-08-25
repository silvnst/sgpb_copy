// helper function favoritisation
function favBtnInner (ind, id) {
    text = ind ? 'Von Favoriten entfernen' : 'Zu Favoriten hinzufügen';
    document.querySelector(`#${id}`).innerHTML = text
}
// csrf protection
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// save csrf token in constant
const csrftoken = getCookie('csrftoken');

// open modal effekt
document.addEventListener('DOMContentLoaded', () => {
    
    const user_id = JSON.parse(document.getElementById('user_id').textContent);

    // Detail ansicht
    document.querySelectorAll('.method-modal').forEach( c =>{
        c.addEventListener('click', () => {
            fetch(`/api/methoden/${c.id}`)
            .then(response => response.json())
            .then(content => {
                console.log(content);
                let mod = document.querySelector('#methodModal');
                let docs = '';
                if (content.file_raw.url) {
                    docs += `<br></br><h5>Hier ein Dokument zu diesem Thema: </h5><p><a <a target="_blank" href="${ content.file_raw.url }">Link</a></p>`;
                }
                pillsCat = '';
                content.category.name.forEach(catName => {
                    pillsCat += `<span class="badge text-wrap rounded-pill bg-light shadow-sm text-dark mx-1" id="${catName.toLowerCase()}-modal">${catName}</span>`;
                });
                mod.innerHTML =
                    `<div class="modal-dialog modal-lg modal-fullscreen-sm-down modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="">${ content.titel }</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            ${ content.content }
                            ${ docs }
                        </div>
                        <div class="modal-body">
                            <div class="d-flex justify-content-start">${ pillsCat }
                            </div>
                        </div>

                        <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Schliessen</button>
                        <button type="button" class="btn btn-primary" id="favBtnModal">${ content.favoriteText }</button>
                        </div>
                    </div>
                    </div>`;
                likeInd = content.likes.includes( user_id );
                favBtnInner(likeInd, 'favBtnModal');
                document.querySelector('#favBtnModal').addEventListener('click', ()=>{
                    request = new Request(`/api/methoden/${c.id}`, {
                        headers: {'X-CSRFToken': csrftoken}
                    })
                    fetch(request, {
                        method: 'POST',
                        mode: 'same-origin',
                        body: JSON.stringify({
                            like: likeInd
                        })
                    })
                    .then(()=>{
                        likeInd = likeInd ? false : true;
                        favBtnInner(likeInd, 'favBtnModal');
                    })
                    self.addEventListener('hide.bs.modal', ()=>{
                        location.reload();
                    })
                })
                let methodModal = new bootstrap.Modal(mod);
                methodModal.toggle();
            })
            .catch(error => {
                console.log(error);
            })
        })
    })
})