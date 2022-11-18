const username = document.getElementById('username')
const idExist = document.getElementById('wrong-username');
const wrongPass = document.getElementById('wrong-pass');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirmPassword');
const errorAlertText = document.getElementById('errorAlertText');
const errorAlertTitle = document.getElementById('errorAlertTitle');
const errorAlertModal = document.getElementById('errorAlertModal');
const errorAlertCloseBtn = document.getElementById('errorAlertCloseBtn');

function submitSignupForm() {
    if (!submitFormValid()) {
        errorAlertCloseBtn.innerText = "Close"
        errorAlertTitle.innerText = "Error!";
        errorAlertText.innerText = "All fields are required!"
        errorAlertModal.style.display = "block";
    }

    else if(!passwordMatches()){
        console.log("Password error!")
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
                    idExist.innerText = "Username already Exists";
                
                if (response.status === 200){
                    errorAlertTitle.innerText = "Registration Successful";
                    errorAlertText.innerText = "Login to continue!"
                    errorAlertModal.style.display = "block";
                    errorAlertCloseBtn.innerText = "Login";

                    errorAlertCloseBtn.onclick = () => {
                        window.location = 'http://localhost:5000/login';
                        errorAlertModal.style.display = "none";
                    }
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

function passwordMatches() {
    let passwords = Array.from(document.querySelectorAll('input[type="password"]'));  // len = 2

    if (passwords[0].value.length >= 8){
        if(passwords[0].value !== passwords[1].value){
            wrongPass.innerText = 'Password does not matched!'
            return false;
        } else {
            return true;
        }
    }
    wrongPass.innerText = 'Password is less than 8 characters!';
    return false;
}


username.addEventListener('input', function() {
    idExist.innerText = "";
})

password.addEventListener('input', function() {
    wrongPass.innerText= "";
})

confirmPassword.addEventListener('input', function() {
    wrongPass.innerText= "";
})

errorAlertCloseBtn.onclick = () => {
    errorAlertModal.style.display = "none";
}