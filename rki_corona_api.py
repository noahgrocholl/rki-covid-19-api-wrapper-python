import requests
import json
import csv


# Mögliche Rückgabewerte
# "AdmUnitId" \
# "BundeslandId" \
# "AnzFall" \
# "AnzTodesfall" \
# "AnzFallNeu" \
# "AnzTodesfallNeu" \
# "AnzFall7T" \
# "AnzGenesen" \
# "AnzGenesenNeu" \
# "AnzAktiv" \
# "AnzAktivNeu" \
# "Inz7T" \
# "ObjectId"


class Rki:

    url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/rki_key_data_v/FeatureServer/0/query?"
    lk_id = 0
    lk_name = ""
    resultjson = ""
    list_results = []

    # lk_id kann hier auch None sein
    def __init__(self, lk_id=None):

        # ermöglicht das lk_id None sein kann
        if lk_id is None:
            return

        # sucht in csv nach lk_id -> Existenz bestätigen, lk_name finden
        test_for_lk_id = False
        csv_file = csv.reader(open('content/Liste LKs.csv', "r"), delimiter=";")
        for row in csv_file:
            if row[0] == str(lk_id):
                self.lk_id = lk_id
                self.lk_name = row[1]
                test_for_lk_id = True
                break

        if test_for_lk_id is False:
            raise ValueError("Id does not exist")

    # der Funktion werden eine beliebege Anzahl an Attributen übergeben
    def get_target_results(self, *kwargs):
        output = []
        parameter = {
            'referer': 'https://www.mywebapp.com',
            'user-agent': 'python-requests/2.9.1',
            'where': f'AdmUnitId = {self.lk_id}',  # Welcher Landkreis/Gebiet sollen zurück gegeben werden
            'outFields': '*',  # Rückgabe aller Felder
            'returnGeometry': False,  # Keine Geometrien
            'f': 'json',  # Rückgabeformat, hier JSON
            'cacheHint': True  # Zugriff über CDN anfragen
        }
        result = requests.get(url=self.url, params=parameter)  # Anfrage absetzen
        self.resultjson = json.loads(result.text)

        # fügt Ergebnis der json Anfrage einzeln zur list_results Liste hinzu
        for result_target in kwargs:
            self.list_results.append(self.resultjson['features'][0]['attributes'][result_target])

        if len(self.list_results) == 1:
            output = float(self.list_results[0])

        else:
            output = self.list_results

        return output

    def change_target_id_by_name_csv(self, lk_name):
        test_for_lk_id = False

        # durchsucht csv nach id für Namen
        file = open('content/Liste LKs.csv', "r")
        csv_read = csv.reader(file, delimiter=";")
        for row in csv_read:
            if row[1].lower() == lk_name.lower():
                lk_id = row[0]
                file.close()
                self.lk_id = lk_id
                self.lk_name = row[1]
                test_for_lk_id = True
                return lk_id

        if test_for_lk_id is False:
            return f"No Id was found with given lk_name: {lk_name}"
