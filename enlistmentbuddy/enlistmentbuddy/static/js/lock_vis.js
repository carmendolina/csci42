var finalLockedList = [];
var finalUnlockedList = [];

// Hi I touched some stuff here hehe
// I essentially pass the color of the class 
// so i can use that to lock everything with that color
// delete this nalang if u didnt need this explanation HAHAHA
function lock(course, color) {
    //console.log(course);
    //console.log(color);
    var tempclass = document.querySelectorAll("." + CSS.escape(color));
    //console.log(tempclass);
    if (course.classList.contains("False")) {
        /*
        course.classList.remove("False");
        course.classList.add("True");
        */
        tempclass.forEach(function (element) {
            element.classList.remove("False");
            element.classList.add("True");
            element.firstElementChild.style.opacity = "1";
            getButton(element).src = "../static/img/button-lock.svg";
        });
        getButton(course).src = "../static/img/button-lock.svg";
        course.firstElementChild.style.opacity = "1";
        lockedClasses = Array.from(document.querySelectorAll(".True"));
        unlockedClasses = Array.from(document.querySelectorAll(".False"));
    } else if (course.classList.contains("True")) {
        /*
        course.classList.remove("True");
        course.classList.add("False");
        */
        tempclass.forEach(function (element) {
            element.classList.remove("True");
            element.classList.add("False");
            element.firstElementChild.style.opacity = "0";
            getButton(element).src = "../static/img/button-lock.svg";
        });
        getButton(course).src = "../static/img/button-unlock.svg";
        course.firstElementChild.style.opacity = "0";
        lockedClasses = Array.from(document.querySelectorAll(".True"));
        unlockedClasses = Array.from(document.querySelectorAll(".False"));
    }
}

function returnFinalLocked(list) {
    list.forEach(
        function getClassList(course) {
            finalLockedList.push(course.classList);
        }
    );
}

function returnFinalUnlocked(list) {
    list.forEach(
        function getClassList(course) {
            finalUnlockedList.push(course.classList);
        }
    );
}

function returnLockedList() {
    lockedClasses = Array.from(document.querySelectorAll(".True"));
    unlockedClasses = Array.from(document.querySelectorAll(".False"));
    
    returnFinalLocked(lockedClasses);
    
    const currentList = [];
    finalLockedList.forEach(
        function(token){
            currentList.push(String(token));
        }
    );
    var field = (document.getElementById("returnlock").value = currentList);
    console.log(currentList);
}

function returnUnlockedList() {
    lockedClasses = Array.from(document.querySelectorAll(".True"));
    unlockedClasses = Array.from(document.querySelectorAll(".False"));
    returnFinalUnlocked(unlockedClasses);

    const currentList = [];
    finalUnlockedList.forEach(
        function(token){
            currentList.push(String(token));
        }
    );
    console.log(currentList);
    var field = (document.getElementById("returnunlock").value = currentList);
}