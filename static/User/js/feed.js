const post = document.getElementById("post-modal");
const createModal = document.getElementById("post-create-modal");
const closeButton = document.getElementById("close-button");
const mediaFile = document.getElementById("mediaFile");
const image = document.getElementById('image');
const video = document.getElementById('video');
const postBtn = document.getElementById('postButton');

const applicableFileTypes = ['jpg', 'jpeg', 'mp4', 'x-m4v'];

post.onclick = function() {
    createModal.style.display = "block";
    video.style.display = "none";
}

closeButton.onclick = function() {
    createModal.style.display = "none";
    mediaFile.value = "";
    image.src = "";
    video.src = "";
}

mediaFile.onchange = function(evt) {
    filepath = mediaFile.value.split(".");
    type = filepath[filepath.length - 1];

    if (!applicableFileTypes.includes(type)) {
        alert(`${type} type file are not supported!`);
        mediaFile.value = "";
    }

    const media = URL.createObjectURL(evt.target.files[0]);
    if (['jpeg','jpg'].includes(type)){
        previewImage(media);
    }
    else {
        previewVideo(media);
    }
}

function previewImage(media){
    image.src = media;
}

function previewVideo(media){
    video.src = media;
    video.style.display = "inline";
}


postBtn.addEventListener('onclick', createPost)


function createPost(){

}