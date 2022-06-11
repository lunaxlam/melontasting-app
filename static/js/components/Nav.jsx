
function Nav() {

    let user = ''

    fetch('/api/session_username')
    .then((res) => res.json())
    .then((data) => {
      
        user = data;

    })

    const showForm = () => {

        if (user != null) {

            document.querySelector('#main-content').innerHTML = 
            `<form id='new-reservation' class='row g-3' method='POST'>
                <h2 class='text-center'>Search for New Reservation</h2>
                <h5 id='alert'>Now accepting reservations for August 2022!</h5> 
                <h6>Daily melon tastings, 11am to 4pm</h6>     
                <div class='col-md-12'>
                    <label for='date-field' class='form-label lb-lg'>Select Date:</label><br />
                    <input type='date' name='date' id='date' value='2022-08-01' required />
                </div>
                <h6 class='coming-soon'>COMING SOON: Option to refine search by selecting a start and end time.</h6>
                <div class='col'>
                    <label for='start-field' class='form-label lb-lg coming-soon'>Start</label>
                    <input type='time' class='form-control' name='start' id='start' min='11:00' max='16:00' disabled/>
                </div>
                <div class='col'>
                    <label for='end-field' class='form-label lb-lg coming-soon'>End</label>
                    <input type='time' class='form-control' name='end' id='end' disabled/>
                </div>
                <div class='col-12'>
                    <button type='submit' class='btn btn-success'>Search</button>
                </div>
            </form>`

            document.querySelector('#new-reservation').addEventListener('submit', (evt) => {
                evt.preventDefault();

                const formInputs = {
                    date: document.querySelector('#date').value,
                    start: document.querySelector('#start').value,
                    end: document.querySelector('#end').value,
                };

                fetch('/api/slots', {
                    method: 'POST',
                    body: JSON.stringify(formInputs),
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                    .then((res) => res.json())
                    .then((resJSON) => {

                        const slots = resJSON

                        if (Object.keys(slots).length === 0) {
                            document.querySelector('#main-content').innerHTML = 
                            `<h2 class='text-center'>Available Slots:</h2>
                            <p>No tastings available. Please search another date.</p>`
                        } else {

                            document.querySelector('#main-content').innerHTML = 
                            `<h2>Available Slots:</h2>
                            <div id='slots-container'>
                                <ul id='slots'>
                                </ul>
                            </div>`

                            for (const i in slots) {

                                document.querySelector('#slots').insertAdjacentHTML(
                                    'beforeend',
                                    `<li>${slots[i]['date']} at ${slots[i]['time']} <a href='/signup/${slots[i]['slot_id']}'><button class='btn btn-success btn-sm'>Sign-Up</button></a>`
                                )

                            }
                        }
                    })
            })
        } else {
            document.querySelector('#main-content').innerHTML = 
            `<p>Please <a href="\">login</a> to view this feature.</p>`
        }
    }

    const showReservations = () => {

        if (user != null) {
        
            fetch('/api/reservations')
                .then((response) => response.json())
                .then((data) => {

                    const reservations = data
                    
                    document.querySelector('#main-content').innerHTML = 
                    `<h2 class='text-center'>My Reservations</h2>
                    <div id='reservations-container'>
                        <ul id='reservations'>
                        </ul>
                    </div>`

                    for (const i in reservations) {

                        document.querySelector('#reservations').insertAdjacentHTML(
                            'beforeend',
                            `<div>
                                <li>${reservations[i]['date']} at ${reservations[i]['time']}<a href='/delete/${reservations[i]['reservation_id']}'><button class='btn btn-danger btn-sm'>Delete</button></a></li>
                            </div>`
                        )

                    }
                })
        } else {
            document.querySelector('#main-content').innerHTML = 
            `<p>Please <a href="\">login</a> to view this feature.</p>`
        }
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