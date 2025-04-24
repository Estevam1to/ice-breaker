# LangChain Course - LinkedIn Agent Project

Este projeto implementa um agente reativo para busca e análise de perfis no LinkedIn utilizando o LangChain e a API da Anthropic. A aplicação realiza as seguintes etapas:

1. Recebe um nome completo e utiliza o [LinkedinLookupAgent](src/agents/linkedin_lookup_agent.py) para buscar a URL do perfil do LinkedIn através do [TavilyClient](src/tools/search_tool.py).
2. Raspa os dados do perfil usando a função [scrape_linkedin_profile](src/utils/likedin.py), que consome a API do ProxyCurl.
3. Gera um resumo sobre o perfil com o modelo `ChatAnthropic`, destacando a personalidade e fatos interessantes da pessoa.

## Tecnologias Utilizadas

- **LangChain**
- **Anthropic API**
- **Tavily API**
- **ProxyCurl API**
- **Pydantic Settings**

## Configuração

1. Defina as variáveis de ambiente necessárias no arquivo [.env](.env).
2. Instale as dependências listadas em [requirements.txt](requirements.txt).

## Execução

Para executar o script principal, use o seguinte comando:

```sh
python3 main.py
```


## Estrutura do Projeto

- `src/`: Contém o código fonte do projeto.
  - `agents/`: Contém o agente responsável por localizar o perfil do LinkedIn (`LinkedinLookupAgent`).
  - `config/`: Contém as configurações do projeto, incluindo variáveis de ambiente e logs.
  - `tools/`: Ferramentas auxiliares, como a busca da URL do perfil através do `TavilyClient`.
  - `utils/`: Utilitários do projeto, incluindo a função de raspagem do perfil (`scrape_linkedin_profile`).
- `main.py`: Script principal que orquestra a execução dos agentes e ferramentas.

## Considerações Finais

Este projeto exemplifica o uso de diversas tecnologias modernas para a criação de agentes inteligentes e a integração de múltiplas APIs. Sinta-se à vontade para explorar, modificar e aprimorar as funcionalidades conforme necessário.
