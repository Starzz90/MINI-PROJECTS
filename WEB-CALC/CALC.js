let display = document.getElementById('display')

function getNumber(num){
    display.value += num;
}

function clearDisplay(){
    display.value = '';
}

//operator basic//

function checkOperator(op){
    display.value += op;
}
function Checks(op){
    if(display.value == ''){
        return;
}
    const char = display.value.slice(-1);
    if('*/'.includes(char)) return;
    display.value += op;
}

function sqrt(op){
    if(display.value == ''){
        return;
}
    const char = display.value.slice(-1);
    if('+-*/'.includes(char)) return;
    display.value =  Math.sqrt(display.value);
}

function power(op){
    if(display.value === ''){
        return;
    }
    const char = display.value.slice(-1);
    if('+-*/'.includes(char)) return;
    display.value += op;

}

function sin(){
    if(display.value === ""){
        return;
    }
    else{
        display.value = Math.sin(display.value);
    }
}
function cos(){
    if(display.value === ""){
        return;
    }
    else{
        display.value = Math.cos(display.value);
    }
}function tan(){
    if(display.value === ""){
        return;
    }
    else{
        display.value = Math.tan(display.value);
    }
}function Log(){
    display.value = Math.log(display.value);
}
function results(){
    try{
        var result = eval(display.value);
        display.value = result
        
    }catch{
        display.value = "Error"; 
    }
}
function phi(){
    display.value = Math.PI;
}

function append(op){
    display.value += op;
}
