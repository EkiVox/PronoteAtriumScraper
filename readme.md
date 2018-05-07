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

You need to give ID parameter.

exemple:

```bash
curl localhost:8000/fetch?id=XXXXXXXX
```

It will return:
-if it's alright, it will return 200 OK and a json like this:

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

-if there is an Error when server connect to PRONOTE (wrong username and password or servilce unavailable), it will return 503 SERVICE UNAVAILABLE and a json string:

```json
"PRONOTE unreachable"
```

-if the ID provided don't exist in the server or wasn't associated with PRONOTE using `/store` method of api, it will return 404 NOT FOUND and a json string:

```json
"Invalid ID or not associated with PRONOTE"
```

### `/store`, POST

You should give pw and id parameter and a JSON list like this:

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

-if it's alright, it will return 200 OK and a json:
```json
"Credits Saved"
```

-if there is an Error when reading the stream, it will  return 400 BAD REQUEST and a json string:

```json
"Stream unreadable"
```

-if you didn't provide a list or tuple, it will  return 400 BAD REQUEST and a json string:

```json
"Posted resource need to be a list or tuple"
```

-if you didn't provide 2 parameter list or tuple, it will  return 400 BAD REQUEST and a json string:

```json
"List need 2 parameters"
```

-if you didn't provide ID parameter, it will  return 400 BAD REQUEST and a json string:

```json
"Need ID parameter"
```

-if you didn't provide pw parameter, it will  return 400 BAD REQUEST and a json string:

```json
"Need PW parameter"
```
