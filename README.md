# Application pokémon django

## Lancement de l'application via l'IDE :
  - Afin de vous déplacer dans le répertoire principal du pokédex, exectuer la commande suivante depuis la racine du projet.
  
    ```cd .\PokedexProject\```
  
  
  - Ensuite pour exectuer les différentes migrations liées au mises a jour de l'application éxécutez la commande suivante :
  
    ```python manage.py migrate```
    
  - Puis lancez l'application sur le serveur local

    ```python manage.py runserver```
    
    
## Page d'accueil

  - Vous arrivez sur la page d'accueil du Pokédex, vous avez la possibilité d'effectuer une recherche sur un pokémon.
  - Plus bas en défilant cette page il est possible de consulter la liste des pokémons.
      - Chaque pokémon est nommé et présenté d'une image dans une cellule de la liste.
      - Le type (feu, eau, eclair, etc..) est affiché.
      - La pagination fonctionne sur 7 pages (car nous récupérons 151 pokémons, chaque page affichant 20 pokémons maximum).

## Page détails d'un pokémon
  
  - Afin de connaître les détails d'un pokémon, cliquez simplement sur la cellule.
  - Vous êtes redirigés sur une page de détails du pokémon avec toutes les informations essentielles du pokémon.
  - Un bouton de retour à la liste des pokémons est disponible en haut à droite. Cliquez dessus pour être redirigé à la page d'accueil.

## Création d'une équipe de pokémon

  - Sur la page d'accueil, il existe un deuxieme bouton sous la barre de recherche qui s'intitule "Créer une équipe".
  - Si vous cliquez sur le bouton vous êtes redirigés sur la page de création d'une équipe de pokémon.
  ###### Il s'agit d'une fonctionnalité que nous n'avons pas encore pu implémenter dans l'application.
