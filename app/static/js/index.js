function changeShow(planElem) {
    let parentElem = planElem.parentNode;
    if (parentElem == null) {
        console.log(parentElem + " not found");
        return;
    } else {
        console.log(parentElem);
    }
    if (parentElem.className == "active") {
        parentElem.className = "";
    } else {
        parentElem.className = "active";
    }
}
document.getElementById("head_plan").addEventListener("click", function () { changeShow(this) });
document.getElementById("report").addEventListener("click", function () { changeShow(this) });
