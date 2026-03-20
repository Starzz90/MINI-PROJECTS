const input = document.getElementById('input');
const list = document.getElementById('list');
const addbutton = document.getElementById('addbutton');
const headbutton = document.getElementById("headbutton");
const head = document.getElementById('head');
const Heads = document.getElementById('Heads');

addbutton.addEventListener('click', Check);
headbutton.addEventListener('click', change);

function change(){
    const Heads = document.getElementById('Heads').value.trim();

    if (Heads === ''){
        alert('Please enter a title');
        return;
    }

    document.getElementById('myH1').textContent = Heads;

}

function Check() {
    const Name = input.value.trim();

    if (Name === '') {
        alert('Please enter a name/item.');
        return;
    }

    const li = document.createElement('li');
    li.textContent = Name;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'X';
    deleteButton.classList.add('delete-button');
    deleteButton.addEventListener('click', function(e) {
        e.stopPropagation();
        li.remove();
    });

    const editButton = document.createElement('button');
    editButton.textContent = 'Edit';
    editButton.classList.add('edit-button');
    editButton.addEventListener('click', function(e) {
        e.stopPropagation();
        const newName = prompt('Edit name/item:', Name);
        if (newName !== null && newName.trim() !== '') {
            li.firstChild.textContent = newName.trim();
        }
    });

    li.appendChild(editButton);


    li.appendChild(deleteButton);
    list.appendChild(li);

    input.value = '';
}