# api.py
from flask import Flask, request, jsonify
from translation_service import preprocess_text, translate_text

# Inicializar o aplicativo Flask
app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_route():
    """
    Rota de tradução que recebe um texto JSON com os parâmetros:
      - text: Texto para tradução
      - src_lang: Idioma de origem
      - target_lang: Idioma de destino
    
    Retorna o texto original, texto pré-processado e texto traduzido.
    """
    data = request.json  # Recebe os dados JSON do cliente

    # Parâmetros de entrada
    text = data.get("text")
    src_lang = data.get("src_lang", "pt")
    target_lang = data.get("target_lang", "en")

    # Verificar se o texto foi fornecido
    if not text:
        return jsonify({"error": "Nenhum texto fornecido"}), 400

    # Pré-processamento
    preprocessed_text = preprocess_text(text, src_lang)

    # Tradução
    translated_text = translate_text(" ".join(preprocessed_text), src_lang, target_lang)

    # Construir a resposta
    result = {
        "original_text": text,
        "preprocessed_text": " ".join(preprocessed_text),
        "translated_text": translated_text
    }

    return jsonify(result)

# Executar o aplicativo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
