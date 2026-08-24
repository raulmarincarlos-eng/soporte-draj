import re
from datetime import datetime

with open('app.py', 'r', encoding='utf-8') as f:
    app_content = f.read()

# Add SLA and KPI logic in /dashboard
old_dashboard = """    current_month = datetime.now().strftime('%Y-%m')
    total_mes = db.atenciones.count_documents({"fecha_registro": {"$regex": f"^{current_month}"}})
    
    resultados_data = db.atenciones.aggregate(["""
new_dashboard = """    current_month = datetime.now().strftime('%Y-%m')
    total_mes = db.atenciones.count_documents({"fecha_registro": {"$regex": f"^{current_month}"}})
    
    # SLA y KPI: Tiempo de Resolución Promedio
    total_dias = 0
    atendidos_count = 0
    now = datetime.now()
    
    for a in atenciones:
        # Calcular SLA para pendientes
        if a.get('resultado') == 'Pendiente':
            fecha_reg = a.get('fecha_registro')
            if fecha_reg:
                try:
                    fecha_obj = datetime.strptime(fecha_reg, '%Y-%m-%d')
                    dias_retraso = (now - fecha_obj).days
                    a['dias_retraso'] = dias_retraso
                except:
                    a['dias_retraso'] = 0
        
        # Calcular KPI de tiempo promedio
        if a.get('resultado') in ['Atendido', 'Parcial'] and a.get('fecha_cierre'):
            try:
                f_ini = datetime.strptime(a.get('fecha_registro'), '%Y-%m-%d')
                f_fin = datetime.strptime(a.get('fecha_cierre'), '%Y-%m-%d')
                dias = (f_fin - f_ini).days
                total_dias += dias
                atendidos_count += 1
            except:
                pass
                
    tiempo_promedio = round(total_dias / atendidos_count, 1) if atendidos_count > 0 else 0
    
    resultados_data = db.atenciones.aggregate(["""
if "# Calcular SLA para pendientes" not in app_content:
    app_content = app_content.replace(old_dashboard, new_dashboard)

# Ensure tiempo_promedio is passed to the template
old_return = """                           total_mes=total_mes, 
                           resultados_dict=resultados_dict, """
new_return = """                           total_mes=total_mes,
                           tiempo_promedio=tiempo_promedio, 
                           resultados_dict=resultados_dict, """
if "tiempo_promedio=tiempo_promedio" not in app_content:
    app_content = app_content.replace(old_return, new_return)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_content)
print("SLA and KPI logic injected in app.py")
