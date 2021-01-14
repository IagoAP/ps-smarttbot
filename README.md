# Processo Seletivo da SmarttBot

## Como rodar o projeto

O projeto foi criado utilizando docker, e necessario apenas ter o docker instalado na maquina e utilizar o comando:

```ShellScript
docker-compose up --build
```

E necessario utilizar o comando com a avariavel --build, senao o container da api nao se mantem, ele e fechado.

## Base de dados

A base de dados foi estruturada de acordo com a tabela exigida:

| moeda | periodicidade | horario | open | low | high | close |
|-------|---------------|---------|------|-----|------|-------|

A tabela e preenchida com 3 servicos que o servidor executa, para calcular a maxima, minima, abertura e fechamento da moeda de acordo com os periodos de 1, 5 e 10 minutos.
Existem duas apenas linhas para o teste unitario escrito.

## API

A API e composta apenas de um post sem nenhuma rota especifica, apenas: '/'.

### [POST] /

O copor da requisicao e opcional e permite que o usuario possa filtrar os resultados.
Inicialmente o unico filtro implementado e o de moeda, sendao simples implementar outros filtros.

body:

```javascript
{
    "moeda": "Bitcoin"
}

```

Exemplo de resposta:

```javascript
[
    {
        "close": 0.0044188,
        "high": 0.00441881,
        "horario": "Thu, 14 Jan 2021 02:22:26 GMT",
        "low": 0.00442285,
        "moeda": "Bitcoin",
        "open": 0.00442788,
        "periodicidade": 1
    },
    {
        "close": 0.00442209,
        "high": 0.00442074,
        "horario": "Thu, 14 Jan 2021 02:23:26 GMT",
        "low": 0.00442208,
        "moeda": "Bitcoin",
        "open": 0.0044188,
        "periodicidade": 1
    },
    {
        "close": 0.00442209,
        "high": 0.0044368,
        "horario": "Thu, 14 Jan 2021 02:24:26 GMT",
        "low": 0.00443885,
        "moeda": "Bitcoin",
        "open": 0.00442209,
        "periodicidade": 1
    },
    {
        "close": 0.00442209,
        "high": 0.00442963,
        "horario": "Thu, 14 Jan 2021 02:25:26 GMT",
        "low": 0.00443834,
        "moeda": "Bitcoin",
        "open": 0.00442209,
        "periodicidade": 1
    },
    {
        "close": 0.00442209,
        "high": 0.00442973,
        "horario": "Thu, 14 Jan 2021 02:26:26 GMT",
        "low": 0.00443704,
        "moeda": "Bitcoin",
        "open": 0.00442209,
        "periodicidade": 1
    }
]

```

## Teste unitario

O teste unitario foi feito com o unittest do python, para roda-lo utilize o coando:

```ShellScript
python tests.py
```

Para ser possivel rodar o teste e necessario que a base de dados esteja rodando.
