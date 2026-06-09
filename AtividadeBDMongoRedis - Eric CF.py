import pymongo
import redis
import json
import datetime

# Configurações
MONGO_URI = "mongodb+srv://manolotwdno_db_user:lffGnXvepEbFVSy3@atividademongobd.lkoft4b.mongodb.net/?appName=AtividadeMongoBD"
REDIS_HOST = "reaction-nut-boundary-31728.db.redis.io"
REDIS_PORT = 11319
REDIS_PASS = "wsaZVQz2bucGcp6PreFpY6kg4fu4mrBV"

# Conecta ao MongoDB
try:
    clienteMongo = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    clienteMongo.admin.command("ping")
    colecao = clienteMongo["desafio_nosql"]["produtos"]
    print("MongoDB conectado!")
except Exception as erro:
    print(f"Erro ao conectar ao MongoDB: {erro}")
    exit()

# Conecta ao Redis
try:
    clienteRedis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, decode_responses=True)
    clienteRedis.ping()
    print("Redis conectado!")
except Exception as erro:
    print(f"Erro ao conectar ao Redis: {erro}")
    exit()

# Operações MongoDB
def inserirProdutos():
    # Limpa a coleção e insere 3 produtos
    colecao.delete_many({})
    colecao.insert_many([
        {"nome": "Mouse",   "preco": 50.0,  "categoria": "Periferico"},
        {"nome": "Teclado", "preco": 150.0, "categoria": "Periferico"},
        {"nome": "Monitor", "preco": 900.0, "categoria": "Monitor"},
    ])
    print("Produtos inseridos.")

def consultarPorPreco():
    # Consulta produtos com preço acima do valor informado
    preco = float(input("Preço mínimo: R$"))
    for produto in colecao.find({"preco": {"$gt": preco}}, {"_id": 0}):
        print(produto)

def atualizarPreco():
    # Atualiza o preço de um produto pelo nome
    nome = input("Nome do produto: ")
    novoPreco = float(input("Novo preço: R$"))
    colecao.update_one({"nome": nome}, {"$set": {"preco": novoPreco}})
    print(f"Preço de '{nome}' atualizado para R${novoPreco}.")

def removerPorCategoria():
    # Remove todos os produtos de uma categoria
    categoria = input("Categoria: ")
    colecao.delete_many({"categoria": categoria})
    print(f"Produtos da categoria '{categoria}' removidos.")

# Operações Redis
def salvarBoasVindas():
    # Salva string de boas-vindas com chave mensagem:inicio
    clienteRedis.set("mensagem:inicio", "Bem-vindo ao sistema!")
    print("mensagem:inicio:", clienteRedis.get("mensagem:inicio"))

def salvarUsuario():
    # Salva dados do usuário em um hash
    clienteRedis.hset("usuario:1", mapping={"nome": "Eric", "email": "eric@email.com"})
    print("usuario:1:", clienteRedis.hgetall("usuario:1"))

def registrarLogs():
    # Salva logs de acesso com timestamp em uma lista e exibe todos
    clienteRedis.delete("logs:acesso")
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for acao in ["LOGIN", "CONSULTA", "LOGOUT"]:
        clienteRedis.rpush("logs:acesso", f"{agora} | {acao}")
    for entrada in clienteRedis.lrange("logs:acesso", 0, -1):
        print(entrada)

# Cache integrado
def buscarProdutoComCache():
    nomeProduto = input("Nome do produto: ")
    chaveCache = f"produto:{nomeProduto}"

    # Verifica se está no cache
    dadosCache = clienteRedis.get(chaveCache)
    if dadosCache:
        print("[CACHE] Veio do Redis.")
        print(json.loads(dadosCache))
        return

    # Busca no MongoDB e salva no cache
    print("[BANCO] Buscando no MongoDB...")
    dadosMongo = colecao.find_one({"nome": nomeProduto}, {"_id": 0})
    if dadosMongo:
        clienteRedis.setex(chaveCache, 60, json.dumps(dadosMongo))
        print("[CACHE] Salvo no Redis por 60 segundos.")
        print(dadosMongo)
    else:
        print("Produto não encontrado.")

# Menu

while True:
	print(
	"\nMENU\n"
	"1. Inserir 3 produtos no MongoDB (Mouse, Teclado, Monitor)\n"
	"2. Consultar produtos com preço acima de um valor\n"
	"3. Atualizar o preço de um produto pelo nome\n"
	"4. Remover todos os produtos de uma categoria\n"
	"5. Salvar mensagem de boas-vindas no Redis\n"
	"6. Salvar dados de usuário em hash no Redis\n"
	"7. Registrar e exibir logs de acesso no Redis\n"
	"8. Buscar produto por nome (com cache Redis)\n"
	"0. Sair")

	opcao = input("\nOpção: ")

	if opcao == "1":
		inserirProdutos()
	elif opcao == "2":
		consultarPorPreco()
	elif opcao == "3":
		atualizarPreco()
	elif opcao == "4":
		removerPorCategoria()
	elif opcao == "5":
		salvarBoasVindas()
	elif opcao == "6":
		salvarUsuario()
	elif opcao == "7":
		registrarLogs()
	elif opcao == "8":
		buscarProdutoComCache()
	elif opcao == "0":
		print("Encerrando...")
		break
	else:
		print("Opção inválida.")