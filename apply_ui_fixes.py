import re

def fix_formulario():
    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\formulario.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add padding-bottom to container so sticky bar doesn't overlap
    old_container = '<div class="container py-4">'
    new_container = '<div class="container py-4" style="padding-bottom: 120px !important;">'
    if old_container in content:
        content = content.replace(old_container, new_container)
        
    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\formulario.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed formulario.html")

def fix_dashboard():
    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove "0 Días" card
    dias_regex = re.compile(r'<!-- KPI Promedio -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
    content = dias_regex.sub('', content)
    
    # 2. Adjust col-md-2 to col-md-3 for the charts to fill space
    content = content.replace('<div class="col-md-2 mb-3">', '<div class="col-md-3 mb-3">')
    content = content.replace('<div class="col-md-2">', '<div class="col-md-3">')
    
    # 3. Replace the static toast robot with an interactive one
    toast_regex = re.compile(r'<!-- Toast / Robotito -->.*?</div>\s*</div>', re.DOTALL)
    content = toast_regex.sub('', content)
    
    new_robot = """
    <!-- Robot Dashboard Interactivo -->
    <div id="admin-robot" style="position: fixed; bottom: 20px; right: 20px; z-index: 9999; display: flex; flex-direction: column-reverse; align-items: flex-end;">
        <img src="{{ url_for('static', filename='img/robot.jpg') }}" class="rounded-circle shadow-lg hover-scale" style="width: 65px; height: 65px; border: 3px solid #0d6efd; cursor: pointer;" onclick="toggleAdminRobot()">
        <div id="admin-robot-bubble" class="shadow-lg" style="background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-radius: 20px 20px 0 20px; padding: 15px; border-bottom: 4px solid #0d6efd; max-width: 250px; margin-bottom: 15px; margin-right: 5px; display: none; animation: popIn 0.3s forwards; transform-origin: bottom right;">
            <h6 class="fw-bold text-primary mb-2"><i class="fas fa-robot me-2"></i>Asistente TI</h6>
            <p class="small mb-2 text-dark"><strong>¡Versión 1.0.1 Activa!</strong><br>El sistema opera al 100%. Las nuevas actualizaciones de estadísticas avanzadas llegarán pronto.</p>
            <button class="btn btn-sm btn-primary w-100 rounded-pill" onclick="toggleAdminRobot()">Entendido</button>
        </div>
    </div>
    <script>
        function toggleAdminRobot() {
            const b = document.getElementById('admin-robot-bubble');
            if(b.style.display === 'none') {
                b.style.display = 'block';
            } else {
                b.style.display = 'none';
            }
        }
    </script>
    """
    if "admin-robot" not in content:
        content += new_robot

    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\dashboard.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed dashboard.html")

def fix_base():
    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\base.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Dark mode table fixes (Force Bootstrap tables to be dark)
    dark_css = """
        body.dark-mode .table { color: #e0e0e0; --bs-table-bg: transparent; --bs-table-color: #e0e0e0; border-color: rgba(255,255,255,0.1); }
        body.dark-mode .table th, body.dark-mode .table td { background-color: transparent !important; color: #e0e0e0 !important; border-bottom-color: rgba(255,255,255,0.05) !important; }
        body.dark-mode .table-hover tbody tr:hover td { background-color: rgba(255,255,255,0.05) !important; }
        body.dark-mode .dataTables_wrapper .dataTables_length, body.dark-mode .dataTables_wrapper .dataTables_filter, body.dark-mode .dataTables_wrapper .dataTables_info, body.dark-mode .dataTables_wrapper .dataTables_processing, body.dark-mode .dataTables_wrapper .dataTables_paginate { color: #e0e0e0 !important; }
        body.dark-mode .page-item.disabled .page-link { background-color: #1e1e1e; border-color: rgba(255,255,255,0.1); }
        body.dark-mode .page-link { background-color: #2d2d2d; border-color: rgba(255,255,255,0.1); color: #fff; }
    """
    if "body.dark-mode .table th" not in content:
        content = content.replace('/* Dark Mode Core */', '/* Dark Mode Core */\n' + dark_css)

    # 2. Premium Navbar (Floating Glassmorphism)
    old_nav = '<nav class="navbar navbar-expand-lg navbar-dark shadow-sm py-3" style="background: linear-gradient(135deg, #198754 0%, #146c43 100%);">'
    new_nav = '<nav class="navbar navbar-expand-lg navbar-dark py-3" style="background: rgba(25, 135, 84, 0.85); backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px); border-radius: 20px; margin: 15px 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); position: sticky; top: 15px; z-index: 1000; border: 1px solid rgba(255,255,255,0.1);">'
    content = content.replace(old_nav, new_nav)
    
    # 3. Add background transition for smooth dark mode
    if 'body { transition: background-color' not in content:
        content = content.replace('</style>', 'body { transition: background-color 0.4s ease, color 0.4s ease; }\n</style>')

    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\base.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed base.html")

if __name__ == '__main__':
    fix_formulario()
    fix_dashboard()
    fix_base()
