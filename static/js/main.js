document.addEventListener("DOMContentLoaded", function() {
    // Autocompletar fecha y hora actual en registro nuevo
    const fechaInput = document.getElementById('fecha_registro');
    const horaInput = document.getElementById('hora_registro');
    
    if(fechaInput && horaInput) {
        const now = new Date();
        
        // Formato YYYY-MM-DD
        const yyyy = now.getFullYear();
        const mm = String(now.getMonth() + 1).padStart(2, '0');
        const dd = String(now.getDate()).padStart(2, '0');
        fechaInput.value = `${yyyy}-${mm}-${dd}`;
        
        // Formato HH:MM
        const hh = String(now.getHours()).padStart(2, '0');
        const min = String(now.getMinutes()).padStart(2, '0');
        horaInput.value = `${hh}:${min}`;
        
        // Fechas automáticas también en inicio
        const fechaInicio = document.getElementById('fecha_inicio_atencion');
        if(fechaInicio) fechaInicio.value = fechaInput.value;
        
        // Fechas conformidad y responsable
        const confFecha = document.getElementById('conf_fecha');
        const respFecha = document.getElementById('resp_fecha');
        if(confFecha) confFecha.value = fechaInput.value;
        if(respFecha) respFecha.value = fechaInput.value;
    }

    // Efecto ripple en botones (Opcional, microanimaciones)
    const btns = document.querySelectorAll('.btn');
    btns.forEach(btn => {
        btn.addEventListener('mousedown', function(e){
            let ripple = document.createElement('span');
            ripple.classList.add('ripple-effect');
            this.appendChild(ripple);
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // --- DARK MODE LOGIC ---
    const htmlElement = document.documentElement;
    const themeToggleBtn = document.getElementById('darkModeToggle');
    const icon = themeToggleBtn ? themeToggleBtn.querySelector('i') : null;

    const currentTheme = localStorage.getItem('theme') || 'light';
    if (currentTheme === 'dark') {
        htmlElement.setAttribute('data-bs-theme', 'dark');
        if (icon) { icon.classList.remove('fa-moon'); icon.classList.add('fa-sun'); }
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const isDark = htmlElement.getAttribute('data-bs-theme') === 'dark';
            if (isDark) {
                htmlElement.setAttribute('data-bs-theme', 'light');
                localStorage.setItem('theme', 'light');
                if(icon) { icon.classList.remove('fa-sun'); icon.classList.add('fa-moon'); }
            } else {
                htmlElement.setAttribute('data-bs-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                if(icon) { icon.classList.remove('fa-moon'); icon.classList.add('fa-sun'); }
            }
        });
    }
});
