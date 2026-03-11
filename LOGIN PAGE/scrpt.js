function login(){
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    
    if(username == "Enzo" && password == "SuperCat"){
        alert("Login Successful");
    }else{
        alert("Login Failed");
    }
}