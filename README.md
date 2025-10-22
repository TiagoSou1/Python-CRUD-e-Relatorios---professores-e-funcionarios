# Python CRUD e Relatorios - professores e funcionarios (oracle)


[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)  [![Oracle](https://img.shields.io/badge/Oracle-Database-orange?logo=oracle)](https://www.oracle.com/database/)  [![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)

Sistema em **Python** para gerenciamento de **Funcionários, Cargos, Professores e Endereços** utilizando banco de dados **Oracle**. Permite CRUD completo e geração de relatórios.

---

##  Funcionalidades

- **CRUD Cargos**: Inserir, alterar, excluir e listar cargos.  
- **CRUD Funcionários**: Inserir, alterar, excluir e listar funcionários.  
- **CRUD Endereços**: Inserir, alterar, excluir e listar endereços.  
- **CRUD Professores**: Inserir, alterar, excluir e listar professores.  
- **Relatórios**:  
  - Funcionários por cargo  
  - Funcionários de TI com idade > 21  
  - Desenvolvedores Front End com salário entre 8000 e 12000  
  - Professores por bairro ou cidade  
  - Professores com titulação específica e faixa etária  

---

##  Tecnologias

- Python 3.x  
- [oracledb](https://pypi.org/project/oracledb/)  
- Oracle Database XE

---

##  Pré-requisitos

- Oracle Database XE instalado  
- Python 3.x  
- Biblioteca oracledb:

```bash
pip install -r requirements.txt
``` 

## Criar as tabelas no Oracle:

- rode o arquivo SQL no ORACLE SQL DEVELOPER
  
---

## Rodando

- Clone o repositório:
  
```bash
git clone <URL_DO_REPOSITORIO>
cd nome-do-repositorio
```

- Configure as credenciais no main.py:
  
```python
USERNAME = "seu_usuario"
PASSWORD = "sua_senha"
DSN = "localhost/XE"
```
- Execute o sistema:
  
```bash
python main.py
```
--- 

## Por fim navegue pelo menu interativo para gerenciar dados e gerar relatórios.

---

## Licença

Este projeto está licenciado sob a Apache License 2.0. 
