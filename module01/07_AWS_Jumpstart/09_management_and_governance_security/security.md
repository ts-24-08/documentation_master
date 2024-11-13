# AWS Grundlagen und Sicherheit

## 1. Security, Identity & Compliance

Diese Services bieten die Grundlage für eine sichere, skalierbare und konforme AWS-Umgebung.

### 1.1 Identity and Access Management (IAM)
   - **Konzept**: Ermöglicht die Verwaltung von Zugriffen auf AWS-Ressourcen durch Erstellen und Verwalten von Benutzern, Rollen und Richtlinien.
   - **Best Practices**:
     - Verwenden Sie Rollen anstelle von root-Zugängen.
     - Implementieren Sie das **Least Privilege Principle** (Minimalprinzip), indem Sie Benutzern nur die Berechtigungen geben, die sie benötigen.
   - **Praxis**: Erstellen von spezifischen IAM-Rollen und -Benutzern mit abgestuften Berechtigungen für eine sicherheitsbewusste und effiziente Verwaltung.

### 1.2 Single Sign-On (SSO)
   - **Konzept**: Zentralisierte Anmeldung für mehrere AWS-Konten und Anwendungen.
   - **Vorteil**: Ermöglicht Benutzern den Zugriff auf alle benötigten Anwendungen mit einem einzigen Satz Anmeldedaten, was die Benutzerfreundlichkeit und Sicherheit erhöht.

### 1.3 Directory Service
   - **Konzept**: Integration von AWS-Ressourcen in bestehende Verzeichnisdienste (z. B. Microsoft Active Directory).
   - **Praxis**: Verbindet lokale und Cloud-Identitäten, um eine nahtlose Benutzerverwaltung zu gewährleisten.

### 1.4 AWS Cognito
   - **Konzept**: Bietet Benutzerverwaltung und Authentifizierung für Web- und mobile Anwendungen.
   - **Praxisbeispiel**: Konfigurieren von Benutzergruppen und Authentifizierungsmechanismen in einer Webanwendung, die auf AWS gehostet wird.

### 1.5 AWS Certificate Manager (ACM)
   - **Konzept**: Bereitstellung und Verwaltung von SSL/TLS-Zertifikaten zur Verschlüsselung des Datenverkehrs für Webanwendungen.
   - **Praxis**: Kostenlose Bereitstellung von Zertifikaten und automatisches Verlängern, um die Sicherheit von Websites und APIs zu gewährleisten.

### 1.6 Key Management Service (KMS) und CloudHSM
   - **KMS**: Verwalten und erstellen kryptografischer Schlüssel zur Verschlüsselung von Daten.
   - **CloudHSM**: Hardware-Sicherheitsmodule (HSMs) zur Erhöhung der kryptografischen Sicherheit.
   - **Praxis**: Verwendung von KMS zur Verschlüsselung von Daten, z. B. in S3, und CloudHSM für besonders sensible Daten.

### 1.7 Secrets Manager
   - **Konzept**: Verwaltung von Zugriffsinformationen wie Passwörtern, API-Schlüsseln und anderen vertraulichen Daten.
   - **Praxisbeispiel**: Sicheres Speichern und regelmäßiges Rotieren von Zugangsdaten für Datenbanken und Anwendungen.

### 1.8 GuardDuty und Macie
   - **GuardDuty**: Automatische Bedrohungserkennung für AWS-Konten, erkennt verdächtige Aktivitäten und potenzielle Risiken.
   - **Macie**: Erkennung und Schutz sensibler Daten, z. B. personenbezogener Informationen (PII).
   - **Praxisbeispiel**: Aktivieren von GuardDuty und Macie, um Bedrohungen zu erkennen und sensible Daten zu schützen.

### 1.9 Inspector
   - **Konzept**: Automatisierte Sicherheitsbewertung von AWS-Ressourcen zur Identifizierung potenzieller Schwachstellen.
   - **Praxis**: Regelmäßige Überprüfung von EC2-Instanzen, um Schwachstellen zu identifizieren und zu beheben.

### 1.10 Netzwerksicherheit: Network Firewall, Firewall Manager, WAF, Shield
   - **Network Firewall**: Verwaltung und Absicherung von Netzwerkzugriffen auf VPC-Ebene.
   - **Firewall Manager**: Zentralisierte Verwaltung von Firewall-Richtlinien über mehrere Konten hinweg.
   - **WAF (Web Application Firewall)**: Schutz von Webanwendungen vor Bedrohungen auf Anwendungsebene.
   - **Shield**: Schutz vor DDoS-Angriffen (Distributed Denial of Service).
   - **Praxis**: Einrichten eines mehrschichtigen Netzwerksicherheitsmodells mit diesen Tools, um Webanwendungen und Netzwerke zu schützen.

### 1.11 Compliance und Audit: Artifact, Audit Manager, Security Hub
   - **Artifact**: Zugriff auf Compliance-Berichte und -Zertifikate von AWS.
   - **Audit Manager**: Automatisierte Sammlung von Nachweisen zur Erfüllung von Compliance-Vorgaben.
   - **Security Hub**: Zentralisierte Übersicht und Bewertung der Sicherheitslage, die Sicherheitsalarme aggregiert und bewertet.
   - **Praxis**: Nutzung dieser Tools zur Sicherstellung und Dokumentation von Compliance-Anforderungen.

---

## Praxisbeispiel: Aufbau einer sicheren AWS-Umgebung

1. **IAM-Benutzer und -Rollen**: Erstellen von Benutzern und Rollen mit **least privilege** Prinzip. Zum Beispiel:
   - Administratorrollen für bestimmte Benutzergruppen
   - Service-gebundene Rollen für EC2, S3, RDS etc.

2. **Multi-Faktor-Authentifizierung (MFA)**: Aktivieren von MFA für Benutzerkonten und besonders sensible Rollen, um die Authentifizierung zu verstärken.

3. **AWS Cognito für Benutzerverwaltung und Authentifizierung**: Einrichten einer einfachen Webanwendung, in der Benutzer sich registrieren und anmelden können. Dies stärkt die Benutzerverwaltung und bietet eine sichere Authentifizierungsebene.

4. **Datenverschlüsselung mit KMS und Secrets Manager**:
   - Verwenden von **KMS** zur Verschlüsselung von Daten in S3 oder RDS.
   - Secrets Manager zum Speichern und regelmäßigen Rotieren von Zugangsdaten für Anwendungen und Datenbanken.

5. **Überwachung und Erkennung von Sicherheitsbedrohungen mit GuardDuty und Macie**:
   - Aktivieren von **GuardDuty**, um das Konto auf verdächtige Aktivitäten zu überwachen.
   - **Macie** analysiert Daten in S3-Buckets und erkennt PII oder andere sensible Informationen, die geschützt werden müssen.

---