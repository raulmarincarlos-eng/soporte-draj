import os
import shutil
import glob
import re

# 1. Copy the latest uploaded image
upload_dir = r"C:\Users\Usuario\.gemini\antigravity-ide\brain\14747729-c9ea-4abd-a19e-4f2b49022e94\.user_uploaded"
dest_dir = r"C:\Users\Usuario\Downloads\sistema_soporte_draj\static\img"
os.makedirs(dest_dir, exist_ok=True)

# Get latest png or jpg
files = glob.glob(os.path.join(upload_dir, "*.*"))
if files:
    latest_file = max(files, key=os.path.getctime)
    shutil.copy2(latest_file, os.path.join(dest_dir, "carlos_profile.png"))
    print(f"Copied {latest_file} to carlos_profile.png")
else:
    print("No images found in user_uploaded directory.")

# 2. Modify app.py to add /creditos route
with open(r"C:\Users\Usuario\Downloads\sistema_soporte_draj\app.py", "r", encoding="utf-8") as f:
    app_content = f.read()

route_code = """
@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

if __name__ == '__main__':
"""
if "@app.route('/creditos')" not in app_content:
    app_content = app_content.replace("if __name__ == '__main__':", route_code)
    with open(r"C:\Users\Usuario\Downloads\sistema_soporte_draj\app.py", "w", encoding="utf-8") as f:
        f.write(app_content)
    print("Added /creditos route to app.py")


# 3. Modify base.html to remove the modal logic and just navigate
with open(r"C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\base.html", "r", encoding="utf-8") as f:
    base_content = f.read()

# I will replace the script logic for btnCredits
old_script = """                btnCredits.addEventListener('click', () => {
                    creditsModal.classList.remove('d-none');
                    // Force reflow
                    void creditsModal.offsetWidth;
                    creditsModal.classList.add('show');
                });
                
                const closeModal = () => {
                    creditsModal.classList.remove('show');
                    setTimeout(() => { creditsModal.classList.add('d-none'); }, 800); // Matches CSS transition duration
                };
                
                closeBtn.addEventListener('click', closeModal);
                backdrop.addEventListener('click', closeModal);"""

new_script = """                btnCredits.addEventListener('click', () => {
                    window.location.href = '/creditos';
                });"""

if "window.location.href = '/creditos';" not in base_content:
    if old_script in base_content:
        base_content = base_content.replace(old_script, new_script)
        with open(r"C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\base.html", "w", encoding="utf-8") as f:
            f.write(base_content)
        print("Updated base.html button logic")
    else:
        print("Warning: could not find old script in base.html")
