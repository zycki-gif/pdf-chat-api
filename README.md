# Projeto de RAG com Python, OpenAI API e Streamlit
### Descrição do Projeto
Este projeto implementa uma aplicação web usando Streamlit, Python e a API da OpenAI para criar um chatbot que usa a tecnologia RAG (Recuperação Automatizada de Respostas). O chatbot permite que os usuários façam upload de um arquivo PDF e façam perguntas sobre o conteúdo do arquivo. Em seguida, o chatbot consulta a API da OpenAI, que utiliza o modelo GPT (Generative Pre-trained Transformer) para fornecer respostas relevantes às perguntas.

### Pré-requisitos
Certifique-se de ter Python instalado na sua máquina. Você também precisará de uma chave de API da OpenAI para acessar a API GPT. Além disso, instale as dependências listadas no arquivo requirements.txt.

### Configuração
1. Clone este repositório para o seu ambiente local:
```bash
git clone https://github.com/zycki-gif/pdf-chat-api.git
```
2. Navegue até o diretório do projeto:
```bash
cd pdf-chat-api
```
3. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

4. Configure sua chave de API da OpenAI:
Crie um arquivo chamado .env no diretório raiz do projeto.
Dentro do arquivo .env, adicione sua chave de API da OpenAI da seguinte maneira:
```makefile
OPENAI_API_KEY=sua-chave-de-api-aqui
```

### Execução
1. Inicie a aplicação Streamlit:
```bash
streamlit run app.py
```
2. Abra o navegador e acesse o endereço fornecido pelo Streamlit.
### Uso
Faça upload de um arquivo PDF.
Digite uma pergunta sobre o conteúdo do arquivo no campo de texto.
Aguarde enquanto o chatbot processa a pergunta e retorna uma resposta relevante.

### Contribuição

- Alan Sprea
