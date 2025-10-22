-- Tabela de Cargos

CREATE TABLE Cargos (
    cargo_id INTEGER PRIMARY KEY,
    cargo_nome VARCHAR2(45),
    cargo_departamento VARCHAR2(30)
);

-- Tabela de Funcionários

CREATE TABLE Funcionarios (
    funcionario_id INTEGER PRIMARY KEY,
    cargo_id INTEGER,
    funcionario_cpf INTEGER,
    funcionario_nome VARCHAR2(50),
    funcionario_salario FLOAT,
    funcionario_idade INTEGER,
    CONSTRAINT funcionario_FKIndex1 FOREIGN KEY (cargo_id)
        REFERENCES Cargos(cargo_id)
);

-- Tabela de Endereços

CREATE TABLE Enderecos (
    endereco_id INTEGER PRIMARY KEY,
    endereco_logradouro VARCHAR2(70),
    endereco_bairro VARCHAR2(50),
    endereco_cidade VARCHAR2(50),
    endereco_estado VARCHAR2(2),
    endereco_CEP INTEGER
);


-- Tabela de Professores

CREATE TABLE Professores (
    professor_id INTEGER PRIMARY KEY,
    endereco_id INTEGER,
    professor_nome VARCHAR2(50),
    professor_idade INTEGER,
    professor_cpf INTEGER,
    CONSTRAINT professor_FKIndex1 FOREIGN KEY (endereco_id)
        REFERENCES Enderecos(endereco_id)
);