
function returnSched(sched){
    var schedulelist = []

    schedulelist = (Array.from(sched)).join('');
    schedulelist = schedulelist.slice(1);
    schedulelist = schedulelist.slice(0, schedulelist.length - 1);
    schedulelist = schedulelist.split(", ")
    var field = (document.getElementById("returnsched").value = schedulelist);
    console.log(field)
}