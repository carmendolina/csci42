
var tabs = document.querySelectorAll(".scheduleGrid"); // length = 1
var tablinks = document.querySelectorAll(".tablinks"); // length = 1
const tabheaders = document.querySelectorAll(".tabhead");
var timetable = document.getElementById("timetable");
const timetableHead = document.querySelectorAll(".timetableHead");
var pinCounter = 0;
var pins = [];
var pinscheds = Array.from(tabs);
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
    var newsched = tabs[0].cloneNode(true);
    pinscheds.push(newsched);
    
    var newtab = document.createElement("div");
    newtab.className = "tablinks";
    pins.push(newtab);
    newtab.setAttribute( "onClick", "displayTab1(pins.indexOf(this)+1);" );

    timetable.appendChild(newsched).style.display = "none";
    tabs = document.querySelectorAll(".scheduleGrid");
    tablinks = document.querySelectorAll(".tablinks");
    
    var newclose = document.createElement("img");
    newclose.setAttribute("src", "../static/img/button-add.svg");
    newclose.setAttribute("class", "closetab");
    newclose.setAttribute("onClick", "deleteTab(this.parentElement)");
    
    var newbutton = document.createElement("button");
    newbutton.innerHTML = pins.indexOf(newtab)+1;
    
    newtab.appendChild(newclose);
    newtab.appendChild(newbutton);
    timetableHead[0].appendChild(newtab);

    console.log(pins);

    tabs = document.querySelectorAll(".scheduleGrid");
    tablinks = document.querySelectorAll(".tablinks");
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
    tabs[0].style.display = "grid";
    tablinks[0].style.backgroundColor = "var(--midpurple2)";
    tablinks[0].addEventListener("mouseout", function() {
        tablinks[0].style.backgroundColor = "var(--midpurple2)";
    });
    for (let i = 1; i < tabs.length; i++) {
        tabs[i].style.display = "none";
        tablinks[i].style.backgroundColor = "var(--lightpurple)";
    }
}

function displayTab1(tabnum) {
    tabs = document.querySelectorAll(".scheduleGrid");
    tablinks = document.querySelectorAll(".tablinks");
    tablinks[0].style.backgroundColor = "var(--lightpurple)";
    for (let i = 0; i < tabs.length; i++) {
        tabs[i].style.display = "none";
        tablinks[i].style.backgroundColor = "var(--lightpurple)";
        tablinks[i].addEventListener("mouseover", function() {
            tablinks[i].style.backgroundColor = "var(--midpurple2)";
        });
        tablinks[i].addEventListener("mouseout", function() {
            tablinks[i].style.backgroundColor = "var(--lightpurple)";
        });
    }
    tabs[tabnum].style.display = "grid";
    tablinks[tabnum].style.backgroundColor = "var(--midpurple2)";
    tablinks[tabnum].addEventListener("mouseout", function() {
        tablinks[tabnum].style.backgroundColor = "var(--midpurple2)";
    });
}

function deleteTab(div) {
    displayGenerator()
    pins.splice(pins.indexOf(div),1);
    pinCounter = pinCounter - 1;
    for (let i = 0; i < pins.length; i++) {
        pins[i].children[1].innerHTML = i+1;
    }
    timetableHead[0].removeChild(div);

    timetable.removeChild(tabs[
        (Array.from(tabs).indexOf(div))+1
    ]);

    tabs = document.querySelectorAll(".scheduleGrid");
    tablinks = document.querySelectorAll(".tablinks");
}

function delTab(tabnum){
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