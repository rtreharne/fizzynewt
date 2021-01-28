function TestButton(props) {
 
    function pingTest(e) { 
        e.preventDefault();
        // We fetch the pings API
        fetch("http://localhost:8000/api/pings")
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            alert("Data outputted to console!")
        });
    }
    return (
        <button onClick={pingTest}>Ping!</button>
    )
}

export default TestButton