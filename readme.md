<h1 align="center"> 
  Microsserviço para Relatório Geral do Sistema
</h1>

Esta API, que permite o visualização de dados gerais sobre o sistema (ex: total de chamados, usuários por cargos, etc.), foi desenvolvida visando sua utilização no projeto "Help Duck" (mais informações [neste link](https://github.com/The-Bugger-Ducks/help-duck-documentation)).

> Aplicação desenvolvida por alunos do 3º semestre do tecnólogo em Desenvolvimento de Software Multiplataforma, na FATEC Profº Jessen Vidal - São José dos Campos, SP :rocket:

### :hammer_and_wrench: Tecnologias

As seguintes tecnologias e ferramentas foram utilizadas neste projeto: `Python, Flask, MongoDB, Docker,Insomnia, Heroku`

## :railway_track: Rotas disponíveis
  
O servidor inciará localmente na porta 5000. Use o Insomnia para simular requisições e respostas das rotas (pelo link [https://localhost:5000](https://localhost:5000)) ou utilize o projeto front-end do "Help Duck" para executar as funcionalidades da aplicação (acesse o repositório por [este link](https://github.com/The-Bugger-Ducks/help-duck-web)).

<div align="center">

|                                                                    Tipo | Rota                                 | Ação                            |
| ----------------------------------------------------------------------: | :----------------------------------- | :------------------------------ |
|    [![](https://img.shields.io/badge/GET-2E8B57?style=for-the-badge)]() | `/dashboard/report`                  | Visualização do relatório       |

</div>

### :gear: Como utilizar
Para consumir esta API, é preciso seguir o passo a passo abaixo ou utilizar a URL do serviço em nuvem (através deste link, desde que de posse do token de autorização: [https://help-duck-dashboard.herokuapp.com](https://help-duck-dashboard.herokuapp.com)).

- Tutorial para rodar o projeto
Como pré-requisitos é preciso a instalação do Python (e do pip - caso não tenha instalado, segue a [documentação oficial](https://pip.pypa.io/en/stable/installing/)) e do MongoDB. Veja a seguir o passo a passo para instalação e configuração do ambiente virtual:

```bash
# verifique se o pip está instalado
python -m pip --version

# instale o virtualenv (ferramenta para criar ambientes Python isolados)
python -m pip install virtualenv

# clone o repositório
git clone https://github.com/The-Bugger-Ducks/help-duck-dashboard.git

# entre na pasta do projeto
cd help-duck-dashboard

# configure o ambiente
python -m venv venv
```

Para ativar o ambiente, pode-se usar o terminal Windows PowerShell ou o terminal do bash
<div align="center">
  
| PowerShell                  | Bash                      |
|:---------------------------:|:-------------------------:|
| ```venv\Scripts\activate``` | ```. venv/bin/activate``` |
</div>

Agora, instale as dependências do projeto digitando num terminal o seguinte comando: `pip install -r requirements.txt`. Finalmente, é necessário alterar o usuário e senha no arquivo localizado em **src/connectDb.py** para realizar a conecão com o MongoDB, substituindo o `<user>`e o `<password>`.

``` python
db = pymongo.MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
```
Após isso, com o ambiente já configurado e ativado, digite em um terminal `python main.py` e o servidor será iniciado, podendo ser acessado em [localhost](http://localhost:5000/).

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