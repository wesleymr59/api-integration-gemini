
# Api Integration Ia Gemini

Api de integração com a inteligencia artificial Gemini, usando arquitetura hexagonal.


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

