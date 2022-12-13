class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        return "{jmeno}\t{prijmeni}\t{vek}\t{tel_cislo}".format(jmeno=self.jmeno, prijmeni=self.prijmeni, vek=self.vek, tel_cislo=self.tel_cislo)
    
# class Evidence:
#     def __init__(self) -> None:
#         pass
#     def pridat(self):
#         jmeno = input("Zadejte jméno:\n")
#         prijmeni = input("Zadejte příjmení:\n")
#         vek = input("Zadejte věk:\n")
#         tel_cislo = input("Zadejte telefonní číslo:\n")
#         Pojistenec(jmeno, prijmeni, vek, tel_cislo)

status = True
users = {} # změnit na dictionary kvůli vyhledávání

while status == True:
    print(
    """
    Zvolte akci:
    1 - Přidat pojištěnce.
    2 - Zobrazit všechny uložené pojištěnce.
    3 - Vyhledat pojištěnce.
    4 - Konec
    """)
    akce = int(input()) # použít matchcase
    if akce == 1:
        jmeno = input("Zadejte jméno:\n")
        prijmeni = input("Zadejte příjmení:\n")
        vek = input("Zadejte věk:\n")
        tel_cislo = input("Zadejte telefonní číslo:\n")
        users[prijmeni] = Pojistenec(jmeno, prijmeni, vek, tel_cislo)
    if akce == 2:
        print(users.values())
    if akce == 3:
        prijmeni = input("Zadejte příjmení:\n")
        print(users.get(prijmeni))
    if akce == 4:
        status = False