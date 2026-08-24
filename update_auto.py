import re

# 1. Update app.py Excel Export
with open('app.py', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Make sure the dataframe ONLY contains the known columns
old_rename = """    nombres_columnas_existentes = {k: v for k, v in nombres_columnas.items() if k in df.columns}
    df.rename(columns=nombres_columnas_existentes, inplace=True)"""

new_rename = """    # Filtrar solo las columnas que queremos en el Excel
    columnas_deseadas = [k for k in nombres_columnas.keys() if k in df.columns]
    df = df[columnas_deseadas]
    
    nombres_columnas_existentes = {k: v for k in columnas_deseadas for k, v in nombres_columnas.items() if k in df.columns}
    df.rename(columns=nombres_columnas, inplace=True)"""
app_content = app_content.replace(old_rename, new_rename)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_content)


# 2. Update formulario.html auto-fill time
with open('templates/formulario.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

old_autofill = """        const respFecha = document.getElementById('resp_fecha');
        if(respFecha && !respFecha.value) respFecha.value = dateString;"""

new_autofill = """        const respFecha = document.getElementById('resp_fecha');
        if(respFecha && !respFecha.value) respFecha.value = dateString;
        
        const respHora = document.getElementById('resp_hora');
        if(respHora && !respHora.value) respHora.value = timeString;"""

html_content = html_content.replace(old_autofill, new_autofill)

# Auto-update time on radio button click for Atendido
script_end = """    document.addEventListener("DOMContentLoaded", function() {"""
new_script_end = """
    // Función para auto-llenar fecha y hora actual al seleccionar un estado de finalización
    function autoFillClosingTime() {
        const today = new Date();
        const dateString = today.toISOString().split('T')[0];
        const timeString = today.toTimeString().split(':')[0] + ':' + today.toTimeString().split(':')[1];
        
        const respFecha = document.getElementById('resp_fecha');
        if(respFecha) respFecha.value = dateString;
        
        const respHora = document.getElementById('resp_hora');
        if(respHora) respHora.value = timeString;
    }
    
    document.addEventListener("DOMContentLoaded", function() {
        // Añadir el listener a los radios de resultado
        const radioBtns = document.querySelectorAll('input[name="resultado"]');
        radioBtns.forEach(btn => {
            btn.addEventListener('change', function() {
                if(this.value === 'Atendido' || this.value === 'Parcial') {
                    autoFillClosingTime();
                }
            });
        });"""

html_content = html_content.replace(script_end, new_script_end)

with open('templates/formulario.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Auto-fill and Excel filter updated successfully.")
