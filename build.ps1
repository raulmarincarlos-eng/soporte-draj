# Compilar a .exe ocultando la consola y agregando recursos estáticos
python -m PyInstaller --noconfirm --onefile --windowed --icon="Soporte_DRAJ.ico" --add-data "templates;templates/" --add-data "static;static/" --hidden-import pymongo --name "Soporte_DRAJ" app.py
