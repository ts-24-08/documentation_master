# FastAPI Todo-App mit AWS RDS und VPC-Integration

In dieser Aufgabe erweitern wir unsere bestehende FastAPI Todo-App, die auf einer EC2-Instanz läuft, um eine Verbindung zu einer Amazon RDS-Datenbank. Die Todos werden dabei in der RDS-Datenbank gespeichert. Diese Anleitung hilft dir beim Anpassen des Skripts, Einrichten eines VPC, einer EC2-Instanz, einer RDS-Datenbank und der Konfiguration der App.

## Voraussetzungen
- AWS-Konto und Berechtigungen zur Verwaltung von EC2, RDS und VPC.
- Ein bestehendes Repository für die FastAPI Todo-App.

## Ziel
Nach Abschluss dieser Anleitung kannst du:
1. Eine Multi-AZ Amazon RDS-DB-Instanz einrichten.
2. Eine EC2-Instanz und ein VPC mit Subnetzen, Internet-Gateway und NAT-Gateway erstellen.
3. Die FastAPI-App für die Kommunikation mit der RDS-Instanz konfigurieren.

---

## Schritt 1: Repository vorbereiten und Skript für die Datenbankverbindung anpassen

1. **Repository klonen und Branch erstellen**:
   - Forke das Repository und klone es auf deine lokale Maschine.
   - Erstelle einen neuen Branch `feature/database`.

2. **Virtuelle Umgebung erstellen und Pakete installieren**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **MySQL Connector installieren**:
   ```bash
   pip install mysql-connector-python
   ```

4. **Datenbankverbindung in der App definieren**:
   - Erstelle eine `.env`-Datei im Projektverzeichnis und füge die Zugangsdaten hinzu:
   ```plaintext
   DB_USER=db_user
   DB_PASSWORD=db_password
   DB_HOST=db_endpoint
   DB_NAME=db_name
   ```

5. **Code für die DB-Verbindung in der App anpassen**:
   ```python
   import os
   from dotenv import load_dotenv
   import mysql.connector
   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel
   from typing import List

   load_dotenv()
   
   app = FastAPI()

   db_config = {
       'user': os.getenv("DB_USER"),
       'password': os.getenv("DB_PASSWORD"),
       'host': os.getenv("DB_HOST"),
       'database': os.getenv("DB_NAME")
   }

   def get_db_connection():
       return mysql.connector.connect(**db_config)

   class TodoCreate(BaseModel):
       title: str
       status: bool = False

   @app.get("/todos", response_model=List[TodoCreate])
   def get_todos():
       connection = get_db_connection()
       cursor = connection.cursor(dictionary=True)
       cursor.execute("SELECT * FROM todos")
       todos = cursor.fetchall()
       cursor.close()
       connection.close()
       return todos

   @app.post("/todos", response_model=List[TodoCreate])
   def post_todos(todo: TodoCreate):
       connection = get_db_connection()
       cursor = connection.cursor()
       cursor.execute(
           "INSERT INTO todos (title, status) VALUES (%s, %s)",
           (todo.title, todo.status)
       )
       connection.commit()

       cursor.close()
       connection.close()

       return get_todos()
   ```

6. **`requirements.txt` aktualisieren**:
   ```bash
   pip freeze > requirements.txt
   ```

---

## Schritt 2: VPC und Netzwerkkonfiguration

1. **VPC erstellen**:
   - Erstelle ein neues VPC (10.0.0.0/16) mit zwei öffentlichen (10.0.5.0/24, 10.0.10.0/24)und 2 privaten Subnetzen (10.0.15.0/24, 10.0.20.0/24).
   - Füge ein Internet Gateway und eine Route Table für die öffentlichen Subnetze hinzu (dazu musst du die Route Table jeweils zu beiden öffentlichen Subnetzen zuweisen).
   - Erstelle ein NAT Gateway in einem öffentlichen Subnetz und eine Route Table, die den Datenverkehr über das NAT Gateway leitet (auch hier bitte beiden privaten Subnetzen die Route Table zuweisen).

---

## Schritt 3: Sicherheitsgruppen einrichten

1. **Sicherheitsgruppe für EC2-Instanz**:
   - Erstelle eine Sicherheitsgruppe für die EC2-Instanz und erlaube Zugriff auf Port 22 (SSH), Port 80 (HTTP) und 8000 (FastAPI). Achte darauf, dass du die Sicherheitsgruppe für die EC2-Instanz mit dem VPC verknüpfst.

2. **Sicherheitsgruppe für RDS-Datenbank**:
   - Erstelle eine separate Sicherheitsgruppe für die RDS-Datenbank und erlaube Zugriff auf Port 3306 nur von der EC2-Instanz, d.h. nur von der Sicherheitsgruppe der EC2-Instanz, die wir im Schritt zuvor erstellt haben. Auch hier musst du das richtige VPC auswählen.

---

## Schritt 4: RDS-Instanz erstellen


1. **DB-Subnetzgruppe hinzufügen**:
   - Gehe zum RDS-Dashboard und klicke auf `Subnet groups`.
   - Klicke auf `Create DB Subnet Group` und füge die privaten Subnetze hinzu.
2. **RDS-Instanz konfigurieren**:
   - Wähle im AWS Management Console unter `Services > RDS`.
   - Klicke auf `Create database`
   - Klicke auf Standard Create und wähle MySQL als Engine.
    - Konfiguriere die Instanz mit Multi-AZ DB Instanz
    - Wähle für Templates Dev/Test
    - Unter Settings konfiguriere den Namen der Datenbank (todos-db), den Benutzernamen (admin) und das Passwort (techstarter).
    - Unter Instanzkonfiguration nehme die Burstable classes und wähle db.t3.micro aus
    - Für Storage wähle SSD und 20 GB aus
    - Unter Connectivity wähle die VPC, die du im vorherigen Schritt erstellt hast.
    - Wähle die DB-Subnetzgruppe, die du im vorherigen Schritt erstellt hast.
    - Wähle die Sicherheitsgruppe für die RDS-Datenbank, die du im vorherigen Schritt erstellt hast. (Alternativ erstellst du eine neue und wir passen die später an)
    - harke unter Monitoring Enable Enhanced Monitoring ab
    - Unter Additional Configuration konfiguriere den intialen Datenbank-Namen mit todos und deaktiviere Enable automated backups
    - Klicke auf Create Database

3. **RDS-Endpoint speichern**:
   - wartet bis die Instanz bereit ist und kopiert den Endpoint der RDS-Datenbank.
   - Kopiere den Endpoint der RDS-Datenbank und füge ihn in die `.env`-Datei im Projektverzeichnis ein.

---

## Schritt 5: EC2-Instanz konfigurieren und App bereitstellen

1. **EC2-Instanz einrichten**:
   - Erstelle eine neue EC2-Instanz (Ubuntu) in einem öffentlichen Subnetz und füge die EC2-Sicherheitsgruppe hinzu.
   - Stelle sicher, dass die Instanz eine öffentliche IP-Adresse hat.

2. **Mit der EC2-Instanz verbinden**:
   - Verbinde dich über SSH mit der EC2-Instanz und installiere die benötigten Pakete:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv mysql-client
   ```

3. **App und Umgebung auf der EC2-Instanz einrichten**:
   - Kopiere die FastAPI-App auf die EC2-Instanz:
   ```bash
   scp -i "dein-key.pem" -r /pfad/zur/app ubuntu@deine-ec2-ip:/home/ubuntu/
   ```
   (bitte nur die Dateien main.py, .env und requirements.txt kopieren)
   - Erstelle und aktiviere eine virtuelle Umgebung:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   - Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

4. **Datenbankverbindung testen**:
   - Verwende `mysql-client`, um eine Verbindung zur RDS-Datenbank herzustellen und die Todos-Tabelle zu erstellen:
   ```bash
   mysql -h your-rds-endpoint -u your-db-username -p
   ```
   - Erstelle die `todos`-Tabelle:
   ```sql
   CREATE TABLE todos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       status BOOLEAN DEFAULT FALSE
   );
   ```
   - Beende die MySQL-Shell mit `exit`.
   - Starte die FastAPI-App auf der EC2-Instanz:
   ```bash
   fastapi run main.py
    ```
    - Öffne einen Browser und rufe die EC2-Instanz über die öffentliche IP und Port 8000 auf, um sicherzustellen, dass die App auf die RDS-Datenbank zugreifen kann. Unter `/docs` kannst du die API-Dokumentation aufrufen.

---

## Schritt 6: Anwendung als Service einrichten

1. **Systemd-Service-Datei erstellen**:
   - Erstelle die Datei `/etc/systemd/system/fastapi.service` und füge den folgenden Inhalt ein:
   ```plaintext
   [Unit]
   Description=FastAPI App
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/todo-api
   ExecStart=/home/ubuntu/todo-api/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. **Service starten und aktivieren**:
   ```bash
   sudo systemctl start fastapi
   sudo systemctl enable fastapi
   ```

3. **App testen**:
   - Rufe die EC2-Instanz über die öffentliche IP und Port 8000 auf und überprüfe, ob die Todos in der RDS-Datenbank gespeichert werden.

---

## Abschluss

Herzlichen Glückwunsch! Du hast die FastAPI-App erfolgreich für die Verwendung einer Amazon RDS-Datenbank im AWS VPC eingerichtet und konfiguriert.
