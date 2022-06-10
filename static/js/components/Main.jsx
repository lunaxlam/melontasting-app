
function Main() {

  React.useEffect(() => {
    fetch('/api/session_username')
    .then((res) => res.json())
    .then((data) => {
      if (data != null) {

        document.querySelector('#main-content').innerHTML = 
        `<div class='welcome-msg'>
          <p>Welcome back to Il Dolce Melone, ${data}.</p>
        </div>`
        
      }

    })
  }, []);

  return (
    <div className='row align-items-center'>
      <div className='col-4'>
        <img src='/static/img/melontasting.jpg' id='img-tasting' />
      </div>
      <div id='main-content' className='col text-center main-content'>
        <div className='welcome-msg'>
          <p>Welcome to Il Dolce Melone, purveyer of the sweetest melons. <br/>
            To schedule a melon tasting with us, please login.
          </p>
        </div>
        <form action ='/login' method='POST'>
          <label htmlFor='username'></label>
          <input type='text' name='username' id='username' placeholder='Username' required />
          <button type='submit' className='btn btn-success btn-sm'>Submit</button>
        </form>
      </div>
    </div>
  )
}