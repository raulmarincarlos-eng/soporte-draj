import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for Robot Widget position
old_css = """    /* WIDGET DEL ROBOT FIJO */
    #robot-widget {
        position: fixed;
        top: 15vh;
        right: 30px;
        z-index: 9999;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1));
    }"""
new_css = """    /* WIDGET DEL ROBOT FIJO */
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
if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Could not find robot widget CSS")

# 2. Update CSS for Speech Bubble margin to fit column-reverse
old_bubble = """        max-width: 280px;
        margin-top: 15px;"""
new_bubble = """        max-width: 320px;
        margin-bottom: 15px; /* Margin changed for column-reverse */"""
if old_bubble in content:
    content = content.replace(old_bubble, new_bubble)

# 3. Update the Voice Synthesis logic
old_voice = """                const utterance = new SpeechSynthesisUtterance(textoLimpio);
                utterance.lang = 'es-MX';
                utterance.pitch = 1.1;
                utterance.rate = 1.0;
                
                if (vocesAmigables.length === 0) vocesAmigables = window.speechSynthesis.getVoices().filter(v => v.lang.includes('es'));
                const vozIdeal = vocesAmigables.find(v => v.name.includes('Google') || v.name.includes('Sabina') || v.name.includes('Mia') || v.name.includes('Paulina'));
                if (vozIdeal) utterance.voice = vozIdeal;"""
new_voice = """                const utterance = new SpeechSynthesisUtterance(textoLimpio);
                utterance.lang = 'es-MX';
                utterance.pitch = 1.0; // Más natural, menos agudo
                utterance.rate = 1.05; // Un poco más dinámico
                
                if (vocesAmigables.length === 0) vocesAmigables = window.speechSynthesis.getVoices().filter(v => v.lang.includes('es'));
                
                // Buscar la voz más premium disponible (Natural/Online suelen ser IA)
                let vozIdeal = vocesAmigables.find(v => v.name.includes('Natural') || v.name.includes('Online'));
                // Si no hay Premium, buscar las estándar buenas
                if (!vozIdeal) {
                    vozIdeal = vocesAmigables.find(v => v.name.includes('Google') || v.name.includes('Sabina') || v.name.includes('Mia'));
                }
                if (vozIdeal) utterance.voice = vozIdeal;"""
if old_voice in content:
    content = content.replace(old_voice, new_voice)
else:
    print("Could not find voice logic")

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\templates\solicitar.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Robot Widget updated successfully!")
