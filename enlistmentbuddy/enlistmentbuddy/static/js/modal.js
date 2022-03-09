var modal = document.getElementById("myModal");

var close = document.getElementsByClassName("close")[0];
var form = document.getElementById("form");

function openModal() {
    modal.style.display = "block";
}
        
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

close.onclick = function(event) {
    if (event.target == close) {
        modal.style.display = "none";
    }
}