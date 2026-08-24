import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Dark Mode Styles
dark_styles = """
        /* Dark Mode Core */
        body.dark-mode {
            background-color: #121212 !important;
            color: #e0e0e0;
        }
        body.dark-mode .modern-island {
            background: rgba(30, 30, 30, 0.9) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4) !important;
        }
        body.dark-mode .island-title { color: #f8f9fa; }
        body.dark-mode .table { color: #e0e0e0; --bs-table-bg: transparent; --bs-table-color: #e0e0e0; }
        body.dark-mode .table thead { background-color: rgba(255,255,255,0.05) !important; color: #fff;}
        body.dark-mode .table-striped>tbody>tr:nth-of-type(odd)>* { background-color: rgba(255,255,255,0.02) !important; color: #e0e0e0;}
        body.dark-mode .soft-input {
            background-color: #2c2c2c !important;
            color: #fff !important;
            border-color: #444 !important;
        }
        body.dark-mode .text-dark { color: #f8f9fa !important; }
        body.dark-mode .glass-row:hover { background-color: rgba(255,255,255,0.08) !important; }
        body.dark-mode .modal-content { background-color: #222; color: #eee; }
        body.dark-mode .form-label { color: #aaa; }
        
        .dark-mode-toggle {
            cursor: pointer;
            background: rgba(255,255,255,0.2);
            border-radius: 50%;
            width: 40px; height: 40px;
            display: inline-flex;
            align-items: center; justify-content: center;
            color: white;
            transition: all 0.3s;
            margin-left: 15px;
        }
        .dark-mode-toggle:hover { background: white; color: #121212; transform: scale(1.1); }
"""
if "/* Dark Mode Core */" not in content:
    content = content.replace("/* CSS FLUIDEZ GLOBAL */", dark_styles + "\n        /* CSS FLUIDEZ GLOBAL */")

# 2. Add Toggle Button in Navbar (only for logged in users)
old_logout = """<a href="{{ url_for('logout') }}" class="btn btn-admin-glow ms-3">
                        <i class="fas fa-sign-out-alt me-2"></i>Cerrar Sesión
                    </a>
                {% endif %}"""
new_logout = """<a href="{{ url_for('logout') }}" class="btn btn-admin-glow ms-3">
                        <i class="fas fa-sign-out-alt me-2"></i>Cerrar Sesión
                    </a>
                    <div class="dark-mode-toggle" id="theme-toggle" title="Alternar Modo Oscuro">
                        <i class="fas fa-moon" id="theme-icon"></i>
                    </div>
                {% endif %}"""
content = content.replace(old_logout, new_logout)

# 3. Add JS Logic for Dark Mode
script_logic = """
    <script>
        // Lógica de Modo Oscuro Global
        const themeToggle = document.getElementById('theme-toggle');
        const themeIcon = document.getElementById('theme-icon');
        const body = document.body;
        
        // Verificar localStorage
        if(localStorage.getItem('theme') === 'dark') {
            body.classList.add('dark-mode');
            if(themeIcon) { themeIcon.classList.remove('fa-moon'); themeIcon.classList.add('fa-sun'); }
        }
        
        if(themeToggle) {
            themeToggle.addEventListener('click', () => {
                body.classList.toggle('dark-mode');
                if(body.classList.contains('dark-mode')) {
                    localStorage.setItem('theme', 'dark');
                    themeIcon.classList.remove('fa-moon');
                    themeIcon.classList.add('fa-sun');
                } else {
                    localStorage.setItem('theme', 'light');
                    themeIcon.classList.remove('fa-sun');
                    themeIcon.classList.add('fa-moon');
                }
            });
        }
    </script>
"""
if "Lógica de Modo Oscuro Global" not in content:
    content = content.replace("</body>", script_logic + "\n</body>")

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Dark Mode integrated in base.html")
