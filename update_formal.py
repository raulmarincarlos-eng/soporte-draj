import os

file_path = "templates/solicitar.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the version badge
content = content.replace('<span class="badge bg-secondary ms-1" style="font-size: 0.6rem;">v1.0.3.04</span>', '')

# 2. Rename to just "Carlos" and keep the robot icon
content = content.replace('<i class="fas fa-robot me-1"></i>Robot Carlos', '<i class="fas fa-robot me-2"></i>Carlos')

# 3. Update the greetings array to be formal and use "Carlos"
old_greetings = """    const greetings = [
        "¡Hola! Soy Robot Carlos. Toca mi imagen para ver mis opciones o minimízame si prefieres silencio.",
        "¡Bienvenido! Robot Carlos a tu servicio, creado por DRAJ. ¿En qué te ayudo?",
        "¡Qué tal! Soy Robot Carlos. Haz clic en mi cabeza para abrir el menú."
    ];"""

new_greetings = """    const greetings = [
        "Estimado usuario, soy Carlos, su asistente virtual de DRAJ. Haga clic en mi imagen para ver las opciones.",
        "Bienvenido. Soy Carlos, asistente de soporte DRAJ. ¿En qué le puedo ayudar hoy?",
        "Saludos cordiales. Soy Carlos. Haga clic en la imagen para desplegar el menú de ayuda."
    ];"""
content = content.replace(old_greetings, new_greetings)

# 4. Update the time-based greetings
content = content.replace('Soy Robot Carlos. Toca mi imagen para ver mis opciones o minimízame si prefieres silencio.', 'Soy Carlos, asistente de DRAJ. Haga clic en mi imagen para ver las opciones disponibles.')
content = content.replace('Soy Robot Carlos, diseñado por DRAJ.', 'Soy Carlos, asistente de soporte de DRAJ.')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Formalized Carlos successfully.")
