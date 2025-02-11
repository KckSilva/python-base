Estudos de Python. Os materiais aqui, são do curso "Python Base", da Linux Tips. 

##### Criando ambiente virtual (venv)

# 1- Acesse o diretório onde está o seu arquivo .py pelo terminal:
cd /caminho/para/seu/diretorio
# 2- Crie o ambiente virtual dentro do diretório:
python -m venv venv
Isso criará uma pasta chamada venv dentro do diretório, onde serão armazenadas as dependências do seu projeto.
# 3- Ative o ambiente virtual:
No Windows (Git Bash, CMD ou PowerShell):
source venv/Scripts/activate
# 4- No macOS/Linux:
source venv/bin/activate
# 5- Verifique se o ambiente está ativo:
python -V

# Instale as dependências (se houver um requirements.txt):
pip install -r requirements.txt

   # Gerar automaticamente um requirements.txt (se já tiver pacotes instalados)
   Se você já tem pacotes instalados no seu sistema global e quer usá-los no ambiente virtual, gere um requirements.txt assim:

   pip freeze > requirements.txt
# Isso criará o arquivo com a lista de pacotes e suas versões. Depois, instale-os no ambiente virtual:
pip install -r requirements.txt

# Dica extra: Atualizar o pip
Para atualizar o pip, rode:

python -m pip install --upgrade pip

Isso garante que você tenha a versão mais recente do gerenciador de pacotes. 🚀

Se precisar de mais ajuda, me avise! 😊