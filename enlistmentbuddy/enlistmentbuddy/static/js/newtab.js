
const tabs = document.querySelectorAll(".scheduleGrid");
tabs[1].style.display = "none";

function returnSched(sched) {
    var schedulelist = []
    schedulelist = (Array.from(sched)).join('');
    schedulelist = schedulelist.slice(1);
    schedulelist = schedulelist.slice(0, schedulelist.length - 1);
    schedulelist = schedulelist.split(", ")
    var field = (document.getElementById("returnsched").value = schedulelist);
    console.log(field)
}

function displayGenerator() {
    tabs[0].style.display = "grid";
    tabs[1].style.display = "none";
}

function displayTab1() {
    tabs[0].style.display = "none";
    tabs[1].style.display = "grid";
}