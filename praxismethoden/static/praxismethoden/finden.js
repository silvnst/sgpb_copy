
const user_id = JSON.parse(document.getElementById('user_id').textContent);
    
    function Categories({ allcategories, filter }) {
        
        return(
            <div>
                {
                    allcategories.map( cat => {
                        return(
                            <button key={ cat.id } id={ cat.id } className='btn btn-dark m-1' onClick={ filter }>
                                { cat.name }
                            </button>
                        )
                    })
                }
            </div>
        )
    }

    function Methods({menuItem}) {
        return (
            <div className="row">
                {
                    menuItem.map(m => {
                        return(
                            <div className="col-12 col-md-6 col-lg-4 method-modal" key={ m.id }>
                                <div className="card position-relative border-0 transition method-card shadow my-3">
                                    <span className="material-icons like-display">
                                        { m.likes.includes(user_id) ? 'favorite' : 'favorite_border' }
                                    </span> 
                                    <div className="card-body">
                                        <h5>{ m.titel }</h5>
                                        <div className="line-clamp-4">
                                            { m.desc }
                                        </div>
                                        <div>

                                        </div>
                                        <a type="button" className="btn btn-sm mt-2 btn-outline-primary text-decoration-none" data-toggle="modal" data-target="#exampleModal">
                                            Erfahre mehr
                                        </a>
                                    </div>
                                </div>
                            </div>
                        )
                    })
                }
            </div>
        )
    }
    
    Promise.all([
        fetch(`/api/all_methods`),
        fetch(`/api/all_categories`),
    ])
    .then(responses => {
        return Promise.all(responses.map(function (response) {
		    return response.json();
	    }))
    })
    .then(data => {
        
        const items = data[0];
        const allcategories = data[1];

        allcategories.unshift({'id': 0, 'name': 'Alle'});

        function App() {

            const [menuItem, setMenuItem] = React.useState(items);

            //Filter Function
            function filter (event) {

                const c = parseInt(event.target.id);

                if (c === 0) {
                    setMenuItem(items);
                    return;
                }

                const filteredData = items.filter(item => item.category.id.includes(c));
                
                setMenuItem(filteredData)
            }


            return (
                <div className="App">

                <Categories allcategories={ allcategories } filter={ filter }/>
                <Methods menuItem={ menuItem }/>

                </div>
            );
        }


        ReactDOM.render(
            <React.StrictMode>
                <App />
            </React.StrictMode>,
            document.querySelector("#root")
        );
    })
    .catch(error => {console.log('Error:', error)})
