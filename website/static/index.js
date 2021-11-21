//JavaScript function that activates on Click

//Backend Request on JavaScript
function deleteNote(noteId) {
    //delete-note: the endpoint for the backend
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
    })
}