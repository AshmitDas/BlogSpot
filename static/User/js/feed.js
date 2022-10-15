const post = document.getElementById("post-modal");
const createModal = document.getElementById("post-create-modal");
const closeButton = document.getElementById("close-button");

post.onclick = function() {
    createModal.style.display = "block";
}

closeButton.onclick = function() {
    createModal.style.display = "none";
}