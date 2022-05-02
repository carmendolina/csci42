var finalLockedList = [];
var finalUnlockedList = [];

function lock(course) {
    if (course.classList.contains("False")) {
        course.classList.remove("False");
        course.classList.add("True");
        getButton(course).src = "../static/img/button-lock.svg";
        course.firstElementChild.style.opacity = "1";
        lockedClasses = Array.from(document.querySelectorAll(".True"));
        unlockedClasses = Array.from(document.querySelectorAll(".False"));
    } else if (course.classList.contains("True")) {
        course.classList.remove("True");
        course.classList.add("False");
        getButton(course).src = "../static/img/button-unlock.svg";
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