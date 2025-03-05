# Chat Deep

Este é um aplicativo simples de chatbot utilizando a API do Groq com o modelo `deepseek-r1-distill-llama-70b`. O app é construído com Streamlit para uma interface interativa e carrega a chave da API a partir de um arquivo `.env`.

## Requisitos

Certifique-se de ter instalado os seguintes pacotes antes de rodar o projeto:

```bash
pip install streamlit langchain_groq python-dotenv
```

## Configuração

Crie um arquivo `.env` no diretório raiz do projeto e adicione sua chave de API do Groq:

```
GROQ_API_KEY=your_api_key_here
```

## Como executar

Para iniciar o chatbot, execute o seguinte comando no terminal:

```bash
streamlit run nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome real do arquivo Python contendo o código.

## Funcionamento

- O chatbot mantém um histórico de mensagens usando `st.session_state`.
- As mensagens são exibidas no formato de chat entre usuário e IA.
- O modelo `deepseek-r1-distill-llama-70b` é utilizado para gerar respostas com base nas interações do usuário.

## Personalização

Você pode modificar o modelo de IA alterando o parâmetro `model` ao instanciar `ChatGroq`. Além disso, ajustes na interface podem ser feitos com os componentes do Streamlit.

## Licença

Este projeto é disponibilizado sob a licença MIT. Sinta-se à vontade para modificar e compartilhar!

