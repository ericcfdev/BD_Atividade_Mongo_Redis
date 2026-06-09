# Conexão Python com NoSQL — MongoDB e Redis

Atividade prática da disciplina de Banco de Dados, desenvolvida em Python utilizando MongoDB Atlas e Redis Cloud. O script realiza operações de CRUD no MongoDB e demonstra o uso de cache com Redis.

---

## Tecnologias Utilizadas

* Python 3.13
* `pymongo` — Driver oficial do MongoDB para Python
* `redis-py` — Cliente Redis para Python

---

## Instalação das Dependências

```bash
pip install pymongo redis
```

---

## Configuração

Abra o arquivo `AtividadeBDMongoRedis - Eric CF.py` e substitua as variáveis pelas suas credenciais:

```python
MONGO_URI = "mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net/?appName=<app>"
REDIS_HOST = "<host>"
REDIS_PORT = <porta>
REDIS_PASS = "<senha>"
```

### MongoDB Atlas

1. Crie uma conta no MongoDB Atlas.
2. Crie um cluster utilizando o plano gratuito (M0).
3. Em **Database Access**, crie um usuário com senha.
4. Em **Network Access**, adicione `0.0.0.0/0` para permitir conexões externas.
5. Copie a URI de conexão em **Connect > Drivers**.

### Redis Cloud

1. Crie uma conta no Redis Cloud.
2. Crie uma instância utilizando o plano gratuito.
3. Copie os dados de **Host**, **Port** e **Password** fornecidos pela plataforma.

---

## Execução

```bash
python "AtividadeBDMongoRedis - Eric CF.py"
```

---

## Funcionalidades

O sistema apresenta um menu interativo com as seguintes opções:

| Opção | Funcionalidade                                                      |
| ----- | ------------------------------------------------------------------- |
| 1     | Inserir três produtos no MongoDB (Mouse, Teclado e Monitor)         |
| 2     | Consultar produtos com preço acima de um valor informado            |
| 3     | Atualizar o preço de um produto pelo nome                           |
| 4     | Remover todos os produtos de uma categoria                          |
| 5     | Salvar mensagem de boas-vindas no Redis (`mensagem:inicio`)         |
| 6     | Salvar dados de usuário em uma estrutura Hash (`usuario:1`)         |
| 7     | Registrar e exibir logs de acesso com data e hora                   |
| 8     | Buscar produto por nome utilizando cache Redis (TTL de 60 segundos) |
| 0     | Encerrar o programa                                                 |

---

## Estrutura do Projeto

```text
.
├── AtividadeBDMongoRedis - Eric CF.py
└── README.md
```

---

## Banco de Dados MongoDB

### Banco Utilizado

```text
desafio_nosql
```

### Coleção Utilizada

```text
produtos
```

### Estrutura de Documento

```json
{
  "nome": "Mouse",
  "categoria": "Periféricos",
  "preco": 89.90
}
```

---

## Utilização do Redis

### Mensagem Simples

Armazenamento de uma mensagem de boas-vindas utilizando chave e valor:

```text
mensagem:inicio
```

### Hash de Usuário

Armazenamento de dados estruturados:

```text
usuario:1
```

### Logs de Acesso

Registro de eventos contendo data e hora da execução.

### Cache de Produtos

Os produtos consultados são armazenados temporariamente no Redis utilizando o padrão:

```text
produto:{nome}
```

Tempo de expiração (TTL):

```text
60 segundos
```

---

## Tratamento de Erros

O sistema realiza tratamento de exceções para:

* Falhas de conexão com MongoDB
* Falhas de autenticação no MongoDB
* Falhas de conexão com Redis
* Erros durante operações de leitura e escrita

Utilizando estruturas:

```python
try:
    # operação
except Exception as erro:
    print(erro)
```

---

## Autor

**Éric CF**

Atividade desenvolvida para a disciplina de Banco de Dados utilizando MongoDB Atlas e Redis Cloud como bancos de dados NoSQL.
