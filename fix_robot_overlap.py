import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #robot-widget CSS
old_widget_css = """    /* WIDGET DEL ROBOT FIJO */
    #robot-widget {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
        display: flex;
        flex-direction: column-reverse; /* Bubble appears ABOVE avatar */
        align-items: flex-end;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));
    }"""
new_widget_css = """    /* WIDGET DEL ROBOT FIJO */
    #robot-widget {
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
if old_widget_css in content:
    content = content.replace(old_widget_css, new_widget_css)
else:
    print("WARNING: Could not find old_widget_css")

# 2. Update .speech-bubble CSS
old_bubble_css = """    .speech-bubble {
        background: #fff;
        border-radius: 20px 0 20px 20px;
        padding: 15px 20px;
        border-left: 5px solid #198754;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        max-width: 320px;
        margin-bottom: 15px; /* Margin changed for column-reverse */
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        opacity: 0;
        transform: scale(0.5);
        transform-origin: top right;
        transition: max-height 0.4s cubic-bezier(0, 1, 0.5, 1), padding 0.4s ease, opacity 0.3s;
        max-height: 500px;
        overflow: hidden;
    }"""
new_bubble_css = """    .speech-bubble {
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
if old_bubble_css in content:
    content = content.replace(old_bubble_css, new_bubble_css)
else:
    print("WARNING: Could not find old_bubble_css")

# 3. Fix the mobile media query so it doesn't break our new left alignment
old_media = """    /* ROBOT MOBILE RESPONSIVE */
    @media (max-width: 768px) {
        #robot-widget {
            bottom: 15px;
            left: 15px;
        }"""
new_media = """    /* ROBOT MOBILE RESPONSIVE */
    @media (max-width: 768px) {
        #robot-widget {
            bottom: 15px;
            left: 15px;
            transform: scale(0.85); /* Un poco más pequeño en móvil para no tapar nada */
            transform-origin: bottom left;
        }"""
if old_media in content:
    content = content.replace(old_media, new_media)
else:
    print("WARNING: Could not find old_media")

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Robot overlap fixed!")
