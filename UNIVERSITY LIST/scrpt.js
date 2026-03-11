const universityinput = document.getElementById('universityinput');
const universitylist = document.getElementById('universitylist');
const addbutton = document.getElementById('addbutton');

addbutton.addEventListener('click', CheckUniversity);

function CheckUniversity() {
    const universityName = universityinput.value.trim();

    if (universityName === '') {
        alert('Please enter a university name.');
        return;
    }

    const li = document.createElement('li');
    li.textContent = universityName;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'X';
    deleteButton.classList.add('delete-button');
    deleteButton.addEventListener('click', function(e) {
        e.stopPropagation();
        li.remove();
    });

    li.appendChild(deleteButton);
    universitylist.appendChild(li);

    universityinput.value = '';
}