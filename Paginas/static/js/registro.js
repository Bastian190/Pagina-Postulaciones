function validarFormulario() {
    // Limpiar mensajes de error previos
    limpiarErrores();

    // Obtener los valores de los campos
    const nombre = document.getElementById("nombre").value.trim();
    const apellido = document.getElementById("apellido").value.trim();
    const correo = document.getElementById("correo").value.trim();
    const password = document.getElementById("password").value.trim();
    const password1 = document.getElementById("password1").value.trim();
    
    // Expresión regular para la validación de la contraseña
    const passwordRegex = /^(?=.*[A-Z])(?=.*\W).{6,}$/;  // Al menos 6 caracteres, 1 mayúscula y 1 carácter especial
    
    let isValid = true;

    // Validar el campo de nombre
    if (nombre === "") {
        mostrarError("nombre", "El nombre no puede estar vacío.");
        isValid = false;
    }

    // Validar el campo de apellido
    if (apellido === "") {
        mostrarError("apellido", "El apellido no puede estar vacío.");
        isValid = false;
    }

    // Validar el correo electrónico
    if (correo === "") {
        mostrarError("correo", "El correo electrónico no puede estar vacío.");
        isValid = false;
    } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(correo)) {
        mostrarError("correo", "El correo electrónico no es válido.");
        isValid = false;
    }

    // Validar la contraseña
    if (password === "") {
        mostrarError("password", "La contraseña no puede estar vacía.");
        isValid = false;
    } else if (!passwordRegex.test(password)) {
        mostrarError("password", "La contraseña debe tener al menos 6 caracteres, una mayúscula y un carácter especial.");
        isValid = false;
    }

    // Validar la confirmación de la contraseña
    if (password1 === "") {
        mostrarError("password1", "Debes repetir la contraseña.");
        isValid = false;
    } else if (password !== password1) {
        mostrarError("password1", "Las contraseñas no coinciden.");
        isValid = false;
    }

    // Si hay algún error, no se envía el formulario
    return isValid;
}

// Función para mostrar el error en el campo
function mostrarError(campo, mensaje) {
    const input = document.getElementById(campo);
    const error = document.getElementById(campo + "Error");
    error.textContent = mensaje;
    input.classList.add("is-invalid");
}

// Función para limpiar los errores
function limpiarErrores() {
    const inputs = document.querySelectorAll(".form-control");
    inputs.forEach(input => {
        input.classList.remove("is-invalid");
    });
    const errores = document.querySelectorAll(".invalid-feedback");
    errores.forEach(error => {
        error.textContent = "";
    });
}