Bianca Bica (20161056)
Chaima Boussora (20159909)
Karine Nguyen (20160036)

Tous les classificateurs ont été implémentés dans des fichiers séparés, chacun étant intitulé en fonction du classificateur correspondant. Par défaut,
tous les algorithmes sont exécutés seulement en se basant sur les 2 mots/catégories situés avant et après le mot "interest", sauf le classificateur 
Naive Bayes. Pour celui-ci, nous avons pris en considération les cas où il y a 1, 2 et 3 mots/catégories avant et après le mot concerné. 

Les fonctions qui nous permettent d'extraire les caractéristiques se retrouvent toutes dans le fichier main.py. Nous importons celui-ci dans les fichiers
qui contiennent les classificateurs afin de simplifier le tout. Le fichier main.py contient également 3 fonctions presque identiques, soit one_before_and_after,
two_before_and_after et three_before_and_after et comme le nom le dit, vont nous permettre d'aller chercher les 1, 2 ou 3 mots/catégories avant et après
"interest".


