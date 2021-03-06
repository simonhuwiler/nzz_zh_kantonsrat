from dateutil import parser
import pandas as pd
import numpy as np

def kantonsrat_to_datetime(kantonsrat):
    for k in kantonsrat:
        for x in k['einsitz']:
            x['start'] = parser.parse(x['start'])
            x['end'] = parser.parse(x['end'])
        for x in k['partei']:
            x['start'] = parser.parse(x['start'])
            x['end'] = parser.parse(x['end'])
        for x in k['funktion']:
            x['start'] = parser.parse(x['start'])
            x['end'] = parser.parse(x['end'])
            
def filter_kantonsrat_by_date(kantonsrat, dt):
    return list(filter(lambda x: len(list(filter(lambda e: (e['start'] <= dt) and (e['end'] >= dt), x['einsitz']))) > 0, kantonsrat))

def members_to_dataframe(members, filterlambda):
    records = []
    for r in members:

        # Get Party
        f = list(filter(filterlambda, r['partei']))
        party = ''
        if len(f) > 0:
            party = f[0]['bezeichnung']

        # Replace "CVP" with "Die Mitte"
        if party.lower() == 'cvp':
            party = 'Die Mitte'

        # Get Funktion
        f = list(filter(filterlambda, r['funktion']))
        funktion = np.nan
        if len(f) > 0:
            funktion = f[0]['bezeichnung']

        # Get Einsitz
        f = list(filter(filterlambda, r['einsitz']))
        einsitzstart = np.nan
        einsitzend = np.nan
        if len(f) > 0:
            einsitzstart = f[0]['start']
            einsitzend = f[0]['end']

        funktion = np.nan if funktion == 'Mitglied' else funktion

        records.append({
            'name': r['name'],
            'vorname': r['vorname'],
            'jahrgang': r['jahrgang'],
            'geschlecht': r['geschlecht'],
            'party': party,
            'funktion': funktion,
            'einsitzstart': einsitzstart,
            'einsitzend': einsitzend
        })

    return pd.DataFrame(records)

def kantonsrat_as_dataframe(kantonsrat, dt):
    members = filter_kantonsrat_by_date(kantonsrat, dt)
    return members_to_dataframe(members, lambda e: (e['start'] <= dt) and (e['end'] >= dt))

def kantonsrat_as_dataframe_from_to(kantonsrat, tStart, tEnd):
    def filter_from_to(e):
        return (
               ((e['end'] >= tStart) and (e['end'] <= tEnd))
            or ((e['start'] >= tStart) and (e['start'] <= tEnd))
            or ((e['start'] <= tStart) and (e['end'] >= tEnd))
        )

    members = list(filter(lambda x: len(list(filter(filter_from_to, x['einsitz']))) > 0, kantonsrat))
    return members_to_dataframe(members, filter_from_to)
    

aliases = [
    ['Stefanie Huber', 'Stefanie Elisabeth', 'Huber'],
    ['Yves De Mestral', 'Yves', 'de Mestral'],
    ['Theresia Weber-Gachnang', 'Theresia', 'Weber'],
    ['Theres Weber-Gachnang', 'Theresia', 'Weber'],
    ['Silvia Seiz', 'Silvia', 'Seiz-Gut'],
    ['Beno Scherrer Moser', 'Benno', 'Scherrer Moser'],
    ['Benno Scherer', 'Benno', 'Scherrer Moser'],
    ['Benno Scherrer', 'Benno', 'Scherrer Moser'],
    ['Beno Scherrer', 'Benno', 'Scherrer Moser'],
    ['Bruno Scherrer', 'Benno', 'Scherrer Moser'],
    ['Benno Scherr', 'Benno', 'Scherrer Moser'],
    ['Regula Kaeser', 'Regula', 'Kaeser-St??ckli'],
    ['Markus Sp??th', 'Markus', 'Sp??th-Walter'],
    ['Benjamin Schwarzenbach', 'Beni', 'Schwarzenbach'],
    ['Hans-Ueli Z??llig', 'Hansueli', 'Z??llig'],
    ['Karin Maeder', 'Karin', 'Maeder-Zuberb??hler'],
    ['Sabine Wettstein', 'Sabine', 'Wettstein-Studer'],
    ['Corinne Thomet', 'Corinne', 'Thomet-B??rki'],
    ['Martin Farner-Brandenberger', 'Martin', 'Farner'],
    ['Katharina Kull', 'Katharina', 'Kull-Benz'],
    ['Max Homberger', 'Max Robert' ,'Homberger'],
    ['Renate B??chi', 'Renate', 'B??chi-Wild'],
    ['Jakob Scheebeli', 'Jakob', 'Schneebeli'],
    ['Judith Stofer', 'Judith Anna', 'Stofer'],
    ['Anna Stofer', 'Judith Anna', 'Stofer'],
    ['Karin Egli', 'Karin', 'Egli-Zimmermann'],
    ['Heidi Bucher', 'Heidi', 'Bucher-Steinegger'],
    ['Heidi Steinegger', 'Heidi', 'Bucher-Steinegger'],
    ['Catherine Heuberger', 'Catherine', 'Heuberger Golta'],
    ['Ursula Moor', 'Ursula', 'Moor-Schwarz'],
    ['Jean-Philipp Pinto', 'Jean-Philippe', 'Pinto'],
    ['Ruth Frei', 'Ruth', 'Frei-Baumann'],
    ['Olivier Hofmann', 'Olivier Mo??se', 'Hofmann'],
    ['Hans Wiesner', 'Hans W.', 'Wiesner'],
    ['Philippe Kutter', 'Philipp', 'Kutter'],
    ['Sabine Sieber', 'Sabine', 'Sieber Hirschi'],
    ['Beatrix Frei', 'Beatrix' ,'Frey-Eigenmann'],
    ['Beatrix Frey', 'Beatrix' ,'Frey-Eigenmann'],
    ['Beatrice Frey', 'Beatrix' ,'Frey-Eigenmann'],
    ['Raphael Steiner', 'Rafael', 'Steiner'],
    ['Hansueli Vogt', 'Hans-Ueli', 'Vogt'],
    ['Sylvie Fee Matter', 'Sylvie', 'Matter'],
    ['C??cilia H??nni', 'C??cilia', 'H??nni-Etter'],
    ['C??cilia H??ni', 'C??cilia', 'H??nni-Etter'],
    ['Kaspar B??ttikofer', 'Kaspar', 'B??tikofer'],
    ['Sonja Rueff', 'Sonja', 'Rueff-Frenkel'],
    ['Silvie Matter', 'Sylvie', 'Matter'],
    ['Bettina Balmer', 'Bettina', 'Balmer-Schiltknecht'],
    ['Claudia Frei-Wyssen', 'Claudia', 'Wyssen'],
    ['Barbara Franzen', 'Ann Barbara', 'Franzen'],
    ['Birgit Tognella', 'Birgit', 'Tognella-Geertsen'],
    ['Mich??le D??nki', 'Mich??le', 'D??nki-B??ttig'],
    ['Michelle B??ttig', 'Mich??le', 'B??ttig'],
    ['Markus Schaff', 'Markus', 'Schaaf'],
    ['Mark Wisskirchen', 'Mark Anthony', 'Wisskirchen'],
    ['Priska Koller', 'Prisca', 'Koller'],
    ['Hans-Heinrich Raths', 'Hans Heinrich', 'Raths'],
    ['Rita Maria Marty', 'Maria Rita', 'Marty'],
    ['David Galeuchet', 'David John', 'Galeuchet'],
    ['Karin Thoma Fehr', 'Karin', 'Fehr Thoma'],
    ['Karin Fehr', 'Karin', 'Fehr Thoma'],
    ['Ester Meier', 'Esther', 'Meier'],
    ['Hans-Peter Hugentobler', 'Hanspeter', 'Hugentobler'],
    ['Katrin Cometta', 'Katrin', 'Cometta-M??ller'],
    ['Nicola Sigrist', 'Nicola', 'Siegrist'],
    ['Q??ndresa Sadriu', 'Q??ndresa (Q??ni)', 'Sadriu'],
    ['Q??ndresa Hoxha-Sadriu', 'Q??ndresa (Q??ni)', 'Sadriu'],
    ['Martin Neukomm', 'Martin', 'Neukom'],
    ['Theres Agosti', 'Theres', 'Agosti Monn'],
    ['These Agosti', 'Theres', 'Agosti Monn'],
    ['Theresia Agosti Monn', 'Theres', 'Agosti Monn'],
    ['Roland Alder', 'Ronald', 'Alder'],
    ['Beat Mohnhart', 'Beat', 'Monhart'],
    ['Marc Anthony Wisskirchen', 'Mark Anthony', 'Wisskirchen'],
    ['Ariane Moser', 'Arianne', 'Moser-Sch??fer'],
    ['Arianne Moser', 'Arianne', 'Moser-Sch??fer'],
    ['Beatrix Frey-Eigenmann', 'Beatrix', 'Frey'],
    ['Harry Brandenberger', 'Harry Robert', 'Brandenberger'],
    ['Gantner Alex', 'Alex', 'Gantner'],
    ['Cristina Cortellini', 'Cristina', 'Wyss-Cortellini'],
    ['Gehrig Sonja', 'Sonja', 'Gehrig Schmidt'],
    ['Sonja Gehrig', 'Sonja', 'Gehrig Schmidt'],
    ['Andreas Halser', 'Andreas', 'Hasler'],
    ['Jasmine Pokerschnig', 'Jasmin', 'Pokerschnig'],
    ['Anthony Wisskirchen', 'Mark Anthony', 'Wisskirchen'],
    ['Carola Etter', 'Carola', 'Etter-Gick'],
    ['Christan Schucan', 'Christian', 'Schucan'],
    ['J??rg K??ndig', 'J??rg', 'K??ndig'],
    ['Edith H??user', 'Edith', 'H??usler-Michel'],
    ['Edith H??usler', 'Edith', 'H??usler-Michel'],
    ['Edith H??ussler', 'Edith', 'H??usler-Michel'],
    ['Edit H??usler', 'Edith', 'H??usler-Michel'],
    ['Franziska Barmetter', 'Franziska', 'Barmettler'],
    ['Stepan Weber', 'Stephan', 'Weber'],
    ['Natalie Aeschbacher', 'Nathalie', 'Aeschbacher'],
    ['Fehr D??sel', 'Nina', 'Fehr D??sel'],
    ['Monica Muri Sanesi', 'Monica', 'Sanesi Muri'],
    ['Peter Brunner', 'Hans-Peter', 'Brunner'],
    ['Domenik Ledergeber', 'Domenik', 'Ledergerber'],
    ["Selma L???Orange Seigo", 'Selma', "L'Orange Seigo"],
    ['Markus Schaaf Markus', 'Markus', 'Schaaf'],
    ['Marc Bourgeoise', 'Marc', 'Bourgeois'],
    ['Silva Rigoni', 'Silvia', 'Rigoni'],
    ['Jeanette B??sser', 'Jeannette', 'B??sser'],
    ['Anne-Claude Hensch-Frei', 'Anne-Claude', 'Hensch Frei'],
    ['Hanspeter Amrein', 'Hans-Peter', 'Amrein'],
    ['Hans Peter Amrein', 'Hans-Peter', 'Amrein'],
    ['Jean-Philippe Pinot', 'Jean-Philippe', 'Pinto'],
    ['Jean Philippe Pinot', 'Jean-Philippe', 'Pinto'],
    ['Jean Philipp Pinto', 'Jean-Philippe', 'Pinto'],
    ['Jean Philippe Pinto', 'Jean-Philippe', 'Pinto'],
    ['Jean-Pilippe Pinto', 'Jean-Philippe', 'Pinto'],
    ['Cyrill von Planta', 'Cyrill', 'Planta von'],
    ['Ursula Gut', 'Ursula', 'Gut-Winterberger'],
    ['Regine Aeppli', 'Regine','Aeppli Wartmann'],
    ['Maria Rohweder', 'Maria', 'Rohweder-Lischer'],
    ['Maria Lischer', 'Maria', 'Rohweder-Lischer'],
    ['Judith Bellaiche', 'Judith', 'Bella??che'],
    ['Yvonne B??rgin', 'Yvonne', 'B??rgin-Hartmann'],
    ['Yvonne B??rgi', 'Yvonne', 'B??rgin-Hartmann'],
    ['Rafael Golta', 'Raphael', 'Golta'],
    ['Gabi Petri', 'Gabriele', 'Petri'],
    ['Margrit Haller', 'Margrit', 'Haller-Traber'],
    ['Elisabeth Pflughshaupt', 'Elisabeth', 'Pflugshaupt'],
    ['Susanne Trost', 'Susanne', 'Trost Vetter'],
    ['Marionna Schlatter', 'Marionna', 'Schlatter-Schmid'],
    ['Christa St??nzi', 'Christa Isabelle', 'St??nzi'],
    ['Paul von Euw', 'Paul', 'Euw von'],
    ['Barbara G??nthard', 'Barbara', 'G??nthard Fitze'],
    ['Melissa N??f', 'Melissa', 'N??f-Doffey'],
    ['Nora Bussmann Bola??os', 'Nora', 'Bussmann Bula??os'],
    ['Nora Bussmann', 'Nora', 'Bussmann Bula??os'],
    ['Romaine Rogenmoser', 'Romaine', 'Roggenmoser'],
    ['Katrin Susanne Meier', 'Katrin', 'Meier'],
    ['Elisabeth Derisiotis', 'Elisabeth', 'Derisiotis-Scherrer'],
    ['Susanne Rihs', 'Susanne', 'Rihs-Lanz'],
    ['Rolf Zimmermann', 'Rolf Robert', 'Zimmermann'],
    ['Marlies Zaugg', 'Marlies', 'Zaugg-Br??llmann'],
    ['Rita Fuhrer', 'Rita', 'Fuhrer-Honegger'],
    ['Brigitta Leiser', 'Brigitta', 'Leiser-Burri'],
    ['Andrea von Planta', 'Andrea', 'Planta von'],
    ['Nicole Barandun', 'Nicole', 'Barandun-Gross'],
    ['Lisette M??ller', 'Lisette', 'M??ller-Jaag'],
    ['J??rg M??der', 'J??rg', 'M??der'],
    ['Maleica Monique Landolt', 'Maleica-Monique', 'Landolt'],
    ['Maleika Landolt', 'Maleica-Monique', 'Landolt'],
    ['Maleica Landolt', 'Maleica-Monique', 'Landolt'],
    ['Rolf Zimmermann', 'Rolf Robert', 'Zimmermann'],
    ['Ernst Stocker', 'Ernst', 'Stocker-Rusterholz'],
    ['Lucius R??egg', 'Luzius', 'R??egg'],
    ['Hans Heinrich Heusser', 'Hans-Heinrich', 'Heusser'],
    ['Moritz Spielmann', 'Moritz', 'Spillmann'],
    ['Andras Erdin', 'Andreas', 'Erdin'],
    ['Hans-Peter H??ring', 'Hans Peter', 'H??ring'],
    ['Hanspeter H??ring', 'Hans Peter', 'H??ring'],
    ['Hans-Heinreich Heusser', 'Hans-Heinrich', 'Heusser'],
    ['Hans Peter Portmann', 'Hans-Peter', 'Portmann'],
    ['Heinz Kyburg', 'Heinz', 'Kyburz'],
    ['Ruth Gurny Cassee', 'Ruth', 'Gurny'],
    ['Yvonne Eugster-Wick', 'Yvonne', 'Eugster'],
    ['Regula Thalmann', 'Regula', 'Thalmann-Meyer'],
    ['Ruedi Jeker', 'Rudolf', 'Jeker'],
    ['Brigitta Johner-G??hwiler', 'Brigitta', 'Johner'],
    ['Brigitte Johner', 'Brigitta', 'Johner'],
    ['Hany Urs', 'Urs', 'Hany'],
    ['Manser Emil', 'Emil', 'Manser'],
    ['Rita Bernoulli-Sch??rmann', 'Rita', 'Bernoulli'],
    ['Johann Jucker', 'Johann', 'Jucker-Inhelder'],
    ['Luzi R??egg', 'Luzius', 'R??egg'],
    ['Esther Guyer-Vogelsang', 'Esther', 'Guyer'],
    ['Lisette M??ller- Jaag', 'Lisette', 'M??ller-Jaag'],
    ['Hans-Peter Amstutz', 'Hanspeter', 'Amstutz'],
    ['Nancy Bolleter', 'Nancy', 'Bolleter-Malcom'],
    ['Rolf Andr?? Siegenthaler-Benz', 'Rolf Andr??', 'Siegenthaler'],
    ['Rolf Siegenthaler', 'Rolf Andr??', 'Siegenthaler'],
    ['Susanna Rusca-Speck', 'Susanna', 'Rusca Speck'],
    ['Susanna Rusca', 'Susanna', 'Rusca Speck'],
    ['Susanne Rusca', 'Susanna', 'Rusca Speck'],
    ['Lilith H??bscher', 'Lilith Claudia', 'H??bscher'],
    ['Lilith C. H??bscher', 'Lilith Claudia', 'H??bscher'],
    ['Marianne Tr??b Klinger', 'Marianne', 'Tr??b Klingler'],
    ['Marianne Tr??b-Klingler', 'Marianne', 'Tr??b Klingler'],
    ['Natalie Vieli', 'Natalie', 'Vieli-Platzer'],
    ['Nathalie Vieli-Platzer', 'Natalie', 'Vieli-Platzer'],
    ['Rosmarie Frehsner-Aebersold', 'Rosmarie', 'Frehsner'],
    ['Regula G??tsch', 'Regula', 'G??tsch Neukom'],
    ['Julia Gerber', 'Julia', 'Gerber R??egg'],
    ['Katharina Prelicz', 'Katharina', 'Prelicz-Huber'],
    ['Anita Simioni', 'Anita', 'Simioni-Dahm'],
    ['Inge Stutz', 'Inge', 'Stutz-Wanner'],
    ['Priska Seiler', 'Priska', 'Seiler Graf'],
    ['Carmen Walker', 'Carmen', 'Walker Sp??h'],
    ['Natalie Rickli', 'Nathalie', 'Rickli'],
    ['Natali Rickli', 'Nathalie', 'Rickli'],
    ['Max Clerici', 'Max F.', 'Clerici'],
    ['Luca Roth', 'Luca Rosario', 'Roth'],
    ['Susanne Bernasconi', 'Susanne', 'Bernasconi-Aeppli'],
    ['Irene Minder', 'Irene', 'Minder-Roost'],
    ['Hans-L??ubli', 'Hans', 'L??ubli'],
    ['Sibylle Marty', 'Sibylle', 'Marti'],
    ['Sybille Marti', 'Sibylle', 'Marti'],
    ['Florian Herr', 'Florian', 'Heer'],
    ['Michale Welz', 'Michael', 'Welz'],
    ['Raffael Fehr', 'Raffaela', 'Fehr'],
    ['Ueli Pfister', 'Ulrich', 'Pfister'],
    ['Christioph Ziegler', 'Christoph', 'Ziegler'],
    ['Markus Bischof', 'Markus', 'Bischoff'],
    ['Andreas Dau??', 'Andreas', 'Daur??'],
    ['Barbara Steinmann', 'Barbara', 'Steinemann'],
    ['Stefan Feldman', 'Stefan', 'Feldmann'],
    ['Willy Handerer', 'Willy', 'Haderer'],
    ['Martin Geilingner', 'Martin', 'Geilinger'],
    ['Hans Maier', 'Hans', 'Meier'],
    ['Blanca Ramer', 'Blanca', 'Ramer-St??ubli'],
    ['Elisabeth Scheffeldt', 'Elisabeth', 'Scheffeldt Kern'],
    ['Christina Zurfluh Fr??fel', 'Christina', 'Zurfluh Fraefel'],
    ['Hans-Egli', 'Hans', 'Egli'],
    ['Jaqueline Hofer', 'Jacqueline', 'Hofer'],
    ['Regula Sauter', 'Regine', 'Sauter'],
    ['Heidi Bucher-Steinmann', 'Heidi', 'Bucher-Steinegger'],
    ['Ursula Braunschweig', 'Ursula', 'Braunschweig-L??tolf'],
    ['Pia Hollenstein Weidmann', 'Pia', 'Holenstein Weidmann']
]

stopwords = ['Kanton', 'Jahr', 'Z??rich', 'Postulat', 'Gemeinde', 'Antrag', 'Prozent', 'Gesetz', 'Vorlage', 'Kommission', 'Kantonsrat', 'Staat', 'Beispiel', 'Frage', 'Massnahmen', 'Schweiz', 'Dank',
             'Vorstoss', 'Parlament', 'Gesch??ft', 'Politik', 'Kollege', 'Debatte', 'Gegenvorschlag']
stopwords_lower = [s.lower() for s in stopwords]