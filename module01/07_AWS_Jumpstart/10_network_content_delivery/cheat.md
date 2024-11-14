
# Grundlegende AWS-Konzepte

## APIs

**API (Application Programming Interface)**: APIs sind Schnittstellen, die es Anwendungen ermöglichen, miteinander zu kommunizieren, ohne dass die Anwendungen die internen Details der anderen Anwendung kennen müssen.

**Beispiel**: Ein Online-Wetterdienst bietet eine API an, mit der andere Anwendungen (z. B. eine Wetter-App) aktuelle Wetterdaten abrufen können.

**Metapher**: Eine API ist wie eine Speisekarte im Restaurant – du bestellst ein Gericht (Anfrage) und die Küche bereitet es für dich zu und bringt es dir (Antwort).

### REST API

**Ressourcen**: REST APIs arbeiten mit "Ressourcen", die eindeutig identifiziert werden.

**HTTP-Methoden**:
- **GET**: Zum Abrufen von Daten (z.B., Anfrage auf `https://api.example.com/weather?city=Berlin` gibt die Wetterdaten für Berlin zurück).
- **POST**: Zum Erstellen neuer Daten (z.B., ein neues Benutzerkonto).
- **PUT**: Zum Aktualisieren bestehender Daten (z.B., Aktualisieren der Benutzer-E-Mail).
- **DELETE**: Zum Löschen von Daten (z.B., Löschen eines Benutzerkontos).

**Vorteile**: REST APIs sind leichtgewichtig und bieten Flexibilität, um Daten und Funktionalitäten in vielen Anwendungen zu nutzen.

## Internet und Netzwerke

**Internet**: Ein globales Netzwerk, das Computer weltweit verbindet, sodass sie miteinander kommunizieren und Daten austauschen können.

**Komponenten**: Server (stellen Daten bereit), Clients (fragen Daten an), Router (leiten Datenpakete), und Protokolle (Regeln für die Datenübertragung wie HTTP oder TCP/IP).

**Metapher**: Das Internet ist wie ein riesiges Spinnennetz, bei dem jeder Knoten ein Computer ist.

### Öffentliches Internet vs. Privates Netzwerk

- **Öffentlich**: Frei zugänglich für alle, aber tendenziell weniger sicher.
- **Privat**: Nur für bestimmte Nutzer, die durch Firewalls und VPNs geschützt sind.

**Metapher**: Das öffentliche Internet ist wie ein öffentlicher Park, während ein privates Netzwerk dein Haus ist – es ist sicherer und nur für bestimmte Personen zugänglich.

### Edge Computing

Eine Methode, die Datenverarbeitung näher am Entstehungsort durchzuführen, um Verzögerungen zu minimieren.

**Anwendungsbereiche**: Zum Beispiel im Internet der Dinge (IoT) oder in autonomen Fahrzeugen.

**Metapher**: Statt einen weit entfernten Supermarkt aufzusuchen, gibt es einen kleinen Laden direkt um die Ecke, um schneller zu sein.


## AWS Networking und Content Delivery Services

### Amazon API Gateway

- **Funktionen**: Erstellen, Bereitstellen und Verwalten von APIs. API Gateway ermöglicht es, RESTful und WebSocket APIs anzubieten.
- **Sicherheit**: Authentifizierung und Autorisierung über AWS IAM, Amazon Cognito oder Lambda Authorizers.
- **Überwachung**: Integration mit CloudWatch, um die API-Nutzung und Performance zu überwachen.
- **Beispiel**: Eine API-Gateway-Ressource, die HTTP-Requests an eine Lambda-Funktion weiterleitet, die eine Antwort generiert (z.B., „Hallo, AWS!“).

### AWS Global Accelerator

- **Funktionen**: Verbessert die Netzwerkleistung durch den Zugriff über das globale AWS-Netzwerk.
- **Vorteile**: Schnellerer und stabilerer Netzwerkzugang, intelligente Verteilung des Datenverkehrs und Schutz vor DDoS-Angriffen.
- **Metapher**: Eine Abkürzung – der Traffic wird direkt über das AWS-Netzwerk geleitet, um den schnellsten Weg zu finden.
- **Beispiel**: Statt das öffentliche Internet zu nutzen, geht die Anfrage über das interne AWS-Netzwerk, was die Latenz reduziert.

### Amazon Route 53

- **Funktionen**: Ein skalierbarer DNS-Service, der Anfragen an die passenden Ressourcen weiterleitet.

### DNS-Routing-Optionen:

- **Simple Routing**: Leitet eine Anfrage direkt an einen Endpunkt weiter.
- **Latency Routing**: Leitet die Anfrage an den nächstgelegenen Server mit der geringsten Latenz.
- **Geo-Routing**: Basierend auf dem geografischen Standort des Benutzers.
- **Failover-Routing**: Bei einem Fehler wird die Anfrage an einen Backup-Endpunkt weitergeleitet.
- **Sicherheit**: Unterstützt DNSSEC zur Vermeidung von DNS-Manipulationen und überwacht die Erreichbarkeit von Endpunkten.

### AWS VPN

- **Site-to-Site VPN**: Baut eine sichere Verbindung zwischen dem lokalen Rechenzentrum und einer AWS-VPC auf, verschlüsselt den Datenverkehr und bietet eine Hybrid-Cloud-Architektur.
- **Client VPN**: Ein Remote-Zugang für Benutzer auf AWS-Ressourcen.
- **Zertifikate und Authentifizierung**: Nutzung von TLS-Zertifikaten für eine sichere Verbindung.
- **Beispiel**: Ein Teammitglied nutzt ein VPN, um sicher auf eine private Anwendung innerhalb der VPC zuzugreifen.

## Domain Name System (DNS)

**Was ist DNS?**

DNS steht für Domain Name System und fungiert als das "Adressbuch" des Internets. Es ist ein hierarchisches und verteiltes System, das Domainnamen (z. B. `www.beispiel.com`) in IP-Adressen (z. B. `192.0.2.1`) übersetzt.

**Funktionsweise von DNS**

- **DNS-Auflösung**: Eine DNS-Abfrage übersetzt die Domain in eine IP-Adresse.
- **DNS-Hierarchie**: Von Root-Level über TLD-Server bis zu den autoritativen Name-Servern.
- **DNS-Typen und -Routing**: Simple, Latency-based, Geo-DNS, Failover, Weighted Routing.
- **Sicherheit im DNS**: DNSSEC schützt vor DNS-Spoofing.

## Virtual Private Network (VPN)

**Was ist ein VPN?**

Ein Virtual Private Network (VPN) stellt eine sichere und verschlüsselte Verbindung her.

**Funktionsweise von VPN**

- **VPN-Tunnel**: Verschlüsselt den Datenverkehr und leitet ihn durch einen sicheren Tunnel.
- **Verschlüsselung und Authentifizierung**: Nutzung von IPsec oder SSL/TLS.
- **Arten von VPN**: Site-to-Site und Client VPN.
- **Sicherheit**: Verschlüsselung, Multi-Factor Authentication, Zero-Trust.

---

Beispielanwendungen für Amazon API Gateway, AWS Global Accelerator, Amazon Route 53 und AWS VPN finden Sie in den jeweiligen Abschnitten.

## Domain Name System (DNS)

### Was ist DNS?

DNS steht für Domain Name System und fungiert als das "Adressbuch" des Internets. Es ist ein hierarchisches und verteiltes System, das Domainnamen (z. B. `www.beispiel.com`) in IP-Adressen (z. B. `192.0.2.1`) übersetzt, die von Computern zur Kommunikation im Netzwerk verwendet werden.

### Funktionsweise von DNS

- **DNS-Auflösung**: Wenn ein Benutzer eine Website aufruft (z. B. `www.example.com`), sendet sein Computer eine DNS-Abfrage an einen DNS-Resolver. Dieser Resolver sucht die zugehörige IP-Adresse, damit die Verbindung hergestellt werden kann.
- **Rekursive und iterative Anfragen**: DNS-Anfragen können rekursiv sein (der Resolver übernimmt die vollständige Suche nach der IP-Adresse) oder iterativ (der Resolver fragt verschiedene Server und erhält schrittweise die Antwort).
- **DNS-Hierarchie**:
  - **Root-Level**: Das höchste Level des DNS-Systems mit Root-Servern, die die Top-Level-Domain-Server (z. B. `.com`, `.org`) kennen.
  - **TLD (Top-Level-Domain) Server**: Verwalten Domains einer bestimmten TLD, wie `.com` oder `.de`.
  - **Authoritative Name Server**: Diese Server kennen die IP-Adressen für bestimmte Domains und geben die endgültige Antwort zurück.

### DNS-Typen und -Routing

- **Simple Routing**: Leitet eine Anfrage direkt an einen Endpunkt weiter.
- **Latency-based Routing**: Leitet Benutzer zu einem Server mit der geringsten Verzögerung (Latenz) – ideal für globale Anwendungen.
- **Geo-DNS (geografisches Routing)**: Leitet Anfragen basierend auf dem geografischen Standort des Benutzers an einen regionalen Server weiter.
- **Failover-Routing**: Verwendet alternative Endpunkte, wenn der primäre Endpunkt ausfällt, um die Verfügbarkeit sicherzustellen.
- **Weighted Routing**: Verteilt Anfragen basierend auf vordefinierten Gewichtungen auf mehrere Server, um Lasten zu verteilen.

### Sicherheit im DNS

**DNSSEC (DNS Security Extensions)**: Eine Sicherheitsfunktion, die sicherstellt, dass die empfangene DNS-Antwort auch wirklich von der vertrauenswürdigen Quelle stammt. DNSSEC schützt vor "DNS-Spoofing"-Angriffen, bei denen Angreifer falsche DNS-Antworten einschleusen könnten.

### Beispiel: Verwendung von Amazon Route 53

Amazon Route 53 ist ein skalierbarer DNS-Webservice von AWS, der eine hohe Verfügbarkeit und Skalierbarkeit bietet. Route 53 unterstützt die oben genannten Routing-Methoden und bietet Funktionen wie Gesundheitschecks für Endpunkte. Durch die Integration von Route 53 können Unternehmen eine höhere Ausfallsicherheit und optimale Leistung sicherstellen.


---


## Anwendungsbeispiele für Amazon API Gateway

Amazon API Gateway ist eine vielseitige Lösung für die Entwicklung und Verwaltung von APIs. Hier sind einige spezifische Anwendungsbeispiele:

### 1. Webanwendungen und Mobil-Backends

API Gateway eignet sich hervorragend zur Bereitstellung von Backend-Diensten für Web- und Mobilanwendungen. Es ermöglicht das Routing von Anfragen zu AWS Lambda-Funktionen, die dann dynamische Daten generieren.

- **Beispiel**: Eine E-Commerce-App, bei der das API Gateway Anfragen für Produktinformationen, Warenkorbdaten und Bestellungen weiterleitet.

### 2. Microservices-Kommunikation

In einer Microservices-Architektur kann API Gateway als zentraler Punkt dienen, um die Kommunikation zwischen verschiedenen Microservices zu steuern und abzusichern.

- **Beispiel**: Eine Anwendung, die über mehrere Microservices verfügt (z. B. für Nutzerverwaltung, Bestandsverwaltung, Zahlungsabwicklung), kann API Gateway verwenden, um alle Anfragen zu zentralisieren und zu verteilen.

### 3. Datenverarbeitung und -weiterleitung

API Gateway kann für die Verwaltung und Verarbeitung von Datenanfragen genutzt werden. Die API empfängt Daten, leitet sie an das Backend weiter und kann die Daten vor der Weitergabe an externe Systeme vorbereiten.

- **Beispiel**: Eine Anwendung, die Bilddaten an das API Gateway sendet, das die Anfragen an AWS Lambda zur Bildverarbeitung weiterleitet, bevor die Daten in einer Datenbank gespeichert werden.

### 4. WebSocket API für Echtzeitanwendungen

API Gateway unterstützt WebSocket APIs, die für Echtzeitanwendungen wie Chat-Apps oder Multiplayer-Spiele genutzt werden. Es ermöglicht bidirektionale Kommunikation zwischen Client und Server.

- **Beispiel**: Eine Chat-Anwendung, die über WebSocket API auf API Gateway aufgebaut ist, um Nachrichten in Echtzeit zwischen Nutzern auszutauschen.

### 5. Sicherer Zugriff auf interne Backend-Services

API Gateway kann als Absicherungsschicht für den Zugriff auf interne Services dienen, insbesondere bei sensiblen oder geschäftskritischen Daten.

- **Beispiel**: Ein Unternehmen stellt eine API für interne Geschäftsberichte bereit, die nur über das interne Netzwerk und nur für autorisierte Benutzer zugänglich ist. Amazon Cognito kann dabei helfen, den Zugriff auf autorisierte Benutzer zu beschränken.

### 6. Integration externer APIs

API Gateway kann auch als Proxy für externe APIs verwendet werden, um deren Nutzung in der eigenen Infrastruktur zu integrieren und zu überwachen.

- **Beispiel**: Ein Unternehmen integriert eine API von Google Maps oder Twitter über API Gateway, um Standortdaten oder soziale Netzwerkinformationen für seine Anwendungen bereitzustellen.

### 7. IoT (Internet of Things) Anwendungen

In IoT-Anwendungen werden häufig Sensordaten kontinuierlich an das Backend gesendet. API Gateway kann diese Daten entgegennehmen und zur weiteren Verarbeitung oder Speicherung weiterleiten.

- **Beispiel**: Ein Netzwerk von Sensoren, die Temperatur- und Luftfeuchtigkeitswerte messen und diese Daten in regelmäßigen Abständen über API Gateway an AWS Lambda-Funktionen senden, die die Daten speichern und analysieren.


### 8. HTTPS in API Gateway
Amazon API Gateway unterstützt von Haus aus HTTPS, um die Kommunikation sicher zu halten. Einige Details dazu:

- *Standardmäßig HTTPS*:
Wenn Sie eine API im API Gateway erstellen, wird sie standardmäßig über HTTPS bereitgestellt. Dies sorgt für eine verschlüsselte Übertragung der Daten zwischen Client und API Gateway.
- *TLS-Zertifikate für benutzerdefinierte Domains*:
Falls Sie eine benutzerdefinierte Domain für Ihre API verwenden (z. B. api.meine-app.de), können Sie ein TLS/SSL-Zertifikat über AWS Certificate Manager (ACM) erstellen und mit dem API Gateway verknüpfen.
So wird sichergestellt, dass Ihre benutzerdefinierte Domain ebenfalls HTTPS unterstützt.
- *API Gateway as Proxy*:
API Gateway kann Anfragen über HTTPS an interne Services oder AWS-Ressourcen weiterleiten. Das heißt, auch die Kommunikation zwischen API Gateway und Ihren internen Services kann verschlüsselt ablaufen, wenn die Services HTTPS unterstützen.
- *Anwendung von Sicherheitsrichtlinien*:
Über API Gateway lassen sich Sicherheitsrichtlinien wie Authentifizierung und Autorisierung einrichten, zum Beispiel durch Integration mit AWS IAM oder Amazon Cognito.
Zusammen mit HTTPS bietet dies eine sichere und autorisierte Kommunikation.
- *Erzwingen von HTTPS*:

API Gateway erlaubt es Ihnen, die API so zu konfigurieren, dass nur HTTPS-Verbindungen akzeptiert werden. Damit wird der Zugriff über unsichere HTTP-Verbindungen unterbunden.
---

Diese Anwendungsbeispiele veranschaulichen die Flexibilität und Leistungsfähigkeit von Amazon API Gateway für eine Vielzahl von Szenarien, von mobilen Backends über Microservices bis hin zur Integration externer APIs und IoT-Daten.
