
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





