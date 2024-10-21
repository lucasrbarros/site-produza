// const wrapper = document.querySelector('.wrapper');
// const loginLink = document.querySelector('.login-link');
// const btnPopup = document.querySelector('.btnLogin')

// loginLink.addEventListener('click', ()=> {
//     wrapper.classList.remove('active');
// });

// btnPopup.addEventListener('click', ()=> {
//     wrapper.classList.remove('active-popup');
// });

window.addEventListener('scroll', () => {
    const menu = document.querySelector('#menu');  // Certifique-se de que o seletor está correto.
    console.log('ScrollY:', window.scrollY);  // Verifique se o evento está disparando.

    if (window.scrollY > 10) {
        menu.classList.add('menu-scrolled');
    } else {
        menu.classList.remove('menu-scrolled');
    }
});

window.addEventListener('scroll', () => {
    const navigation = document.querySelector('#navigation');  // Certifique-se de que o seletor está correto.
    console.log('ScrollY:', window.scrollY);  // Verifique se o evento está disparando.

    if (window.scrollY > 10) {
        navigation.classList.add('navigation-scrolled');
    } else {
        navigation.classList.remove('navigation-scrolled');
    }
});



