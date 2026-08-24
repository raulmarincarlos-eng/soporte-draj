import re

with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add DataTables CSS to top
if "dataTables.bootstrap5.min.css" not in content:
    content = content.replace("</style>", "</style>\n<link rel=\"stylesheet\" href=\"https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css\">")

# 2. Update Stats Cards to make room for KPI
old_stats = """    <div class="col-md-3 col-sm-6 mb-3">
        <div class="card border-0 shadow-sm rounded-4 h-100 stats-card hover-lift">
            <div class="card-body d-flex align-items-center">
                <div class="rounded-circle bg-primary bg-opacity-10 p-3 me-3 text-primary">
                    <i class="fas fa-calendar-alt fa-2x"></i>
                </div>
                <div>
                    <h3 class="fw-bold mb-0 text-primary">{{ total_mes }}</h3>
                    <span class="text-muted small fw-bold text-uppercase tracking-wide">Este Mes</span>
                </div>
            </div>
        </div>
    </div>
    <!-- Gráfico Circular -->
    <div class="col-md-3 mb-3">"""
new_stats = """    <div class="col-md-3 col-sm-6 mb-3">
        <div class="card border-0 shadow-sm rounded-4 h-100 stats-card hover-lift">
            <div class="card-body d-flex align-items-center">
                <div class="rounded-circle bg-primary bg-opacity-10 p-3 me-3 text-primary">
                    <i class="fas fa-calendar-alt fa-2x"></i>
                </div>
                <div>
                    <h3 class="fw-bold mb-0 text-primary">{{ total_mes }}</h3>
                    <span class="text-muted small fw-bold text-uppercase tracking-wide">Este Mes</span>
                </div>
            </div>
        </div>
    </div>
    <!-- KPI Promedio -->
    <div class="col-md-2 col-sm-6 mb-3">
        <div class="card border-0 shadow-sm rounded-4 h-100 stats-card hover-lift">
            <div class="card-body p-2 d-flex flex-column justify-content-center align-items-center text-center">
                <i class="fas fa-stopwatch text-info mb-1" style="font-size: 1.5rem;"></i>
                <h4 class="fw-bold mb-0 text-info">{{ tiempo_promedio }} <small class="fs-6">Días</small></h4>
                <span class="text-muted" style="font-size: 0.65rem; font-weight: 700; text-transform: uppercase;">Promedio<br>Resolución</span>
            </div>
        </div>
    </div>
    <!-- Gráfico Circular -->
    <div class="col-md-2 mb-3">"""
content = content.replace(old_stats, new_stats)
# Also fix col-md-3 to col-md-2 for the charts so they fit
content = content.replace('<!-- Gráfico de Barras -->\n    <div class="col-md-3">', '<!-- Gráfico de Barras -->\n    <div class="col-md-2">')

# 3. Add PDF Button to top right
old_btn = """            <a href="{{ url_for('exportar_excel') }}" class="btn btn-outline-success btn-lg shadow-sm fw-bold rounded-pill hover-scale">
                <i class="fas fa-file-excel me-2"></i>Exportar Excel
            </a>"""
new_btn = """            <a href="{{ url_for('exportar_excel') }}" class="btn btn-outline-success shadow-sm fw-bold rounded-pill hover-scale">
                <i class="fas fa-file-excel me-1"></i> Excel
            </a>
            <button id="btnExportPDF" class="btn btn-danger shadow-sm fw-bold rounded-pill hover-scale">
                <i class="fas fa-file-pdf me-1"></i> PDF
            </button>"""
content = content.replace(old_btn, new_btn)

# 4. Add SLA indicator in table
old_badge = """                            {% if item.resultado == 'Pendiente' %}
                                <span class="badge bg-info text-dark"><i class="fas fa-clock me-1"></i>Pendiente</span>"""
new_badge = """                            {% if item.resultado == 'Pendiente' %}
                                {% if item.dias_retraso and item.dias_retraso > 1 %}
                                <span class="badge bg-danger pulse-danger"><i class="fas fa-fire me-1"></i>Crítico ({{ item.dias_retraso }}d)</span>
                                <style>@keyframes pulse-danger { 0% { box-shadow: 0 0 0 0 rgba(220,53,69,0.7); } 70% { box-shadow: 0 0 0 10px rgba(220,53,69,0); } 100% { box-shadow: 0 0 0 0 rgba(220,53,69,0); } } .pulse-danger { animation: pulse-danger 2s infinite; }</style>
                                {% else %}
                                <span class="badge bg-info text-dark"><i class="fas fa-clock me-1"></i>Pendiente</span>
                                {% endif %}"""
content = content.replace(old_badge, new_badge)

# 5. Add JS for DataTables and html2pdf
old_scripts = """<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>"""
new_scripts = """<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script>
    // Inicializar DataTable
    $(document).ready(function() {
        $('.table').DataTable({
            language: { url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json' },
            pageLength: 10,
            ordering: false,
            dom: 'rt<"d-flex justify-content-between mt-3"ip>'
        });
    });
    
    // Generar PDF
    document.getElementById('btnExportPDF').addEventListener('click', function() {
        const element = document.querySelector('.row.mb-4'); // Stats + Charts
        const opt = {
            margin:       0.5,
            filename:     'Reporte_Gerencial_DRAJ.pdf',
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2 },
            jsPDF:        { unit: 'in', format: 'a4', orientation: 'landscape' }
        };
        html2pdf().set(opt).from(element).save();
    });
"""
content = content.replace(old_scripts, new_scripts)

# Note: because DataTable adds its own search, we should disable our custom search if we want, or keep both. I'll keep both for now, but DataTables handles the pagination beautifully.

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Dashboard UI updated with DataTables, SLA, and PDF")
