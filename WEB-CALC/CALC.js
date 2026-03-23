let display = document.getElementById('display')

function getNumber(num){
    display.value += num;
}

function clearDisplay(){
    display.value = '';
}

//operator basic//

function checkOperator(op){
    if(display.value == ''){
        return;
    }
    
    const char = display.value.slice(-1);
    if('+-*/'.includes(char)) return;
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

function results(){
    try{
        var result = eval(display.value);
        display.value = result
        
    }catch{
        display.value = "Error"; 
    }
}
function phi(op){
    display.value = Math.PI;
}

function append(op){
    display.value += op;
}
