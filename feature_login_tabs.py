import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\login.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject custom CSS for tabs
tab_css = """
        /* Tabs Premium */
        .auth-tabs {
            display: flex;
            background: rgba(15, 23, 42, 0.4);
            border-radius: 14px;
            padding: 5px;
            margin-bottom: 25px;
        }
        .auth-tab {
            flex: 1;
            text-align: center;
            padding: 10px;
            color: #64748b;
            font-weight: 600;
            cursor: pointer;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .auth-tab.active {
            background: rgba(16, 185, 129, 0.2);
            color: #10b981;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        
        .auth-form {
            display: none;
            animation: fadeInRight 0.4s ease forwards;
        }
        .auth-form.active {
            display: block;
        }
        @keyframes fadeInRight {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }
"""
if '.auth-tabs {' not in content:
    content = content.replace('/* Custom Alert */', tab_css + '\n        /* Custom Alert */')

# 2. Replace the form with the new tabbed interface
old_form = """        <form method="POST" action="{{ url_for('login') }}">
            <div class="mb-4">
                <label class="form-label">Usuario</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="fas fa-user-shield"></i></span>
                    <input type="text" class="form-control" name="username" required autofocus placeholder="Ingresa tu usuario">
                </div>
            </div>
            <div class="mb-4">
                <label class="form-label">Contraseña</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="fas fa-lock"></i></span>
                    <input type="password" class="form-control" name="password" required placeholder="••••••••">
                </div>
            </div>
            <button type="submit" class="btn btn-login w-100 mt-2">
                Iniciar Sesión <i class="fas fa-arrow-right ms-2"></i>
            </button>
            <div class="text-center mt-4">
                <a href="{{ url_for('solicitar') }}" class="back-link small"><i class="fas fa-chevron-left me-1" style="font-size:10px;"></i> Portal de Solicitudes</a>
            </div>
        </form>"""

new_forms = """
        <div class="auth-tabs">
            <div class="auth-tab active" onclick="switchTab('login')" id="tab-login">Ingresar</div>
            <div class="auth-tab" onclick="switchTab('register')" id="tab-register">Crear Cuenta</div>
        </div>

        <!-- FORMULARIO DE LOGIN -->
        <form method="POST" action="{{ url_for('login') }}" class="auth-form active" id="form-login">
            <div class="mb-4">
                <label class="form-label">DNI o Usuario Administrativo</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="fas fa-user"></i></span>
                    <input type="text" class="form-control" name="username" required autofocus placeholder="Ingresa tu usuario o DNI">
                </div>
            </div>
            <div class="mb-4">
                <label class="form-label">Contraseña</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="fas fa-lock"></i></span>
                    <input type="password" class="form-control" name="password" required placeholder="••••••••">
                </div>
            </div>
            <button type="submit" class="btn btn-login w-100 mt-2">
                Iniciar Sesión <i class="fas fa-arrow-right ms-2"></i>
            </button>
            <div class="text-center mt-4">
                <a href="{{ url_for('solicitar') }}" class="back-link small"><i class="fas fa-chevron-left me-1" style="font-size:10px;"></i> Portal de Solicitudes Públicas</a>
            </div>
        </form>

        <!-- FORMULARIO DE REGISTRO -->
        <form method="POST" action="{{ url_for('registro') }}" class="auth-form" id="form-register">
            <div class="mb-3">
                <label class="form-label">DNI (Será tu usuario)</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="fas fa-id-card"></i></span>
                    <input type="text" class="form-control" name="dni" required placeholder="Ej. 76543210" pattern="[0-9]{8}">
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">Nombre Completo</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="fas fa-user-circle"></i></span>
                    <input type="text" class="form-control" name="nombre" required placeholder="Nombres y Apellidos">
                </div>
            </div>
            <div class="mb-4">
                <label class="form-label">Contraseña Segura</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="fas fa-key"></i></span>
                    <input type="password" class="form-control" name="password" required placeholder="Mínimo 6 caracteres" minlength="6">
                </div>
            </div>
            <button type="submit" class="btn btn-login w-100 mt-2" style="background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%); border-color: #2563eb; box-shadow: 0 10px 20px rgba(59, 130, 246, 0.2);">
                Registrarme <i class="fas fa-user-plus ms-2"></i>
            </button>
        </form>

        <script>
            function switchTab(tab) {
                document.getElementById('tab-login').classList.remove('active');
                document.getElementById('tab-register').classList.remove('active');
                document.getElementById('form-login').classList.remove('active');
                document.getElementById('form-register').classList.remove('active');
                
                document.getElementById('tab-' + tab).classList.add('active');
                document.getElementById('form-' + tab).classList.add('active');
            }
        </script>
"""
if old_form in content:
    content = content.replace(old_form, new_forms)

# 3. Change subtitle text
content = content.replace('<p class="subtitle">Panel de Control Administrativo</p>', '<p class="subtitle">Portal Unificado DRAJ</p>')

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\login.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("login.html updated with tabs successfully.")
