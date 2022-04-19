const ulcourses = document.getElementsByClassName('day unlocked');
const lcourses = document.getElementsByClassName('day locked');

function lock(course) {
    if (course.className == 'day unlocked') {
        course.className = "day locked";
    } else if (course.className == 'day locked') {
        course.className = "day unlocked";
    }
}