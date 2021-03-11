# DinoALasFakeNews-Backend
Back-end para las Fake News

---

## Links importantes

- [Trello](https://trello.com/b/gw72hzyx/dino-a-las-fake-news)
- [Tutorial Conectar Chatbot](https://medium.com/zenofai/creating-chatbot-using-python-flask-d6947d8ef805)

---

## Instrucciones para correr aplicación

### __Variables de ambiente__

Crear archivos `.env` y `.flaskenv`.

En el archivo de `.flaskenv` agrega las siguientes variables:
```
FLASK_APP=app.py
FLASK_ENV=development
```

Para el archivo de `.env`, están las siguiente variables:

| Variable | Descripcion |
| ------------- | ------------- |
| DIALOGFLOW_PROJECT_ID | ID del chatbot personal |
| GOOGLE_APPLICATION_CREDENTIALS | Path al json |

### __Correr aplicación__

En caso que quieras correr un ambiente virtual, corre los siguientes comandos:
``` bash
$ python -m venv env

# Si estás en Linux/Mac, utiliza esto
$ source env/bin/activate

# Si estás en Windows, utiliza esto
$ env/Scripts/activate  
```

Para instalar las dependencias de Python, corre esto:
``` bash
$ pip install -r requirements.txt
```

Y por último, corre esto para correr el servidor:
``` bash
$ flask run
```

## Conectar Chatbot

Para estos pasos asumiré que ya tienes un chatbot hecho.

Para poder conectar el chatbot con el servidor, hay que descargar ngrok ([sigue este link para instalarlo](https://ngrok.com/)). Después de instalarlo, corre el siguiente comando (puede que necesites moverte a la carpeta donde tengas el ejecutable):
``` bash
$ ngrok http 5000
```

En caso de que tengas el servidor corriendo en otro puerto, cambia el 5000 por dicho puerto.

Al correr ngrok, te dará dos links, uno `http` y otro `https`. Copia y pega este link en el campo de URL dentro de Fullfilment.

---

## Contribuidores
| Nombre | No sé |
| ------------- | ------------- |
| Ale | Personita |
| Adrian | Personita |
| Mago | Personita |
