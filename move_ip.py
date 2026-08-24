import re

with open('templates/formulario.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The IP block to remove from Section VII
ip_block = """                <div class="mb-3 mt-3">
                    <label class="form-label">Dirección IP (del Equipo Atendido):</label>
                    <input type="text" class="form-control soft-input font-monospace border-primary" name="ip_maquina" placeholder="192.168.x.x" value="{{ atencion.ip_maquina if atencion else '' }}">
                </div>"""

# Remove from Section VII
content = content.replace(ip_block + '\n', '')

# Insert at the end of Section VI, after observaciones
observaciones_block = """        <div>
            <label class="form-label">Observaciones adicionales:</label>
            <input type="text" class="form-control soft-input" name="observaciones" value="{{ atencion.observaciones if atencion else '' }}" placeholder="Opcional">
        </div>"""

new_observaciones_block = observaciones_block + '\n' + ip_block.replace('                <div', '        <div')

content = content.replace(observaciones_block, new_observaciones_block)

with open('templates/formulario.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Moved IP box successfully.")
