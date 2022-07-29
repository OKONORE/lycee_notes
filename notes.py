import csv, os.path

def csv2table(chemin):
    with open(chemin, 'r', encoding="utf-8") as fichier:
        return list(csv.DictReader(fichier, delimiter=';'))

def table2csv(table, chemin):
    with open(chemin, 'w', encoding="utf-8") as fichier:
        w = csv.DictWriter(fichier, fieldnames=list(table[0].keys()), delimiter=';', lineterminator="\n")
        w.writeheader()
        for element in table:
            w.writerow(element)

def test_dans_dict(valeur, dico, dict_key):
    for valeur_test in dico:
        if valeur == valeur_test[dict_key]:
            return True
    return False

def init_data():
    classe = None
    while "première" != classe != "terminale":
        classe = input("En quelle classe êtes vous ? (première/terminale)")  

    if not os.path.exists("data/1ere.csv") and classe == "première":
        build_data_1ere(temp_data_1ere())
    elif not os.path.exists("data/term.csv") and classe == "terminale":
        build_data_term(temp_data_term())

def temp_data_term():
    x = 1

def temp_data_1ere():
    temp_data_1ere = dict()
    temp_data_1ere["classe"] = "première"
      
    temp_data_1ere["filière"] = None
    while "générale" != temp_data_1ere["filière"] != "technologique":
        temp_data_1ere["filière"] = input("En quelle fillière êtes vous ? (générale/technologique)")    
    temp_data_1ere["année"] = 1
    while 2022 <= temp_data_1ere["année"] <= 2023:
        temp_data_1ere["année"] = input("En quelle classe êtes vous ? (entre 2022 et 2023)")  

    temp_data_1ere["spés"]= [
        {"nom": input("Quelle est votre spécialitée 1"), "abandonnée":False},
        {"nom": input("Quelle est votre spécialitée 2"), "abandonnée":False},
        {"nom": input("Quelle est votre spécialitée 3"), "abandonnée":False},
    ] 
    temp_data_1ere["spé_abandonnée"] = 1
    while not test_dans_dict(temp_data_1ere["spé_abandonnée"], temp_data_1ere["spés"], "nom"):
        temp_data_1ere["spé_abandonnée"] = input("Quelle spécialitée abandonnez vous à la fin de l'année ?")
    
    for id_spés in range(len(temp_data_1ere["spés"])):
        if temp_data_1ere["spés"][id_spés]["nom"] == temp_data_1ere["spé_abandonnée"]:
            temp_data_1ere["spés"][id_spés]["abandonnée"] = True
    del temp_data_1ere["spé_abandonnée"]

    return temp_data_1ere

def build_data_1ere(temp_data):
    data_1ere = []
    for spé in temp_data["spés"]:
        if spé["abandonnée"] == True:
            data_1ere.append({"Matière":spé["nom"], "type":"Spécialitée abandonnée", "coefficient":80,})
        else:
            data_1ere.append({"Matière":spé["nom"], "type":"Spécialitée", "coefficient":00,},)
    
    table2csv(data_1ere, "data/1ere")


def build_data_term(temp_data):
    x = 1

if not (os.path.exists('data/1ere.csv') or os.path.exists("data/term.csv")):
    init_data()



#data = csv2table("data.csv")
