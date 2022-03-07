function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

const upvote = document.querySelector('#btn_like')
const downvote = document.querySelector('#dislike_btn')


let counter = 0;


upvote.addEventListener('click', like);
downvote.addEventListener('click', dislike);

function like(){
  count++
  counter.innerHTML = count;


}
