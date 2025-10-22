import oracledb


# CONEXÃO

USERNAME = "seu_usuario"      # Exemplo: system
PASSWORD = "sua_senha"        # Senha do Oracle
DSN = "localhost/XE"          # Ajuste conforme seu Oracle (ex: localhost:1521/XEPDB1)

def conectar():
    """Conecta ao banco Oracle"""
    try:
        conn = oracledb.connect(user=USERNAME, password=PASSWORD, dsn=DSN)
        print("✅ Conexão bem-sucedida!")
        return conn
    except Exception as e:
        print("Erro ao conectar ao Oracle:", e)
        exit()


# CRUD CARGOS

def inserir_cargo(conn):
    cursor = conn.cursor()
    cargo_id = int(input("ID do cargo: "))
    nome = input("Nome do cargo: ")
    departamento = input("Departamento: ")
    cursor.execute("""
        INSERT INTO Cargos (cargo_id, cargo_nome, cargo_departamento)
        VALUES (:1, :2, :3)
    """, (cargo_id, nome, departamento))
    conn.commit()
    print("Cargo inserido com sucesso.\n")

def alterar_cargo(conn):
    cursor = conn.cursor()
    cargo_id = int(input("ID do cargo a alterar: "))
    novo_nome = input("Novo nome do cargo: ")
    cursor.execute("""
        UPDATE Cargos SET cargo_nome = :1 WHERE cargo_id = :2
    """, (novo_nome, cargo_id))
    conn.commit()
    print("Cargo alterado com sucesso.\n")

def excluir_cargo(conn):
    cursor = conn.cursor()
    cargo_id = int(input("ID do cargo a excluir: "))
    cursor.execute("DELETE FROM Cargos WHERE cargo_id = :1", (cargo_id,))
    conn.commit()
    print("Cargo excluído com sucesso.\n")

def listar_cargos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cargos")
    print("\n=== LISTA DE CARGOS ===")
    for row in cursor:
        print(row)
    print()


# CRUD FUNCIONÁRIOS

def inserir_funcionario(conn):
    cursor = conn.cursor()
    funcionario_id = int(input("ID do funcionário: "))
    cargo_id = int(input("ID do cargo: "))
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    salario = float(input("Salário: "))
    idade = int(input("Idade: "))

    cursor.execute("""
        INSERT INTO Funcionarios (funcionario_id, cargo_id, funcionario_cpf, funcionario_nome, funcionario_salario, funcionario_idade)
        VALUES (:1, :2, :3, :4, :5, :6)
    """, (funcionario_id, cargo_id, cpf, nome, salario, idade))
    conn.commit()
    print("Funcionário inserido com sucesso.\n")

def alterar_funcionario(conn):
    cursor = conn.cursor()
    funcionario_id = int(input("ID do funcionário a alterar: "))
    novo_nome = input("Novo nome: ")

    cursor.execute("""
        UPDATE Funcionarios SET funcionario_nome = :1 WHERE funcionario_id = :2
    """, (novo_nome, funcionario_id))
    conn.commit()
    print("Funcionário alterado com sucesso.\n")

def excluir_funcionario(conn):
    cursor = conn.cursor()
    funcionario_id = int(input("ID do funcionário a excluir: "))
    cursor.execute("DELETE FROM Funcionarios WHERE funcionario_id = :1", (funcionario_id,))
    conn.commit()
    print("Funcionário excluído com sucesso.\n")

def listar_funcionarios(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT f.funcionario_id, f.funcionario_nome, c.cargo_nome, f.funcionario_salario, f.funcionario_idade
        FROM Funcionarios f
        JOIN Cargos c ON f.cargo_id = c.cargo_id
    """)
    print("\n=== LISTA DE FUNCIONÁRIOS ===")
    for row in cursor:
        print(row)
    print()


# CRUD ENDEREÇOS

def inserir_endereco(conn):
    cursor = conn.cursor()
    endereco_id = int(input("ID do endereço: "))
    logradouro = input("Logradouro: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (UF): ")
    cep = int(input("CEP: "))

    cursor.execute("""
        INSERT INTO Enderecos (endereco_id, endereco_logradouro, endereco_bairro, endereco_cidade, endereco_estado, endereco_CEP)
        VALUES (:1, :2, :3, :4, :5, :6)
    """, (endereco_id, logradouro, bairro, cidade, estado, cep))
    conn.commit()
    print("Endereço inserido com sucesso.\n")

def alterar_endereco(conn):
    cursor = conn.cursor()
    endereco_id = int(input("ID do endereço a alterar: "))
    nova_cidade = input("Nova cidade: ")
    cursor.execute("""
        UPDATE Enderecos SET endereco_cidade = :1 WHERE endereco_id = :2
    """, (nova_cidade, endereco_id))
    conn.commit()
    print("Endereço alterado com sucesso.\n")

def excluir_endereco(conn):
    cursor = conn.cursor()
    endereco_id = int(input("ID do endereço a excluir: "))
    cursor.execute("DELETE FROM Enderecos WHERE endereco_id = :1", (endereco_id,))
    conn.commit()
    print("Endereço excluído com sucesso.\n")

def listar_enderecos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Enderecos")
    print("\n=== LISTA DE ENDEREÇOS ===")
    for row in cursor:
        print(row)
    print()

# CRUD PROFESSORES

def inserir_professor(conn):
    cursor = conn.cursor()
    professor_id = int(input("ID do professor: "))
    endereco_id = int(input("ID do endereço: "))
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = int(input("CPF: "))

    cursor.execute("""
        INSERT INTO Professores (professor_id, endereco_id, professor_nome, professor_idade, professor_cpf)
        VALUES (:1, :2, :3, :4, :5)
    """, (professor_id, endereco_id, nome, idade, cpf))
    conn.commit()
    print("Professor inserido com sucesso.\n")

def alterar_professor(conn):
    cursor = conn.cursor()
    professor_id = int(input("ID do professor a alterar: "))
    novo_nome = input("Novo nome: ")
    cursor.execute("""
        UPDATE Professores SET professor_nome = :1 WHERE professor_id = :2
    """, (novo_nome, professor_id))
    conn.commit()
    print("Professor alterado com sucesso.\n")

def excluir_professor(conn):
    cursor = conn.cursor()
    professor_id = int(input("ID do professor a excluir: "))
    cursor.execute("DELETE FROM Professores WHERE professor_id = :1", (professor_id,))
    conn.commit()
    print("Professor excluído com sucesso.\n")

def listar_professores(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.professor_id, p.professor_nome, e.endereco_cidade, p.professor_idade
        FROM Professores p
        JOIN Enderecos e ON p.endereco_id = e.endereco_id
    """)
    print("\n=== LISTA DE PROFESSORES ===")
    for row in cursor:
        print(row)
    print()

# RELATÓRIOS

def relatorios(conn):
    cursor = conn.cursor()
    print("\n===== RELATÓRIOS =====")
    print("1 - Funcionários")
    print("2 - Professores")
    print("0 - Voltar")
    opc = input("Escolha: ")

     # RELATÓRIOS FUNCIONÁRIOS

    if opc == '1':
        print("\n1 - Funcionários por cargo")
        print("2 - Desenvolvedores Front End (salário entre 8000 e 12000)")
        print("3 - Funcionários do departamento de TI (idade > 21)")
        escolha = input("Escolha: ")

        if escolha == '1':
            cargo_nome = input("Informe o nome do cargo: ")
            cursor.execute("""
                SELECT f.funcionario_nome, c.cargo_nome
                FROM Funcionarios f
                JOIN Cargos c ON f.cargo_id = c.cargo_id
                WHERE c.cargo_nome = :1
            """, (cargo_nome,))
        elif escolha == '2':
            cursor.execute("""
                SELECT f.funcionario_nome, f.funcionario_salario
                FROM Funcionarios f
                JOIN Cargos c ON f.cargo_id = c.cargo_id
                WHERE c.cargo_nome = 'Desenvolvedor Front End'
                  AND f.funcionario_salario BETWEEN 8000 AND 12000
            """)
        elif escolha == '3':
            cursor.execute("""
                SELECT f.funcionario_nome, f.funcionario_idade
                FROM Funcionarios f
                JOIN Cargos c ON f.cargo_id = c.cargo_id
                WHERE c.cargo_departamento = 'TI'
                  AND f.funcionario_idade > 21
            """)
        else:
            return

    # RELATÓRIOS PROFESSORES

    elif opc == '2':
        print("\n1 - Professores por endereço")
        print("2 - Professores com titulação Mestrado e cidade São Paulo")
        print("3 - Professores no Centro do RJ com idade entre 28 e 45")
        escolha = input("Escolha: ")

        if escolha == '1':
            bairro = input("Informe o bairro: ")
            cursor.execute("""
                SELECT p.professor_nome, e.endereco_bairro
                FROM Professores p
                JOIN Enderecos e ON p.endereco_id = e.endereco_id
                WHERE e.endereco_bairro = :1
            """, (bairro,))
        elif escolha == '2':
            cursor.execute("""
                SELECT p.professor_nome, e.endereco_cidade
                FROM Professores p
                JOIN Enderecos e ON p.endereco_id = e.endereco_id
                WHERE e.endereco_cidade = 'São Paulo'
                  AND p.professor_nome LIKE '%Mestrado%'
            """)
        elif escolha == '3':
            cursor.execute("""
                SELECT p.professor_nome, p.professor_idade
                FROM Professores p
                JOIN Enderecos e ON p.endereco_id = e.endereco_id
                WHERE e.endereco_cidade = 'Rio de Janeiro'
                  AND e.endereco_bairro = 'Centro'
                  AND p.professor_idade BETWEEN 28 AND 45
            """)
        else:
            return
    else:
        return

    print("\n=== RESULTADOS ===")
    for row in cursor:
        print(row)
    print()


# MENU PRINCIPAL

def main():
    conn = conectar()
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Funcionários")
        print("2 - Cargos")
        print("3 - Professores")
        print("4 - Endereços")
        print("5 - Relatórios")
        print("0 - Sair")
        opc = input("Escolha: ")

        if opc == '1':
            print("\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Listar\n0 - Voltar")
            op = input("Escolha: ")
            if op == '1': inserir_funcionario(conn)
            elif op == '2': alterar_funcionario(conn)
            elif op == '3': excluir_funcionario(conn)
            elif op == '4': listar_funcionarios(conn)

        elif opc == '2':
            print("\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Listar\n0 - Voltar")
            op = input("Escolha: ")
            if op == '1': inserir_cargo(conn)
            elif op == '2': alterar_cargo(conn)
            elif op == '3': excluir_cargo(conn)
            elif op == '4': listar_cargos(conn)

        elif opc == '3':
            print("\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Listar\n0 - Voltar")
            op = input("Escolha: ")
            if op == '1': inserir_professor(conn)
            elif op == '2': alterar_professor(conn)
            elif op == '3': excluir_professor(conn)
            elif op == '4': listar_professores(conn)

        elif opc == '4':
            print("\n1 - Inserir\n2 - Alterar\n3 - Excluir\n4 - Listar\n0 - Voltar")
            op = input("Escolha: ")
            if op == '1': inserir_endereco(conn)
            elif op == '2': alterar_endereco(conn)
            elif op == '3': excluir_endereco(conn)
            elif op == '4': listar_enderecos(conn)

        elif opc == '5':
            relatorios(conn)

        elif opc == '0':
            conn.close()
            print("Conexão encerrada.")
            break

if __name__ == "__main__":
    main()