var finalLockedList = [];
var finalUnlockedList = [];

function lock(course) {
    if (course.classList.contains("unlocked")) {
        course.classList.remove("unlocked");
        course.classList.add("locked");
        getButton(course).src = "../static/img/button-lock.svg";
        lockedClasses = Array.from(document.querySelectorAll(".locked"));
        unlockedClasses = Array.from(document.querySelectorAll(".unlocked"));
    } else if (course.classList.contains("locked")) {
        course.classList.remove("locked");
        course.classList.add("unlocked");
        getButton(course).src = "../static/img/button-unlock.svg";
        lockedClasses = Array.from(document.querySelectorAll(".locked"));
        unlockedClasses = Array.from(document.querySelectorAll(".unlocked"));
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
    returnFinalLocked(lockedClasses);

    const currentList = [];
    finalLockedList.forEach(
        function(token){
            currentList.push(String(token));
        }
    );
    var field = (document.getElementById("returnlock").value = currentList);
}

function returnUnlockedList() {
    returnFinalUnlocked(unlockedClasses);

    const currentList = [];
    finalUnlockedList.forEach(
        function(token){
            currentList.push(String(token));
        }
    );
    var field = (document.getElementById("returnunlock").value = currentList);
}