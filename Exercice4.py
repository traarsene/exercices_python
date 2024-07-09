panier = []

while True:
    print("\nChoisissez parmi les 5 options suivantes:")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles")
    print("4- Vider le panier")
    print("5- Quitter")

    choix = input("Quel est votre choix? ")

    if choix == "1":
        nom_article = input("Entrez le nom de l'article : ")
        prix = float(input("Entrez le prix de l'article : "))
        article = {"name": nom_article, "price": prix}
        panier.append(article)
        print(f"L'article {nom_article} a été ajouté au panier.")

    elif choix == "2":
        nom_article_a_supprimer = input("Entrez le nom de l'article à supprimer : ")
        article_trouve = False
        for article in panier:
            if article["name"] == nom_article_a_supprimer:
                panier.remove(article)
                article_trouve = True
                print(f"L'article {nom_article_a_supprimer} a été supprimé du panier.")
                break
        if not article_trouve:
            print(f"Aucun article avec le nom {nom_article_a_supprimer} n'a été trouvé.")

    elif choix == "3":
        if panier:
            print("\nListe des articles :")
            for article in panier:
                print(f"- {article['name']}: {article['price']}")
        else:
            print("Le panier est vide.")

    elif choix == "4":
        panier.clear()
        print("Le panier a été vidé.")

    elif choix == "5":
        print("Fin du programme.")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")
