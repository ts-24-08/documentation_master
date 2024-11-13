
# Anleitung zur Erweiterung der FastAPI-Anwendung mit CORS und Bereitstellung auf einer EC2-Instanz

Diese Anleitung zeigt dir, wie du dein bestehendes FastAPI-Skript um CORS (Cross-Origin Resource Sharing) erweiterst und die Anwendung auf einer EC2-Instanz bereitstellst. Außerdem richten wir ein API Gateway ein, um die API für externe Anfragen zugänglich zu machen.

## Was ist CORS und warum ist es wichtig?

CORS (Cross-Origin Resource Sharing) ist ein Mechanismus, der Webanwendungen erlaubt, Ressourcen von einer anderen Domain anzufordern. Das ist besonders wichtig, wenn deine API von einem anderen Frontend (z. B. einer Website) aus aufgerufen wird, das auf einer anderen Domain oder einem anderen Port läuft. Ohne CORS-Berechtigungen werden Anfragen von anderen Domains blockiert, was die Funktionalität deiner Anwendung einschränken kann.

## 1. CORS in FastAPI integrieren

Um CORS in FastAPI zu integrieren, nutzen wir das `CORSMiddleware`, das in `fastapi.middleware.cors` verfügbar ist.

### Schritte:

1. Importiere `CORSMiddleware` in deinem Skript.
2. Füge `CORSMiddleware` zur Anwendung hinzu und konfiguriere die erlaubten Ursprünge.

Hier ist das aktualisierte Skript:

```python
from fastapi import Request, FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware  # CORS-Middleware importieren

class TodoCreate(BaseModel):
    id: int
    title: str
    status: bool = False

class Todo(BaseModel):
    id: int
    title: str
    status: bool = False

# Framework initializieren
app = FastAPI()

# CORS konfigurieren
origins = ["*"]  # Erlaubt alle Ursprünge; für Produktionssysteme spezifische Domains angeben
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = []

# Routen definieren
@app.get("/")
def root():
    return "Hallo Welt"

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos", response_model=List[Todo])
def post_todos(todo: TodoCreate):
    new_todo = Todo(
        id=todo.id,
        title=todo.title,
        status=todo.status
    )
    todos.append(new_todo)
    return todos
```

### Erklärung der CORS-Konfiguration

- **allow_origins**: Gibt die erlaubten Ursprünge an. `["*"]` erlaubt alle Ursprünge; für eine sicherere Produktion empfiehlt es sich, nur spezifische Ursprünge anzugeben.
- **allow_methods**: Definiert die HTTP-Methoden, die erlaubt sind (z. B. `["GET", "POST"]`).
- **allow_headers**: Erlaubt bestimmte Header für Anfragen.

## 2. FastAPI-Anwendung auf EC2-Instanz bereitstellen

### Schritt 1: EC2-Instanz einrichten

1. Erstelle eine EC2-Instanz und installiere die nötigen Pakete (z. B. `uvicorn` zum Starten der Anwendung und `fastapi`).
2. Verbinde dich per SSH mit der EC2-Instanz und installiere die Pakete:

   ```bash
   sudo apt update
   sudo apt install python3-pip
   git clone https://github.com/ts-24-08/todo-api.git
   cd todo-api
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Übertrage das Skript auf die EC2-Instanz oder erstelle es direkt auf der Instanz.

### Schritt 2: FastAPI-Anwendung starten

Starte die Anwendung auf der EC2-Instanz:

```bash
fastapi run main.py
```

Damit ist deine Anwendung unter `http://<EC2-Instance-Public-IP>:8000` erreichbar.

### Schritt 3: Anwendung als Dienst einrichten

Damit die Anwendung auch nach einem SSH-Disconnect weiterläuft, richten wir einen systemd-Dienst ein:

1. Erstelle eine Service-Datei:

   ```bash
   sudo nano /etc/systemd/system/fastapi.service
   ```

2. Füge Folgendes ein und speichere die Datei:

   ```ini
   [Unit]
   Description=FastAPI Application
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu
   ExecStart=/usr/bin/uvicorn your_script_name:app --host 0.0.0.0 --port 8000
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

3. Lade die systemd-Konfiguration neu und starte den Dienst:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start fastapi.service
   sudo systemctl enable fastapi.service
   ```

## 3. Amazon API Gateway einrichten

1. Gehe in die AWS-Konsole und öffne **API Gateway**.
2. Erstelle eine neue REST API und wähle den Typ **Regional**.
3. Erstelle eine **neue Ressource** für die API (z. B. `/todos`).
4. Richte HTTP-Methoden (z. B. GET, POST) ein und verbinde sie mit dem öffentlichen Endpoint deiner EC2-Instanz (`http://<EC2-Instance-Public-IP>:8000/todos`).
5. Konfiguriere **CORS** im API Gateway für jede Methode, um Anfragen von anderen Domains zuzulassen.
6. Deploye die API und teste die Endpunkte.

## 4. API testen

Verwende `curl` oder Tools wie Postman, um die Endpunkte zu testen. Beispiel:

```bash
curl -X GET "https://<api-id>.execute-api.<region>.amazonaws.com/prod/todos"
```

Deine FastAPI-Anwendung sollte nun auf einer EC2-Instanz laufen, CORS-Anfragen erlauben und über das API Gateway zugänglich sein.
