import re

with open('templates/creditos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Navbar links
old_nav = """        <div class="nav-links">
            <a href="#" class="active">INICIO</a>
            <a href="#">SOBRE MI</a>
            <a href="#">PROYECTOS</a>
            <a href="#">CONTACTO</a>
        </div>"""
new_nav = """        <div class="nav-links" id="mainNav">
            <a href="#" data-target="view-inicio" class="nav-btn active">INICIO</a>
            <a href="#" data-target="view-sobre-mi" class="nav-btn">SOBRE MI</a>
            <a href="#" data-target="view-proyectos" class="nav-btn">PROYECTOS</a>
            <a href="https://wa.me/51936461400" target="_blank">CONTACTO</a>
        </div>"""
if old_nav in content:
    content = content.replace(old_nav, new_nav)

# 2. Update the left content to support multiple views
old_left = """        <div class="content-left">
            <p class="greeting">HOLA, SOY</p>
            <h1 class="name-title">CARLOS<br>MARÍN</h1>
            <p class="roles">DESARROLLADOR WEB<br>Y CREADOR DIGITAL</p>
            <p class="description">
                Creo experiencias digitales elegantes, funcionales y con propósito.
            </p>
            <a href="#" class="btn-outline">VER PROYECTOS <i class="fas fa-arrow-right"></i></a>
        </div>"""

new_left = """        <div class="content-left">
            
            <!-- Vista Inicio -->
            <div id="view-inicio" class="view-section active">
                <p class="greeting">HOLA, SOY</p>
                <h1 class="name-title">CARLOS<br>MARÍN</h1>
                <p class="roles">DESARROLLADOR WEB<br>Y CREADOR DIGITAL</p>
                <p class="description">
                    Creo experiencias digitales elegantes, funcionales y con propósito.
                </p>
                <a href="#" data-target="view-proyectos" class="btn-outline nav-btn">VER PROYECTOS <i class="fas fa-arrow-right"></i></a>
            </div>

            <!-- Vista Sobre Mí -->
            <div id="view-sobre-mi" class="view-section d-none">
                <p class="greeting">SOBRE MÍ</p>
                <h2 class="name-title" style="font-size: 3.5rem;">Arquitecto de<br>Software</h2>
                <p class="roles">Ingeniería & Inteligencia Artificial</p>
                <p class="description" style="font-size: 0.95rem; line-height: 1.8; text-align: justify; max-width: 450px;">
                    Soy un apasionado de la ingeniería de software y la inteligencia artificial, enfocado en transformar ideas complejas en soluciones digitales eficientes, escalables y orientadas a la experiencia del usuario. <br><br>
                    Creo firmemente en la optimización continua, el código limpio y la adaptabilidad frente a los retos tecnológicos actuales. Mi objetivo es liderar y aportar valor en proyectos innovadores.
                </p>
            </div>

            <!-- Vista Proyectos -->
            <div id="view-proyectos" class="view-section d-none">
                <p class="greeting">PORTAFOLIO</p>
                <h2 class="name-title" style="font-size: 3.5rem;">Proyectos<br>Destacados</h2>
                <p class="roles">Desarrollo Integral & Lógica Avanzada</p>
                
                <div class="projects-list mt-4">
                    <div class="project-item mb-4">
                        <h4 class="text-white fw-bold mb-1" style="font-family: var(--font-serif); color: var(--text-gold); font-size: 1.4rem;">Lendora Web</h4>
                        <p class="description mb-0" style="font-size: 0.85rem;">Aplicación web desarrollada de manera integral, abarcando desde su modelado funcional hasta la implementación de su lógica y base de datos.</p>
                    </div>
                    <div class="project-item mb-4">
                        <h4 class="text-white fw-bold mb-1" style="font-family: var(--font-serif); color: var(--text-gold); font-size: 1.4rem;">Livacentro E-Commerce</h4>
                        <p class="description mb-0" style="font-size: 0.85rem;">Plataforma comercial moderna con experiencia de usuario optimizada y arquitectura escalable.</p>
                    </div>
                    <div class="project-item">
                        <h4 class="text-white fw-bold mb-1" style="font-family: var(--font-serif); color: var(--text-gold); font-size: 1.4rem;">Soporte TI DRAJ</h4>
                        <p class="description mb-0" style="font-size: 0.85rem;">Sistema de gestión de incidencias con dashboard analítico, modo oscuro integral y reportes PDF automatizados.</p>
                    </div>
                </div>
            </div>

        </div>"""
if old_left in content:
    content = content.replace(old_left, new_left)

# 3. Update Social Sidebar links
old_social = """    <div class="social-sidebar">
        <a href="#" title="Code"><i class="fas fa-code"></i></a>
        <a href="#" title="Website"><i class="fas fa-globe"></i></a>
        <a href="#" title="GitHub"><i class="fab fa-github"></i></a>
        <a href="#" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
    </div>"""

new_social = """    <div class="social-sidebar">
        <a href="https://wa.me/51936461400" target="_blank" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
        <a href="https://www.livacentro.com" target="_blank" title="Livacentro"><i class="fas fa-globe"></i></a>
        <a href="#" title="GitHub"><i class="fab fa-github"></i></a>
        <a href="https://www.linkedin.com/in/carlos-raul-marin-alarcon-b79935415/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
    </div>"""
if old_social in content:
    content = content.replace(old_social, new_social)

# 4. Add CSS and JS for the view switching
old_css_end = """        @media (max-width: 992px) {
            .name-title { font-size: 4rem; }
            .content-right { opacity: 0.3 !important; width: 100%; mask-image: none; -webkit-mask-image: none; }
            .content-left { z-index: 5; padding: 20px; }
            nav { padding: 20px; }
            .nav-links { display: none; }
            .social-sidebar { right: 20px; }
        }
    </style>"""

new_css_end = """        .view-section {
            transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .view-section.d-none {
            display: none;
            opacity: 0;
            transform: translateY(20px);
        }
        .view-section.active {
            display: block;
            opacity: 1;
            transform: translateY(0);
            animation: fadeUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        @media (max-width: 992px) {
            .name-title { font-size: 4rem !important; }
            .content-right { opacity: 0.3 !important; width: 100%; mask-image: none; -webkit-mask-image: none; }
            .content-left { z-index: 5; padding: 20px; }
            nav { padding: 20px; }
            .nav-links { display: none; }
            .social-sidebar { right: 20px; }
        }
    </style>"""
if old_css_end in content:
    content = content.replace(old_css_end, new_css_end)

script_js = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const navBtns = document.querySelectorAll('.nav-btn');
        const views = document.querySelectorAll('.view-section');

        navBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = btn.getAttribute('data-target');
                
                // Update nav active state (only if it's a top nav link)
                if(btn.parentElement.id === 'mainNav') {
                    navBtns.forEach(b => { if(b.parentElement.id === 'mainNav') b.classList.remove('active') });
                    btn.classList.add('active');
                }

                // Hide all views
                views.forEach(v => {
                    v.classList.remove('active');
                    v.classList.add('d-none');
                });

                // Show target view
                const targetView = document.getElementById(targetId);
                if(targetView) {
                    targetView.classList.remove('d-none');
                    // force reflow
                    void targetView.offsetWidth;
                    targetView.classList.add('active');
                }
            });
        });
    });
</script>
</body>"""

if "<script>" not in content:
    content = content.replace("</body>", script_js)

with open('templates/creditos.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated creditos.html with user data and interactive views.")
