
var tabs = document.querySelectorAll(".scheduleGrid");
var tablinks = document.querySelectorAll(".tablinks");
const tabheaders = document.querySelectorAll(".tabhead");
const timetable = document.getElementById("timetable");
const timetableHead = document.querySelectorAll(".timetableHead");
var pinCounter = 0;
var pins = [];
tablinks[0].style.backgroundColor = "var(--midpurple2)";

tabs[1].style.display = "none";
for (let i = 1; i < tabs.length; i++) {
    tabs[i].style.display = "none";
    tablinks[i].style.backgroundColor = "var(--lightpurple)";
    console.log(tabs[i]);
}
var deletedtabs = [];

function returnStaticHome() {
    pinCounter = pinCounter + 1;
    // tabs.push(tabs[0].cloneNode(true));
    timetable.appendChild(tabs[0].cloneNode(true)).style.display = "none";
    var newtab = document.createElement("div")
    newtab.className = "tablinks";
    var newbutton = document.createElement("button");
    newbutton.innerHTML = pinCounter;
    newtab.setAttribute( "onClick", "displayTab1(pinCounter-1);" );
    newtab.appendChild(newbutton);
    timetableHead[0].appendChild(newtab);
    tabs = document.querySelectorAll(".scheduleGrid");
    tablinks = document.querySelectorAll(".tablinks");
    console.log(tablinks);
}

function returnSched(sched) {
    var schedulelist = []
    schedulelist = (Array.from(sched)).join('');
    schedulelist = schedulelist.slice(1);
    schedulelist = schedulelist.slice(0, schedulelist.length - 1);
    schedulelist = schedulelist.split(", ")
    var field = (document.getElementById("returnsched").value = schedulelist);
    console.log(field)
}

// I made it functional for any number of tabs <3 
function displayGenerator() {
    tabs = document.querySelectorAll(".scheduleGrid");
    tablinks = document.querySelectorAll(".tablinks");
    for (let i = 1; i < tabs.length; i++) {
        tabs[i].style.display = "none";
        tablinks[i].style.backgroundColor = "var(--lightpurple)";
    }
    tabs[0].style.display = "grid";
    tablinks[0].style.backgroundColor = "var(--midpurple2)";
}

function displayTab1(tabnum) {
    tabs = document.querySelectorAll(".scheduleGrid");
    tablinks = document.querySelectorAll(".tablinks");
    console.log(tablinks[0]);
    tablinks[0].style.backgroundColor = "var(--lightpurple)";
    for (let i = 0; i < tabs.length; i++) {
        tabs[i].style.display = "none";
        tablinks[i].style.backgroundColor = "var(--lightpurple)";
        console.log(tabs[i]);
    }
    tabs[tabnum].style.display = "grid";
    tablinks[tabnum+1].style.backgroundColor = "var(--midpurple2)";
}

function deleteTab(tabnum) {
    console.log(tabnum);
    tabheaders[tabnum-1].style.display = "none";
    deletedtabs.push(tabnum-1);
    console.log(deletedtabs);
}

// hi ana this is what i need passed into views <3
// its var deletedtabs tysm
function returnDeletedTabs() {
    document.getElementById("returndeltab").value = deletedtabs;
}