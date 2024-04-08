### Devoir de Création de Pages Web avec Django

#### Objectif :
Le but de ce devoir est de créer des pages web pour une application de gestion des employés de la compagnie Busko en utilisant Django, un framework web Python.

#### Tâches à Réaliser :
1. **Page d'Accueil (`accueil.html`)** :
   - Présenter une bannière avec le message de la compagnie et un bouton "Contactez-nous".
   - Section "À Propos" avec une brève description de l'entreprise.
   - Section "Solutions" avec trois services offerts par Busko.
   - Section "Portfolio" pour afficher les projets réalisés.
   - Section "Témoignages" avec des avis de clients.
   - Section "FAQ" avec les questions fréquemment posées.

2. **Page de Gestion des Départements (`gestion.html`)** :
   - Tableau affichant les départements avec possibilité d'ajouter, modifier ou supprimer.
   - Bouton "Ajouter Département" pour ouvrir le formulaire d'ajout.

3. **Page d'Ajout de Département (`ajouter_departement.html`)** :
   - Formulaire pour saisir les informations d'un nouveau département.

4. **Page de Gestion des Employés (`employee.html`)** :
   - Tableau affichant les employés avec possibilité d'ajouter, modifier ou supprimer.
   - Bouton "Ajouter Employé" pour ouvrir le formulaire d'ajout.

5. **Page d'Ajout d'Employé (`ajouter_employee.html`)** :
   - Formulaire pour saisir les informations d'un nouvel employé.

#### Instructions Supplémentaires :
- Utiliser Bootstrap pour le design responsive.
- Charger les fichiers statiques (images, CSS) avec `{% load static %}`.
- Utiliser les URLs Django avec `{% url 'nom_url' %}` pour les liens internes.
- Inclure des emojis pour rendre l'interface plus attrayante. 🌟🚀

#### Détails des Pages :
##### Page d'Accueil (`accueil.html`) :
```markdown
- Bannière avec le message de la compagnie et bouton 🏢💼
- Section "À Propos" 👨‍💼👩‍💻
- Section "Solutions" 🛠️📱💻
- Section "Portfolio" 🎨📸
- Section "Témoignages" 🌟🗣️
- Section "FAQ" ❓❔❓

- Tableau des départements avec CRUD 📊📝
- Bouton "Ajouter Département" ➕

- Formulaire pour ajouter un département 📋✍️

- Formulaire pour ajouter un employé 📋✍️
