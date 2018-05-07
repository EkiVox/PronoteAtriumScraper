# SmartCopyBookCase
allow to scrap/fetch the next day courses via pronote using atrium authentification for permit turn on led in case which is stocked copybook of these courses... and play music! 
All of this throught a smart copy book case

## Serveur

### Installation

Install the dependencies:

```bash
pip install gunicorn selenium falcon
```
### Launch:

symply:

```bash
sh start-server.py
```

## API use

### `/fetch`, GET

You need to give __ID parameter__.

exemple:

```bash
curl localhost:8000/fetch?id=XXXXXXXX
```

It will return:

-if it's __alright__, it will return __200 OK__ and a json like this:

```json
[
    [
        "MATHEMATIQUES",
        "MATHEMATIQUES",
        "ESPAGNOL LV2",
        "SCIENCES INGENIEUR"
    ],
    [
        "PARDONA A.",
        "PARDONA A.",
        "TARGEMINI F.",
        "COBELLARO R."
    ]
]
```

-if there is an __Error when server connect to PRONOTE__ (wrong username and password or servilce unavailable), it will return __503 SERVICE UNAVAILABLE__ and a json string:

```json
"PRONOTE unreachable"
```

-if the __ID provided doesn't exist__ in the server or wasn't associated with PRONOTE using `/store` method of api, it will return __404 NOT FOUND__ and a json string:

```json
"Invalid ID or not associated with PRONOTE"
```

### `/store`, POST

You should give __pw and id parameter__ and a __JSON list__ like this:

```json
[
  "USERNAME",
  "PASSWORD"
]
```

exemple:

```bash
curl -X POST -d '["USER","PASSWORD"]' "http://localhost:8000/store?id=JBHP0QVX&pw=ZXPJC3HA"

```

-if it's __alright__, it will return __200 OK__ and a json:
```json
"Credits Saved"
```

-if there is an __Error when reading the stream__, it will  return __400 BAD REQUEST__ and a json string:

```json
"Stream unreadable"
```

-if you __didn't provide a list or tuple__, it will  return __400 BAD REQUEST__ and a json string:

```json
"Posted resource need to be a list or tuple"
```

-if you didn't __provide a 2 parameter list or tuple__, it will  return __400 BAD REQUEST__ and a json string:

```json
"List need 2 parameters"
```

-if you __didn't provide ID parameter__, it will  return __400 BAD REQUEST__ and a json string:

```json
"Need ID parameter"
```

-if you __didn't provide pw parameter__, it will  return __400 BAD REQUEST__ and a json string:

```json
"Need PW parameter"
```
