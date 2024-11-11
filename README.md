# Text Translation API - Python

Esta API realiza a tradução de textos entre Português e Inglês utilizando o Google Translate API, com pré-processamento de texto usando NLTK e SpaCy. O pré-processamento inclui tokenização, remoção de stopwords, lematização e radicalização.

## Estrutura do Projeto

- `translation_service.py`: Contém a lógica de pré-processamento e tradução.
- `api.py`: API Flask que expõe os serviços de tradução.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `README.md`: Documentação do projeto.

## Funcionalidades

1. **Tradução de Texto**: Traduz textos entre Português e Inglês utilizando a API do Google Translate.
2. **Pré-processamento**: 
   - Tokenização
   - Remoção de Stopwords
   - Lematização e Radicalização

## Como Executar

### 1. Instalar as Dependências

Primeiro, instale as dependências necessárias usando o `pip`:

```bash
pip install -r requirements.txt
