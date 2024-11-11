# translation_service.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer, WordNetLemmatizer
import spacy
import os
from google.cloud import translate_v2 as translate

# Baixar pacotes do NLTK necessários
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Carregar modelos SpaCy para português e inglês
nlp_pt = spacy.load("pt_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

# Inicializa o cliente do Google Translate usando o arquivo de credenciais do serviço
def get_translate_client():
    """
    Cria e retorna um cliente autenticado para a API Google Translate.

    Certifique-se de que a variável de ambiente 'GOOGLE_APPLICATION_CREDENTIALS'
    aponta para o caminho do arquivo JSON com as credenciais de serviço.
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/service-account-file.json"
    return translate.Client()

# Função para tradução de texto com Google Translate API
def translate_text(text, src_lang="pt", target_lang="en"):
    """
    Traduz o texto usando a API Google Cloud Translate.
    
    :param text: Texto para tradução.
    :param src_lang: Idioma de origem ("pt" ou "en").
    :param target_lang: Idioma de destino ("pt" ou "en").
    :return: Texto traduzido.
    """
    client = get_translate_client()  # Obtém o cliente autenticado
    translation = client.translate(
        text,
        source_language=src_lang,
        target_language=target_lang
    )
    return translation['translatedText']

# Função para pré-processar o texto
def preprocess_text(text, lang="pt"):
    """
    Tokeniza, remove stopwords, lematiza e aplica radicalização ao texto.
    
    :param text: Texto para pré-processamento.
    :param lang: Idioma do texto ("pt" para português, "en" para inglês).
    :return: Lista de tokens pré-processados.
    """
    # Tokenização
    tokens = word_tokenize(text)

    # Remoção de Stopwords
    stop_words = set(stopwords.words('portuguese' if lang == "pt" else 'english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]

    # Lematização e Radicalização
    if lang == "pt":
        # Lematização com SpaCy para português
        doc = nlp_pt(" ".join(tokens))
        tokens = [token.lemma_ for token in doc]
        
        # Radicalização com NLTK
        stemmer = RSLPStemmer()
        tokens = [stemmer.stem(word) for word in tokens]
    else:
        # Lematização com NLTK para inglês
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens
