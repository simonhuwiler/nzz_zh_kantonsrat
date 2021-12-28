# Kantonsrat Zürich: Analyse
Diese Scripte machen folgendes:

### Voten
* Herunterladen von allen Sitzungsprotokollen
* Gesprochenes Wort je Kantonsratsmitglied erkennen und extrahieren
* Mitgliederliste anhand Daten des Staatsarchives aufbereiten
* Auswerten, wer wie oft und was gesagt hat

### Vorstösse
* Herunterladen von allen Vorstössen
* Erstunterzeichner extrahieren und mit Mitgliederliste erweitern
* Auswerten, wer welche Vorstösse einreicht

## Datenquellen
* "API" des Kantonsrats, nur für Geschäfte. Verwende diese nicht für Mitglieder, die Api ist, gelinde gesagt, "interessant"
* Historisches Archiv für Mitglieder und Funktionen. Datenquelle ebenfalls nicht über alle Zweifel erhaben. Manuelle Korrekturen nötig.

## Scripte
* `0_scrape_geschaefte.ipynb`: Lädt alle Daten (Sitzungsinformationen und Protokolle als PDF) herunter
* `0_scrape_sitzung.ipynb`: Lädt alle Vorstösse herunter
* `1_additional_data.ipynb`: Lädt alle Kantonsräte der Vergangenheit anhand Daten des Staatsarchives
* `2_extract.ipynb`: Durchsucht PDFs und versucht, gesprochenes Wort zu extrahieren
* `3_clean.ipynb`: Bereinigt die extrahierten Wortprotokolle und fügt Informationen über die sprechende Person hinzu
* `4_analyse_base.ipynb`: Quantitative Analysen der **Voten**
* `5_text_analysis.ipynb`: Textanalysen der **Voten**
* `6_topic_modelling.ipynb`: Toppic Modelling der **Voten**
* `7_geschaefte_analyse.ipynb`: Analyse der eingereichten Vorstösse

## Kontakt:
simon.huwiler@nzz.ch