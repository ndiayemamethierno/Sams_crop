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

const titles = document.querySelectorAll(".params .param .title")
titles.forEach(title => {
    title.addEventListener("click", function() {
        if (title.parentElement.getAttribute("status") === "opened") {
            title.parentElement.setAttribute("status", "closed")
        }
        else {
            title.parentElement.setAttribute("status", "opened")
        }
    })
});

const chevrons = document.querySelectorAll(".sidebar .pages div.item .d .chevron")
chevrons.forEach(chevron => {
    chevron.addEventListener("click", function() {
        const item = chevron.closest(".item");
        const sublist = item.querySelector(".l");
        if (item.getAttribute("list") === "opened") {
            item.setAttribute("list", "closed");
        } else {
            item.setAttribute("list", "opened");
        }
    })
});




