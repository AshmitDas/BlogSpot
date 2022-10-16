const post = document.getElementById("post-modal");
const createModal = document.getElementById("post-create-modal");
const closeButton = document.getElementById("close-button");
const formFile = document.getElementById("formFile");

const applicableFileTypes = ['jpg', 'jpeg', 'mp4', 'x-m4v'];

post.onclick = function() {
    createModal.style.display = "block";
}

closeButton.onclick = function() {
    createModal.style.display = "none";
}

formFile.onchange = function() {
    filepath = formFile.value.split(".");
    type = filepath[filepath.length - 1];

    if (!applicableFileTypes.includes(type)) {
        alert('File Type not applicable');
        formFile.value = "";
    }
}