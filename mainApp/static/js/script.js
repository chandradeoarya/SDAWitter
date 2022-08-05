function hover(e){
    e.className += "Hover";
}
function unHover(e){
    e.className = e.className.replace('Hover','')
}
window.onclick = function(event) {
    console.log(event.target)
    if (!event.target.matches('.settingsIcon')) {
        var dropdowns = document.getElementsByClassName("dropContent");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
        }
    }
}
function showMenu(e){
    e = e.nextElementSibling
    e.classList.toggle("show")
}