# Überblick über die AWS-Preismodelle

## 1. AWS-Abrechnungsmodelle

### On-Demand Instances
- **Beschreibung**: Bezahlen Sie für Rechenleistung ohne langfristige Verpflichtungen.
- **Einsatzgebiet**: Ideal für unvorhersehbare oder kurzlebige Workloads.

### Reserved Instances
- **Beschreibung**: Rabatte für langfristige Verpflichtungen (1 oder 3 Jahre).
- **Einsatzgebiet**: Nützlich für stabile und vorhersehbare Workloads.

### Spot Instances
- **Beschreibung**: Günstige Instanzen, wenn AWS ungenutzte Kapazität hat. 
- **Einschränkungen**: Kann jedoch unterbrochen werden.
- **Einsatzgebiet**: Batch-Verarbeitung oder maschinelles Lernen.

### Savings Plans
- **Beschreibung**: Flexibler als Reserved Instances, bietet jedoch ebenfalls Rabatte bei längerfristiger Nutzung.

### Dedicated Hosts
- **Beschreibung**: Physische Server, die exklusiv für Sie bereitgestellt werden.
- **Einsatzgebiet**: Compliance- oder Lizenzanforderungen.

### Dedicated Instances
- **Beschreibung**: Dedizierte Hardware, aber ohne Kontrolle über den Host wie bei Dedicated Hosts.

### Kapazitätsreservierungen
- **Beschreibung**: Reservieren Kapazität für eine bestimmte Verfügbarkeit.

---

## 2. Datenübertragungskosten

### Faktoren
- **Eingehende Daten (Inbound)**: In der Regel kostenlos.
- **Ausgehende Daten (Outbound)**: Wird nach GB berechnet und ist teurer.
- **Innerhalb einer Region**: Kostengünstiger als zwischen Regionen.
- **Zwischen Regionen**: Höhere Kosten.

---

## 3. Speicheroptionen und Stufen

### Speicherlösungen
- **Amazon S3**:
  - S3 Standard: Für häufig genutzte Daten.
  - S3 Standard-IA: Für seltenere Zugriffe.
  - S3 Glacier: Archivierungszwecke.
- **EBS (Elastic Block Store)**:
  - Verschiedene Typen wie `gp3`, `io2`.
  - Einsatzgebiet: Betriebssysteme, Datenbanken.
- **EFS (Elastic File System)**:
  - Skalierbares, serverloses Dateisystem.

### Speicherstufen
- Kosten reduzieren sich mit längerfristigem Zugriff:
  - S3 Glacier Deep Archive: Für selten genutzte Daten.

---

## 4. Fähigkeiten im Kontext

### 4.1 Identifizieren und Vergleichen der Computing-Kaufoptionen
- **On-Demand**: Tests oder kurzlebige Workloads.
- **Reserved Instances**: Langfristig bekannte Workloads wie Datenbanken.
- **Spot Instances**: Batchverarbeitung oder maschinelles Lernen.

### 4.2 Flexibilität der Reserved Instances
- Wechsel zwischen Availability Zones und teilweise zwischen Familien.

### 4.3 Verhalten von Reserved Instances in Organisationen
- Rabatte gelten über Konten hinweg in einer Organisation.

### 4.4 Verstehen der Datenübertragungskosten
- **Kostenminimierung**:
  - Lokale Datenübertragung innerhalb derselben Region.
  - Amazon CloudFront für kostengünstige globale Verteilung.

### 4.5 Verstehen der Preissituationen für Speicheroptionen
- **Häufige Zugriffe**: S3 Standard.
- **Seltene Zugriffe**: S3 Standard-IA oder Glacier.

---

## Vergleichstabellen

### Vergleich der Kaufoptionen

| Kaufoption        | Einsatzgebiet            | Kosten         | Vorteile                               |
|--------------------|--------------------------|----------------|----------------------------------------|
| On-Demand         | Kurzfristig, flexibel    | Höher          | Keine Verpflichtungen                  |
| Reserved Instances| Langfristige Workloads   | Niedriger      | Rabatt bis zu 75 %                     |
| Spot Instances    | Batch-Verarbeitung       | Sehr niedrig   | Nutzen ungenutzter Kapazität           |
| Dedicated Hosts   | Lizenzpflichtige Anwendungen | Hoch       | Exklusive Nutzung physischer Server    |

### Speicherlösungen

| Speicherlösung    | Einsatzgebiet            | Kosten         | Vorteile                               |
|--------------------|--------------------------|----------------|----------------------------------------|
| S3 Standard       | Häufig genutzte Daten    | Mittel         | Hohe Verfügbarkeit                     |
| S3 Glacier        | Archivierung             | Sehr niedrig   | Langfristige Speicherung               |
| EBS               | Betriebssysteme, Datenbanken | Variabel   | Schnell und konsistent                 |
| EFS               | Gemeinsamer Dateizugriff | Variabel       | Skalierbare Nutzung                    |
