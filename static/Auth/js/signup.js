function submitSignupForm() {
    if (!submitFormValid()) {
        alert("All fields are required!");
    }
    else if(!passwordMatches()){
        document.getElementById('wrong-pass').innerText = "Password does not matched!";
    }
    else {
        let form = document.getElementById('signup-form');
        let formdata = new FormData(form);

        let payload = {
            method: "POST",
            body: formdata
        };

        fetch('http://localhost:5000/signup', payload)
            .then(function (response) {
                console.log("Response status code: ", response.status);
                if (response.status === 409)
                    document.getElementById('wrong-username').innerText = "Username already Exists";
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

function passwordMatches() {
    let passwords = Array.from(document.querySelectorAll('input[type="password"]'));  // len = 2
    if (passwords[0].value.length < 8){
        document.getElementById('wrong-pass').innerText = "Password is less than 8 characters!";
    } else {
        return passwords[0].value === passwords[1].value;
    }

}