
const tabs = document.querySelectorAll(".scheduleGrid");
const tablinks = document.querySelectorAll(".tablinks");
const tabheaders = document.querySelectorAll(".tabhead");
tablinks[0].style.backgroundColor = "var(--midpurple2)";
tabs[1].style.display = "none";
var deletedtabs = [];

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
    for (let i = 1; i < tabs.length; i++) {
        tabs[i].style.display = "none";
        tablinks[i].style.backgroundColor = "var(--lightpurple)";
        console.log(tabs[i]);
    }
    tabs[0].style.display = "grid";
    tablinks[0].style.backgroundColor = "var(--midpurple2)";
}

function displayTab1(tabnum) {
    console.log(tabnum);
    for (let i = 0; i < tabs.length; i++) {
        tabs[i].style.display = "none";
        tablinks[i].style.backgroundColor = "var(--lightpurple)";
        console.log(tabs[i]);
    }
    tabs[tabnum].style.display = "grid";
    tablinks[tabnum].style.backgroundColor = "var(--midpurple2)";
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

}