const idExist = document.getElementById('wrong-username');
const errorAlertText = document.getElementById('errorAlertText');
const errorAlertTitle = document.getElementById('errorAlertTitle');
const errorAlertModal = document.getElementById('errorAlertModal');
const errorAlertCloseBtn = document.getElementById('errorAlertCloseBtn');

function submitSignupForm() {
    if (!submitFormValid()) {
        errorAlertTitle.innerText = "";
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

errorAlertCloseBtn.onclick = () => {
    errorAlertModal.style.display = "none";
}

function passwordMatches() {
    let passwords = Array.from(document.querySelectorAll('input[type="password"]'));  // len = 2

    if (passwords[0].value.length >= 8){
        if(passwords[0].value !== passwords[1].value){
            document.getElementById('wrong-pass').innerText = 'Password does not matched!'
            return false;
        } else {
            return true;
        }
    }
    document.getElementById('wrong-pass').innerText = 'Password is less than 8 characters!'
    return false;
}


idExist.addEventListener('input', function() {
    idExist.innerText = "";
})