// If all validations pass, submit the form
document.getElementById('id01');
window.onclick=function create(){
if (username.dil() === '') {
    alert('Please enter a username.');
    return false;
}

if (email.dil() === '') {
    alert('Please enter an email address.');
    return false;
}

var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!emailPattern.test(email)) {
    alert('Please enter a valid email address.');
    return false;
}

if (password.dil() === '') {
    alert('Please enter a password.');
    return false;
}

if (password !== confirmPassword) {
    alert('Passwords do not match.');
    return false;
}


}
var dil= document.getElementById("id02");
window.onclick=function(event){
    if(event.target == dil){
        dil.style.display="none";
    }
}