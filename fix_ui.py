import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix "Nuevo Registro Admin" button visibility (remove nav-link to prevent white-on-white text)
old_nuevo = """                    <li class="nav-item">
                        <a class="nav-link btn btn-light text-success ms-lg-2 px-4 rounded-pill fw-bold hover-scale shadow-sm" href="{{ url_for('nuevo') }}" style="padding: 8px 16px !important;">
                            <i class="fas fa-plus-circle me-1"></i> Nuevo Registro Admin
                        </a>
                    </li>"""
new_nuevo = """                    <li class="nav-item ms-lg-2">
                        <a class="btn bg-white text-success px-4 rounded-pill fw-bold hover-scale shadow-sm d-flex align-items-center" href="{{ url_for('nuevo') }}" style="padding: 8px 16px !important; border: 1px solid rgba(25,135,84,0.2);">
                            <i class="fas fa-plus-circle me-2"></i> Nuevo Registro Admin
                        </a>
                    </li>"""
if old_nuevo in content:
    content = content.replace(old_nuevo, new_nuevo)


# 2. Put the dark mode toggle back in the navbar elegantly
old_logout = """                    <li class="nav-item">
                        <a class="nav-link nav-link-custom text-warning ms-lg-2" href="{{ url_for('logout') }}" title="Cerrar Sesión">
                            <i class="fas fa-sign-out-alt"></i> Salir
                        </a>
                    </li>"""
new_logout = """                    <li class="nav-item">
                        <a class="nav-link nav-link-custom text-warning ms-lg-2" href="{{ url_for('logout') }}" title="Cerrar Sesión">
                            <i class="fas fa-sign-out-alt"></i> Salir
                        </a>
                    </li>
                    <li class="nav-item ms-lg-3">
                        <div class="dark-mode-toggle" id="theme-toggle" title="Alternar Modo Oscuro" style="position: static; box-shadow: none; width: 38px; height: 38px; background: rgba(255,255,255,0.2); border: none;">
                            <i class="fas fa-moon" id="theme-icon"></i>
                        </div>
                    </li>"""
if old_logout in content:
    content = content.replace(old_logout, new_logout)

# 3. Remove the floating toggle from the bottom
old_floating = """    {% if session.get('user_id') %}
    <div class="dark-mode-toggle" id="theme-toggle" title="Alternar Modo Oscuro">
        <i class="fas fa-moon" id="theme-icon"></i>
    </div>
    {% endif %}"""
if old_floating in content:
    content = content.replace(old_floating, "")

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 4. Make the Robot widget prettier in dashboard.html and just "v1.0.1"
with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    dash_content = f.read()

old_robot = """        <!-- Robot Widget -->
        <div class="d-flex justify-content-end mb-3">
            <div class="d-inline-flex align-items-center bg-white shadow-sm px-3 py-2 rounded-pill border" style="border-color: rgba(0,0,0,0.05) !important;">
                <div class="rounded-circle bg-primary bg-opacity-10 d-flex align-items-center justify-content-center me-2" style="width: 30px; height: 30px;">
                    <i class="fas fa-robot text-primary fa-sm heartbeat-robot"></i>
                </div>
                <span class="text-muted fw-bold" style="font-size: 0.75rem;">¡Más actualizaciones próximamente! v1.0.3.05</span>
                <style>@keyframes heartbeat { 0% { transform: scale(1); } 50% { transform: scale(1.15); } 100% { transform: scale(1); } } .heartbeat-robot { animation: heartbeat 1.5s infinite; }</style>
            </div>
        </div>"""

new_robot = """        <!-- Robot Widget Premium -->
        <div class="d-flex justify-content-end mb-4">
            <div class="d-inline-flex align-items-center bg-white shadow rounded-pill pe-4 ps-1 py-1 position-relative hover-scale" style="border: 1px solid rgba(13, 110, 253, 0.15); cursor: default; overflow: hidden;">
                <div class="position-absolute top-0 start-0 w-100 h-100" style="background: linear-gradient(90deg, rgba(13,110,253,0.05) 0%, transparent 100%); z-index: 0;"></div>
                <div class="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center me-3 position-relative z-1 shadow-sm" style="width: 35px; height: 35px;">
                    <i class="fas fa-robot heartbeat-robot"></i>
                </div>
                <div class="d-flex flex-column justify-content-center position-relative z-1">
                    <span class="text-dark fw-bolder" style="font-size: 0.8rem; letter-spacing: 0.2px;">¡Más actualizaciones próximamente!</span>
                    <span class="text-primary fw-bold" style="font-size: 0.65rem; letter-spacing: 1px;">VERSIÓN 1.0.1</span>
                </div>
                <style>@keyframes heartbeat { 0% { transform: scale(1); } 25% { transform: scale(1.1); rotate: -5deg; } 50% { transform: scale(1.1); rotate: 5deg; } 100% { transform: scale(1); } } .heartbeat-robot { animation: heartbeat 2s infinite ease-in-out; }</style>
            </div>
        </div>"""

if old_robot in dash_content:
    dash_content = dash_content.replace(old_robot, new_robot)

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("UI tweaks successfully applied.")
