import re

# 1. Update app.py
with open('app.py', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Fix /nuevo crash
nuevo_bad = """        estado_firma = request.form.get('estado_firma', 'Pendiente')
        
        file = request.files.get('evidencia_parcial')
        evidencia_filename = atencion.get('evidencia_parcial')
        
        if file and file.filename != '':
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = f"{atencion['id']}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                evidencia_filename = filename"""
nuevo_good = """        file = request.files.get('evidencia_parcial')
        evidencia_filename = None
        
        if file and file.filename != '':
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = f"{id_atencion}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                evidencia_filename = filename"""
app_content = app_content.replace(nuevo_bad, nuevo_good)

# Remove estado_firma from nuevo
nuevo_doc_bad = """            "id_secuencial": nuevo_num, # Para ordenar correctamente
            "estado_firma": estado_firma,"""
nuevo_doc_good = """            "id_secuencial": nuevo_num, # Para ordenar correctamente"""
app_content = app_content.replace(nuevo_doc_bad, nuevo_doc_good)

# Fix /editar 
editar_bad = """        estado_firma = request.form.get('estado_firma', 'Pendiente')
        
        file = request.files.get('evidencia_parcial')"""
editar_good = """        file = request.files.get('evidencia_parcial')"""
app_content = app_content.replace(editar_bad, editar_good)

editar_doc_bad = """        update_data = {
            "estado_firma": estado_firma,"""
editar_doc_good = """        update_data = {"""
app_content = app_content.replace(editar_doc_bad, editar_doc_good)

# Remove from Excel
excel_bad = """    nombres_columnas = {
        'id': 'Código',
        'estado_firma': 'Estado Firma Física',"""
excel_good = """    nombres_columnas = {
        'id': 'Código',"""
app_content = app_content.replace(excel_bad, excel_good)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_content)

# 2. Update formulario.html
with open('templates/formulario.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Remove Firma Fisica block
firma_block = """                <div class="mb-3">
                    <label class="form-label text-danger"><i class="fas fa-file-signature me-1"></i>Firma Física (Auditoría):</label>
                    <select class="form-select soft-input border-danger" name="estado_firma" style="color: #dc3545; font-weight: bold;">
                        <option value="Pendiente" {% if atencion and atencion.estado_firma == 'Pendiente' %}selected{% endif %}>Pendiente (Falta Imprimir)</option>
                        <option value="Firmado y Archivado" {% if atencion and atencion.estado_firma == 'Firmado y Archivado' %}selected{% endif %}>Firmado y Archivado</option>
                    </select>
                </div>"""
html_content = html_content.replace(firma_block + '\n', '')

with open('templates/formulario.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Fixed 500 error and removed Firma Física completely.")
