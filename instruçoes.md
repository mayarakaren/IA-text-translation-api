# **README - Conectando a API Python com o Node.js**
---

## Integrando a API Python de Tradução com Node.js

Este README explica como integrar a API de Tradução Python (Flask) com um backend Node.js, para que a aplicação web ou mobile possa realizar traduções entre os idiomas Português e Inglês.

## Passos para Conectar o Backend Node.js com a API Python

### 1. Configurar a API Python (Flask)

Siga os passos no [README da API Python](./README-python-api.md) para configurar e rodar a API Python localmente. Certifique-se de que a API esteja rodando em `http://localhost:5000` ou em qualquer outro endereço configurado.

### 2. Configurar o Backend Node.js

No seu backend Node.js, você irá criar um serviço para se comunicar com a API Flask. Isso pode ser feito usando a biblioteca `axios` ou o módulo `node-fetch` para realizar as requisições HTTP.

#### Exemplo com `axios`

1. **Instalar `axios`**:

   No diretório do seu projeto Node.js, execute:

   ```bash
   npm install axios
   ```

2. **Criar um serviço de tradução**:

   No seu backend, crie um arquivo, por exemplo, `translationService.js`, para fazer a comunicação com a API Python.

   ```javascript
   // translationService.js

   const axios = require('axios');

   async function translateText(text, srcLang = "pt", targetLang = "en") {
       try {
           const response = await axios.post('http://localhost:5000/translate', {
               text: text,
               src_lang: srcLang,
               target_lang: targetLang
           });

           return response.data; // Retorna o JSON com texto original, pré-processado e traduzido
       } catch (error) {
           console.error('Erro na tradução:', error);
           throw error;
       }
   }

   module.exports = {
       translateText
   };
   ```

3. **Utilizar o serviço de tradução no seu controlador ou rota**:

   Agora, você pode importar e usar o `translateText` em qualquer parte do seu código Node.js para obter a tradução.

   ```javascript
   // app.js (ou onde você precisar usar a tradução)

   const express = require('express');
   const { translateText } = require('./translationService');
   const app = express();

   app.use(express.json());

   app.post('/api/translate', async (req, res) => {
       const { text, src_lang, target_lang } = req.body;

       try {
           const translation = await translateText(text, src_lang, target_lang);
           res.json(translation);  // Retorna o resultado da tradução
       } catch (error) {
           res.status(500).json({ error: 'Erro ao realizar a tradução' });
       }
   });

   app.listen(3000, () => {
       console.log('Backend rodando em http://localhost:3000');
   });
   ```

4. **Testar a integração**:

   Agora, ao enviar uma requisição para o seu backend Node.js (`POST /api/translate`), a API Node.js fará uma requisição para a API Python Flask, obterá a tradução e retornará ao cliente.

#### Exemplo de Requisição para o Backend Node.js

```json
{
  "text": "Olá, como você está?",
  "src_lang": "pt",
  "target_lang": "en"
}
```

#### Exemplo de Resposta do Backend Node.js

```json
{
  "original_text": "Olá, como você está?",
  "preprocessed_text": "olá como você estar",
  "translated_text": "Hello, how are you?"
}
```

### 3. Executar o Projeto

1. Certifique-se de que a API Python está em execução.
2. Inicie o servidor Node.js:

   ```bash
   node app.js
   ```

Agora sua aplicação Node.js está configurada para se comunicar com a API de tradução Python. As traduções podem ser feitas chamando o endpoint `/api/translate` do seu backend Node.js.

---
