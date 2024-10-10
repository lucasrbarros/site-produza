# add_user.py

from models import User
import getpass

def main():
    print("Adicionar Novo Usuário")
    username = input("Nome de usuário: ").strip()
    
    # Utilize getpass para não exibir a senha no terminal
    password = getpass.getpass("Senha: ").strip()
    
    drive_link = input("Link para Fotos: ").strip()
    role = input("Papel do usuário (admin/user): ").strip().lower()

    if role not in ['admin', 'user']:
        print("Papel inválido. Definindo como 'user' por padrão.")
        role = 'user'

    success = User.create(username, password, drive_link, role)
    if success:
        print(f'Usuário "{username}" adicionado com sucesso como "{role}"!')
    else:
        print(f'Erro: O usuário "{username}" já existe.')

if __name__ == "__main__":
    main()
