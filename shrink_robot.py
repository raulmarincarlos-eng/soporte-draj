import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Shrink Avatar size
old_avatar = """    .robot-avatar {
        width: 100px;
        height: 100px;
        border-radius: 50%;"""
new_avatar = """    .robot-avatar {
        width: 70px;
        height: 70px;
        border-radius: 50%;"""
if old_avatar in content:
    content = content.replace(old_avatar, new_avatar)

# 2. Add 'collapsed' to the bubble on load
old_bubble_html = """<div class="speech-bubble" id="robot-bubble">"""
new_bubble_html = """<div class="speech-bubble collapsed" id="robot-bubble">"""
if old_bubble_html in content:
    content = content.replace(old_bubble_html, new_bubble_html)

# 3. Add a tooltip telling the user to click the robot, so they know it's there
old_widget_html = """<div id="robot-widget">
    <img src="{{ url_for('static', filename='img/robot.jpg') }}" alt="Robot Soporte" class="robot-avatar" id="robot-img" style="cursor: pointer;" onclick="toggleFAQ()">
    <div class="speech-bubble collapsed" id="robot-bubble">"""
new_widget_html = """<div id="robot-widget">
    <div id="robot-hint" style="background:#198754; color:white; padding:4px 10px; border-radius:12px; font-size:12px; font-weight:bold; margin-bottom:5px; animation: popIn 1s forwards; animation-delay: 2s; opacity:0; transform:scale(0.5); transform-origin:bottom center;">¡Hola! Tócame</div>
    <img src="{{ url_for('static', filename='img/robot.jpg') }}" alt="Robot Soporte" class="robot-avatar" id="robot-img" style="cursor: pointer;" onclick="toggleFAQ(); document.getElementById('robot-hint').style.display='none';">
    <div class="speech-bubble collapsed" id="robot-bubble">"""
if old_widget_html in content:
    content = content.replace(old_widget_html, new_widget_html)

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Robot shrunk and collapsed by default.")
