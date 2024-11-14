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

const users = document.querySelectorAll('.user');

function validatePassword(password) {
    const minLength = 6;
    let errors = [];

    if (password.length < minLength) {
        errors.push("رمز عبور باید حداقل " + minLength + " کاراکتر باشد.");
    }

    if (!/[A-Z]/.test(password) || !/[a-z]/.test(password)) {
        errors.push("رمز عبور باید شامل حداقل یک حرف بزرگ و یک حرف کوچک باشد.");
    }

    if (errors.length > 0) {
        return errors.join("\n");
    }

    return "رمز عبور معتبر است.";
}

function validatePhoneNumber(phoneNumber) {
    let errors = [];
    const phoneRegex = /^[0-9]{10}$/;

    if (!/^\d+$/.test(phoneNumber)) {
        errors.push("شماره موبایل باید فقط شامل اعداد باشد.");
    }

    if (!phoneRegex.test(phoneNumber)) {
        errors.push("شماره موبایل باید دقیقاً 10 رقمی باشد.");
    }

    users.forEach(user => {
        if (user.innerHTML == phoneNumber) {
            errors.push("کاربری با این شماره ثبت نام کرده است!");
        }
    });

    if (errors.length > 0) {
        return errors.join("\n");
    }

    return "شماره موبایل معتبر است.";
}

function validatePhoneNumber2(phoneNumber) {
    let errors = [];
    let user_phones = [];

    users.forEach(user => {
        let user_phone = user.innerHTML;
        user_phones.push(user_phone);
    });

    if (!user_phones.includes(phoneNumber)) {
        errors.push("کاربری با این شماره یافت نشد!");
    }

    if (errors.length > 0) {
        return errors.join("\n");
    }

    return "شماره موبایل معتبر است.";
}

function validateForm() {
    const password = document.getElementById('password').value;
    const phoneNumber = document.getElementById('phone_number');
    const phoneValue = phoneNumber.value.trim();

    const validationMessage = validatePassword(password);
    const validationMessage2 = validatePhoneNumber(phoneValue);

    if (validationMessage !== "رمز عبور معتبر است.") {
        alert(validationMessage);
        return false;
    } if (validationMessage2 !== "شماره موبایل معتبر است.") {
        alert(validationMessage2);
        return false;
    } else {
        firstForm.style.display = 'flex';
        firstSign.style.display = 'none';
        hidden.style.display = 'block';
        saveState();

        return true;
    }
}

function validateLogin() {
    const phoneNumber = document.getElementById('phone_number2');
    const phoneValue = phoneNumber.value.trim();

    const validationMessage2 = validatePhoneNumber2(phoneValue);

    if (validationMessage2 !== "شماره موبایل معتبر است.") {
        alert(validationMessage2);

        return false;
    } else {
        firstForm.style.display = 'none';
        firstSign.style.display = 'none';
        hidden.style.display = 'none';
        saveState();

        return true;
    }
}