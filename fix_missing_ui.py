import re

def fix_dashboard():
    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\dashboard.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove lines 119 to 132 (1-indexed, so index 118 to 131)
    # Let's dynamically find it in case line numbers shifted slightly
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if '<!-- Robot Widget Premium -->' in line:
            start_idx = i
        if start_idx != -1 and i > start_idx and '</div>' in line and i - start_idx >= 13:
            end_idx = i
            break
            
    if start_idx != -1:
        # Also remove the wrapper <div class="d-flex justify-content-end mb-4">
        # Looking at my previous view_file, the wrapper closes at line 132.
        # It's exactly 14 lines. Let's just delete the block by matching the string.
        content = "".join(lines)
        toast_regex = re.compile(r'<!-- Robot Widget Premium -->.*?</div>\s*</div>', re.DOTALL)
        content = toast_regex.sub('', content)
        with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\dashboard.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Removed static toast from dashboard.html")

def fix_base():
    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\base.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_to_add = """
        /* Premium Navbar Glassmorphism */
        .navbar-floating-wrapper { padding: 15px 20px; }
        .navbar-glass {
            background: linear-gradient(135deg, rgba(25, 135, 84, 0.9) 0%, rgba(20, 108, 67, 0.95) 100%) !important;
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 25px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            border: 1px solid rgba(255,255,255,0.1);
        }
        body.dark-mode .navbar-glass {
            background: linear-gradient(135deg, rgba(20, 20, 20, 0.9) 0%, rgba(10, 10, 10, 0.95) 100%) !important;
            border: 1px solid rgba(25, 135, 84, 0.5);
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }
    """
    if "Premium Navbar Glassmorphism" not in content:
        content = content.replace('/* Micro-interacciones Globales */', css_to_add + '\n        /* Micro-interacciones Globales */')

    with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\base.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added premium navbar CSS to base.html")

if __name__ == '__main__':
    fix_dashboard()
    fix_base()
