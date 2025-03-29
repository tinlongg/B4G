
document.getElementById("add").onclick = function() {
    let task = document.getElementById("textbox").value;


    if(task.trim() != ""){
        let lis = document.createElement("li");
        lis.textContent = task;
        lis.classList.add("tasking");


        lis.onclick = function() {
            lis.remove();
        }


        document.getElementById("list").appendChild(lis);
        document.getElementById("textbox").value = "";
    }


    }



    function saveNote() {
        const note = document.getElementById('notesBox').value;
    
        fetch('/add_note', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ note: note })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            getNotes(); // Refresh list
        });
    }
    
    // Get notes
    function getNotes() {
        fetch('/get_notes')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('savedNotes');
            container.innerHTML = '';
            data.forEach(note => {
                const div = document.createElement('div');
                div.textContent = note;
                container.appendChild(div);
            });
        });
    }
    
    window.onload = getNotes;




