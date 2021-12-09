// helper function favoritisation
function favBtnInner (ind, id) {
    text = ind ? 'Von Favoriten entfernen' : 'Zu Favoriten hinzufügen';
    replacement = ind ? 'btn-danger' : 'btn-success';
    document.querySelector(`#${id}`).innerHTML = text;
    document.querySelector(`#${id}`).classList.replace('btn-primary', replacement);
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
                let mod = document.querySelector('#methodModal');
                let docs = '';
                if (content.files.name) {
                    let fileArray = content.files.name.map((k, i) => {return[k, content.files.url[i]]});
                    docs += '<br><h5>Weitere Unterlagen zu diesem Thema: </h5>';
                    fileArray.forEach(file => {
                        docs += `<a target="_blank" class="text-decoration-none" href="${ file[1] }">${ file[0] }</a><br>`;
                    });
                }
                let tipp = '';
                if (content.tipp) {
                    tipp += '<br><h5><img src="static/img/lightbulb.png" alt="enlightened" title="enlightened" style="height: 23px; width: 23px;">Tipp:</h5>' + content.tipp;
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
                            <h5>Beschreibung:</h5>
                            ${ content.desc }
                            ${ tipp }
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

                let methodModal = new bootstrap.Modal(mod);

                // method liking
                document.querySelector('#favBtnModal').addEventListener('click', ()=>{
                    methodModal.toggle();
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
                methodModal.toggle();
            })
            .catch(error => {
                console.log(error);
            })
        })
    })
})