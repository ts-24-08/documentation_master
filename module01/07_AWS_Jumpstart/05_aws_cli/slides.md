
---
marp: true
theme: default
paginate: true
---

# AWS Infrastruktur aufbauen

**Themenübersicht**

1. EC2-Instanzen und User Data Script
2. EBS Volumes
3. Snapshots
4. Auto Scaling Group (ASG)
5. Elastic Load Balancer (ELB)

---

# EC2-Instanzen

### Was ist EC2?
- Amazon EC2 (Elastic Compute Cloud) ist ein skalierbarer Cloud-Computing-Dienst.
- Bietet virtuelle Maschinen („Instanzen“) zum Ausführen von Anwendungen.
- Vorteile: Skalierbarkeit, Flexibilität, verschiedene Instanztypen für unterschiedliche Workloads.

### Technische Hintergründe
- Instanzen können für kurze Zeit (Spot Instances), lange Zeit (Reserved Instances) oder on-demand gestartet werden.
- Konfigurationen wie CPU, RAM und Speicher hängen vom gewählten Instanztyp ab.
- Sicherheit und Netzwerkzugriff werden über **Security Groups** gesteuert.

---

# User Data Script

### Was ist User Data?
- Skripte oder Befehle, die beim Start einer EC2-Instanz ausgeführt werden.
- Nützlich zur Automatisierung von Software-Installationen und Konfigurationen direkt beim Start.

### Technische Details
- Wird als Bash-Skript (Linux) oder PowerShell (Windows) beim Start eingelesen.
- Das Skript läuft nur einmal bei der ersten Initialisierung der Instanz.
- Beispiel: Einrichten einer Python-Umgebung oder Starten einer Webanwendung.

```bash
#!/bin/bash
yum update -y
yum install -y python3
echo "print(\"Hello, World!\")" > /home/ec2-user/script.py
python3 /home/ec2-user/script.py
```

---

# EBS Volumes

### Was ist EBS?
- Amazon Elastic Block Store (EBS) bietet persistenten Speicher für EC2-Instanzen.
- Wird wie eine Festplatte an die Instanz angehängt.
- Verschiedene Typen (gp2, io1, etc.) für unterschiedliche Leistung und Kosten.

### Technische Hintergründe
- EBS ist persistent, d.h., Daten bleiben auch nach dem Herunterfahren der Instanz erhalten.
- EBS Volumes können von einer Instanz getrennt und an eine andere Instanz angehängt werden.
- Volumes werden im selben Verfügbarkeitsbereich wie die EC2-Instanz erstellt.

```bash
# EBS Volume erstellen
aws ec2 create-volume --availability-zone <deine-AZ> --size 10 --volume-type gp2
```

---

# Snapshots

### Was ist ein Snapshot?
- Ein Snapshot ist ein speicherabbild von einem EBS Volume.
- Nützlich als Backup oder zur Wiederherstellung eines früheren Zustands.

### Technische Details
- Snapshots werden inkrementell erstellt; nur Änderungen seit dem letzten Snapshot werden gespeichert.
- Snapshots können verwendet werden, um ein neues EBS Volume in derselben oder einer anderen Region zu erstellen.

```bash
# Snapshot erstellen
aws ec2 create-snapshot --volume-id <VolumeId> --description "Backup of my EBS volume"
```

---

# Auto Scaling Group (ASG)

### Was ist eine Auto Scaling Group?
- ASG passt die Anzahl der EC2-Instanzen basierend auf dem Bedarf an.
- Bietet Hochverfügbarkeit und Flexibilität durch automatische Skalierung.

### Technische Hintergründe
- Besteht aus einer Gruppe von EC2-Instanzen, die nach definierten Regeln skaliert werden.
- ASG arbeitet mit **Launch Configurations** oder **Launch Templates**, die die Startparameter der Instanzen festlegen.
- Skalierungsoptionen:
  - **Horizontal Scaling**: Instanzen hinzufügen oder entfernen.
  - **Vertical Scaling**: Leistungsstärkere Instanzen verwenden.

```bash
aws autoscaling create-auto-scaling-group --auto-scaling-group-name my-asg --launch-configuration-name my-launch-config --min-size 1 --max-size 3 --desired-capacity 1 --vpc-zone-identifier <SubnetIds>
```

---

# Elastic Load Balancer (ELB)

### Was ist ein Elastic Load Balancer?
- ELB verteilt eingehenden Datenverkehr auf mehrere EC2-Instanzen.
- Bietet Skalierbarkeit, Redundanz und hohe Verfügbarkeit.

### Technische Hintergründe
- Es gibt verschiedene ELB-Typen:
  - **Application Load Balancer (ALB)**: Lastausgleich auf Anwendungsebene (HTTP, HTTPS).
  - **Network Load Balancer (NLB)**: Hohe Durchsatzanforderungen auf Netzwerkebene (TCP).
  - **Gateway Load Balancer (GLB)**: Unterstützt Routing von Traffic durch virtuelle Netzwerksicherheitsebenen.
- Ein ELB kann in mehreren Availability Zones arbeiten, um Failover-Schutz zu gewährleisten.

```bash
# ELB erstellen und konfigurieren
aws elbv2 create-load-balancer --name my-load-balancer --subnets <SubnetIds> --security-groups <SecurityGroupId>
```

---

# Zusammenfassung

- **EC2 und User Data**: Instanzen flexibel verwalten und automatisch konfigurieren.
- **EBS und Snapshots**: Persistenter Speicher und Backups.
- **ASG**: Sicherstellen, dass genügend Instanzen verfügbar sind.
- **ELB**: Lastverteilung für bessere Verfügbarkeit und Skalierbarkeit.

Diese Infrastruktur ermöglicht eine robuste und skalierbare Anwendungsarchitektur auf AWS.

---

# Fragen?
Vielen Dank für die Aufmerksamkeit! 🚀
