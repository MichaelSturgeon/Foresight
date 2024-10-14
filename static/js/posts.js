// Delete post variables
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Delete modal function
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("post_id");
        deleteConfirm.href = `delete_post/${postId}`;
        deleteModal.show();
    });
}