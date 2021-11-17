# Kantonsrat Zürich: Analyse
Diese Scripte machen folgendes:
* Herunterladen von allen Sitzungsprotokollen
* Gesprochenes Wort je Kantonsratsmitglied erkennen und extrahieren
* Mitgliederliste anhand Daten des Staatsarchives aufbereiten
* Auswerten, wer wie oft und was gesagt hat

## Datenquellen
* "API" des Kantonsrats, nur für Geschäfte. Verwende diese nicht für Mitglieder, die Api ist, gelinde gesagt, "interessant"
* Historisches Archiv für Mitglieder und Funktionen. Datenquelle ebenfalls nicht über alle Zweifel erhaben. Manuelle Korrekturen nötig.

## Scripte
* `0_scraper.ipynb`: Lädt alle Daten (Sitzungsinformationen und Protokolle als PDF) herunter
* `1_additional_data.ipynb`: Lädt alle Kantonsräte der Vergangenheit anhand Daten des Staatsarchives
* `2_extract.ipynb`: Durchsucht PDFs und versucht, gesprochenes Wort zu extrahieren
* `3_clean.ipynb`: Bereinigt die extrahierten Wortprotokolle und fügt Informationen über die sprechende Person hinzu
* `4_analyse_base.ipynb`: Quantitative Analysen
* `5_text_analysis.ipynb`: Textanalysen

## Kontakt:
simon.huwiler@nzz.ch