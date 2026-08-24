import re

# 1. Fix JavaScript crash in dashboard.html
with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    dash_content = f.read()

# Make the event listener safe (check if element exists)
old_js = """    // Generar PDF
    document.getElementById('btnExportPDF').addEventListener('click', function() {"""
new_js = """    // Generar PDF
    const btnPdf = document.getElementById('btnExportPDF');
    if (btnPdf) {
        btnPdf.addEventListener('click', function() {"""
if old_js in dash_content:
    dash_content = dash_content.replace(old_js, new_js)
    dash_content = dash_content.replace("        html2pdf().set(opt).from(element).save();\n    });", "        html2pdf().set(opt).from(element).save();\n        });\n    }")

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash_content)


# 2. Fix Dark Mode CSS for Cards and Dashboard elements in base.html
with open('templates/base.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

dark_css_patch = """
        body.dark-mode .card { background-color: #1e1e1e !important; border-color: rgba(255,255,255,0.05) !important; color: #f8f9fa; }
        body.dark-mode .bg-white { background-color: #1e1e1e !important; color: #f8f9fa !important; }
        body.dark-mode .text-dark { color: #f8f9fa !important; }
        body.dark-mode .table-light { background-color: rgba(255,255,255,0.05) !important; color: #fff !important;}
        body.dark-mode .text-muted { color: #aaa !important; }
"""
if "body.dark-mode .card" not in base_content:
    base_content = base_content.replace("body.dark-mode .table {", dark_css_patch + "\n        body.dark-mode .table {")

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_content)

print("Hotfix applied.")
