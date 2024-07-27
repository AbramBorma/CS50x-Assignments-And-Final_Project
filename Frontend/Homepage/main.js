// Getting all the Lists in my page

let switchedLis = document.querySelectorAll(".switch li");
let images = Array.from(document.getElementsByClassName("img-fluid"));

switchedLis.forEach((li) => {
    li.addEventListener('click', removeActiveClass);
    li.addEventListener('click', manageImages)
});

function removeActiveClass ()
{
    switchedLis.forEach((li) => {
        li.classList.remove("active"); // Removed the dot before "active"
    });
    this.classList.add("active"); // Removed the dot before "active"
};

function manageImages()
{
    images.forEach((img) => {
        if (!img.classList.contains(this.dataset.work.slice(1))) {
            img.parentElement.parentElement.style.display = 'none';
        } else {
            img.parentElement.parentElement.style.display = 'block';
        }
    });
}

let currentYear = new Date().getFullYear();

document.getElementById('date').innerHTML = currentYear;

let submit = document.querySelector('.submit');
let subscribe = document.querySelector('.subscribe');

submit.addEventListener('click', function (event)
{
    event.preventDefault(); // Prevent the form from submitting
    if (subscribe.value === '')
    {
        alert("Enter a Valid Email Address...");
    }
    else
    {
        subscribe.value = '';
    }
});

// Form

(() => {

    'use strict'
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
        }

        form.classList.add('was-validated')
    }, false)
    })
})()