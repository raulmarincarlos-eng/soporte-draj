import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Padding bottom del body
content = re.sub(r'padding-bottom:\s*50px;', 'padding-bottom: 200px;', content)

# 2. Robot widget (vuelta a la derecha, alineado a flex-end)
old_widget = """    #robot-widget {
        position: fixed;
        bottom: 20px;
        left: 20px; /* MOVIDO A LA IZQUIERDA PARA NO TAPAR BOTONES DEL WIZARD */
        z-index: 9999;
        display: flex;
        flex-direction: column-reverse; /* Burbuja arriba del avatar */
        align-items: flex-start; /* Alineado a la izquierda */
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));
    }"""
new_widget = """    #robot-widget {
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
if old_widget in content:
    content = content.replace(old_widget, new_widget)

# 3. Speech bubble
old_bubble = """    .speech-bubble {
        background: #fff;
        border-radius: 20px 20px 20px 0; /* Cola del globo apuntando al avatar en la izq */
        padding: 15px 20px;
        border-left: 5px solid #198754;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        max-width: 320px;
        margin-bottom: 15px;
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        opacity: 0;
        transform: scale(0.5);
        transform-origin: bottom left; /* Crece desde abajo a la izquierda */
        transition: max-height 0.4s cubic-bezier(0, 1, 0.5, 1), padding 0.4s ease, opacity 0.3s;
        max-height: 500px;
        overflow: hidden;
    }"""
new_bubble = """    .speech-bubble {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px 20px 0 20px;
        padding: 12px 18px;
        border: 1px solid rgba(25, 135, 84, 0.2);
        border-bottom: 4px solid #198754;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        max-width: 260px;
        margin-bottom: 15px;
        margin-right: 5px;
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        opacity: 0;
        transform: scale(0.5);
        transform-origin: bottom right;
        transition: max-height 0.4s cubic-bezier(0, 1, 0.5, 1), padding 0.4s ease, opacity 0.3s;
        max-height: 500px;
        overflow: hidden;
    }"""
if old_bubble in content:
    content = content.replace(old_bubble, new_bubble)

# 4. Mobile media query
old_mobile = """    @media (max-width: 768px) {
        #robot-widget {
            bottom: 15px;
            left: 15px;
            transform: scale(0.85); /* Un poco más pequeño en móvil para no tapar nada */
            transform-origin: bottom left;
        }"""
new_mobile = """    @media (max-width: 768px) {
        #robot-widget {
            bottom: 15px;
            right: 15px;
            left: auto;
            transform: scale(0.85);
            transform-origin: bottom right;
        }"""
if old_mobile in content:
    content = content.replace(old_mobile, new_mobile)

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ultra fix aplicado.")
