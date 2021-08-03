
document.addEventListener('DOMContentLoaded', function(){
    
    // get categories
    fetch('api/all_categories')
    .then(response => response.json())
    .then(allCat => {
        let html = '';
        allCat.forEach(cat => {
            html += `<span class="badge rounded-pill bg-light shadow-sm text-dark mx-1" id="${cat.name.toLowerCase()}">${cat.name}</span>`
        });
        html += '<span class="badge rounded-pill bg-info shadow-sm mx-1" id="alle">Alle</span>'
        document.querySelector('#categories').innerHTML = html;
    })

    // interaktion
    document.querySelector('#other').addEventListener('click', () => {
        let modal = new bootstrap.Modal(document.querySelector('#exampleModal'));
        modal.toggle();
    });
})