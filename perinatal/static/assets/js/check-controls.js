document.addEventListener("DOMContentLoaded", function () {
    const fechaNacimientoInput = document.querySelector('#id_hcp_fechanacimiento_0006');
    const edadInput = document.querySelector('#id_hcp_edad_0009');
    const alfabetaRadios = document.querySelectorAll('input[name="hcp_alfabeta_0012"]');
    const estudiosRadios = document.querySelectorAll('input[name="hcp_estudios_0013"]');
    const inputAniosEstudios = document.querySelector('#id_hcp_aniosmayornivel_0014')


    alfabetaRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if (radio.value === 'N' && radio.checked) {
                estudiosRadios.forEach(estudioRadio => {
                    estudioRadio.disabled = true;
                    inputAniosEstudios.disabled = true;
                });
            } else {
                estudiosRadios.forEach(estudioRadio => {
                    estudioRadio.disabled = false;
                    inputAniosEstudios.disabled = false;
                });
            }
        });
    });

    estudiosRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if(radio.value === 'Ninguno' && radio.checked){
                inputAniosEstudios.disabled = true;
            } else {
                inputAniosEstudios.disabled = false;
            }
        });
    });



    fechaNacimientoInput.addEventListener('change', function () {
        const fechaNacimiento = new Date(this.value);
        const hoy = new Date();
        const diferencia = hoy - fechaNacimiento;
        const edad = Math.floor(diferencia / (1000 * 60 * 60 * 24 * 365.25));

        if (edad >= 0 && edad <= 100) {
            edadInput.value = edad;
        } else {
            edadInput.value = '';
        }

        if (edad < 15 || edad > 35) {
            edadInput.style.border = "2px solid red";
        } else {
            edadInput.style.border = "";
        }
    });

    
});
