window.addEventListener('scroll', function () {
    const scrollPosition = window.scrollY;

    const div = document.querySelector('#content_text');
    const searchscroll = document.querySelector('.search_scroll');
    const divPosition = div.offsetTop;

    const divHeight = div.offsetHeight;

    if (scrollPosition >= divPosition + divHeight) {
        searchscroll.style.display = 'flex';

    } else {
        searchscroll.style.display = 'none';
    }
});


window.addEventListener('load', updateChildHeight);
window.addEventListener('resize', updateChildHeight);

function updateChildHeight() {
    const parentDiv = document.querySelector('header');
    const childDiv = document.querySelector('.search');

    const parentHeight = parentDiv.offsetHeight;

    childDiv.style.top = (parentHeight - 45) + 'px';
}

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visit');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5
});

const items = document.querySelectorAll('.li');
items.forEach(item => {
    observer.observe(item);
});

const hidden = document.querySelector('.hidden');
const add = document.querySelector('.add');
const addBox = document.querySelector('.add_box');
const searchs = document.querySelectorAll('.search');
const searchBox = document.querySelector('.search_box');
const deleteBtns = document.querySelectorAll('.delete-btn');
const deleteBoxs = document.querySelectorAll('.delete_box');
const box_completes = document.querySelectorAll('.box_complete');
const firstLogin = document.querySelector('.first_login');
const firstForm = document.querySelector('.login_form');
const firstSign = document.querySelector('.signup_form');
const moveSign = document.getElementById('signup');
const movesLogin = document.querySelectorAll('#login');
const loginBtns = document.querySelectorAll('#login_btn');
const closeButtons = document.querySelectorAll('.close');

function saveState() {
    sessionStorage.setItem('firstForm', firstForm.style.display);
    sessionStorage.setItem('firstSign', firstSign.style.display);
    sessionStorage.setItem('addBox', addBox.style.display);
    sessionStorage.setItem('searchBox', searchBox.style.display);
    if (deleteBoxs) {
        deleteBoxs.forEach(deleteBox => {
            sessionStorage.setItem('deleteBox', deleteBox.style.display);
        });
    }
    sessionStorage.setItem('hidden', hidden.style.display);
}

function loadState() {
    firstForm.style.display = sessionStorage.getItem('firstForm') || 'none';
    firstSign.style.display = sessionStorage.getItem('firstSign') || 'none';
    addBox.style.display = sessionStorage.getItem('addBox') || 'none';
    searchBox.style.display = sessionStorage.getItem('searchBox') || 'none';
    if (deleteBoxs) {
        deleteBoxs.forEach(deleteBox => {
            deleteBox.style.display = sessionStorage.getItem('deleteBox') || 'none';
        });
    }
    hidden.style.display = sessionStorage.getItem('hidden') || 'none';
}

loadState();

if (firstLogin) {
    firstLogin.addEventListener("click", () => {
        firstForm.style.display = 'flex';
        hidden.style.display = 'block';
        saveState();
    });
}

moveSign.addEventListener("click", () => {
    firstForm.style.display = 'none';
    firstSign.style.display = 'flex';
    hidden.style.display = 'block';
    saveState();
});

movesLogin.forEach(moveLogin => {
    moveLogin.addEventListener("click", () => {
        firstForm.style.display = 'flex';
        firstSign.style.display = 'none';
        hidden.style.display = 'block';
        saveState();
    });
});

searchs.forEach(search => {
    search.addEventListener("click", () => {
        searchBox.style.display = 'flex';
        hidden.style.display = 'block';
        saveState();
    });
});

add.addEventListener("click", () => {
    addBox.style.display = 'flex';
    hidden.style.display = 'block';
    saveState();
});

closeButtons.forEach(closeButton => {
    closeButton.addEventListener("click", () => {
        firstForm.style.display = 'none';
        firstSign.style.display = 'none';
        searchBox.style.display = 'none';
        if (deleteBoxs) {
            deleteBoxs.forEach(deleteBox => {
                deleteBox.style.display = 'none';
            });
        }
        addBox.style.display = 'none';
        hidden.style.display = 'none';
        saveState();
    });
});

deleteBtns.forEach(button => {
    let id = button.getAttribute('data-sms-id');
    const self_delete_box = document.getElementById(`number${id}`);

    button.addEventListener('click', () => {
        if (self_delete_box) {
            self_delete_box.style.display = 'flex';
        }
        hidden.style.display = 'block';
        saveState();
    });
});

box_completes.forEach(box_complete => {
    box_complete.addEventListener("click", () => {
        if (deleteBoxs) {
            deleteBoxs.forEach(deleteBox => {
                deleteBox.style.display = 'none';
            });
        }
        searchBox.style.display = 'none';
        addBox.style.display = 'none';
        hidden.style.display = 'none';
        saveState();
    });
});

const usernames = document.querySelectorAll('.self_username');

function validatePhoneNumber(phoneNumber) {
    let errors = [];
    const phoneRegex = /^[0-9]{10}$/;

    if (!/^\d+$/.test(phoneNumber)) {
        errors.push("شماره موبایل باید فقط شامل اعداد باشد.");
    }

    if (!phoneRegex.test(phoneNumber)) {
        errors.push("شماره موبایل باید دقیقاً 10 رقمی باشد.");
    }

    usernames.forEach(user => {        
        if (user.innerHTML == phoneNumber) {
            errors.push("کاربری با این شماره ثبت نام کرده است!");
        }
    });

    if (errors.length > 0) {
        return errors.join("\n");
    }

    return "شماره موبایل معتبر است.";
}

function validatePass(pass1, pass2) {
    let errors = [];

    if (pass1 !== pass2) {
        errors.push("فیلد تکرار رمز یکسان نیست.")
    }

    if (errors.length > 0) {
        return errors.join("\n");
    }

    return "شماره موبایل معتبر است.";
}

function validateForm() {
    const phoneNumber = document.getElementById('phone_number');
    const phoneValue = phoneNumber.value.trim();
    const pass1 = document.getElementById('password1').value;
    const pass2 = document.getElementById('password2').value;
    

    const validationMessage1 = validatePhoneNumber(phoneValue);
    const validationMessage3 = validatePass(pass1, pass2);

    if (validationMessage1 !== "شماره موبایل معتبر است.") {
        alert(validationMessage1);
        return false;
    } if (validationMessage3 !== "شماره موبایل معتبر است.") {
        alert(validationMessage3)
        return false
    } else {
        firstForm.style.display = 'none';
        firstSign.style.display = 'none';
        hidden.style.display = 'none';
        saveState();

        return true;
    }
}

function validateLogin() {
    firstForm.style.display = 'none';
    firstSign.style.display = 'none';
    hidden.style.display = 'none';
    saveState();

    return true;
}