
function App() {

    return (
        <React.Fragment>
            <Nav />
            <div id='main' className='container'>
                <Title title='il dolce melone' />
                <Main />
            </div>
            <Footer />
        </React.Fragment>
    );
}

ReactDOM.render(<App />, document.querySelector('#root'));
