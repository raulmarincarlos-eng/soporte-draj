import os

file_path = "templates/solicitar.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update #robot-widget position
content = content.replace("bottom: 100px;", "top: 15vh;")

# 2. Update .speech-bubble CSS
content = content.replace("border-radius: 20px 20px 0 20px;", "border-radius: 20px 0 20px 20px;")
content = content.replace("margin-bottom: 15px;", "margin-top: 15px;")
content = content.replace("transform-origin: bottom right;", "transform-origin: top right;")
content = content.replace("margin-bottom: 0;", "margin-top: 0;")

# 3. Swap img and speech bubble
img_tag = '<img src="{{ url_for(\'static\', filename=\'img/robot.jpg\') }}" alt="Robot Soporte" class="robot-avatar" id="robot-img" style="cursor: pointer;" onclick="toggleFAQ()">'
if img_tag in content:
    content = content.replace(img_tag, "")
    content = content.replace('<div id="robot-widget">', '<div id="robot-widget">\n    ' + img_tag)

# 4. Rename Tech-E to Robot Carlos v1.0.3.04 in HTML
content = content.replace('<i class="fas fa-robot me-2"></i>Tech-E', '<i class="fas fa-robot me-2"></i>Robot Carlos <span class="badge bg-secondary ms-1" style="font-size: 0.6rem;">v1.0.3.04</span>')

# 5. Rename in JS Speech
content = content.replace('Soy Tech-E.', 'Soy Robot Carlos, diseñado por DRAJ.')

# 6. Change chevron-down to chevron-up since bubble expands down now
content = content.replace('<i class="fas fa-chevron-down"></i>', '<i class="fas fa-chevron-up"></i>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully.")
