document.addEventListener("DOMContentLoaded", function () {
    // Seleccionar el formulario
    const form = document.getElementById("form-subvencion");

    // Función para mostrar errores específicos debajo del campo
    const showError = (input, message) => {
        const errorDiv = document.createElement("div");
        errorDiv.className = "error-message";
        errorDiv.textContent = message;

        // Agregar el mensaje de error después del último input del grupo
        const parentDiv = input.closest(".form-group");
        if (parentDiv && !parentDiv.querySelector(".error-message")) {
            parentDiv.appendChild(errorDiv);
        }
    };

    // Función para limpiar errores previos
    const clearErrors = () => {
        document.querySelectorAll(".error-message").forEach(el => el.remove());
    };

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Detener el envío del formulario

        // Limpiar errores previos
        clearErrors();

        // Variable para rastrear si hay errores
        let isValid = true;

        // Lista de campos obligatorios (excepto las cotizaciones)
        const requiredFields = [
            { name: "formulario", label: "Formulario de Postulación" },
            { name: "rut_organizacion", label: "RUT de la organización" },
            { name: "ci_representante", label: "Cédula de Identidad del Representante" },
            { name: "certificado_personalidad", label: "Certificado de Personalidad Jurídica" },
            { name: "certificado_fondos", label: "Certificado de Fondos Públicos" },
            { name: "cuenta_corriente", label: "Fotocopia de la Cuenta Corriente" },
        ];

        // Validar cada campo obligatorio
        requiredFields.forEach(field => {
            const input = form.querySelector(`[name="${field.name}"]`);
            if (!input || input.files.length === 0) {
                isValid = false;
                showError(input, `${field.label} es obligatorio.`);
            }
        });

        // Validar las cotizaciones como un grupo
        const cotizacionInputs = form.querySelectorAll(`[name="cotizaciones[]"]`);
        let cotizacionesValidas = true;
        cotizacionInputs.forEach(input => {
            if (!input || input.files.length === 0) {
                cotizacionesValidas = false;
            }
        });

        if (!cotizacionesValidas) {
            isValid = false;
            // Mostrar un solo mensaje de error para ambas cotizaciones
            const firstCotizacionInput = cotizacionInputs[0];
            showError(firstCotizacionInput, `Ambas cotizaciones son obligatorias.`);
        }

        // Validación para el campo "Acreditación de Propiedad" (opcional)
        const acreditacionInput = form.querySelector('[name="acreditacion_propiedad"]');
        if (acreditacionInput && acreditacionInput.files.length > 0 && acreditacionInput.files[0].type !== "application/pdf") {
            isValid = false;
            showError(acreditacionInput, `La Acreditación de Propiedad debe ser un archivo PDF.`);
        }

        // Validación para los campos "Otros Documentos" (opcional)
        const otrosDocumentosInputs = form.querySelectorAll('[name="otros_documentos[]"]');
        if (otrosDocumentosInputs.length > 0) {
            let otrosDocumentosValidos = true;
            otrosDocumentosInputs.forEach(input => {
                if (input.files.length > 0 && !Array.from(input.files).every(file => file.type === "application/pdf" || file.type.startsWith("image/"))) {
                    otrosDocumentosValidos = false;
                }
            });
            if (!otrosDocumentosValidos) {
                isValid = false;
                showError(otrosDocumentosInputs[0], `Los archivos de "Otros Documentos" deben ser PDF o imágenes.`);
            }
        }

        // Si no es válido, mostrar mensaje
        if (!isValid) {
            alert("Por favor complete todos los campos obligatorios.");
        } else {
            alert("Formulario validado correctamente.");
            form.submit(); // Envía el formulario manualmente si es válido
        }
    });
});
