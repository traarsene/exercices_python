try:
    note = float(input("Entrez votre note : "))

    if note >= 18:
        mention = "Excellent"
    elif note >= 16:
        mention = "Très bien"
    elif note >= 14:
        mention = "Bien"
    elif note >= 12:
        mention = "Satisfaisant"
    elif note >= 10:
        mention = "Passable"
    else:
        mention = "Échec"

    print(f"Votre note est {note} et votre mention est {mention}.")
except ValueError:
    print("Veuillez entrer un nombre valide.")
    note = float(input("Entrez votre note : "))  # Demandez à nouveau la note
    