# Projeto encurta_url

## Descrição

O projeto **encurta_url** é uma API desenvolvida com Django que permite encurtar URLs. Ele gera URLs encurtadas com identificadores de 5 a 10 dígitos alfanuméricos e possui a funcionalidade de expirar e apagar os links do banco de dados após um tempo determinado.

## Funcionalidades

- **Encurtar URL**: Gera uma URL encurtada a partir de um link fornecido.
- **Expiração de Links**: Os links encurtados expiram após um período pré-definido.
- **Remoção de Links Expirados**: Links expirados são automaticamente removidos do banco de dados.

## Requisitos

- Python 3.x ou superior
- Django 3.x ou superior
- Banco de dados suportado pelo Django (SQLite, PostgreSQL, MySQL, etc.)

## Endpoints da API

- todos os endpoints estão dentro da propria rota **/Swagger** do app

## Configuração do Projeto

### 1. Clone o repositório

   ```bash
   git clone https://github.com/amorajoaovictor/encurta_url.git
   ```

### 2. crie uma maqina virtual para executar o projeto

   ```python
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\Activate.ps1`
   ```

### 3. Instale os requisitos do projeto

   ```python
   pip install -r requirements.txt
   ```

### 3. faça as migrações

   ```python
   python manage.py makemigrations

   python manage.py migrate
   ```

### 4. Inicie o servidor

  ```python
 cd encurta_url

 python manage.py runserver
  ```
