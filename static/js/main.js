async function fetchSearchResults(substring) {
    try {
        const response = await fetch(`/search-item?substring=${encodeURIComponent(substring)}`);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        displayResults(data);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

function displayResults(results) {
    console.log(results);
    const returnDIV = document.getElementById('display');
    returnDIV.innerHTML = '';

    if (results.length === 0) {
        returnDIV.innerHTML = '<p>No items found.</p>';
    } else {
        const items = processPaths(results); // Use 'results' instead of 'data'
        items.forEach(item => createItem(item.name, item.type));
    }
}

document.getElementById('search-btn').addEventListener('click', () => {
    const searchInput = document.getElementById('item-name-input');
    const substring = searchInput.value.trim();
    if (substring) {
        fetchSearchResults(substring);
    } else {
        alert('Please enter a search substring.');
    }
});

function getNameFromPath(path) {
    // Normalize the path to use forward slashes
    const normalizedPath = path.replace(/\\/g, '/');
    // Split the path by '/' and get the last part
    const parts = normalizedPath.split('/');
    return parts[parts.length - 1];
}

function determineType(name) {
    // Check if the name contains a period (indicating a file extension)
    return name.includes('.') ? 'file' : 'folder';
}

function processPaths(paths) {
    return paths.map(path => {
        const name = getNameFromPath(path);
        const type = determineType(name);
        return { name, type };
    });
}

function createItem(name, type) {
    const itemDiv = document.createElement('div');
    itemDiv.classList.add('item');

    const imageSpan = document.createElement('span');
    imageSpan.classList.add('item-image');

    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");

    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("stroke", "#000000");
    path.setAttribute("stroke-width", "1.5");
    path.setAttribute("stroke-linecap", "round");
    path.setAttribute("stroke-linejoin", "round");

    if (type === 'folder') {
        itemDiv.setAttribute("type", "folder");
        path.setAttribute("d", "M6 3H8C8.69805 3.00421 9.38286 3.19101 9.98634 3.54187C10.5898 3.89273 11.091 4.39545 11.44 5C11.797 5.60635 12.3055 6.10947 12.9156 6.46008C13.5256 6.8107 14.2164 6.99678 14.92 7H18C19.0609 7 20.0783 7.42136 20.8284 8.17151C21.5786 8.92165 22 9.93913 22 11V17C22 18.0609 21.5786 19.0782 20.8284 19.8284C20.0783 20.5785 19.0609 21 18 21H6C4.93913 21 3.92172 20.5785 3.17157 19.8284C2.42142 19.0782 2 18.0609 2 17V7C2 5.93913 2.42142 4.92165 3.17157 4.17151C3.92172 3.42136 4.93913 3 6 3Z");
        path.setAttribute("stroke-width", "2.5");
    } else if (type === 'file') {
        itemDiv.setAttribute("type", "file");
        path.setAttribute("d", "M13 3L13.7071 2.29289C13.5196 2.10536 13.2652 2 13 2V3ZM19 9H20C20 8.73478 19.8946 8.48043 19.7071 8.29289L19 9ZM13.109 8.45399L14 8V8L13.109 8.45399ZM13.546 8.89101L14 8L13.546 8.89101ZM10 13C10 12.4477 9.55228 12 9 12C8.44772 12 8 12.4477 8 13H10ZM8 16C8 16.5523 8.44772 17 9 17C9.55228 17 10 16.5523 10 16H8ZM8.5 9C7.94772 9 7.5 9.44772 7.5 10C7.5 10.5523 7.94772 11 8.5 11V9ZM9.5 11C10.0523 11 10.5 10.5523 10.5 10C10.5 9.44772 10.0523 9 9.5 9V11ZM8.5 6C7.94772 6 7.5 6.44772 7.5 7C7.5 7.55228 7.94772 8 8.5 8V6ZM9.5 8C10.0523 8 10.5 7.55228 10.5 7C10.5 6.44772 10.0523 6 9.5 6V8ZM17.908 20.782L17.454 19.891L17.454 19.891L17.908 20.782ZM18.782 19.908L19.673 20.362L18.782 19.908ZM5.21799 19.908L4.32698 20.362H4.32698L5.21799 19.908ZM6.09202 20.782L6.54601 19.891L6.54601 19.891L6.09202 20.782ZM6.09202 3.21799L5.63803 2.32698L5.63803 2.32698L6.09202 3.21799ZM5.21799 4.09202L4.32698 3.63803L4.32698 3.63803L5.21799 4.09202ZM12 3V7.4H14V3H12ZM14.6 10H19V8H14.6V10ZM12 7.4C12 7.66353 11.9992 7.92131 12.0169 8.13823C12.0356 8.36682 12.0797 8.63656 12.218 8.90798L14 8C14.0293 8.05751 14.0189 8.08028 14.0103 7.97537C14.0008 7.85878 14 7.69653 14 7.4H12ZM14.6 8C14.3035 8 14.1412 7.99922 14.0246 7.9897C13.9197 7.98113 13.9425 7.9707 14 8L13.092 9.78201C13.3634 9.92031 13.6332 9.96438 13.8618 9.98305C14.0787 10.0008 14.3365 10 14.6 10V8ZM12.218 8.90798C12.4097 9.2843 12.7157 9.59027 13.092 9.78201L14 8V8L12.218 8.90798ZM8 13V16H10V13H8ZM8.5 11H9.5V9H8.5V11ZM8.5 8H9.5V6H8.5V8ZM13 2H8.2V4H13V2ZM4 6.2V17.8H6V6.2H4ZM8.2 22H15.8V20H8.2V22ZM20 17.8V9H18V17.8H20ZM19.7071 8.29289L13.7071 2.29289L12.2929 3.70711L18.2929 9.70711L19.7071 8.29289ZM15.8 22C16.3436 22 16.8114 22.0008 17.195 21.9694C17.5904 21.9371 17.9836 21.8658 18.362 21.673L17.454 19.891C17.4045 19.9162 17.3038 19.9539 17.0322 19.9761C16.7488 19.9992 16.3766 20 15.8 20V22ZM18 17.8C18 18.3766 17.9992 18.7488 17.9761 19.0322C17.9539 19.3038 17.9162 19.4045 17.891 19.454L19.673 20.362C19.8658 19.9836 19.9371 19.5904 19.9694 19.195C20.0008 18.8114 20 18.3436 20 17.8H18ZM18.362 21.673C18.9265 21.3854 19.3854 20.9265 19.673 20.362L17.891 19.454C17.7951 19.6422 17.6422 19.7951 17.454 19.891L18.362 21.673ZM4 17.8C4 18.3436 3.99922 18.8114 4.03057 19.195C4.06287 19.5904 4.13419 19.9836 4.32698 20.362L6.10899 19.454C6.0838 19.4045 6.04612 19.3038 6.02393 19.0322C6.00078 18.7488 6 18.3766 6 17.8H4ZM8.2 20C7.62345 20 7.25117 19.9992 6.96784 19.9761C6.69617 19.9539 6.59545 19.9162 6.54601 19.891L5.63803 21.673C6.01641 21.8658 6.40963 21.9371 6.80497 21.9694C7.18864 22.0008 7.65645 22 8.2 22V20ZM4.32698 20.362C4.6146 20.9265 5.07354 21.3854 5.63803 21.673L6.54601 19.891C6.35785 19.7951 6.20487 19.6422 6.10899 19.454L4.32698 20.362ZM8.2 2C7.65645 2 7.18864 1.99922 6.80497 2.03057C6.40963 2.06287 6.01641 2.13419 5.63803 2.32698L6.54601 4.10899C6.59545 4.0838 6.69617 4.04612 6.96784 4.02393C7.25117 4.00078 7.62345 4 8.2 4V2ZM6 6.2C6 5.62345 6.00078 5.25117 6.02393 4.96784C6.04612 4.69617 6.0838 4.59545 6.10899 4.54601L4.32698 3.63803C4.13419 4.01641 4.06287 4.40963 4.03057 4.80497C3.99922 5.18864 4 5.65645 4 6.2H6ZM5.63803 2.32698C5.07354 2.6146 4.6146 3.07354 4.32698 3.63803L6.10899 4.54601C6.20487 4.35785 6.35785 4.20487 6.54601 4.10899L5.63803 2.32698Z");
        path.setAttribute("stroke-width", "0.5");
        path.setAttribute("fill", "#000000")
    }

    svg.appendChild(path);
    imageSpan.appendChild(svg);

    const nameP = document.createElement('p');
    nameP.textContent = name;
    nameP.setAttribute("style", "font-weight: bolder;");

    itemDiv.appendChild(imageSpan);
    itemDiv.appendChild(nameP);

    document.getElementById('display').appendChild(itemDiv);
}

function disableFolder() {
    const container = document.getElementById('display');

    for (let i = 0; i < container.children.length; i++) {
        const child = container.children[i];
        if (child.getAttribute('type') === "folder") {
            child.style.display = "none";
        }
    }
}

function ableFolder() {
    const container = document.getElementById('display');

    for (let i = 0; i < container.children.length; i++) {
        const child = container.children[i];
        if (child.getAttribute('type') === "folder") {
            child.style.display = "flex";
        }
    }
}

function disableFile() {
    const container = document.getElementById('display');

    for (let i = 0; i < container.children.length; i++) {
        const child = container.children[i];
        if (child.getAttribute('type') === "file") {
            child.style.display = "none";
        }
    }
}

function ableFile() {
    const container = document.getElementById('display');

    for (let i = 0; i < container.children.length; i++) {
        const child = container.children[i];
        if (child.getAttribute('type') === "file") {
            child.style.display = "flex";
        }
    }
}

function createFilter(txt, funcActive, funcDeactive) {
    const div = document.createElement('div');
    div.classList.add('option');
    div.setAttribute('data-state', 'deactive');  // Use a custom data attribute

    div.textContent = txt;
    div.onclick = function() {
        function toggleFilter() {
            if (div.getAttribute('data-state') === 'deactive') {
                div.style.backgroundColor = 'rgb(87, 87, 87)';
                div.style.color = 'white';
                div.setAttribute('data-state', 'active');
                funcActive();
            } else if (div.getAttribute('data-state') === 'active') {
                div.style.backgroundColor = 'rgb(250, 250, 250)';
                div.style.color = 'black';
                div.setAttribute('data-state', 'deactive');
                funcDeactive();
            }
        }
        toggleFilter();
    }
    const parent = document.getElementById('options');
    parent.appendChild(div);
}

const option = [
    { "txt": "Files Only", "funcA": disableFolder, "funcD": ableFolder },
    { "txt": "Folders Only", "funcA": disableFile, "funcD": ableFile}
];

option.forEach(item => createFilter(item.txt, item.funcA, item.funcD));