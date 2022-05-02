
const tabs = document.querySelectorAll(".scheduleGrid");
const tablinks = document.querySelectorAll(".tablinks");
tablinks[0].style.backgroundColor = "var(--midpurple2)";
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
    tablinks[0].style.backgroundColor = "var(--midpurple2)";
    tablinks[1].style.backgroundColor = "var(--lightpurple)";
}

function displayTab1() {
    tabs[0].style.display = "none";
    tabs[1].style.display = "grid";
    tablinks[1].style.backgroundColor = "var(--midpurple2)";
    tablinks[0].style.backgroundColor = "var(--lightpurple)";
}