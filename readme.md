<h1 align="center"> 
  Microsserviço para Relatório Geral do Sistema
</h1>

Esta API, que permite o visualização de dados gerais sobre o sistema (ex: total de chamados, usuários por cargos, etc.), foi desenvolvida visando sua utilização no projeto "Help Duck" (mais informações vide [este link](https://github.com/The-Bugger-Ducks/help-duck-documentation)).

> Aplicação desenvolvida por alunos do 3º semestre do tecnólogo em Desenvolvimento de Software Multiplataforma, na FATEC Profº Jessen Vidal - São José dos Campos, SP :rocket:

### :hammer_and_wrench: Tecnologias

As seguintes tecnologias e ferramentas foram utilizadas neste projeto: `Python, Flask, MongoDB, Docker,Insomnia, Heroku`

---

## :railway_track: Rotas disponíveis
  
O servidor inciará localmente na porta 5000. Use o Insomnia para simular requisições e respostas das rotas (pelo link [https://localhost:5000](https://localhost:5000)) ou utilize o projeto front-end do "Help Duck" para executar as funcionalidades da aplicação (acesse o repositório por [este link](https://github.com/The-Bugger-Ducks/help-duck-web)).

<div align="center">

|                                                                    Tipo | Rota                                 | Ação                            |
| ----------------------------------------------------------------------: | :----------------------------------- | :------------------------------ |
|    [![](https://img.shields.io/badge/GET-2E8B57?style=for-the-badge)]() | `/dashboard/report`                  | Visualização do relatório       |

</div>

</div>

### Explicação da estrutura das pastas

| Pasta                                                     | Definição                                                                        |
| --------------------------------------------------------- | -------------------------------------------------------------------------------- |
| :open_file_folder: src/                                   | Arquivos com o código fonte do projeto                                           |
| :open_file_folder: src/controller                         | Arquivos para metodos de cada endpoint da API                                    |
| :open_file_folder: src/models                             | Arquivos para execução de calculos ou processos para o controller                |
| :open_file_folder: src/models/tickets                     | Arquivos para execução de calculos ou processos que tenha como centro os chamados|
| :open_file_folder: src/models/tickets                     | Arquivos para execução de calculos ou processos que tenha como centro os usuários|
| :open_file_folder: src/routes                             | Arquivos gerenciadores de rotas para os endpoints da aplicação                   |
| :page_facing_up: connectDb.py                             | Arquivo para conexão com o banco de dados MongoDB                                |
| :page_facing_up: connectRedis.py                          | Arquivo para conexão com o banco de dados Redis                                  |
| :page_facing_up: app.py                                   | Arquivo principal do projeto                                                     |
| :page_facing_up: Procfile                                 | Arquivo usado para indicar para o Heroku cofigurações de inicialização do server |
| :page_facing_up: requirements.txt                         | Arquivo usado gerenciar as dependencias do projeto                               |


### Requisitos mínimos

1. _Python_
2. _MongoDB_

<br/>
<br/>

---

## Instalação e configuração do ambiente virtual

**Verifique se o pip está instalado**

```bash
python -m pip --version
```

_Siga a documentação oficial do pip caso você não tenha instalado:_

[Installation - pip documentation v21.1](https://pip.pypa.io/en/stable/installing/)

<br/>

**Instalando o virtualenv**

_Ferramenta para criar ambientes Python isolados._

```bash
python -m pip install virtualenv
```

**Clone o repositório do backend**

```bash
git clone https://github.com/ThHenrique/fa-connect-mongodb.git
```

**Abra o projeto no vsCode**

```bash
cd fa-connect-mongodb
code .
```

**Abra o terminal do VsCode e Configure o ambiente**

```bash
python -m venv venv
```

**Ative o ambiente**

No terminal Windows PowerShell

```powershell
venv\Scripts\activate
```

**OU**

Terminal Bash

```bash
. venv/bin/activate

# Linux: . venv/bin/activate
```

**Atualize a versão pip**

```bash
pip install -U pip
```

**Instalando as dependências do projeto**

```bash
pip install -r requirements.txt
```

**Setup Completo :)**

---

<br/>
<br/>

# Configuração do MongoDB 🍃

### Para realizar conexão com o MongoDB é necessário alterar o usuário e senha no arquivo connectDb em **src/connectDb.py**. Caso necessário, entre em contato comigo.



``` python
db = pymongo.MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
```

<br/>

---

# Utilizando o FLASK 🌶️

Com o ambiente ativado ...

```bash
python main.py
```

O servidor foi iniciado e pode ser acessado em [localhost](http://localhost:5000/).

A porta padrão do projeto é 5000.

---

## Instalação e configuração do Insomnia


Siga a documentação oficial do insomnia caso você não tenha instalado:_

[Installation - insomnia](https://insomnia.rest/download)

Caso você não conheça esse software veja o link a seguir para aprender:_

[Get Started - insomnia](https://docs.insomnia.rest/insomnia/send-your-first-request)

---

Para consumir esta API, é preciso seguir o passo a passo abaixo ou utilizar a URL do serviço em nuvem (através deste link, desde que de posse do token de autorização: https://help-duck-dashboard.herokuapp.com).

Caso tenha algum problema no processo, entre em contato.
