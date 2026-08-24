import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos el inicio y fin exacto del formulario
start_marker = '<div class="p-4 p-md-5">\n                    <form method="POST" action="{{ url_for(\'solicitar\') }}" id="form-solicitud">'
end_marker = '                    </form>\n                </div>'

if start_marker in content and end_marker in content:
    before_form = content.split(start_marker)[0]
    after_form = content.split(end_marker)[1]
    
    new_wizard_form = """
<div class="p-4 p-md-5 position-relative">
    
    <!-- WIZARD PROGRESS BAR -->
    <div class="wizard-progress-container mb-5 position-relative">
        <div class="progress" style="height: 4px; background-color: #e9ecef;">
            <div class="progress-bar bg-success transition-all" id="wizard-progress" role="progressbar" style="width: 33%;" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <div class="d-flex justify-content-between position-absolute w-100" style="top: -10px;">
            <div class="wizard-step-indicator active" id="indicator-1">
                <div class="icon"><i class="fas fa-user"></i></div>
                <span class="small fw-bold mt-2">Identidad</span>
            </div>
            <div class="wizard-step-indicator" id="indicator-2">
                <div class="icon"><i class="fas fa-map-marker-alt"></i></div>
                <span class="small fw-bold mt-2">Ubicación</span>
            </div>
            <div class="wizard-step-indicator" id="indicator-3">
                <div class="icon"><i class="fas fa-tools"></i></div>
                <span class="small fw-bold mt-2">Problema</span>
            </div>
        </div>
    </div>
    
    <style>
        .wizard-step-indicator { display: flex; flex-direction: column; align-items: center; color: #adb5bd; transition: all 0.4s; }
        .wizard-step-indicator .icon {
            width: 35px; height: 35px; background: #fff; border: 2px solid #e9ecef; border-radius: 50%;
            display: flex; align-items: center; justify-content: center; z-index: 2; transition: all 0.4s;
        }
        .wizard-step-indicator.active { color: #198754; }
        .wizard-step-indicator.active .icon { background: #198754; color: #fff; border-color: #198754; box-shadow: 0 0 15px rgba(25,135,84,0.4); }
        .wizard-step-indicator.completed .icon { background: #198754; color: #fff; border-color: #198754; }
        
        .wizard-step { display: none; animation: fadeInRight 0.5s cubic-bezier(0.16, 1, 0.3, 1); }
        .wizard-step.active { display: block; }
        
        @keyframes fadeInRight {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }
    </style>

    <form method="POST" action="{{ url_for('solicitar') }}" id="form-solicitud">
        
        <!-- PASO 1: IDENTIDAD -->
        <div class="wizard-step active" id="step-1">
            <h4 class="fw-bold mb-4 text-dark"><i class="fas fa-id-badge text-success me-2"></i>¿Quién reporta?</h4>
            <div class="row g-4">
                <div class="col-md-6">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="nombre_solicitante" name="nombre_solicitante" required placeholder="Ej: Juan Pérez">
                        <label for="nombre_solicitante">Nombre Solicitante *</label>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="contacto" name="contacto" required placeholder="Ej: Anexo 102 o Celular">
                        <label for="contacto">Celular / Anexo *</label>
                    </div>
                </div>
            </div>
            <div class="mt-5 d-flex justify-content-end">
                <button type="button" class="btn btn-glowing btn-lg px-5 rounded-pill fw-bold text-white shadow-lg" onclick="nextStep(1, 2)">
                    Siguiente <i class="fas fa-arrow-right ms-2"></i>
                </button>
            </div>
        </div>

        <!-- PASO 2: UBICACIÓN -->
        <div class="wizard-step" id="step-2">
            <h4 class="fw-bold mb-4 text-dark"><i class="fas fa-building text-success me-2"></i>¿Dónde te encuentras?</h4>
            <div class="row g-4">
                <div class="col-md-6">
                    <div class="form-floating">
                        <select class="form-select text-uppercase" name="direccion" id="direccion" required onchange="actualizarSubAreas()">
                            <option value="">Seleccione...</option>
                        </select>
                        <label for="direccion">Dirección / Agencia *</label>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-floating">
                        <select class="form-select" name="sub_area" id="sub_area">
                            <option value="">Seleccione la Dirección primero...</option>
                        </select>
                        <label for="sub_area">Oficina Específica</label>
                    </div>
                </div>
            </div>
            <div class="mt-5 d-flex justify-content-between">
                <button type="button" class="btn btn-outline-secondary btn-lg px-4 rounded-pill fw-bold" onclick="prevStep(2, 1)">
                    <i class="fas fa-arrow-left me-2"></i> Atrás
                </button>
                <button type="button" class="btn btn-glowing btn-lg px-5 rounded-pill fw-bold text-white shadow-lg" onclick="nextStep(2, 3)">
                    Siguiente <i class="fas fa-arrow-right ms-2"></i>
                </button>
            </div>
        </div>

        <!-- PASO 3: REQUERIMIENTO -->
        <div class="wizard-step" id="step-3">
            <h4 class="fw-bold mb-4 text-dark"><i class="fas fa-laptop-medical text-success me-2"></i>Detalles del Problema</h4>
            <div class="row g-4">
                <div class="col-md-6">
                    <div class="form-floating">
                        <select class="form-select" name="tipo_atencion" id="tipo_atencion" required>
                            <option value="">Seleccione...</option>
                            <option value="Incidencia">Incidencia (Problema/Falla)</option>
                            <option value="Requerimiento">Requerimiento (Nuevo servicio)</option>
                            <option value="Otros">Otros</option>
                        </select>
                        <label for="tipo_atencion">Tipo de Atención *</label>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-floating">
                        <input type="text" class="form-control" id="equipo" name="equipo" placeholder="Ej: 123 456 789">
                        <label for="equipo">PC / AnyDesk (Opcional)</label>
                    </div>
                </div>
                <div class="col-12">
                    <div class="form-floating">
                        <textarea class="form-control" id="descripcion" name="descripcion" style="height: 120px" required placeholder="Describa el problema con su equipo o sistema aquí..."></textarea>
                        <label for="descripcion">Descripción Detallada del Problema *</label>
                    </div>
                </div>
            </div>
            <div class="mt-5 d-flex justify-content-between">
                <button type="button" class="btn btn-outline-secondary btn-lg px-4 rounded-pill fw-bold" onclick="prevStep(3, 2)">
                    <i class="fas fa-arrow-left me-2"></i> Atrás
                </button>
                <button type="submit" id="btn-submit" class="btn btn-glowing btn-lg px-5 rounded-pill fw-bold text-white shadow-lg">
                    <span id="btn-text">Enviar Solicitud</span> <i class="fas fa-paper-plane ms-2" id="btn-icon"></i>
                    <span class="spinner-border spinner-border-sm ms-2 d-none" id="btn-spinner" role="status" aria-hidden="true"></span>
                </button>
            </div>
        </div>
    </form>
    
    <script>
        function validateStep(step) {
            let isValid = true;
            const currentStep = document.getElementById(`step-${step}`);
            const requiredInputs = currentStep.querySelectorAll('[required]');
            
            requiredInputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('is-invalid');
                    // Shake animation for error
                    input.style.animation = 'shake 0.5s';
                    setTimeout(() => input.style.animation = '', 500);
                } else {
                    input.classList.remove('is-invalid');
                    input.classList.add('is-valid');
                }
            });
            return isValid;
        }

        function nextStep(current, next) {
            if (validateStep(current)) {
                // Hide current, show next
                document.getElementById(`step-${current}`).classList.remove('active');
                document.getElementById(`step-${next}`).classList.add('active');
                
                // Update Progress bar
                const progressWidth = (next / 3) * 100;
                document.getElementById('wizard-progress').style.width = `${progressWidth}%`;
                
                // Update Indicators
                document.getElementById(`indicator-${current}`).classList.add('completed');
                document.getElementById(`indicator-${current}`).classList.remove('active');
                document.getElementById(`indicator-${next}`).classList.add('active');
                
                // Make robot talk (Optional UX touch)
                if (typeof hablarTexto === "function") {
                    if (next === 2) hablarTexto("Perfecto. Ahora indícame en qué agencia u oficina te encuentras.");
                    if (next === 3) hablarTexto("Casi listos. Descríbeme a detalle el problema que estás experimentando.");
                }
            }
        }

        function prevStep(current, prev) {
            document.getElementById(`step-${current}`).classList.remove('active');
            document.getElementById(`step-${prev}`).classList.add('active');
            
            const progressWidth = (prev / 3) * 100;
            document.getElementById('wizard-progress').style.width = `${progressWidth}%`;
            
            document.getElementById(`indicator-${current}`).classList.remove('active');
            document.getElementById(`indicator-${prev}`).classList.add('active');
            document.getElementById(`indicator-${prev}`).classList.remove('completed');
        }
        
        // CSS for shake
        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                25% { transform: translateX(-5px); }
                75% { transform: translateX(5px); }
            }
            .is-invalid { border-color: #dc3545 !important; box-shadow: 0 0 0 4px rgba(220, 53, 69, 0.15) !important; }
            .is-valid { border-color: #198754 !important; }
        `;
        document.head.appendChild(style);
    </script>
</div>
"""
    
    new_content = before_form + new_wizard_form + after_form
    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Wizard form successfully injected!")
else:
    print("Could not find the target form section to replace.")
