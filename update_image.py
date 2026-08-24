import shutil
import os
import re

# 1. Copy the clean image to overwrite the old one
src_image = r"C:\Users\Usuario\.gemini\antigravity-ide\brain\14747729-c9ea-4abd-a19e-4f2b49022e94\.user_uploaded\media_1787444961774.jpg"
dst_image = r"C:\Users\Usuario\Downloads\sistema_soporte_draj\static\img\carlos_profile.jpg"
shutil.copy2(src_image, dst_image)
print("Clean image copied.")

# 2. Update HTML to remove mask and change livacentro link to #
with open(r"C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\creditos.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the CSS mask
old_css = """        .profile-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top center;
            mask-image: linear-gradient(to right, transparent, black 15%);
            -webkit-mask-image: linear-gradient(to right, transparent, black 15%);
        }"""
new_css = """        .profile-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top center;
        }"""
if old_css in content:
    content = content.replace(old_css, new_css)

# Change the Livacentro link to #
old_link = """<a href="https://www.livacentro.com" target="_blank" title="Livacentro"><i class="fas fa-globe"></i></a>"""
new_link = """<a href="#" title="Website (Próximamente)"><i class="fas fa-globe"></i></a>"""
if old_link in content:
    content = content.replace(old_link, new_link)

with open(r"C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\creditos.html", "w", encoding="utf-8") as f:
    f.write(content)

print("HTML updated.")
