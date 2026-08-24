import re

# 1. Update app.py
with open('app.py', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Add imports for secure_filename and configure upload folder
import_block = """import os
import sys"""

new_import_block = """import os
import sys
from werkzeug.utils import secure_filename"""
app_content = app_content.replace(import_block, new_import_block)

# Add upload folder config right after Flask init
flask_init = """else:
    app = Flask(__name__)"""
flask_upload_config = """else:
    app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB max
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'doc', 'docx', 'xls', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
"""
app_content = app_content.replace(flask_init, flask_upload_config)

# In the editar route, catch the uploaded file
editar_start = """        estado_firma = request.form.get('estado_firma', 'Pendiente')"""
editar_upload = """        estado_firma = request.form.get('estado_firma', 'Pendiente')
        
        file = request.files.get('evidencia_parcial')
        evidencia_filename = atencion.get('evidencia_parcial')
        
        if file and file.filename != '':
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = f"{atencion['id']}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                evidencia_filename = filename
"""
app_content = app_content.replace(editar_start, editar_upload)

# Add to update_data dictionary
update_data_old = """"ip_maquina": request.form.get('ip_maquina')
        }"""
update_data_new = """"ip_maquina": request.form.get('ip_maquina'),
            "evidencia_parcial": evidencia_filename
        }"""
app_content = app_content.replace(update_data_old, update_data_new)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_content)


# 2. Update formulario.html
with open('templates/formulario.html', 'r', encoding='utf-8') as f:
    form_content = f.read()

# Add enctype to form
form_content = form_content.replace('<form method="POST" action="{% if atencion %}{{ url_for(\'editar\', id_str=atencion.id) }}{% else %}{{ url_for(\'nuevo\') }}{% endif %}">', '<form method="POST" action="{% if atencion %}{{ url_for(\'editar\', id_str=atencion.id) }}{% else %}{{ url_for(\'nuevo\') }}{% endif %}" enctype="multipart/form-data">')

# Add the file upload box in section VI
radio_box_end = """            <div class="col-md-3">
                <input type="radio" class="btn-check" name="resultado" id="res_noatendido" value="No atendido" {% if atencion and atencion.resultado == 'No atendido' %}checked{% endif %}>
                <label class="pill-label pill-label-danger text-center fs-5" for="res_noatendido"><i class="fas fa-times-circle me-2"></i>No Atendido</label>
            </div>
        </div>"""

upload_html = """            <div class="col-md-3">
                <input type="radio" class="btn-check" name="resultado" id="res_noatendido" value="No atendido" {% if atencion and atencion.resultado == 'No atendido' %}checked{% endif %}>
                <label class="pill-label pill-label-danger text-center fs-5" for="res_noatendido"><i class="fas fa-times-circle me-2"></i>No Atendido</label>
            </div>
        </div>
        
        <div id="upload-evidencia" class="mb-3 d-none p-3 rounded" style="background: #fff3cd; border: 1px dashed #ffc107;">
            <label class="form-label text-warning" style="font-weight: 600;"><i class="fas fa-file-upload me-2"></i>Subir Evidencia (Solo si la atención es Parcial)</label>
            <input type="file" class="form-control soft-input" name="evidencia_parcial" accept=".png,.jpg,.jpeg,.pdf,.doc,.docx,.xls,.xlsx">
            {% if atencion and atencion.evidencia_parcial %}
            <div class="mt-2 small text-muted fw-bold">
                <i class="fas fa-check-circle text-success me-1"></i>Archivo actual adjuntado: <a href="{{ url_for('static', filename='uploads/' + atencion.evidencia_parcial) }}" target="_blank" class="text-primary text-decoration-underline">{{ atencion.evidencia_parcial }}</a>
            </div>
            {% endif %}
        </div>"""
form_content = form_content.replace(radio_box_end, upload_html)

# Update JS to toggle visibility
js_old = """        // Añadir el listener a los radios de resultado
        const radioBtns = document.querySelectorAll('input[name="resultado"]');
        radioBtns.forEach(btn => {
            btn.addEventListener('change', function() {
                if(this.value === 'Atendido' || this.value === 'Parcial') {
                    autoFillClosingTime();
                }
            });
        });"""
js_new = """        // Añadir el listener a los radios de resultado
        const radioBtns = document.querySelectorAll('input[name="resultado"]');
        const uploadBox = document.getElementById('upload-evidencia');
        
        function toggleUploadBox() {
            const parcialRadio = document.getElementById('res_parcial');
            if(parcialRadio && parcialRadio.checked) {
                uploadBox.classList.remove('d-none');
            } else {
                uploadBox.classList.add('d-none');
            }
        }
        
        radioBtns.forEach(btn => {
            btn.addEventListener('change', function() {
                toggleUploadBox();
                if(this.value === 'Atendido' || this.value === 'Parcial') {
                    autoFillClosingTime();
                }
            });
        });
        toggleUploadBox(); // Ejecutar al cargar la página"""
form_content = form_content.replace(js_old, js_new)

with open('templates/formulario.html', 'w', encoding='utf-8') as f:
    f.write(form_content)

# 3. Update detalle.html
with open('templates/detalle.html', 'r', encoding='utf-8') as f:
    det_content = f.read()

obs_row = """        <tr>
            <td colspan="6" class="field-value p-2" style="height: 35px; border-top: none;">
                <span class="fw-bold">Observaciones:</span> <span class="text-primary-color">{{ atencion.observaciones }}</span>
            </td>
        </tr>"""

new_obs_row = """        <tr>
            <td colspan="6" class="field-value p-2" style="height: 35px; border-top: none;">
                <span class="fw-bold">Observaciones:</span> <span class="text-primary-color">{{ atencion.observaciones }}</span>
                {% if atencion.evidencia_parcial %}
                <br><span class="fw-bold text-warning"><i class="fas fa-paperclip me-1"></i>Evidencia Adjunta:</span> <span class="text-muted" style="font-size: 10px;">{{ atencion.evidencia_parcial }} (Archivo digital guardado en sistema)</span>
                {% endif %}
            </td>
        </tr>"""
det_content = det_content.replace(obs_row, new_obs_row)

with open('templates/detalle.html', 'w', encoding='utf-8') as f:
    f.write(det_content)

print("Parcial upload feature implemented.")
