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
    const startYear = urlParams.get('startYear') || '1995';
    const endYear = urlParams.get('endYear') || '2024';
    const groupBy = urlParams.get('groupBy') || 'default';
    const plotType = urlParams.get('plotType') || 'scatter';
    document.getElementById("selectStart").value = startYear;
    document.getElementById("selectEnd").value = endYear;
    document.getElementById("selectGroupBy").value = groupBy;
    document.getElementById("selectPlotType").value = plotType;
}

function update() {
    const selectedStartYear = document.getElementById("selectStart").value;
    const selectedEndYear = document.getElementById("selectEnd").value;
    const selectedGroupBy = document.getElementById("selectGroupBy").value;
    const selectedPlotType = document.getElementById("selectPlotType").value;
    if (parseInt(selectedStartYear) <= parseInt(selectedEndYear)) {
        const url = new URL(window.location.href);
        url.searchParams.set('startYear', selectedStartYear);
        url.searchParams.set('endYear', selectedEndYear);
        url.searchParams.set('groupBy', selectedGroupBy);
        url.searchParams.set('plotType', selectedPlotType);
        window.location.href = url.toString();
    } else {
        alert("Start Year greater that End Year")
    }
}

function setSelectedDays() {
    const urlParams = new URLSearchParams(window.location.search);
    const fcstDays = urlParams.get('fcstDays') || '90';
    document.getElementById("selectdays").value = fcstDays;
}

function updateDays() {
    const selectedDays = document.getElementById("selectdays").value;
    const url = new URL(window.location.href);
    url.searchParams.set('fcstDays', selectedDays);
    window.location.href = url.toString();
}

window.onload = function() {
    setSelected();
    setSelectedDays();
};

document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll("table tr");
    
    rows.forEach((row, index) => {
        if (index > 1) {
            const prevRow = rows[index - 1];
            const cells = row.querySelectorAll("td");
            const prevCells = prevRow.querySelectorAll("td");
            
            cells.forEach((cell, i) => {
                if (i > 0) {
                    const currentValue = parseFloat(cell.textContent);
                    const prevValue = parseFloat(prevCells[i].textContent);
                    
                    if (currentValue > prevValue) {
                        cell.classList.add("up");
                    } else if (currentValue < prevValue) {
                        cell.classList.add("down");
                    } else {
                        cell.classList.add("equal");
                    }
                }
            });
        }
    });
});









