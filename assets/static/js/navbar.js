function openSideMenu() {
    document.getElementById("sidebar").style.width = "20%";
    document.getElementById("open").style.display = "none";
    document.getElementById("close").style.display = "unset";
    document.getElementById("sidelink1").style.opacity = 1;
    document.getElementById("sidelink1").style.pointerEvents = "auto";
}

function closeSideMenu() {
    document.getElementById("sidebar").style.width = "0";
    document.getElementById("close").style.display = "none";
    document.getElementById("open").style.display = "unset";
    document.getElementById("sidelink1").style.opacity = 0;
    document.getElementById("sidelink1").style.pointerEvents = "none";
}