## Cloudformation
- Konzept: Infrastructure as Code (IaC) Service, der es ermöglicht, AWS-Ressourcen mithilfe von Vorlagen zu definieren und automatisiert bereitzustellen.
### Wichtige Vorteile
- **Automatisierung**: Schnelle Bereitstellung und Konfiguration von AWS-Ressourcen.
- **Konsistenz**: Wiederholbare und konsistente Bereitstellung von Infrastruktur.
- **Versionierung**: Verfolgung von Änderungen und Rollbacks.
### Beispielprojekt
Erstelle eine Cloudformation-Vorlage, um ein einfaches VPC mit public Subnetz und einer EC2-Instanz mit laufenden NGINX Webserver zu erstellen
```yaml
```
## CloudTrail
- Konzept: AWS-Dienst, der Aktivitäten und API-Nutzung im AWS-Konto aufzeichnet und Änderungen in der Umgebung für Governance, Compliance und Auditierung protokolliert.
### Wichtige Funktionen
- **Protokollierung von API-Aufrufen**: Verfolgung von API-Aktivitäten und Änderungen.
- **Überwachung von Ressourcen**: Protokollierung von Ressourcenänderungen und Zugriffen.
- **Compliance und Governance**: Unterstützung bei der Einhaltung von Sicherheitsrichtlinien und Auditierung.
### Anwendungsfälle
- **Sicherheitsüberwachung**: Erkennung von ungewöhnlichen Aktivitäten und Sicherheitsverletzungen.
- **Compliance**: Nachverfolgung von Änderungen und Zugriffen für Compliance-Anforderungen.
- **Troubleshooting**: Analyse von Änderungen und Aktivitäten zur Fehlerbehebung.
### Beispiel
- Überwachte spezifische Aktivitäten wie den Zugriff auf sensible Daten oder Erstellung von Ressourcen.
- Erstelle Alarme für ungewöhnliche Aktionen, z.B. Änderungen an IAM-Richtlinien oder das Löschen einer VPC
## CloudWatch
- Konzept: Überwachungs- und Alarmdienst von AWS zur Überwachung von Ressourcen und Anwendungen in Echtzeit.
### Wichtige Funktionen
- **Metriken und Alarme**: Überwachung von Metriken und Benachrichtigung bei Schwellenwerten.
- **Log-Überwachung**: Echtzeit-Überwachung und Analyse von Log-Dateien.
- **Dashboards und Events**: Erstellung von Dashboards und Reaktion auf Systemereignisse.
### Anwendungsfälle
- **Leistungsüberwachung**: Überwachung von Ressourcen wie EC2-Instanzen und Datenbanken.
- **Fehlerbehebung**: Echtzeit-Überwachung von Anwendungen und Systemen.
- **Automatisierung**: Reaktion auf Systemereignisse und Auslösen von Aktionen.
### Beispiel
- Erstelle ein CloudWatch-Dashboard zur Überwachung von EC2-Metriken (CPU-Auslastung, Speicher, ...) oder RDS-Metriken (DAtenbankverbindungen, Latenz, ...)
## Control Tower
- Konzept: AWS-Dienst, der die Einrichtung einer sicheren, Multi-Account-Umgebung gemäß Best Practices automatisiert.
### Wichtige Funktionen
- **Account-Bereitstellung**: Automatisierte Einrichtung von AWS-Konten und -Ressourcen.
- **Zentralisierte Governance**: Etabliert und erzwingt Richtlinien in mehreren AWS-Konten.
- **Vorlagen für Best Practices**: Vorgefertigte Richtlinien, Sicherheitsgrundlagen und Best Practices werden auf alle Konten angewendet.
- **Skalierbarkeit**: Ermöglicht die effiziente Skalierung einer Multi-Account-Umgebung.
### Anwendungsfälle
- Guardrails (Richtlinien) definieren, um z.B. bestimmte Regionen zu sperren oder unverschlüsselten Speicher zu verhindern
- Organisationseinheiten (z.B. Entwicklung, Test und Produktion) mit gemeinsamen Basiskonfigurationen
## Trusted Advisor
- Konzept: AWS-Tool, das Echtzeitempfehlungen zur Optimierung von AWS-Ressourcen gibt und sicherstellt, dass sie den Best Practices für Leistung, Sicherheit, Ausfallsicherheit und Kosten entsprechen.
### Wichtige Funktionen
- **Kostenoptimierung**: Empfehlungen zur Reduzierung von Kosten und Verbesserung der Ressourcennutzung.
- **Leistungsverbesserung**: Optimierung von Ressourcen für bessere Leistung und Skalierbarkeit.
- **Sicherheitsbewertung**: Überprüfung der Sicherheitskonfiguration und Empfehlungen zur Verbesserung.
- **Fehlerbehebung**: Identifizierung von potenziellen Problemen und Empfehlungen zur Behebung.
### Anwendungsfälle
- Potenzielle Kosteneinsparungen zu identifizieren, wie z. B. das Stoppen oder Anpassen ungenutzter Ressourcen.
- Sicherheitslücken zu überprüfen und sicherzustellen, dass keine öffentlichen IPs an sensible Instanzen gebunden sind.
