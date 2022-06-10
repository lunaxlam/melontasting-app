
function Nav() {

    const showForm = () => {
        document.querySelector('#main-content').innerHTML = 
        `<form id='new-reservation' class='row g-3' action='/search' method='POST'>
            <h2 class='text-center'>Search for New Reservation</h2><br />            
            <div class="col-md-12">
                <label for="date" class="form-label lb-lg">Select Date:</label><br />
                <input type="date" name="date" id="date" required />
            </div>
            <h6>Optional: Refine search by selecting a start and end time</h6>
            <div class="col">
                <label for="start-time" class="form-label lb-lg">Start</label>
                <input type="time" class="form-control" name="start" id="start" />
            </div>
            <div class="col">
                <label for="end-time" class="form-label lb-lg">End</label>
                <input type="time" class="form-control" name="end" id="end" />
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-success">Search</button>
            </div>
        </form>
        `
    }

    const showReservations = () => {
        
        fetch('/api/reservations')
            .then((response) => response.json())
            .then((data) => {

                const reservations = data
                
                document.querySelector('#main-content').innerHTML = 
                `<h2 class='text-center'>My Reservations</h2>
                <ul id='reservations'>
                </ul>`

                for (const i in reservations) {

                    document.querySelector('#reservations').insertAdjacentHTML(
                        'beforeend',
                        `<div>
                            <li>${reservations[i]["date"]} at ${reservations[i]["time"]}</li>
                        </div>`
                    )

                }
            })
    }

    return (
        <div className='container'>
            <ul className='nav justify-content-end'>
                <li className='nav-item'>
                    <a className='nav-link' href='#' onClick={showForm}>New Reservation</a>
                </li>
                <li className='nav-item'>
                    <a className='nav-link nav-hover' href='#' onClick={showReservations}>My Reservations</a>
                </li>
                <li className='nav-item'>
                    <a className='nav-link nav-hover' href='/logout'>Logout</a>
                </li>
            </ul>
        </div>
    )
  }