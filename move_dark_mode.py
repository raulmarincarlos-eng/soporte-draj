import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the CSS for the toggle
old_css = """        .dark-mode-toggle {
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
        .dark-mode-toggle:hover { background: white; color: #121212; transform: scale(1.1); }"""

new_css = """        .dark-mode-toggle {
            cursor: pointer;
            background: rgba(0,0,0,0.5);
            border-radius: 50%;
            width: 45px; height: 45px;
            display: inline-flex;
            align-items: center; justify-content: center;
            color: white;
            transition: all 0.3s;
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 9999;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.1);
        }
        body.dark-mode .dark-mode-toggle {
            background: rgba(255,255,255,0.1);
        }
        .dark-mode-toggle:hover { background: #198754; color: white; transform: scale(1.1); box-shadow: 0 6px 20px rgba(25, 135, 84, 0.4); }"""
content = content.replace(old_css, new_css)

# 2. Remove from Navbar
navbar_block = """                    <a href="{{ url_for('logout') }}" class="btn btn-admin-glow ms-3">
                        <i class="fas fa-sign-out-alt me-2"></i>Cerrar Sesión
                    </a>
                    <div class="dark-mode-toggle" id="theme-toggle" title="Alternar Modo Oscuro">
                        <i class="fas fa-moon" id="theme-icon"></i>
                    </div>
                {% endif %}"""

navbar_clean = """                    <a href="{{ url_for('logout') }}" class="btn btn-admin-glow ms-3">
                        <i class="fas fa-sign-out-alt me-2"></i>Cerrar Sesión
                    </a>
                {% endif %}"""
content = content.replace(navbar_block, navbar_clean)

# 3. Inject before the closing body tag
inject_button = """    <!-- Custom JS -->
    <script src="{{ url_for('static', filename='js/main.js') }}?v=2"></script>

    {% if session.get('user_id') %}
    <div class="dark-mode-toggle" id="theme-toggle" title="Alternar Modo Oscuro">
        <i class="fas fa-moon" id="theme-icon"></i>
    </div>
    {% endif %}

    <script>"""
content = content.replace("""    <!-- Custom JS -->
    <script src="{{ url_for('static', filename='js/main.js') }}?v=2"></script>

    <script>""", inject_button)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Dark Mode toggle moved successfully.")
