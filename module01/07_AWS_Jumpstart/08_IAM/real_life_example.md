# Anwendungssituation
Stell dir vor, ein Unternehmen, nennen wir es TechCorp, hat beschlossen, seine IT-Infrastruktur in die Cloud zu verlagern und nutzt dazu AWS (Amazon Web Services). TechCorp möchte AWS nutzen, um eine Anwendung bereitzustellen, die von verschiedenen Teams wie der Entwicklung, dem Marketing und dem Management genutzt wird. Gleichzeitig muss TechCorp die Sicherheitsanforderungen einhalten und sicherstellen, dass jedes Team nur Zugriff auf die Ressourcen und Daten hat, die es benötigt.

Hier beschreiben wir, wie TechCorp die einzelnen IAM-Konzepte und Sicherheitsmechanismen nutzt, um die Anforderungen umzusetzen.
## 1. Authentifizierung und Autorisierung
Anwendungsszenario: Bevor Mitarbeiter auf die AWS-Umgebung zugreifen können, müssen sie authentifiziert werden – das bedeutet, dass AWS sicherstellen muss, dass jede Person die ist, die sie vorgibt zu sein (Authentifizierung). Nach erfolgreicher Authentifizierung muss das System sicherstellen, dass diese Mitarbeiter nur die Berechtigungen haben, die sie benötigen (Autorisierung).

- Authentifizierung: Jeder Mitarbeiter bekommt ein AWS-Konto mit Anmeldeinformationen (Benutzername und Passwort). Für zusätzliche Sicherheit nutzt TechCorp die Multi-Faktor-Authentifizierung (MFA), sodass Mitarbeiter zusätzlich zu ihrem Passwort einen Code eingeben müssen, der auf ihr Mobiltelefon gesendet wird.
- Autorisierung: Die Berechtigungen werden so konfiguriert, dass jeder Benutzer nur auf bestimmte AWS-Dienste und Ressourcen zugreifen kann, z. B. dürfen Entwickler auf EC2-Instanzen zugreifen, während das Marketing-Team nur Zugriff auf bestimmte S3-Buckets hat.
## 2. IAM und Security Groups
TechCorp benötigt ein zuverlässiges Identitäts- und Zugriffsmanagement, um sicherzustellen, dass jeder Benutzer und jedes System nur die Daten und Ressourcen sehen und nutzen kann, die für ihn relevant sind.

- IAM: Über IAM legt TechCorp fest, wer auf welche AWS-Ressourcen zugreifen darf. Sie erstellen IAM-Benutzer und -Gruppen für ihre Mitarbeiter und ordnen ihnen spezifische Berechtigungen zu, sodass beispielsweise Entwickler auf Entwicklungsressourcen zugreifen können, Marketing-Mitarbeiter aber nur auf Marketingdaten.

- Security Groups: Security Groups werden genutzt, um den Netzwerkzugriff auf Ressourcen wie EC2-Instanzen zu kontrollieren. Beispielsweise erstellt TechCorp Security Groups, die den Zugriff auf die Produktionsdatenbank nur von IP-Adressen innerhalb des Unternehmensnetzwerks aus erlauben. So können Entwickler nur über das sichere Firmennetzwerk auf die Datenbank zugreifen, was die Sicherheit weiter erhöht.

## 3. IAM-Benutzer und der Root-Benutzer
Beim Einrichten ihres AWS-Kontos erhalten die Administratoren von TechCorp den Root-Benutzerzugang. Der Root-Benutzer ist das „Master-Konto“ in AWS und hat uneingeschränkte Rechte. Da der Root-Benutzer kritisch ist, wird er nur für wichtige Aufgaben genutzt und gesichert abgelegt.

- IAM-Benutzer: Anstatt jeden Mitarbeiter als Root-Benutzer einzurichten, erstellt TechCorp IAM-Benutzer für jeden Mitarbeiter. Entwickler, das Marketing-Team und die IT-Abteilung erhalten jeweils eigene IAM-Benutzerkonten, sodass sie auf AWS-Ressourcen zugreifen können, ohne den Root-Benutzer verwenden zu müssen.

## 4. IAM-Rollen
Bestimmte AWS-Ressourcen müssen in der Lage sein, auf andere Ressourcen zuzugreifen, ohne dass ein menschlicher Benutzer beteiligt ist. Hier kommen IAM-Rollen ins Spiel.

**Beispiel**: TechCorp hat eine Anwendung, die auf EC2-Instanzen läuft und auf einen S3-Bucket zugreifen muss, um Dateien zu speichern. Sie erstellt eine IAM-Rolle für diese EC2-Instanz, die dem S3-Bucket Zugriff auf bestimmte Daten gewährt, ohne dass ein Entwickler Anmeldeinformationen manuell eingeben muss. Dies vereinfacht die Verwaltung und ist sicherer, da keine festen Zugangsdaten in der Anwendung gespeichert werden müssen.

## 5. IAM-Policies
IAM-Policies helfen TechCorp dabei, detaillierte Berechtigungen festzulegen und zu kontrollieren, was jede Person oder jedes System in der AWS-Umgebung tun darf.

**Beispiel**: TechCorp erstellt eine Policy für das Entwicklungsteam, die nur Lese- und Schreibzugriff auf S3-Buckets ermöglicht, die als „Entwicklung“ markiert sind. Die Richtlinie wird einer IAM-Gruppe für Entwickler zugewiesen. Gleichzeitig wird das Marketing-Team in einer separaten Gruppe zusammengefasst, deren Policy nur Lesezugriff auf bestimmte Marketingdaten in S3 erlaubt. So wird sichergestellt, dass jeder Mitarbeiter nur auf die relevanten Ressourcen zugreifen kann.

## 6. IAM-Gruppen
Da TechCorp mehrere Abteilungen hat, vereinfacht die Verwendung von IAM-Gruppen die Verwaltung der Zugriffsrechte.

**Beispiel**: TechCorp erstellt eine Gruppe für Entwickler und fügt alle Entwickler als Mitglieder hinzu. Der Gruppe wird eine Policy zugewiesen, die es den Entwicklern ermöglicht, EC2-Instanzen zu verwalten und S3-Buckets zu nutzen. Ähnlich wird eine separate Gruppe für das Marketing-Team erstellt, das nur Zugriff auf die Marketingdaten in S3 erhält. Durch Gruppen können Berechtigungen effizient für mehrere Benutzer gleichzeitig verwaltet werden.

## 7. AWS Organizations
TechCorp hat mehrere Abteilungen und möglicherweise sogar Tochterunternehmen, die separate AWS-Konten verwenden. AWS Organizations hilft dabei, diese Konten zentral zu verwalten und Regeln für die gesamte Organisation festzulegen.

Beispiel: TechCorp erstellt eine Organisation mit Haupt- und Unterkonten für verschiedene Abteilungen (z. B. Entwicklung, Marketing und Finanzen). Über Organizations kann das Hauptkonto zentrale Richtlinien für alle Unterkonten festlegen, z. B. dass alle Daten nur innerhalb der Region EU (Frankfurt) gespeichert werden dürfen, was auch die Einhaltung der Datenschutzrichtlinien wie der DSGVO unterstützt.