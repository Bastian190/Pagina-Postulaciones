// Función para validar el formulario
function validarFormulario() {
    // Obtener los valores de los inputs
    const usuario = document.getElementById("usuario").value.trim();
    const password = document.getElementById("password").value.trim();

    // Limpiar mensajes de error previos
    limpiarErrores();

    // Validar el campo de usuario
    if (usuario === "") {
        document.getElementById("usuarioError").textContent = "El campo de usuario no puede estar vacío.";
        document.getElementById("usuario").classList.add("is-invalid");
        return false;
    }
    if (usuario.length < 4) {
        document.getElementById("usuarioError").textContent = "El usuario debe tener al menos 4 caracteres.";
        document.getElementById("usuario").classList.add("is-invalid");
        return false;
    }

    // Validar el campo de contraseña
    if (password === "") {
        document.getElementById("passwordError").textContent = "El campo de contraseña no puede estar vacío.";
        document.getElementById("password").classList.add("is-invalid");
        return false;
    }
    if (password.length < 6) {
        document.getElementById("passwordError").textContent = "La contraseña debe tener al menos 6 caracteres.";
        document.getElementById("password").classList.add("is-invalid");
        return false;
    }

    // Si pasa todas las validaciones, enviar el formulario
    return true;
}

// Limpiar los mensajes de error y las clases de validación
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