function submitLoginForm() {
    if (!submitFormValid()) {
        alert("All fields are required!");
    }

    else {
        let form = document.getElementById('login-form');
        let formdata = new FormData(form);

        let payload = {
            method: "POST",
            body: formdata 
        };

        fetch('http://localhost:5000/login', payload)
        .then(function(response){
            console.log("Response status code: ", response.status);
            console.log(response.statusText)
            if(response.status === 404){
                document.getElementById('wrong-userID').innerText = 'Username does not exist!'
            } else {
            document.getElementById('wrong-pass').innerText = 'Password does not matched!'
            }

        });
    }
}

function submitFormValid() {
    let formDatas = Array.from(document.getElementsByClassName('form-control'));
    for (let field of formDatas) {
        if (field.value === "")
            return;
    }
    return true;
}