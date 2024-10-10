# app.py

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from auth import authenticate_user
from models import User
from database import initialize_db, get_db_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Substitua por uma chave secreta real e segura

# Inicializar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Nome da função de rota para login

# Inicializar o banco de dados
initialize_db()

# Carrega o usuário para as sessões de login
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = authenticate_user(username, password)
        if user:
            login_user(user)
            # flash('Login realizado com sucesso!', 'success')
            # Redireciona para a área administrativa se o usuário for admin, senão para o dashboard
            if user.role == 'admin':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('dashboard'))
        else:
            flash('Login inválido. Verifique seu usuário e senha.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', drive_link=current_user.drive_link)

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if current_user.role != 'admin':
        flash('Acesso negado: Área administrativa.', 'danger')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        drive_link = request.form.get('drive_link')
        role = request.form.get('role', 'user').lower()

        if role not in ['admin', 'user']:
            flash('Papel inválido. Definindo como "user" por padrão.', 'warning')
            role = 'user'

        # Inserir o novo usuário
        success = User.create(username, password, drive_link, role)
        if success:
            flash(f'Usuário "{username}" adicionado com sucesso como "{role}"!', 'success')
            return redirect(url_for('admin'))
        else:
            flash(f'Erro: O usuário "{username}" já existe.', 'danger')

    # Recupera todos os usuários para exibir na área administrativa (opcional)
    conn = get_db_connection()
    users = conn.execute('SELECT username, role FROM users').fetchall()
    conn.close()

    return render_template('admin.html', users=users)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu com sucesso.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
