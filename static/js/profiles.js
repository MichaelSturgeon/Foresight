// Upload Image variables
const profileImageModal = new bootstrap.Modal(document.getElementById("profileImageModal"));
const uploadButtons = document.getElementsByClassName("btn-upload");
const uploadConfirm = document.getElementById("uploadConfirm");


// Upload Image Modal function
for (let button of uploadButtons) {
    button.addEventListener("click", (e) => {
        profileImageModal.show();
    });
}