from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Arquivos onde as informações são salvas
DADOS_FILE = "dados.json"
USUARIOS_FILE = "usuarios.json"

# ===================== Funções de Aulas =====================

# Carrega a lista de aulas do arquivo JSON
def carregar_aulas():
    try:
        with open(DADOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Se não existir, retorna lista vazia

# Salva lista de aulas no JSON
def salvar_aulas(aulas):
    with open(DADOS_FILE, "w", encoding="utf-8") as f:
        json.dump(aulas, f, indent=4, ensure_ascii=False)

# ===================== Funções de Usuários =====================

# Carrega usuários cadastrados
def carregar_usuarios():
    try:
        with open(USUARIOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Se não existir, retorna vazio

# Salva usuários no JSON
def salvar_usuarios(usuarios):
    with open(USUARIOS_FILE, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# ===================== Rotas =====================

# Redireciona raiz para a tela de login
@app.route("/")
def raiz():
    return redirect("/login")

# --------- Cadastro ---------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    erro = None  # mensagem de erro para exibir no HTML

    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        usuarios = carregar_usuarios()

        # Verifica se usuário já existe
        if any(u["usuario"] == usuario for u in usuarios):
            erro = "Usuário já existe!"
            return render_template("cadastro.html", erro=erro)

        # Salva novo usuário
        usuarios.append({
            "usuario": usuario,
            "senha": senha
        })
        salvar_usuarios(usuarios)
        return redirect("/login")

    return render_template("cadastro.html", erro=erro)

# --------- Login ---------
@app.route("/login", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None  # Mensagem para mostrar na tela

    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        usuarios = carregar_usuarios()

        # Verifica credenciais
        for u in usuarios:
            if u["usuario"] == usuario and u["senha"] == senha:
                return redirect("/index")  # Login aprovado

        # Se não encontrou usuário válido
        erro = "Usuário ou senha incorretos!"

    return render_template("login.html", erro=erro)

# --------- Página principal ---------
@app.route("/index")
def index():
    aulas = carregar_aulas()
    aulas.sort(key=lambda x: x["data"])  # Ordena por data
    return render_template("index.html", aulas=aulas)

# --------- Criar nova aula ---------
@app.route("/novo", methods=["GET", "POST"])
def novo():
    aulas = carregar_aulas()

    if request.method == "POST":
        titulo = request.form.get("titulo")
        instrutor = request.form.get("instrutor")
        data = request.form.get("data")
        sala = request.form.get("sala")
        horario = request.form.get("horario")
        descricao = request.form.get("descricao")

        # Gera ID automático
        novo_id = max([d["id"] for d in aulas] or [0]) + 1

        nova_aula = {
            "id": novo_id,
            "titulo": titulo,
            "instrutor": instrutor,
            "data": data,
            "sala": sala,
            "horario": horario,
            "descricao": descricao
        }

        aulas.append(nova_aula)
        salvar_aulas(aulas)
        return redirect("/index")

    return render_template("nova_aula.html")

# --------- Excluir aula ---------
@app.route("/excluir", methods=["POST"])
def excluir():
    aulas = carregar_aulas()
    titulo = request.form.get("titulo")

    if not titulo:
        return redirect("/index")

    # Remove a aula pelo título
    aulas = [a for a in aulas if a.get("titulo") != titulo]

    salvar_aulas(aulas)
    return redirect("/index")

# --------- Editar aula ---------
@app.route("/editar", methods=["POST"])
def editar():
    aulas = carregar_aulas()

    titulo_original = request.form.get("titulo_original")
    novo_titulo = request.form.get("titulo")
    instrutor = request.form.get("instrutor")
    data = request.form.get("data")
    horario = request.form.get("horario")
    descricao = request.form.get("descricao")

    # Busca a aula original e atualiza os dados
    for aula in aulas:
        if aula["titulo"] == titulo_original:
            aula["titulo"] = novo_titulo
            aula["instrutor"] = instrutor
            aula["data"] = data
            aula["sala"] = request.form.get("sala")
            aula["horario"] = horario
            aula["descricao"] = descricao
            break

    salvar_aulas(aulas)
    return redirect("/index")

# --------- Página Criadores ---------
@app.route("/criadores")
def criadores():
    return render_template("criadores.html")

# ===================== Execução =====================
if __name__ == "__main__":
    app.run(debug=True)
