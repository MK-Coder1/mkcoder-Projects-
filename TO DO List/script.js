console.log("Jai Bajrang Bali");


// To Do List:-

document.querySelector("#push").onclick = function () {
    if (document.querySelector("#newTask input").value.length == 0) {
        alert("Please Enter a Task")
    }
    else {
        document.querySelector("#tasks").innerHTML +=
            `        <div class="task" >
            <span id="taskname">
            ${document.querySelector('#newTask input').value}
            </span>
            <button class="delete">
          <i class="fa-solid fa-trash"></i>
            </button>
            </div >
           `;

        var currTask = document.querySelectorAll(".delete");
        for (var i = 0; i < currTask.length; i++) {
            currTask[i].onclick = function () {
                this.parentNode.remove();
            }
        }

        var tasks = document.querySelectorAll(".task");
        for (var i = 0; i < tasks.length; i++) {
            tasks[i].onclick = function () {
                this.classList.tooggle("completed");
            }
        }

        document.querySelector("#newTask input").value = "";
    }
}