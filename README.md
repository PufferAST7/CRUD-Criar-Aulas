📌Sistema Web de Gerenciamento de Aulas

🧠 Sobre o projeto

Este projeto consiste em um sistema web completo desenvolvido com Flask, que permite o gerenciamento de aulas com funcionalidades de cadastro, edição e exclusão, além de um sistema de autenticação de usuários.

A aplicação simula um ambiente real de organização de aulas, com persistência de dados em arquivos JSON.

🔐 Sistema de Autenticação

👤 Cadastro de usuários<br>
🔑 Login com validação de credenciais<br>
⚠️ Mensagens de erro para login inválido<br>
🚫 Prevenção de usuários duplicados

📚 Gerenciamento de Aulas (CRUD)

➕ Criar novas aulas<br>
📋 Listar aulas cadastradas<br>
✏️ Editar informações das aulas<br>
❌ Excluir aulas<br>
🆔 ID automático para cada aula<br>
📅 Ordenação por data

🖥️ Páginas do sistema

/login → Tela de login<br>
/cadastro → Cadastro de usuário<br>
/index → Página principal com lista de aulas<br>
/novo → Cadastro de nova aula<br>
/criadores → Página informativa

🧱 Tecnologias utilizadas

Python 🐍<br>
Flask 🌐<br>
HTML (templates)<br>
CSS<br>
JSON (armazenamento de dados)

⚙️ Funcionamento

O sistema utiliza arquivos JSON para armazenar dados:

usuarios.json → guarda usuários cadastrados
dados.json → guarda as aulas

As operações são feitas através de rotas Flask:

GET → exibição de páginas
POST → envio e processamento de dados

🔄 Funcionalidades internas

Leitura e escrita de arquivos JSON<br>
Geração automática de IDs<br>
Validação de login<br>
Manipulação de listas e dicionários<br>
Uso de templates com render_template<br>
Redirecionamento com redirect()

Objetivo

Este projeto foi desenvolvido com foco em aprender desenvolvimento web com Flask, incluindo autenticação, manipulação de dados e criação de rotas.
