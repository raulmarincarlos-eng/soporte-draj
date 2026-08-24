import re

# 1. Update formulario.html
with open('templates/formulario.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add IP input field in the Conformidad section
ip_html = """
                <div class="mb-3 mt-3">
                    <label class="form-label">Dirección IP (del Equipo Atendido):</label>
                    <input type="text" class="form-control soft-input font-monospace border-primary" name="ip_maquina" placeholder="192.168.x.x" value="{{ atencion.ip_maquina if atencion else '' }}">
                </div>
"""
# Insert before "Firma Física (Auditoría):"
content = content.replace('<div class="mb-3">\\n                    <label class="form-label text-danger"><i class="fas fa-file-signature me-1"></i>Firma Física (Auditoría):</label>', ip_html.strip() + '\\n                <div class="mb-3 mt-3">\\n                    <label class="form-label text-danger"><i class="fas fa-file-signature me-1"></i>Firma Física (Auditoría):</label>')

# Add resp_hora to Responsable TI
old_resp_row = """
                    <div class="col-7">
                        <label class="form-label">Cargo:</label>
                        <input type="text" class="form-control soft-input bg-white" name="resp_cargo" value="{{ atencion.resp_cargo if atencion else 'Responsable de Informática' }}">
                    </div>
                    <div class="col-5">
                        <label class="form-label">Fecha:</label>
                        <input type="date" class="form-control soft-input bg-white" name="resp_fecha" id="resp_fecha" value="{{ atencion.resp_fecha if atencion else '' }}">
                    </div>"""

new_resp_row = """
                    <div class="col-12 col-md-5">
                        <label class="form-label">Cargo:</label>
                        <input type="text" class="form-control soft-input bg-white" name="resp_cargo" value="{{ atencion.resp_cargo if atencion else 'Responsable de Informática' }}">
                    </div>
                    <div class="col-6 col-md-4">
                        <label class="form-label">Fecha Cierre:</label>
                        <input type="date" class="form-control soft-input bg-white" name="resp_fecha" id="resp_fecha" value="{{ atencion.resp_fecha if atencion else '' }}">
                    </div>
                    <div class="col-6 col-md-3">
                        <label class="form-label">Hora Cierre:</label>
                        <input type="time" class="form-control soft-input bg-white" name="resp_hora" id="resp_hora" value="{{ atencion.resp_hora if atencion else '' }}">
                    </div>"""
content = content.replace(old_resp_row, new_resp_row)

with open('templates/formulario.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Update detalle.html
with open('templates/detalle.html', 'r', encoding='utf-8') as f:
    content_det = f.read()

# Delete Huella Digital completely
huella_regex = r'<div class="mt-2" style="border-top: 1px dashed #ccc; padding-top: 8px; display: flex; align-items: flex-start; gap: 10px; font-family: \'Courier New\', Courier, monospace; font-size: 8px; color: #555;">.*?</div>\s*</div>'
content_det = re.sub(huella_regex, '', content_det, flags=re.DOTALL)

with open('templates/detalle.html', 'w', encoding='utf-8') as f:
    f.write(content_det)


# 3. Update app.py
with open('app.py', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Add to update_data dictionary
app_content = app_content.replace(
    '"resp_fecha": request.form.get(\'resp_fecha\')',
    '"resp_fecha": request.form.get(\'resp_fecha\'),\n            "resp_hora": request.form.get(\'resp_hora\'),\n            "ip_maquina": request.form.get(\'ip_maquina\')'
)

# Update Excel deletion fields
old_del = """
    for a in atenciones:
        if '_id' in a:
            del a['_id']
        if 'id_secuencial' in a:
            del a['id_secuencial']
"""
new_del = """
    for a in atenciones:
        if '_id' in a: del a['_id']
        if 'id_secuencial' in a: del a['id_secuencial']
        if 'ip_cliente' in a: del a['ip_cliente']
        if 'user_agent' in a: del a['user_agent']
"""
app_content = app_content.replace(old_del, new_del)

# Update Excel columns
old_cols = """
        'resp_nombre': 'Técnico Responsable',
        'resp_cargo': 'Cargo Técnico',
        'resp_fecha': 'Fecha Cierre'
    }"""
new_cols = """
        'resp_nombre': 'Técnico Responsable',
        'resp_cargo': 'Cargo Técnico',
        'resp_fecha': 'Fecha Cierre',
        'resp_hora': 'Hora Cierre',
        'ip_maquina': 'IP Máquina'
    }"""
app_content = app_content.replace(old_cols, new_cols)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_content)

print("Updates completed successfully.")
