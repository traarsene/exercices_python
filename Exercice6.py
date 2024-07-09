class Client:
    def __init__(self, code, nom, telephone, adresse, email):
        self.code = code
        self.nom = nom
        self.telephone = telephone
        self.adresse = adresse
        self.email = email
        self.solde = 0  # Initialiser le solde à zéro

class Transaction:
    def __init__(self, ref_paiement, code_emmeteur, code_recepteur, date_transaction, montant, canal):
        self.ref_paiement = ref_paiement
        self.code_emmeteur = code_emmeteur
        self.code_recepteur = code_recepteur
        self.date_transaction = date_transaction
        self.montant = montant
        self.canal = canal

# Créer des listes pour les clients et les transactions
customers = []
transactions = []

def afficher_clients():
    for client in customers:
        print(f"Code: {client.code}, Nom: {client.nom}, Solde: {client.solde}")

def ajouter_client():
    code = input("Entrez le code du client : ")
    nom = input("Entrez le nom du client : ")
    telephone = input("Entrez le numéro de téléphone : ")
    adresse = input("Entrez l'adresse : ")
    email = input("Entrez l'adresse e-mail : ")
    customers.append(Client(code, nom, telephone, adresse, email))
    print("Le client a été ajouté.")

def supprimer_client(code):
    for client in customers:
        if client.code == code:
            customers.remove(client)
            print(f"Le client avec le code {code} a été supprimé.")
            return
    print(f"Le client avec le code {code} n'existe pas.")

def modifier_client(code):
    for client in customers:
        if client.code == code:
            client.nom = input("Nouveau nom : ")
            client.telephone = input("Nouveau téléphone : ")
            client.adresse = input("Nouvelle adresse : ")
            client.email = input("Nouvel email : ")
            print(f"Les informations du client avec le code {code} ont été mises à jour.")
            return
    print(f"Le client avec le code {code} n'existe pas.")

def afficher_solde(code):
    for client in customers:
        if client.code == code:
            print(f"Solde du client {client.nom} ({client.code}) : {client.solde}")
            return
    print(f"Le client avec le code {code} n'existe pas.")

def ajouter_transaction():
    ref_paiement = input("Référence de paiement : ")
    code_emmeteur = input("Code de l'émetteur : ")
    code_recepteur = input("Code du récepteur : ")
    date_transaction = input("Date de la transaction : ")
    montant = float(input("Montant : "))
    canal = input("Canal (ORANGE MONEY, WAVE, FREE MONEY, VIREMENT BANCAIRE) : ")
    transactions.append(Transaction(ref_paiement, code_emmeteur, code_recepteur, date_transaction, montant, canal))
    print("La transaction a été ajoutée.")

def mettre_a_jour_solde(code, montant):
    for client in customers:
        if client.code == code:
            client.solde += montant
            print(f"Solde du client {client.nom} ({client.code}) mis à jour.")
            return
    print(f"Le client avec le code {code} n'existe pas.")

while True:
    print("\nMenu :")
    print("1 - Gestion des clients")
    print("2 - Gestion des transactions")
    print("3 - Sortir")
    choix = input("Choisissez une option : ")

    if choix == "1":
        print("\n1 - Afficher la liste des clients")
        print("2 - Ajouter un client")
        print("3 - Supprimer un client")
        print("4 - Modifier les informations d'un client")
        print("5 - Afficher le solde d'un client")
        option = input("Choisissez une option : ")

        if option == "1":
            afficher_clients()
        elif option == "2":
            ajouter_client()
        elif option == "3":
            code_client = input("Entrez le code du client à supprimer : ")
            supprimer_client(code_client)
        elif option == "4":
             code_client = input("Entrez le code du client à modifier : ")
             modifier_client(code_client)
        elif option == "5":
            code_client = input("Entrez le code du client dont vous souhaitez afficher le solde : ")
            afficher_solde(code_client)
        else:
            print("Option invalide. Veuillez choisir à nouveau.")

    elif choix == "2":
            print("\n1 - Afficher toutes les transactions")
            print("2 - Afficher les transactions d'un client")
            print("3 - Ajouter une transaction entre deux clients")
            print("4 - Modifier le solde d'un client")
            option = input("Choisissez une option : ")

            if option == "1":
                # Afficher toutes les transactions
                for transaction in transactions:
                    print(f"Référence de paiement : {transaction.ref_paiement}, Montant : {transaction.montant}, Canal : {transaction.canal}")
            elif option == "2":
                code_client = input("Entrez le code du client pour afficher ses transactions : ")
                # Afficher les transactions du client
                for transaction in transactions:
                    if transaction.code_emmeteur == code_client or transaction.code_recepteur == code_client:
                        print(f"Référence de paiement : {transaction.ref_paiement}, Montant : {transaction.montant}, Canal : {transaction.canal}")
            elif option == "3":
                ajouter_transaction()
            elif option == "4":
                code_client = input("Entrez le code du client pour mettre à jour son solde : ")
                montant = float(input("Entrez le montant de la transaction : "))
                mettre_a_jour_solde(code_client, montant)
            else:
                print("Option invalide. Veuillez choisir à nouveau.")

    elif choix == "3":
        print("Merci d'avoir utilisé notre application !")
        break
    else:
        print("Option invalide. Veuillez choisir à nouveau.")
