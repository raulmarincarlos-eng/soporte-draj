import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Mover el widget a la derecha extrema
old_widget = """    #robot-widget {
        position: fixed;
        bottom: 20px;
        right: 20px;
        left: auto;
        z-index: 9999;
        display: flex;
        flex-direction: column-reverse;
        align-items: flex-end;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2));
    }"""
new_widget = """    #robot-widget {
        position: fixed;
        bottom: 15px;
        right: 15px; /* Más pegado al borde derecho */
        left: auto;
        z-index: 9999;
        display: flex;
        flex-direction: column-reverse;
        align-items: flex-end;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2));
    }"""
if old_widget in content:
    content = content.replace(old_widget, new_widget)

# 2. Ajustar la burbuja para que la cola apunte mejor al centro del avatar
old_bubble = """        margin-bottom: 15px;
        margin-right: 5px;"""
new_bubble = """        margin-bottom: 15px;
        margin-right: 10px; /* Alinea la colita más al centro del avatar */"""
if old_bubble in content:
    content = content.replace(old_bubble, new_bubble)

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Widget movido más a la derecha.")
