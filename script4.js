const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const main_signup = document.getElementById('main_signup');
const body=document.querySelector('body');
const data_container = document.querySelector('.data-container')

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
    body.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
    body.classList.remove("right-panel-active");
});

main_signup.addEventListener('click',()=>{
    data_container.classList.add('active');
});


