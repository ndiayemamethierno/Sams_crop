const menu_btn = document.querySelector(".main .header .left");
const sidebar = document.querySelector(".sidebar");

if (menu_btn) {
    menu_btn.addEventListener('click', function() {
        if (sidebar) {
            if (sidebar.classList.contains('opened')) {
                sidebar.classList.remove('opened');
                sidebar.classList.add('closed');
                localStorage.setItem('sidebarHidden', 'true');
            }
            else if (sidebar.classList.contains('closed')){
                sidebar.classList.remove('closed');
                sidebar.classList.add('opened');
                localStorage.setItem('sidebarHidden', 'false');
            }
        }
    })
}

document.addEventListener('DOMContentLoaded', function() {
    var isSidebarHidden = localStorage.getItem('sidebarHidden');

    if (isSidebarHidden === 'true') {
        sidebar.classList.remove('opened');
        sidebar.classList.add('closed');
    }
    else {
        sidebar.classList.remove('closed');
        sidebar.classList.add('opened');
    }
});

const pageItems = document.querySelectorAll(".item");

pageItems.forEach(item => {
    item.addEventListener('click', function() {
        const pcSelecs = document.querySelectorAll("[status='selected']");
        pcSelecs.forEach(pcSelec => {
            pcSelec.setAttribute("status", "none");
        });
        const ncSelecs = document.querySelectorAll('.' + item.classList[1]);
        ncSelecs.forEach(ncSelec => {
            ncSelec.setAttribute("status", "selected");
        });
    })    
});

const tCloses = document.querySelectorAll(".tabV .close");
tCloses.forEach(tClose => {
    tClose.addEventListener('click', function() {
        tClose.parentElement.parentElement.setAttribute("type", "rolled");
    })
});

const tRolls = document.querySelectorAll(".tabV .roll-btn");
tRolls.forEach(tRoll => {
    tRoll.addEventListener("click", function() {
        tRoll.parentElement.setAttribute("type", "unrolled");
    })
});




