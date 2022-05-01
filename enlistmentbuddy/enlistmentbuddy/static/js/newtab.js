var schedulelist = []
var templist = []

function pain(sched){
    templist = (Array.from(sched)).join('');
    templist = templist.slice(1);
    templist = templist.slice(0, templist.length - 1);
    templist = templist.split(", ")
    console.log(templist);
}