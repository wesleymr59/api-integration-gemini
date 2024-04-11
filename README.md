
# Api Integration Ia Gemini

Api de integração com a inteligencia artificial Gemini, usando arquitetura hexagonal.

# Estrutura da Aplicação

Este projeto segue uma arquitetura limpa (Clean Architecture), também conhecida como arquitetura hexagonal. A seguir, é apresentada a estrutura de pastas e sua finalidade:

## Pastas

### adapters

Contém os adaptadores responsáveis por fazer requisições para uma API externa.

### application

Esta pasta contém a camada de aplicação da nossa arquitetura. Ela é subdividida da seguinte forma:

- **composers**: Responsável por montar a inversão de dependência e configurar a aplicação.
- **interfaces**: Define a interface para o repositório, que é implementada pelos adaptadores na camada de infraestrutura.
- **routers**: Cria as rotas do FastAPI e injeta as dependências dos casos de uso, incluindo o repositório.

### usecases

Contém os casos de uso da aplicação, que representam a regra de negócio.

### domain

Esta pasta contém os conceitos fundamentais do domínio da nossa aplicação. Ela é subdividida da seguinte forma:

- **dto**: Define os schemas de resposta das rotas.
- **entities**: Define as entidades do banco de dados.

## Instalação

build image docker

```bash
docker image build -t ia-gemini-api:latest .
```

Execute container
```bash
docker container run --rm -it -v $(pwd):/usr/src --env-file .env -p 8090:8090 --name ia-gemini-api ia-gemini-api:latest
```
## Licença

[MIT](https://choosealicense.com/licenses/mit/)

