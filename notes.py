import csv, os.path

def init_data():
    data = list()
    classe = None
    while "premiere" != classe != "terminale":
        classe = input("En quelle classe êtes vous ? (premiere/terminale)")
    coef_manuels = None
    if classe == "premiere":
        spés= {
            "spé1": input("Quelle est votre spécialitée 1"),
            "spé2": input("Quelle est votre spécialitée 2"),
            "spé3": input("Quelle est votre spécialitée 3"),
        }
        spé_abandonnée = None
        while spé_abandonnée != spés["spé1"] and spé_abandonnée != spés["spé3"] and spé_abandonnée != spés["spé3"]:
            spé_abandonnée = input("Quelle spécialitée abandonnez vous à la fin de l'année ?")
    else:
        data= [
            {"Matière":"Histoire-géographie", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
            {"Matière":"", "coefficient":},
        ]
def csv2table(nom):
    with open(nom, 'r', encoding="utf-8") as fichier:
        return list(csv.DictReader(fichier, delimiter=','))

def table2csv(table, nom):
    with open(nom, 'w', encoding="utf-8") as fichier:
        w = csv.DictWriter(fichier, fieldnames=list(table[0].keys()), delimiter=',', lineterminator="\n")
        w.writeheader()
        for element in table:
            w.writerow(element)

if not os.path.exists('ddata.csv'):
    init_data()



data = csv2table("data.csv")
