document.addEventListener('DOMContentLoaded', () => {
    const allCards = document.querySelectorAll('.method-modal');
    const allBtn = document.querySelectorAll('.category-btn');

    allBtn.forEach(btn => {
        btn.addEventListener('click', event => {
            allBtn.forEach(b => { b.classList.replace('btn-secondary', 'btn-light'); });
            btn.classList.replace('btn-light', 'btn-secondary');
            const catId = parseInt(event.target.dataset['catId']);

            allCards.forEach(card => {

                let spans = card.querySelectorAll('#category-badge');

                Array.from(spans).every(span => {

                    if (parseInt(span.dataset['category']) === catId || catId === 0) {
                        card.style.display = 'block';
                        return false;
                        
                    } else {
                        card.style.display = 'none';
                        return true;
                    }
                });
            });
        });
    });
});