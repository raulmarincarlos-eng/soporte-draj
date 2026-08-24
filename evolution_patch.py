import re

# 1. Update base.html to use SweetAlert2 and Inter font globally
with open('templates/base.html', 'r', encoding='utf-8') as f:
    base_content = f.read()

# Add font-family to body
body_tag = """<body>
    <style>"""
body_new = """<body style="font-family: 'Inter', sans-serif; background-color: #f4f7f9;">
    <!-- SweetAlert2 -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <style>"""
base_content = base_content.replace(body_tag, body_new)

# Replace standard Flask flashes with SweetAlert Toasts
flash_block = """        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ 'success' if category == 'success' else ('danger' if category == 'danger' else 'warning') }} alert-dismissible fade show mb-4 shadow-sm" role="alert" style="border-radius: 12px; border-left: 5px solid {{ '#198754' if category=='success' else ('#dc3545' if category=='danger' else '#ffc107') }};">
                    {% if category == 'success' %}
                        <i class="fas fa-check-circle me-2"></i>
                    {% elif category == 'danger' %}
                        <i class="fas fa-exclamation-triangle me-2"></i>
                    {% else %}
                        <i class="fas fa-info-circle me-2"></i>
                    {% endif %}
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            {% endfor %}
        {% endif %}
        {% endwith %}"""

sweetalert_block = """        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <script>
                document.addEventListener('DOMContentLoaded', function() {
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'top-end',
                        showConfirmButton: false,
                        timer: 4000,
                        timerProgressBar: true,
                        didOpen: (toast) => {
                            toast.addEventListener('mouseenter', Swal.stopTimer)
                            toast.addEventListener('mouseleave', Swal.resumeTimer)
                        }
                    });
                    {% for category, message in messages %}
                    Toast.fire({
                        icon: '{{ "success" if category == "success" else ("error" if category == "danger" else "warning") }}',
                        title: '{{ message }}'
                    });
                    {% endfor %}
                });
            </script>
        {% endif %}
        {% endwith %}"""
base_content = base_content.replace(flash_block, sweetalert_block)

# Add glassmorphism upgrade to style
old_island = """    .modern-island {
        background: #fff;
        border-radius: 20px;
        border: none;
        box-shadow: 0 8px 25px rgba(0,0,0,0.03);"""
new_island = """    .modern-island {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);"""
if old_island in base_content:
    base_content = base_content.replace(old_island, new_island)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_content)

# Also update modern-island in formulario.html since it has its own style block
with open('templates/formulario.html', 'r', encoding='utf-8') as f:
    form_content = f.read()
if old_island in form_content:
    form_content = form_content.replace(old_island, new_island)
with open('templates/formulario.html', 'w', encoding='utf-8') as f:
    f.write(form_content)


# 2. Update dashboard.html to add Counter Animations and hover scales
with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    dash_content = f.read()

# Animate counters in dashboard
counter_script = """
    // Animación de contadores numéricos
    const animateCounters = () => {
        const counters = document.querySelectorAll('.stat-number');
        counters.forEach(counter => {
            const target = +counter.innerText;
            const duration = 1500; // ms
            const step = target / (duration / 16); // 60fps
            
            let current = 0;
            counter.innerText = '0';
            
            const updateCounter = () => {
                current += step;
                if (current < target) {
                    counter.innerText = Math.ceil(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.innerText = target;
                }
            };
            if(target > 0) updateCounter();
        });
    };
    document.addEventListener('DOMContentLoaded', animateCounters);
"""
if 'animateCounters' not in dash_content:
    dash_content = dash_content.replace("</script>\n{% endblock %}", counter_script + "\n</script>\n{% endblock %}")

# Add hover effects to table rows for elegance
table_hover_style = """<style>
    .glass-row { transition: all 0.2s ease; }
    .glass-row:hover { background-color: rgba(25, 135, 84, 0.04) !important; transform: scale(1.005); box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-radius: 8px; z-index: 10; position: relative;}
</style>"""
if 'glass-row' not in dash_content:
    dash_content = dash_content.replace('{% block content %}', '{% block content %}\n' + table_hover_style)
dash_content = dash_content.replace('<tr class="align-middle">', '<tr class="align-middle glass-row">')

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("Evolution patch applied.")
