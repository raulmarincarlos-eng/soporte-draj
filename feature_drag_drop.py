import re

with open('templates/formulario.html', 'r', encoding='utf-8') as f:
    form_content = f.read()

# Replace the simple upload box with a Drag and Drop Zone
old_upload = """        <div id="upload-evidencia" class="mb-3 d-none p-3 rounded" style="background: #fff3cd; border: 1px dashed #ffc107;">
            <label class="form-label text-warning" style="font-weight: 600;"><i class="fas fa-file-upload me-2"></i>Subir Evidencia (Solo si la atención es Parcial)</label>
            <input type="file" class="form-control soft-input" name="evidencia_parcial" accept=".png,.jpg,.jpeg,.pdf,.doc,.docx,.xls,.xlsx">
            {% if atencion and atencion.evidencia_parcial %}
            <div class="mt-2 small text-muted fw-bold">
                <i class="fas fa-check-circle text-success me-1"></i>Archivo actual adjuntado: <a href="{{ url_for('static', filename='uploads/' + atencion.evidencia_parcial) }}" target="_blank" class="text-primary text-decoration-underline">{{ atencion.evidencia_parcial }}</a>
            </div>
            {% endif %}
        </div>"""

new_upload = """        <div id="upload-evidencia" class="mb-3 d-none p-4 rounded text-center position-relative transition-all" style="background: rgba(255,193,7,0.1); border: 2px dashed #ffc107; cursor: pointer;">
            <input type="file" id="fileInputDnd" class="position-absolute top-0 start-0 w-100 h-100 opacity-0" name="evidencia_parcial" accept=".png,.jpg,.jpeg,.pdf,.doc,.docx,.xls,.xlsx" style="cursor: pointer; z-index: 10;">
            <div id="dnd-content" class="pointer-events-none">
                <i class="fas fa-cloud-upload-alt fa-3x text-warning mb-2"></i>
                <h5 class="text-warning fw-bold mb-1">Arrastra tu Evidencia Aquí</h5>
                <p class="text-muted small mb-0">o haz clic para explorar archivos (JPG, PDF, DOC, XLS)</p>
                <div id="fileNameDisplay" class="mt-2 fw-bold text-success d-none">
                    <i class="fas fa-file-alt me-1"></i> <span></span>
                </div>
            </div>
            {% if atencion and atencion.evidencia_parcial %}
            <div class="mt-3 small text-muted fw-bold position-relative z-3">
                <i class="fas fa-check-circle text-success me-1"></i>Archivo actual adjuntado: <a href="{{ url_for('static', filename='uploads/' + atencion.evidencia_parcial) }}" target="_blank" class="text-primary text-decoration-underline">{{ atencion.evidencia_parcial }}</a>
            </div>
            {% endif %}
        </div>
        
        <script>
            // Drag and Drop Effects
            const dropZone = document.getElementById('upload-evidencia');
            const fileInput = document.getElementById('fileInputDnd');
            const fileNameDisplay = document.getElementById('fileNameDisplay');
            
            if(dropZone && fileInput) {
                ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                    dropZone.addEventListener(eventName, preventDefaults, false);
                });
                
                function preventDefaults(e) { e.preventDefault(); e.stopPropagation(); }
                
                ['dragenter', 'dragover'].forEach(eventName => {
                    dropZone.addEventListener(eventName, () => {
                        dropZone.style.background = 'rgba(255,193,7,0.2)';
                        dropZone.style.transform = 'scale(1.02)';
                    }, false);
                });
                
                ['dragleave', 'drop'].forEach(eventName => {
                    dropZone.addEventListener(eventName, () => {
                        dropZone.style.background = 'rgba(255,193,7,0.1)';
                        dropZone.style.transform = 'scale(1)';
                    }, false);
                });
                
                fileInput.addEventListener('change', function(e) {
                    if(this.files && this.files[0]) {
                        fileNameDisplay.classList.remove('d-none');
                        fileNameDisplay.querySelector('span').textContent = this.files[0].name;
                    }
                });
            }
        </script>"""

if old_upload in form_content:
    form_content = form_content.replace(old_upload, new_upload)

with open('templates/formulario.html', 'w', encoding='utf-8') as f:
    f.write(form_content)

print("Drag and Drop Feature implemented.")
