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

// function returnLockedList() {
//     console.log(lockedClasses);
//     return lockedClasses;
// }

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