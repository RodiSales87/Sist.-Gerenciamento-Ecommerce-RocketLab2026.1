# Como Executar o Projeto

Para rodar a aplicação, você precisará abrir dois terminais: um para o backend e outro para o frontend.

## 1. Backend

No primeiro terminal, navegue até a pasta do backend, ative o ambiente virtual e inicie o servidor:

```bash
# Entre na pasta do backend
cd back

# Ative o ambiente virtual (Linux/macOS)
source venv/bin/activate
# Se estiver no Windows, use: .\venv\Scripts\activate

# Rode o servidor (ajuste o comando conforme o seu arquivo principal, ex: uvicorn main:app --reload)
python main.py

# Entre na pasta do frontend
cd front

# Inicie o servidor
pnpm dev
