const post = document.getElementById("post-modal");
const title = document.getElementById('title');
const description = document.getElementById('body');
const createModal = document.getElementById("post-create-modal");
const closeButton = document.getElementById("close-button");
const mediaFile = document.getElementById("mediaFile");
const image = document.getElementById('image');
const video = document.getElementById('video');
const postBtn = document.getElementById('postButton');
const errorAlertText = document.getElementById('errorAlertText');
const errorAlertTitle = document.getElementById('errorAlertTitle');
const errorAlertModal = document.getElementById('errorAlertModal');
const errorAlertCloseBtn = document.getElementById('errorAlertCloseBtn');

const applicableFileTypes = ['jpg', 'jpeg', 'mp4', 'x-m4v'];

post.onclick = function() {
    createModal.style.display = "block";
    video.style.display = "none";
}

closeButton.onclick = function() {
    cleanPostForm();
}

mediaFile.onchange = function(evt) {
    filepath = mediaFile.value.split(".");
    type = filepath[filepath.length - 1];

    if (!applicableFileTypes.includes(type)) {
        alert(`.${type} type file are not supported!`);
        mediaFile.value = "";
    }

    checkValidMediaFile();

    const media = URL.createObjectURL(evt.target.files[0]);
    if (['jpeg','jpg'].includes(type)){
        previewImage(media);
    }
    else {
        previewVideo(media);
    }
}

errorAlertCloseBtn.onclick = () => {
    errorAlertModal.style.display = "none";
    mediaFile.value = "";
}

function previewImage(media){
    image.src = media;
}

function previewVideo(media){
    video.src = media;
    video.style.display = "inline";
}

function checkValidMediaFile(){
    let filenameArr = mediaFile.value.split(".");

    if ((mediaFile.value.split(".").length - 1) !== 1 || filenameArr[0] === "C:\\fakepath\\") {
        errorAlertText.innerText = `{Your Filename}.${filenameArr[filenameArr.length - 1]}`;
        errorAlertModal.style.display = "block";
    }
}


postBtn.onclick = function(){
    if(title.value === "" || description.value === ""){
        alert("Title and Description cannot be empty!");
    }

    let form = document.getElementById('postForm');
    let formdata = new FormData(form);

    let payload = {
        method: "POST",
        body: formdata
    };
    console.log(payload);
    fetch('http://localhost:5000/post', payload)
    .then(function(response){
        console.log('Response Status Code: ', response.status);
        
        if(response.status === 200) {
            cleanPostForm();
            window.location.reload();
        }

        if (response.status === 400){
            errorAlertText.innerText = `{Your Filename}`;
            errorAlertModal.style.display = "block";
        }
    });
}

function cleanPostForm() {
    createModal.style.display = "none";
    mediaFile.value = "";
    title.value="";
    description.value = "";
    image.src = "";
    video.src = "";
}

