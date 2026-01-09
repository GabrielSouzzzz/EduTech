from db import conectar

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT
        )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()

def cadastrar():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome, email, telefone) VALUES (?, ?, ?)",
        (nome, email, telefone)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Usuário cadastrado com sucesso!")

def listar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    print("\n📋 LISTA DE USUÁRIOS")
    for u in usuarios:
        print(u)

    cursor.close()
    conexao.close()

def atualizar():
    id_usuario = input("ID do usuário a atualizar: ")
    nome = input("Novo nome: ")
    email = input("Novo email: ")
    telefone = input("Novo telefone: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE usuarios SET nome=?, email=?, telefone=? WHERE id=?",
        (nome, email, telefone, id_usuario)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✏️ Usuário atualizado!")

def excluir():
    id_usuario = input("ID do usuário a excluir: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("🗑️ Usuário excluído!")

# PROGRAMA PRINCIPAL
criar_tabela()

while True:
    print("""
1 - Cadastrar usuário
2 - Listar usuários
3 - Atualizar usuário
4 - Excluir usuário
0 - Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        excluir()
    elif opcao == "0":
        print("👋 Saindo...")
        break
    else:
        print("❌ Opção inválida")
