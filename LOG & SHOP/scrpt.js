function login(){
    let username = document.getElementById('username').value
    let password = document.getElementById('password').value
    let saveduser = localStorage.getItem("username");
    let savedcode = localStorage.getItem("password");
    if(username ==  saveduser && password == savedcode){
        window.alert("Login Successful");
        window.location.href = "idx.html";
    }else{
        window.alert("Login Failed");
    }
}

function sign_up(){
    window.location.href = "signup.html";
}
function backLogin(){
    window.location.href = "index.html";
}

function signup(){
    let log = document.getElementById('log').value
    let code = document.getElementById('code').value

    if(log == "" && code == ""){
        window.alert("Please input your new sign up");
    }else{
        localStorage.setItem("username", log);
        localStorage.setItem("password", code);
        window.alert("your account has been created");
    }
}