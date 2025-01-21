## Einleitende Fragen:
- Warum sollten Passwörter niemals im Klartext gespeichert werden?
- Was bedeutet es, ein Passwort zu hashen, und wie schützt bcrypt Passwörter?
- Was ist ein JSON Web Token (JWT) und wofür wird es verwendet?
- Warum wird ein JWT nach erfolgreichem Login erzeugt und nicht vorher?
- Wie sichert die Signatur eines JWT die Integrität des Tokens?
- Wie würdest du einen Token in einer Client-Anwendung sicher speichern?
---

# Detaillierte Einführung in Authentifizierung, JWT und bcrypt

## 1. Einführung: Was ist Authentifizierung?
- **Definition:** Authentifizierung ist der Prozess, mit dem ein Benutzer nachweist, dass er ist, wer er vorgibt zu sein.
- **Warum wichtig?**
  - Schutz sensibler Daten.
  - Zugriffskontrolle für Anwendungen (z. B. nur angemeldete Benutzer können Inhalte bearbeiten).
  - Verhindert unbefugten Zugriff.

---

## 2. JSON Web Token (JWT)

### Was ist ein JWT?
- Ein **JWT (JSON Web Token)** ist ein kompakter, URL-sicherer Token-Standard, der Daten zwischen zwei Parteien sicher überträgt.
- **Einsatzgebiete:**
  - Token-basierte Authentifizierung.
  - Informationsaustausch mit Integritätsprüfung.

### Aufbau eines JWT
Ein JWT besteht aus drei Teilen:
1. **Header**: Enthält den Algorithmus und den Typ des Tokens.
2. **Payload**: Enthält die Daten, wie Benutzer-ID und Ablaufdatum.
3. **Signature**: Sichert den Token vor Manipulation.

Beispiel eines Tokens:
```plaintext
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.eyJ1c2VySWQiOjEyMywiZXhwIjoxNjcxMDEwMDAwfQ
.H5Lr7Z_JWDB5czmtb5yDnW8MtYVsfM3bg9-y9SJcz6M
```

#### Header
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

#### Payload
```json
{
  "userId": 123,
  "exp": 1671010000
}
```

#### Signature
Die Signatur sichert den Token:
```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secretKey
)
```

---

### Warum JWT?
- **Stateless:** Der Server muss keine Sitzungsdaten speichern.
- **Effizient:** Einfach in HTTP-Headern zu übertragen.
- **Sicher:** Verhindert Manipulation durch Signatur.

### Vorteile von JWT
1. **Skalierbarkeit:** Keine serverseitige Speicherung nötig.
2. **Flexibilität:** Kann für viele Anwendungen eingesetzt werden (z. B. Web, Mobile).
3. **Einfachheit:** JSON-Datenstruktur ist leicht zu handhaben.

---

## 3. bcrypt: Sicheres Passwort-Hashing

### Warum Passwörter hashen?
- **Sicherheit:** Passwörter sollten niemals im Klartext gespeichert werden.
- **Verhindert Brute-Force-Angriffe:** Selbst bei einem Datenbankleck bleiben gehashte Passwörter schwer entschlüsselbar.

### Was ist bcrypt?
- Ein Algorithmus zum Hashen von Passwörtern, der:
  - Einen Salt (zufälliger Wert) hinzufügt.
  - Den Prozess absichtlich verlangsamt.

---

### Wichtige bcrypt-Funktionen
1. **Passwort hashen:**
   ```javascript
   const bcrypt = require('bcrypt');
   const hashedPassword = await bcrypt.hash('meinPasswort', 10);
   console.log(hashedPassword);
   ```
   - `10` gibt die Anzahl der Salt-Runden an.

2. **Passwort prüfen:**
   ```javascript
   const isValid = await bcrypt.compare('meinPasswort', hashedPassword);
   console.log(isValid);
   ```

---

## 4. Wie funktionieren bcrypt und JWT zusammen?

### Registrierung:
1. Benutzer gibt Benutzername und Passwort ein.
2. Das Passwort wird mit bcrypt gehasht und in der Datenbank gespeichert.
3. Beispiel:
   ```javascript
   const hashedPassword = await bcrypt.hash(password, 10);
   users.push({ username, password: hashedPassword });
   ```

### Login:
1. Benutzer gibt Benutzername und Passwort ein.
2. Das eingegebene Passwort wird mit dem gespeicherten Hash verglichen:
   ```javascript
   const isValid = await bcrypt.compare(password, user.password);
   ```
3. Bei Erfolg wird ein JWT generiert:
   ```javascript
   const token = jwt.sign({ id: user.id }, 'geheimerSchlüssel', { expiresIn: '1h' });
   ```

### Geschützte Routen:
1. Der Benutzer sendet den Token bei jeder Anfrage:
   ```
   Authorization: Bearer <token>
   ```
2. Der Server prüft die Gültigkeit des Tokens:
   ```javascript
   const decoded = jwt.verify(token, 'geheimerSchlüssel');
   ```

---

## 5. Sicherheits-Best Practices
1. **Verwende HTTPS:** Token dürfen nicht über unsichere Verbindungen gesendet werden.
2. **Setze ein Ablaufdatum:** Token sollten nicht unbegrenzt gültig sein.
3. **Verwende starke Schlüssel:** Geheime Schlüssel sollten sicher und komplex sein.
4. **Vermeide sensible Daten in der Payload:** Nur notwendige Informationen speichern.

---

## 6. Beispiel-Code für ein Mini-Backend

### Installation
```bash
npm install express bcrypt jsonwebtoken body-parser
```

### Server-Setup
```javascript
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');

const app = express();
const SECRET_KEY = 'meinGeheimerSchlüssel';
const users = [];

app.use(bodyParser.json());

// Registrierung
app.post('/register', async (req, res) => {
  const { username, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);
  users.push({ username, password: hashedPassword });
  res.json({ message: 'Registrierung erfolgreich' });
});

// Login
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username);
  if (!user || !(await bcrypt.compare(password, user.password))) {
    return res.status(401).json({ message: 'Ungültige Anmeldedaten' });
  }
  const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });
  res.json({ token });
});

// Geschützte Route
app.get('/profile', (req, res) => {
  const token = req.headers.authorization?.split(' ')[1];
  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    res.json({ message: `Willkommen, ${decoded.username}` });
  } catch {
    res.status(403).json({ message: 'Ungültiger Token' });
  }
});

app.listen(3000, () => console.log('Server läuft auf http://localhost:3000'));
```

---

## 7. Ressourcen
- [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)
- [bcrypt](https://www.npmjs.com/package/bcrypt)
- [JWT Debugger](https://jwt.io/)

