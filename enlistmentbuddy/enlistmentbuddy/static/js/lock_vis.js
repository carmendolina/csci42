const ulcourses = document.getElementsByClassName('day unlocked');
const lcourses = document.getElementsByClassName('day locked');

function getButton(div) {
    var buttonimg = div.firstElementChild.firstElementChild.firstElementChild.firstElementChild;
    return buttonimg;
}

function lock(course) {
    if (course.className == 'day unlocked') {
        course.className = "day locked";
        getButton(course).src = "../static/img/button-lock.svg";
    } else if (course.className == 'day locked') {
        course.className = "day unlocked";
        getButton(course).src = "../static/img/button-unlock.svg";
    }
}