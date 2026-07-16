var update = document.getElementById('update');
var body2 = document.querySelector('.body-2');
if(update){
    update.addEventListener('click', function(e){
        body2.style.display = 'block';
    });
};