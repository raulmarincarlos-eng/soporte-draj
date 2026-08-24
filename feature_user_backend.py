import re

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ensure generate_password_hash is imported
if 'generate_password_hash' not in content:
    content = content.replace('from werkzeug.security import check_password_hash', 'from werkzeug.security import check_password_hash, generate_password_hash')

# 2. Update the login logic to handle roles and redirect
old_login = """        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            session['nombre'] = user['nombre']
            return redirect(url_for('dashboard'))"""
new_login = """        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            session['nombre'] = user['nombre']
            session['role'] = user.get('role', 'admin') # Default to admin for backwards compatibility
            
            if session['role'] == 'user':
                return redirect(url_for('mis_tickets'))
            else:
                return redirect(url_for('dashboard'))"""
if old_login in content:
    content = content.replace(old_login, new_login)

# 3. Add the registro and mis_tickets routes
# We can insert them after the logout route
old_logout = """@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))"""

new_routes = """@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/registro', methods=['POST'])
def registro():
    db = get_db_connection()
    dni = request.form.get('dni')
    password = request.form.get('password')
    nombre = request.form.get('nombre')
    
    if db.usuarios.find_one({"username": dni}):
        flash('Este DNI ya está registrado.', 'danger')
        return redirect(url_for('login'))
        
    db.usuarios.insert_one({
        "username": dni,
        "password": generate_password_hash(password),
        "nombre": nombre.upper(),
        "role": "user"
    })
    flash('Cuenta creada con éxito. Ahora puedes iniciar sesión.', 'success')
    return redirect(url_for('login'))

@app.route('/mis_tickets')
@login_required
def mis_tickets():
    if session.get('role') != 'user':
        return redirect(url_for('dashboard'))
        
    db = get_db_connection()
    atenciones = list(db.atenciones.find({
        "$or": [
            {"usuario_id": session['user_id']},
            {"conf_nombre": session['nombre']}
        ]
    }).sort("id_secuencial", -1))
    
    return render_template('mis_tickets.html', atenciones=atenciones)"""
if old_logout in content:
    content = content.replace(old_logout, new_routes)

# 4. Update the index redirect
old_index = """@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('solicitar'))"""
new_index = """@app.route('/')
def index():
    if 'user_id' in session:
        if session.get('role') == 'user':
            return redirect(url_for('mis_tickets'))
        return redirect(url_for('dashboard'))
    return redirect(url_for('solicitar'))"""
if old_index in content:
    content = content.replace(old_index, new_index)

# 5. Link User ID in solicitar
old_solicitar_doc = """            "conf_nombre": request.form.get('nombre_solicitante', '').upper(),
            "conf_cargo": "", "conf_fecha": "", "resp_nombre": "", "resp_cargo": "", "resp_fecha": ""
        }
        db.atenciones.insert_one(doc)"""
new_solicitar_doc = """            "conf_nombre": request.form.get('nombre_solicitante', '').upper(),
            "conf_cargo": "", "conf_fecha": "", "resp_nombre": "", "resp_cargo": "", "resp_fecha": ""
        }
        
        if 'user_id' in session:
            doc['usuario_id'] = session['user_id']
            # If user is logged in, use their real name if form was skipped
            if not doc['conf_nombre']:
                doc['conf_nombre'] = session.get('nombre', '').upper()
                
        db.atenciones.insert_one(doc)"""
if old_solicitar_doc in content:
    content = content.replace(old_solicitar_doc, new_solicitar_doc)

with open(r'C:\Users\Usuario\Downloads\sistema_soporte_draj\app.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Backend para Portal de Usuarios completado.")
