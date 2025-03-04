
    document.querySelector('.user-icon').addEventListener('click', function (e) {
        const userOptions = document.querySelector('.user-options');
        userOptions.style.display = (userOptions.style.display === 'block') ? 'none' : 'block';
        e.preventDefault(); // Evita que se siga el enlace al hacer clic
    });

    document.addEventListener('click', function (e) {
        const userOptions = document.querySelector('.user-options');
        const userMenu = document.querySelector('.user-menu');
        if (!userMenu.contains(e.target)) {
            userOptions.style.display = 'none'; // Cierra el menú si se hace clic fuera de él
        }
    });

