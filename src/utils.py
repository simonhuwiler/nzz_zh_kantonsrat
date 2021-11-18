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

def kantonsrat_as_dataframe(kantonsrat, dt):
    members = filter_kantonsrat_by_date(kantonsrat, dt)
    records = []
    for r in members:

        # Get Party
        f = list(filter(lambda e: (e['start'] <= dt) and (e['end'] >= dt), r['partei']))
        party = ''
        if len(f) > 0:
            party = f[0]['bezeichnung']

        # Get Funktion
        f = list(filter(lambda e: (e['start'] <= dt) and (e['end'] >= dt), r['funktion']))
        funktion = np.nan
        if len(f) > 0:
            funktion = f[0]['bezeichnung']  

        funktion = np.nan if funktion == 'Mitglied' else funktion  

        records.append({
            'name': r['name'],
            'vorname': r['vorname'],
            'jahrgang': r['jahrgang'],
            'geschlecht': r['geschlecht'],
            'party': party,
            'funktion': funktion
        })

    return pd.DataFrame(records)    

aliases = [
    ['Theresia Weber-Gachnang', 'Theresia', 'Weber'],
    ['Silvia Seiz', 'Silvia', 'Seiz-Gut'],
    ['Beno Scherrer Moser', 'Benno', 'Scherrer Moser'],
    ['Benno Scherer', 'Benno', 'Scherrer Moser'],
    ['Benno Scherrer', 'Benno', 'Scherrer Moser'],    
    ['Regula Kaeser', 'Regula', 'Kaeser-Stöckli'],
    ['Markus Späth', 'Markus', 'Späth-Walter'],
    ['Benjamin Schwarzenbach', 'Beni', 'Schwarzenbach'],
    ['Hans-Ueli Züllig', 'Hansueli', 'Züllig'],
    ['Karin Maeder', 'Karin', 'Maeder-Zuberbühler'],
    ['Sabine Wettstein', 'Sabine', 'Wettstein-Studer'],
    ['Corinne Thomet', 'Corinne', 'Thomet-Bürki'],
    ['Martin Farner-Brandenberger', 'Martin', 'Farner'],
    ['Katharina Kull', 'Katharina', 'Kull-Benz'],
    ['Max Homberger', 'Max Robert' ,'Homberger'],
    ['Renate Büchi', 'Renate', 'Büchi-Wild'],
    ['Jakob Scheebeli', 'Jakob', 'Schneebeli'],
    ['Judith Stofer', 'Judith Anna', 'Stofer'],
    ['Anna Stofer', 'Judith Anna', 'Stofer'],
    ['Karin Egli', 'Karin', 'Egli-Zimmermann'],
    ['Heidi Bucher', 'Heidi', 'Bucher-Steinegger'],
    ['Catherine Heuberger', 'Catherine', 'Heuberger Golta'],
    ['Ursula Moor', 'Ursula', 'Moor-Schwarz'],
    ['Jean-Philipp Pinto', 'Jean-Philippe', 'Pinto'],
    ['Ruth Frei', 'Ruth', 'Frei-Baumann'],
    ['Olivier Hofmann', 'Olivier Moïse', 'Hofmann'],
    ['Hans Wiesner', 'Hans W.', 'Wiesner'],
    ['Philippe Kutter', 'Philipp', 'Kutter'],
    ['Sabine Sieber', 'Sabine', 'Sieber Hirschi'],
    ['Beatrix Frei', 'Beatrix' ,'Frey-Eigenmann'],
    ['Beatrix Frey', 'Beatrix' ,'Frey-Eigenmann'],
    ['Beatrice Frey', 'Beatrix' ,'Frey-Eigenmann'],
    ['Raphael Steiner', 'Rafael', 'Steiner'],
    ['Hansueli Vogt', 'Hans-Ueli', 'Vogt'],
    ['Sylvie Fee Matter', 'Sylvie', 'Matter'],
    ['Cäcilia Hänni', 'Cäcilia', 'Hänni-Etter'],
    ['Kaspar Büttikofer', 'Kaspar', 'Bütikofer'],
    ['Sonja Rueff', 'Sonja', 'Rueff-Frenkel'],
    ['Silvie Matter', 'Sylvie', 'Matter'],
    ['Bettina Balmer', 'Bettina', 'Balmer-Schiltknecht'],
    ['Claudia Frei-Wyssen', 'Claudia', 'Wyssen'],
    ['Barbara Franzen', 'Ann Barbara', 'Franzen'],
    ['Birgit Tognella', 'Birgit', 'Tognella-Geertsen'],
    ['Michèle Dünki', 'Michèle', 'Dünki-Bättig'],
    ['Michelle Bättig', 'Michèle', 'Bättig'],
    ['Markus Schaff', 'Markus', 'Schaaf'],
    ['Mark Wisskirchen', 'Mark Anthony', 'Wisskirchen'],
    ['Priska Koller', 'Prisca', 'Koller'],
    ['Hans-Heinrich Raths', 'Hans Heinrich', 'Raths'],
    ['Rita Maria Marty', 'Maria Rita', 'Marty'],
    ['David Galeuchet', 'David John', 'Galeuchet'],
    ['Karin Thoma Fehr', 'Karin', 'Fehr Thoma'],
    ['Ester Meier', 'Esther', 'Meier'],
    ['Hans-Peter Hugentobler', 'Hanspeter', 'Hugentobler'],
    ['Katrin Cometta', 'Katrin', 'Cometta-Müller'],
    ['Nicola Sigrist', 'Nicola', 'Siegrist'],
    ['Qëndresa Sadriu', 'Qëndresa (Qëni)', 'Sadriu'],
    ['Martin Neukomm', 'Martin', 'Neukom'],
    ['Theres Agosti', 'Theres', 'Agosti Monn'],
    ['These Agosti', 'Theres', 'Agosti Monn'],
    ['Roland Alder', 'Ronald', 'Alder'],
    ['Beat Mohnhart', 'Beat', 'Monhart'],
    ['Marc Anthony Wisskirchen', 'Mark Anthony', 'Wisskirchen'],
    ['Ariane Moser', 'Arianne', 'Moser-Schäfer'],
    ['Arianne Moser', 'Arianne', 'Moser-Schäfer'],
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
    ['Jürg Kündig', 'Jörg', 'Kündig'],
    ['Edith Häuser', 'Edith', 'Häusler-Michel'],
    ['Edith Häusler', 'Edith', 'Häusler-Michel'],
    ['Edit Häusler', 'Edith', 'Häusler-Michel'],
    ['Franziska Barmetter', 'Franziska', 'Barmettler'],
    ['Stepan Weber', 'Stephan', 'Weber'],
    ['Natalie Aeschbacher', 'Nathalie', 'Aeschbacher'],
    ['Fehr Düsel', 'Nina', 'Fehr Düsel'],
    ['Monica Muri Sanesi', 'Monica', 'Sanesi Muri'],
    ['Peter Brunner', 'Hans-Peter', 'Brunner'],
    ['Domenik Ledergeber', 'Domenik', 'Ledergerber'],
    ["Selma L’Orange Seigo", 'Selma', "L'Orange Seigo"],
    ['Markus Schaaf Markus', 'Markus', 'Schaaf'],
    ['Marc Bourgeoise', 'Marc', 'Bourgeois'],
    ['Silva Rigoni', 'Silvia', 'Rigoni'],
    ['Jeanette Büsser', 'Jeannette', 'Büsser'],
    ['Anne-Claude Hensch-Frei', 'Anne-Claude', 'Hensch Frei'],
    ['Hanspeter Amrein', 'Hans-Peter', 'Amrein'],
    ['Hans Peter Amrein', 'Hans-Peter', 'Amrein'],
    ['Jean-Philippe Pinot', 'Jean-Philippe', 'Pinto'],
    ['Jean Philippe Pinot', 'Jean-Philippe', 'Pinto'],
    ['Jean Philipp Pinto', 'Jean-Philippe', 'Pinto'],
    ['Cyrill von Planta', 'Cyrill', 'Planta von'],
    ['Ursula Gut', 'Ursula', 'Gut-Winterberger'],
    ['Regine Aeppli', 'Regine','Aeppli Wartmann'],
    ['Maria Rohweder', 'Maria', 'Rohweder-Lischer'],
    ['Maria Lischer', 'Maria', 'Rohweder-Lischer'],
    ['Judith Bellaiche', 'Judith', 'Bellaïche'],
    ['Yvonne Bürgin', 'Yvonne', 'Bürgin-Hartmann'],
    ['Yvonne Bürgi', 'Yvonne', 'Bürgin-Hartmann'],
    ['Rafael Golta', 'Raphael', 'Golta'],
    ['Gabi Petri', 'Gabriele', 'Petri'],
    ['Margrit Haller', 'Margrit', 'Haller-Traber'],
    ['Elisabeth Pflughshaupt', 'Elisabeth', 'Pflugshaupt'],
    ['Susanne Trost', 'Susanne', 'Trost Vetter'],
    ['Marionna Schlatter', 'Marionna', 'Schlatter-Schmid'],
    ['Christa Stünzi', 'Christa Isabelle', 'Stünzi'],
    ['Paul von Euw', 'Paul', 'Euw von'],
    ['Barbara Günthard', 'Barbara', 'Günthard Fitze'],
    ['Melissa Näf', 'Melissa', 'Näf-Doffey'],
    ['Nora Bussmann Bolaños', 'Nora', 'Bussmann Bulaños'],
    ['Romaine Rogenmoser', 'Romaine', 'Roggenmoser'],
    ['Katrin Susanne Meier', 'Katrin', 'Meier'],
    ['Elisabeth Derisiotis', 'Elisabeth', 'Derisiotis-Scherrer'],
    ['Susanne Rihs', 'Susanne', 'Rihs-Lanz'],
    ['Rolf Zimmermann', 'Rolf Robert', 'Zimmermann'],
    ['Marlies Zaugg', 'Marlies', 'Zaugg-Brüllmann'],
    ['Rita Fuhrer', 'Rita', 'Fuhrer-Honegger'],
    ['Brigitta Leiser', 'Brigitta', 'Leiser-Burri'],
    ['Andrea von Planta', 'Andrea', 'Planta von'],
    ['Nicole Barandun', 'Nicole', 'Barandun-Gross'],
    ['Lisette Müller', 'Lisette', 'Müller-Jaag'],
    ['Jürg Mäder', 'Jörg', 'Mäder'],
    ['Maleica Monique Landolt', 'Maleica-Monique', 'Landolt'],
    ['Maleika Landolt', 'Maleica-Monique', 'Landolt'],
    ['Maleica Landolt', 'Maleica-Monique', 'Landolt'],
    ['Rolf Zimmermann', 'Rolf Robert', 'Zimmermann'],
    ['Ernst Stocker', 'Ernst', 'Stocker-Rusterholz'],
    ['Lucius Rüegg', 'Luzius', 'Rüegg'],
    ['Hans Heinrich Heusser', 'Hans-Heinrich', 'Heusser'],
    ['Moritz Spielmann', 'Moritz', 'Spillmann'],
    ['Andras Erdin', 'Andreas', 'Erdin'],
    ['Hans-Peter Häring', 'Hans Peter', 'Häring'],
    ['Hanspeter Häring', 'Hans Peter', 'Häring'],
    ['Hans-Heinreich Heusser', 'Hans-Heinrich', 'Heusser'],
    ['Hans Peter Portmann', 'Hans-Peter', 'Portmann'],
    ['Heinz Kyburg', 'Heinz', 'Kyburz'],
    ['Ruth Gurny Cassee', 'Ruth', 'Gurny'],
    ['Yvonne Eugster-Wick', 'Yvonne', 'Eugster'],
    ['Regula Thalmann', 'Regula', 'Thalmann-Meyer'],
    ['Ruedi Jeker', 'Rudolf', 'Jeker'],
    ['Brigitta Johner-Gähwiler', 'Brigitta', 'Johner'],
    ['Hany Urs', 'Urs', 'Hany'],
    ['Manser Emil', 'Emil', 'Manser'],
    ['Rita Bernoulli-Schürmann', 'Rita', 'Bernoulli'],
    ['Johann Jucker', 'Johann', 'Jucker-Inhelder'],
    ['Luzi Rüegg', 'Luzius', 'Rüegg'],
    ['Esther Guyer-Vogelsang', 'Esther', 'Guyer'],
    ['Lisette Müller- Jaag', 'Lisette', 'Müller-Jaag'],
    ['Hans-Peter Amstutz', 'Hanspeter', 'Amstutz'],
    ['Nancy Bolleter', 'Nancy', 'Bolleter-Malcom'],
    ['Rolf André Siegenthaler-Benz', 'Rolf André', 'Siegenthaler'],
    ['Rolf Siegenthaler', 'Rolf André', 'Siegenthaler'],
    ['Susanna Rusca-Speck', 'Susanna', 'Rusca Speck'],
    ['Susanna Rusca', 'Susanna', 'Rusca Speck'],
    ['Lilith Hübscher', 'Lilith Claudia', 'Hübscher'],
    ['Lilith C. Hübscher', 'Lilith Claudia', 'Hübscher'],
    ['Marianne Trüb Klinger', 'Marianne', 'Trüb Klingler'],
    ['Natalie Vieli', 'Natalie', 'Vieli-Platzer'],
    ['Nathalie Vieli-Platzer', 'Natalie', 'Vieli-Platzer'],
    ['Rosmarie Frehsner-Aebersold', 'Rosmarie', 'Frehsner'],
    ['Regula Götsch', 'Regula', 'Götsch Neukom'],
    ['Julia Gerber', 'Julia', 'Gerber Rüegg'],
    ['Katharina Prelicz', 'Katharina', 'Prelicz-Huber'],
    ['Anita Simioni', 'Anita', 'Simioni-Dahm'],
    ['Inge Stutz', 'Inge', 'Stutz-Wanner'],
    ['Priska Seiler', 'Priska', 'Seiler Graf'],
    ['Carmen Walker', 'Carmen', 'Walker Späh'],
    ['Natalie Rickli', 'Nathalie', 'Rickli'],
    ['Max Clerici', 'Max F.', 'Clerici'],
    ['Luca Roth', 'Luca Rosario', 'Roth'],
    ['Susanne Bernasconi', 'Susanne', 'Bernasconi-Aeppli'],
    ['Irene Minder', 'Irene', 'Minder-Roost'],
    ['Hans-Läubli', 'Hans', 'Läubli'],
]