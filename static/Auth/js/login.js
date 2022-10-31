const inputFieldID = document.getElementById('userInputID');
const inputFieldPass = document.getElementById('userInputPASS');
const wrongID = document.getElementById('wrong-userID');
const wrongPassword = document.getElementById('wrong-pass');
const errorAlertText = document.getElementById('errorAlertText');
const errorAlertTitle = document.getElementById('errorAlertTitle');
const errorAlertModal = document.getElementById('errorAlertModal');
const errorAlertCloseBtn = document.getElementById('errorAlertCloseBtn');


function submitLoginForm() {
    if (!submitFormValid()) {
        errorAlertTitle.innerText = "";
        errorAlertText.innerText = "All fields are required!"
        errorAlertModal.style.display = "block";
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
                wrongID.innerText = 'Username does not exist!';
            } 
            if (response.status === 401) {
                wrongPassword.innerText = 'Password does not matched!';
            }
        });
    }
}

errorAlertCloseBtn.onclick = () => {
    errorAlertModal.style.display = "none";
}

function submitFormValid() {
    let formDatas = Array.from(document.getElementsByClassName('form-control'));
    for (let field of formDatas) {
        if (field.value === "")
            return;
    }
    return true;
}

inputFieldID.addEventListener('input', function(){
    wrongID.innerText = "";
})

inputFieldPass.addEventListener('input', function(){
    wrongPassword.innerText = "";
})