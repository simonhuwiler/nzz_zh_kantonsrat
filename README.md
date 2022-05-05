# Kantonsrat Zürich: Analyse
This is the repository for the NZZ cantonal council analysis. Here you can find all scrapers, cleaned word transcripts and analyses.

## Installation
Clone Git
```
git clone git@github.com:simonhuwiler/nzz_zh_kantonsrat_genderstudy.git
```
Install dependencies (would recommend doing it in a virtual environment)
```
pip install -r ./requirements.txt
```

## What these scripts do:

### Speeches ("Voten")
* Download all protocols
* Recognize and extract spoken words ("votes") per cantonal council member
* Prepare list of members based on data from the state archives
* Evaluate who said what and how often

### Submissions ("Vorstösse")
* Download of all submissions
* Extract first signatories and expand with member list
* Evaluate who submits which initiatives

## Data sources
* "API" of the Canton Council, for business only. Do not use this for members, the api is "interesting" to say the least.
* Historical archive for members and functions. Data source also not above reproach. Manual corrections needed.

## Scripts
* `0_scrape_geschaefte.ipynb`: Downloads all data (session information and protocols as PDF)
* `0_scrape_sitzung.ipynb`: Downloads all submissions
* `1_additional_data.ipynb`: Loads all cantonal councils of the past using data from the state archives
* `2_extract.ipynb`: Searches PDFs and tries to extract spoken word
* `3_clean.ipynb`: Cleans the extracted word logs and adds information about the person speaking
* `4_analyse_base.ipynb`: QQuantitative analyses of **speeches** ("Voten")
* `5_text_analysis.ipynb`: Text analysesof **speeches** ("Voten")
* `6_geschaefte_analyse.ipynb`: Analysis of the submitted proposals

## Cleaned data you might need:
* `export/votum/votum_*.csv`: Prepared spoken votes with metadata about the person speaking
* `export/geschaefte.csv`: Prepared data on submitted transactions and originators
* `export/tags/tag_*.json`: Tagged votes (parts of speech)
* `export/nouns/nouns_*.csv`: Only nouns

### Data description
**export/votum/votum_*.csv**
|property|type|description|
|---|---|---|
|`name`|str|Name of politician. Already normalized|
|`vorname`|str|First name of politician. Already normalized|
|`text`|str|Speech|
|`page`|int|Page Number in protocol|
|`f`|string|Path to protocol|
|`sitzung_name`|string|Name of debate (from XML-API)|
|`sitzung_date`|date|Date of debate (from XML-API)|
|`sitzung_start`|datetime|Start of debate (from XML-API). When there are more than one debates per day, a time is given|
|`sitzung_gremium`|string|Alway `KR`|
|`dokument_titel`|string|Title of the document (from XML-API)|
|`partei`|string|Party of politician at given time (can vary over time)|
|`geschlecht`|string|Gender|
|`jahrgang`|int|Year born|
|`funktion`|enum|Function: `Präsidium`, `1. Vizepräsidium`, `2. Vizepräsidium` or *NULL* |
|`ismember`|bool|Speaker is member of the parliament. For example: Member of the government speak at a debate but are not a member of the parliament. Be aware, there are members which were first a member of parliament and later in the gouvernment. `ismember` looks at the state at the day of speech|

**export/geschaefte.csv**
|property|type|description|
|---|---|---|
|`krnr`|str|Name of submission|
|`vorlagenr`|str|Another number, often empty. Do not use it|
|`titel`|str|Title of submission|
|`geschaeftsart`|enum|Type of submission. One of these: `Diverses`, `Vorlage`, `Postulat`, `Dringliches Postulat`, `Wahl`, `Einzelinitiative`, `Interpellation`, `Geschäftsbericht`, `Anfrage`, `Dringliche Anfrage`, `Parlamentarische Initiative`, `Motion`, `Leistungsmotion`, `Behördeninitiative`, `Tätigkeitsbericht`, `Bericht`, `Rechenschaftsbericht`, `Eintritt KR`, `Dringliche Interpellation`, `Finanzmotion` or  *nan*|
|`behandelndekommission`|str|Committee|
|`behandelndekommissionkurzname`|str|Committee short|
|`direktion`|str|Directorate|
|`direktionKurzname`|str|Directorate short|
|`start`|date|When submitted|
|`end`|date|When submitted end. Do not use it|
|`eingereicht`|date|Another date|
|`zusammenfassung`|str|Summary|
|`status`|enum|State. One of these: `Erledigt`, `Kantonsrat`, `Kommission`, `Regierungsrat`, `Kommission für soziale Sicherheit und Gesundheit`, `Geschäftsleitung KR`, `Fremdbenutzer`, `Kantonsrat Zugriff`|
|`erstunterzeichnervorname`|str|First signee first name|
|`erstunterzeichnername`|str|First signee last name|
|`erstunterzeichneristkantonsrat`|bool|First signee is member of parliament|
|`erstunterzeichnerpartei`|str|First signee party|
|`letzterschrittstart`|date|Last time state changed|
|`letzterschritttyp`|enum|Last state. One of many like `Zustimmung`, `Ablehnung`, ...|
|`letzterschritttext`|str|Last state text|
|`_name`|str|Concated name|
|`geschlecht`|str|Gender|
|`jahrgang`|int|Year born|

**export/tags/tag_*.json**
All votes already tagged (is it a noun, verb, etc.)
JSON-Array with same as in *export/votum/votum_*.csv*. Used HanTa for tagging.


## Text export: How it works, what is reliable, what not
The protocols are written by hand. Although they are all based on the same template, deviations may occur. A new speech is introduced in each case with the name of the speaker in italics. The export looks for italic text beginnings that make sense in context.  

The protocols usually start with the rules of procedure. There, the Council President speaks, but the formatting is often different than later in the proceedings. Since the focus was on the debate, these rules of procedure were usually not exported correctly. For furthertext analyses, it is therefore recommended to remove the votes of the acting Council President.



## Kontakt:
simon.huwiler@nzz.ch