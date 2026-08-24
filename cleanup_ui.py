import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

# 1. Remove duplicate dark mode toggle from navbar
bad_toggle = """                    <li class="nav-item ms-lg-2">
                        <button id="darkModeToggle" class="btn btn-outline-light btn-sm rounded-circle d-flex align-items-center justify-content-center" style="width: 35px; height: 35px;" title="Alternar Modo Oscuro">
                            <i class="fas fa-moon"></i>
                        </button>
                    </li>"""
if bad_toggle in base_content:
    base_content = base_content.replace(bad_toggle, "")

# 2. Add signature in the navbar
old_brand = """                <span class="fw-bold fs-5" style="letter-spacing: 0.5px;">Soporte TI <span class="fw-light opacity-75">| DRAJ 2026</span></span>
            </a>"""
new_brand = """                <span class="fw-bold fs-5" style="letter-spacing: 0.5px;">Soporte TI <span class="fw-light opacity-75">| DRAJ 2026</span></span>
            </a>
            <span class="d-none d-lg-inline ms-3 badge bg-light text-dark shadow-sm" style="font-size: 0.65rem; letter-spacing: 0.5px; border-radius: 20px; font-weight: 600;"><i class="fas fa-code me-1 text-primary"></i>Dev: Carlos</span>"""
if "Dev: Carlos" not in base_content:
    base_content = base_content.replace(old_brand, new_brand)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_content)


with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    dash_content = f.read()

# 3. Remove PDF Button
pdf_btn = """            <button id="btnExportPDF" class="btn btn-danger shadow-sm fw-bold rounded-pill hover-scale">
                <i class="fas fa-file-pdf me-1"></i> PDF
            </button>"""
if pdf_btn in dash_content:
    dash_content = dash_content.replace(pdf_btn, "")

# 4. Add "Proximas actualizaciones" robot widget
# Let's add it right under the Search / Filters, before the table. Or next to the stats.
# Let's put a small floating widget or a small inline alert.
robot_widget = """
        <!-- Robot Widget -->
        <div class="d-flex justify-content-end mb-3">
            <div class="d-inline-flex align-items-center bg-white shadow-sm px-3 py-2 rounded-pill border" style="border-color: rgba(0,0,0,0.05) !important;">
                <div class="rounded-circle bg-primary bg-opacity-10 d-flex align-items-center justify-content-center me-2" style="width: 30px; height: 30px;">
                    <i class="fas fa-robot text-primary fa-sm heartbeat-robot"></i>
                </div>
                <span class="text-muted fw-bold" style="font-size: 0.75rem;">¡Más actualizaciones próximamente! v1.0.3.05</span>
                <style>@keyframes heartbeat { 0% { transform: scale(1); } 50% { transform: scale(1.15); } 100% { transform: scale(1); } } .heartbeat-robot { animation: heartbeat 1.5s infinite; }</style>
            </div>
        </div>
"""
if "heartbeat-robot" not in dash_content:
    dash_content = dash_content.replace('<div class="table-responsive">', robot_widget + '\n        <div class="table-responsive">')

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("UI tweaks successfully applied.")
