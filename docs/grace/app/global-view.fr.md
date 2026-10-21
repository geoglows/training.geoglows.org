# Vue Globale

## La vue globale { #the-global-view }

Cliquez sur **Global** pour afficher la couche sélectionnée sur toutes les mailles continentales du monde. À la première ouverture,
l’application télécharge la série complète de cette couche, ce qui peut prendre un peu de temps ; elle est ensuite mise en cache dans votre
navigateur.

La carte globale est sur une grille à 1° pour les deux jeux de données, même si GLDAS 2.2 est nativement à 0.25°. Une couche mondiale à 0.25°
représente un tableau de 971 Mo dans le navigateur pour une seule variable, qu’aucune patience ne rend exploitable. La grille plus fine n’est lue
qu’à l’intérieur d’une région, où une limite permet de la découper ; voir [Vue Régionale](regional-view.md#which-cells-are-averaged).

![Vue globale de l’anomalie de stockage des eaux souterraines en avril 2002, le premier mois de la série](../../static/images/grace/app-global.webp)

Appuyez sur lecture dans le contrôle temporel pour animer la série mois par mois. La vue globale défile plus vite que la vue régionale, environ
quatre mois par seconde, et reprend au début en boucle. L’animation fait ressortir les grandes structures : la baisse continue dans le nord de
l’Inde, au Moyen-Orient et dans la plaine de Chine du Nord, la hausse du stockage dans le Sahel depuis 2010 environ, et les années humides et
sèches qui balaient l’Amazonie et l’Afrique australe.

Changez la couche affichée (**Displayed layer**) pour comparer les composantes. Sur le jeu de données GRACE, la TWSa porte encore l’empreinte
des mascons de 3° même avec les facteurs de gain appliqués (voir
[Comment GRACE Mesure le Stockage de l'Eau](../mission/measuring-water-storage.md#the-mascon-solution-used-by-the-app)) ; la SWEa est proche de zéro partout sauf aux hautes
latitudes et en montagne ; la SMa montre l’humidification et l’assèchement saisonniers des sols.

Changez le jeu de données (**Dataset**) pour comparer les deux voies vers les eaux souterraines sur le monde entier. Les structures concordent
là où le signal est important — le nord de l’Inde, la plaine de Chine du Nord, le Moyen-Orient — et cette concordance veut dire quelque chose,
puisque les deux ont été obtenues indépendamment. La carte 2.2 commence en février 2003 et non en avril 2002 et a une valeur à chaque mois : son
animation se déroule donc sans les pauses que les mois manquants de GRACE laissent dans l’autre.

## Série temporelle d’une maille { #time-series-for-a-single-cell }

Cliquez sur n’importe quelle maille continentale pour tracer sa série temporelle. Le fil d’Ariane affiche alors les coordonnées de la maille, et
le graphique présente ses valeurs, avec la bande d’incertitude ±1σ sur le jeu de données GRACE ; GLDAS 2.2 n’a pas de bande (voir
[Vue Régionale](regional-view.md#uncertainty)). Le graphique fonctionne comme pour une région (voir
[Vue Régionale](regional-view.md#the-time-series-chart)), et le fichier CSV téléchargé pour une maille porte le nom de ses coordonnées.

![Série temporelle d’une maille de 1° dans le nord-ouest de l’Iran](../../static/images/grace/app-global-cell.webp)

Une maille isolée se consulte rapidement, mais n’oubliez pas que GRACE résout environ 3° : la TWSa de la maille repose donc sur la même mesure
que celle de ses voisines du même mascon. Les facteurs de gain donnent à ces voisines des nombres différents, et cette différence vient d’un
modèle de surface terrestre et non de GRACE (voir
[Résolution, Fuite du Signal et Petites Régions](../mission/resolution-and-leakage.md)). La même mise en garde vaut pour une maille 2.2 : sa
grille est plus fine, mais la correction GRACE derrière ses eaux souterraines ne l’est pas. Pour un bassin ou un aquifère, utilisez la
[vue régionale](regional-view.md), qui fait la moyenne de toutes les mailles de la région.

## Cartes de tendance et d’écarts { #trend-and-difference-maps }

Lorsque l’analyse est activée, la vue globale colore chaque maille par un seul nombre pour l’enregistrement entier au lieu de l’anomalie
mensuelle, et l’animation est masquée. La légende compte les mailles de chaque classe. Une tendance fonctionne sur l’un comme sur l’autre jeu de
données ; les nombres de mailles diffèrent, parce que les deux ont des masques terrestres différents et commencent à des années différentes.

![Tendance du stockage des eaux souterraines sur les cinq dernières années, par maille](../../static/images/grace/app-global-trends.webp)

Avec l’eau souterraine affichée, **Color by** propose aussi les trois comparaisons entre les deux jeux de données, et chacune colore les mêmes
mailles selon l’ampleur du désaccord entre GRACE et GLDAS 2.2 à cet endroit. En calculer une lit l’enregistrement entier des deux jeux : cela
prend donc quelques secondes de plus qu’une tendance.

![Chaque maille terrestre colorée par l’écart entre les tendances d’eau souterraine sur cinq ans des deux jeux de données](../../static/images/grace/app-diff-global.webp)

Maille par maille, ces comparaisons sont bruitées, comme le montre la carte ci-dessus. Servez-vous-en pour voir où sont les grands motifs, et de
la vue régionale pour dire quoi que ce soit d’un aquifère donné.

Voir [Analyse des Tendances et des Écarts](trends.md) pour le calcul de chaque nombre et le choix de la fenêtre, et
[Explorer les écarts dans l’application](../compare/exploring.md) pour la lecture des cartes de comparaison.
