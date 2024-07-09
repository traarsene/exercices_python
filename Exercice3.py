def main():
    try:
        # Demande à l'utilisateur d'entrer un nombre
        nombre = int(input("Entrez un nombre entier : "))
        
        # Vérifie que le nombre est positif
        if nombre <= 0:
            print("Veuillez entrer un nombre positif.")
            return
        
        # Utilisation d'une boucle for pour afficher les entiers de 1 à nombre
        print("Nombres entiers entre 1 et", nombre, ":")
        for i in range(1, nombre + 1):
            print(i)
        
        # Utilisation d'une boucle while pour afficher les entiers de 1 à nombre
        print("\nNombres entiers (version while) entre 1 et", nombre, ":")
        i = 1
        while i <= nombre:
            print(i)
            i += 1
    except ValueError:
        print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
