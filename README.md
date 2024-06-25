# chat

Web Chat, almost same as ChatGPT UI.

<div align="center">
    <img align="center" src="./index.png">
</div>

## how-to

1. Run Docker Compose,

```bash
docker-compose up --build
```

## push to dockerhub

```
docker build -t mesoliticadev/chat:main .
docker push mesoliticadev/chat:main
```