var lockedClasses = [];

function getButton(div) {
    var buttonimg = div.firstElementChild.firstElementChild.firstElementChild;
    return buttonimg;
}

function lock(course) {
    if (course.classList.contains("unlocked")) {
        course.classList.remove("unlocked");
        course.classList.add("locked");
        getButton(course).src = "../static/img/button-lock.svg";
        if (!lockedClasses.includes(course.classList)) {
            lockedClasses.push(course.classList);
        }
    } else if (course.classList.contains("locked")) {
        course.classList.remove("locked");
        course.classList.add("unlocked");
        getButton(course).src = "../static/img/button-unlock.svg";
        if (lockedClasses.includes(course.classList)) {
            lockedClasses.pop(course.classList);
        }
    }
    console.log(lockedClasses);
}

function returnLockedList() {
    console.log(lockedClasses);
    return lockedClasses;
}