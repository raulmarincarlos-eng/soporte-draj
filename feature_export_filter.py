import re

# 1. Update app.py export route
with open('app.py', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Modify /exportar_excel route
old_export = """@app.route('/exportar_excel')
@login_required
def exportar_excel():
    db = get_db_connection()
    atenciones = list(db.atenciones.find().sort("id_secuencial", 1))"""
new_export = """@app.route('/exportar_excel')
@login_required
def exportar_excel():
    db = get_db_connection()
    
    # Soporte para filtrado de fechas
    fecha_inicio = request.args.get('inicio', '')
    fecha_fin = request.args.get('fin', '')
    
    query = {}
    if fecha_inicio and fecha_fin:
        query['fecha_registro'] = {"$gte": fecha_inicio, "$lte": fecha_fin}
    elif fecha_inicio:
        query['fecha_registro'] = {"$gte": fecha_inicio}
    elif fecha_fin:
        query['fecha_registro'] = {"$lte": fecha_fin}
        
    atenciones = list(db.atenciones.find(query).sort("id_secuencial", 1))"""
app_content = app_content.replace(old_export, new_export)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_content)


# 2. Update dashboard.html UI
with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    dash_content = f.read()

old_search = """                    <div class="col-md-6">
                        <div class="input-group shadow-sm">
                            <span class="input-group-text bg-white border-end-0 text-muted"><i class="fas fa-search"></i></span>
                            <input type="text" id="searchInput" class="form-control border-start-0 ps-0" placeholder="Buscar por área, código o contenido..." value="{{ search }}">
                        </div>
                    </div>"""
new_search = """                    <div class="col-md-4">
                        <div class="input-group shadow-sm">
                            <span class="input-group-text bg-white border-end-0 text-muted"><i class="fas fa-search"></i></span>
                            <input type="text" id="searchInput" class="form-control border-start-0 ps-0" placeholder="Buscar ticket..." value="{{ search }}">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="input-group shadow-sm">
                            <span class="input-group-text bg-white text-muted"><i class="fas fa-calendar-alt"></i></span>
                            <input type="date" id="dateStart" class="form-control" title="Fecha Inicio">
                            <input type="date" id="dateEnd" class="form-control" title="Fecha Fin">
                        </div>
                    </div>"""
dash_content = dash_content.replace(old_search, new_search)

# Update Export Button ID and onClick logic
old_export_btn = """<a href="{{ url_for('exportar_excel') }}" class="btn btn-outline-success shadow-sm hover-scale fw-bold">
                        <i class="fas fa-file-excel me-2"></i>Exportar Excel
                    </a>"""
new_export_btn = """<a href="#" id="btnExportExcel" class="btn btn-outline-success shadow-sm hover-scale fw-bold">
                        <i class="fas fa-file-excel me-2"></i>Exportar Excel
                    </a>"""
dash_content = dash_content.replace(old_export_btn, new_export_btn)

# Add logic for export button
js_export = """    // Export to Excel with dates
    const btnExportExcel = document.getElementById('btnExportExcel');
    if(btnExportExcel) {
        btnExportExcel.addEventListener('click', function(e) {
            e.preventDefault();
            const dateStart = document.getElementById('dateStart').value;
            const dateEnd = document.getElementById('dateEnd').value;
            let url = "{{ url_for('exportar_excel') }}";
            if(dateStart || dateEnd) {
                url += `?inicio=${dateStart}&fin=${dateEnd}`;
            }
            window.location.href = url;
        });
    }"""
if "btnExportExcel" not in dash_content:
    dash_content = dash_content.replace("// Buscar en la tabla", js_export + "\n    // Buscar en la tabla")

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("Export Filter Feature implemented.")
