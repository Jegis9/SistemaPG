document.addEventListener("DOMContentLoaded", function () {
  const servicioRadios = document.getElementsByName("servicio");
  const camposVarios = document.getElementById("campos-varios");
  const camposAmbulancia = document.getElementById("campos-ambulancia");
  const camposIncendios = document.getElementById("campos-incendios");

  function toggleCampos() {
    const selectedServicio = document.querySelector(
      'input[name="servicio"]:checked'
    );
    if (selectedServicio) {
      const valor = selectedServicio.value;
      // Ocultar todos los campos específicos
      camposVarios.style.display = "none";
      camposAmbulancia.style.display = "none";
      camposIncendios.style.display = "none";

      // Mostrar los campos correspondientes
      if (valor === "Varios") {
        camposVarios.style.display = "block";
      } else if (valor === "Ambulancia") {
        camposAmbulancia.style.display = "block";
      } else if (valor === "Incendios") {
        camposIncendios.style.display = "block";
      }
    }
  }

  // Convertir NodeList a Array para usar forEach
  Array.from(servicioRadios).forEach((radio) => {
    radio.addEventListener("change", toggleCampos);
  });

  // Ejecutar la función al cargar la página para manejar ediciones
  toggleCampos();
});
