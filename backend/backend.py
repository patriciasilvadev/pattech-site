from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import google.generativeai as genai

# Configurar a chave da API do Google
os.environ["GOOGLE_API_KEY"] = "SUA_CHAVE_AQUI"

# Inicializar modelo Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
modelo = genai.GenerativeModel("gemini-2.0-pro")

# Criar aplicação Flask
app = Flask(__name__)
CORS(app)

# Rota para página inicial (para evitar erro 404)
app = Flask(__name__, template_folder="../frontend")
@app.route("/")
def home():
    return render_template("index.html")  # Agora busca na pasta correta

# Rota para receber perguntas e gerar respostas
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    pergunta_usuario = data.get("pergunta", "")

    try:
        # Instruções do agente
        instrucoes_do_agente = """
        Você é o PatTech, um assistente amigável que ajuda pessoas com dificuldades em tecnologia.
        Suas respostas devem ser claras, simples e explicadas passo a passo.
        """

        # Criar prompt para enviar à IA
        prompt_completo = f"{instrucoes_do_agente}\n\nPergunta do usuário: {pergunta_usuario}"
        
        # Gerar resposta usando Google Generative AI
        resposta = modelo.generate_content(prompt_completo)
        resposta_final = resposta.text if resposta and resposta.text else "Não consegui gerar uma resposta. Tente novamente!"

        return jsonify({"resposta": resposta_final})

    except Exception as e:
        return jsonify({"erro": str(e)})

# Rodar o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
