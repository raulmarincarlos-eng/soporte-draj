import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_input = """<input type="text" class="form-control" id="nombre_solicitante" name="nombre_solicitante" required placeholder="Ej: Juan Pérez">"""
new_input = """<input type="text" class="form-control" id="nombre_solicitante" name="nombre_solicitante" required placeholder="Ej: Juan Pérez" value="{{ session.get('nombre', '') }}" {% if session.get('nombre') %}readonly style="background-color: #f8f9fa; color: #6c757d;"{% endif %}>
                        {% if session.get('nombre') %}
                        <small class="text-success mt-1 d-block"><i class="fas fa-check-circle me-1"></i>Detectado automáticamente por tu sesión</small>
                        {% endif %}"""

if old_input in content:
    content = content.replace(old_input, new_input)
else:
    print("Could not find the target input string.")

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Prefill logic applied successfully.")
