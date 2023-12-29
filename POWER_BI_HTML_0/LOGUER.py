from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import secrets

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Genera una clave secreta aleatoria
app.secret_key = secrets.token_hex(16)

# Crear una instancia de LoginManager y asociarla con la aplicación Flask
login_manager = LoginManager(app)

# Establecer la vista de función para manejar el inicio de sesión si el usuario no está autenticado
login_manager.login_view = 'login_page'

# Definir un diccionario de usuarios de ejemplo (reemplazar con una base de datos en producción)
users = {
    'Contratacion1': {'password': '123', 'report_page': 'report_page'},
    'Supervision1': {'password': '123', 'report_page': 'report_page_SUPERVISION'},
    'Valores1': {'password': '123', 'report_page': 'report_page_SOLO_VALORES'},
}
# Definir una clase de Usuario que hereda de UserMixin
class User(UserMixin):
    pass

# Definir una función para cargar un usuario por ID para el administrador de inicio de sesión
@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

# Definir una ruta para la URL raíz que renderiza la página de inicio de sesión
@app.route('/')
def login_page():
    return render_template('LOGUER.html')

# Definir rutas para diferentes páginas de informes, cada una requiere autenticación
@app.route('/ANO_DE_REPORTE_52R34F9T6S3A2_')
@login_required
def report_page():
    return render_template('ANO_DE_REPORTE.html')

@app.route('/ANO_DE_REPORTE_SUPERVISION')
@login_required
def report_page_SUPERVISION():
    return render_template('ANO_DE_REPORTE_SUPERVISION.html')

@app.route('/ANO_PARA_VALORES')
@login_required
def report_page_SOLO_VALORES():
    return render_template('ANO_PARA_VALORES.html')

# Definir rutas para diferentes páginas de informes para el año 2023
@app.route('/2023_R8T5C6O4N2A')
@login_required
def informe_2023():
    return render_template('2023.html')

@app.route('/2023_8S4UPE5RV5ICI6ON65642')
@login_required
def informe_2023_SUPERVICION():
    return render_template('2023_SUPERVICION.html')

@app.route('/2023_PARA_8S4UPE5RV5ICI6ON65642')
@login_required
def informe_2023_PARA_SUPERVICION():
    return render_template('2023_PARA_SUPERVICION.html')

# Definir rutas para diferentes páginas de informes relacionadas con valores
@app.route('/VALORES_*44554GRGFV*FDG')
@login_required
def informe_VALORES():
    return render_template('VALORES.html')

@app.route('/SOLO_VALORES_*445EWSFDVC54GRGFV*FDG')
@login_required
def informe_SOLO_VALORES():
    return render_template('SOLO_VALORES.html')

#-----------------------------------------
#manejador de errores comunes
#-----------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
#-----------------------------------------

# Definir una ruta para manejar el envío del formulario de inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    # Obtener el nombre de usuario y la contraseña del formulario
    username = request.form.get('username')
    password = request.form.get('password')

    # Verificar si el usuario existe y si la contraseña es correcta
    user = users.get(username)
    if user and user['password'] == password:
        user_obj = User()
        user_obj.id = username
        login_user(user_obj)
        return redirect(url_for(user['report_page']))
    else:
        return redirect(url_for('login_page'))

# Definir una ruta para manejar el cierre de sesión del usuario
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))

# Ejecutar la aplicación si el script se ejecuta directamente
if __name__ == '__main__':
    #app.run(debug=True, port=5017) #Modo de desarrollo de Flask
    app.run(debug=False) #modo de producción
