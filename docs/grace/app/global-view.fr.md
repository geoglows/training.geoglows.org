# Vue Globale

## La vue globale { #the-global-view }

Cliquez sur **Global** pour afficher la couche sélectionnée sur toutes les mailles continentales du monde. À la première ouverture,
l’application télécharge la série complète de cette couche, ce qui peut prendre un peu de temps ; elle est ensuite mise en cache dans votre
navigateur.

![Vue globale de l’anomalie de stockage des eaux souterraines en septembre 2024](../../static/images/grace/app-global.webp)

Appuyez sur lecture dans le contrôle temporel pour animer la série mois par mois. La vue globale défile plus vite que la vue régionale, environ
quatre mois par seconde, et reprend au début en boucle. L’animation fait ressortir les grandes structures : la baisse continue dans le nord de
l’Inde, au Moyen-Orient et dans la plaine de Chine du Nord, la hausse du stockage dans le Sahel depuis 2010 environ, et les années humides et
sèches qui balaient l’Amazonie et l’Afrique australe.

Changez la couche affichée (**Displayed layer**) pour comparer les composantes. La TWSa montre le contour en blocs des mascons de 3° (voir
[La Mission GRACE](../background/grace-mission.md#the-mascon-solution-used-by-the-app)) ; la SWEa est proche de zéro partout sauf aux hautes
latitudes et en montagne ; la SMa montre l’humidification et l’assèchement saisonniers des sols.

## Série temporelle d’une maille { #time-series-for-a-single-cell }

Cliquez sur n’importe quelle maille continentale pour tracer sa série temporelle. Le fil d’Ariane affiche alors les coordonnées de la maille, et
le graphique présente ses valeurs avec la bande d’incertitude ±1σ. Le graphique fonctionne comme pour une région (voir
[Vue Régionale](regional-view.md#the-time-series-chart)), et le fichier CSV téléchargé pour une maille porte le nom de ses coordonnées.

![Série temporelle d’une maille de 1° dans le centre de l’Iran](../../static/images/grace/app-global-cell.webp)

Une maille isolée se consulte rapidement, mais n’oubliez pas que GRACE résout environ 3° : la TWSa de la maille est donc partagée avec ses
voisines du même mascon. Pour un bassin ou un aquifère, utilisez la [vue régionale](regional-view.md), qui fait la moyenne de toutes les mailles
de la région.

## Carte des tendances { #trend-map }

Lorsque les tendances sont activées, la vue globale colore chaque maille selon sa tendance au lieu de l’anomalie mensuelle, et l’animation est
masquée. La légende compte les mailles de chaque classe.

![Tendance du stockage des eaux souterraines sur les cinq dernières années, par maille](../../static/images/grace/app-global-trends.webp)

Voir [Analyse des Tendances](trends.md) pour le calcul de la tendance et le choix de la fenêtre.
