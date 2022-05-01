var lockedClasses = Array.from(document.querySelectorAll(".locked"));
var unlockedClasses = Array.from(document.querySelectorAll(".unlocked"));

function getButton(div) {
    var buttonimg = div.firstElementChild.firstElementChild.firstElementChild;
    return buttonimg;
}

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
    console.log(lockedClasses);
    console.log(unlockedClasses);
    returnLists(lockedClasses);
    returnLists(unlockedClasses);
}

function returnLists(list) {
    list.forEach(
        function getClassList(course) {
            console.log(course.classList);
        }
    );
}

function returnLockedList() {

    const currentList = [];
    lockedClasses.forEach(
        function(token){
            currentList.push(String(token));
        }
    );
    var field = (document.getElementById("returnlock").value = currentList);
    console.log(field);
    // $.ajax({
    //     headers: { "X-CSRFToken": $.cookie("csrftoken") },
    //     type: 'POST',
    //     url: '/index_card',
    //     contentType:"application/json",
    //     data: {
    //         'field':field,
    //         'csrfmiddlewaretoken': '{{ csrf_token }}',
    //     },
    //     dataType: 'json',
    //     success: function() {
    //         alert("it worked!");
    //     },
    //     error: function(){
    //         alert("it didnt work");
    //     }
    // });
}