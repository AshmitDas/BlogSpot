const post = document.getElementById("post-modal");
const createModal = document.getElementById("post-create-modal");
const closeButton = document.getElementById("close-button");
const mediaFile = document.getElementById("mediaFile");
const image = document.getElementById('image');

const applicableFileTypes = ['jpg', 'jpeg', 'mp4', 'x-m4v'];

post.onclick = function() {
    createModal.style.display = "block";
}

closeButton.onclick = function() {
    createModal.style.display = "none";
    mediaFile.value = "";
    image.src = "";
}

mediaFile.onchange = function(evt) {
    filepath = mediaFile.value.split(".");
    type = filepath[filepath.length - 1];

    if (!applicableFileTypes.includes(type)) {
        alert('File Type not applicable');
        mediaFile.value = "";
    }
    previewImage(evt);
}

function previewImage(event){
    const media = URL.createObjectURL(event.target.files[0]);
    image.src = media;
}