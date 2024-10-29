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

function setSelected() {
    const urlParams = new URLSearchParams(window.location.search);
    const year = urlParams.get('year') || '2020';
    const tech = urlParams.get('tech') || 'R';
    const crops = urlParams.get('crop') ? urlParams.get('crop').split(',') : ['whea'];
    document.getElementById("selectYear").value = year;
    document.getElementById("selectTech").value = tech;
    
    Array.from(selectCul.options).forEach(option => {
        option.selected = crops.includes(option.value); // Select the crops that are in the URL
    });
}

function update() {
    const selectedYear = document.getElementById("selectYear").value;
    const selectedTech = document.getElementById("selectTech").value;
    const options = Array.from(document.getElementById("selectCul").selectedOptions);
    const selectedCrops = options.map(option => option.value).join(',');

    const url = new URL(window.location.href);
    url.searchParams.set('year', selectedYear);
    url.searchParams.set('tech', selectedTech);
    url.searchParams.set('crop', selectedCrops);
    window.location.href = url.toString();
}

window.onload = setSelected;





