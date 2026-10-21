# L’Interface de l’Application

## Ouvrir l’application { #opening-the-app }

Ouvrez [apps.geoglows.org/grace-anomalies](https://apps.geoglows.org/grace-anomalies){:target="_blank"} dans une version récente de Chrome, Edge,
Firefox ou Safari. Rien n’est à installer et aucun identifiant n’est demandé. La première visite télécharge les données des couches par défaut, ce
qui peut prendre quelques secondes sur une connexion lente ; ensuite, l’application en conserve une copie dans le navigateur et s’ouvre rapidement.

![GRACE Regional Analyst à l’ouverture](../../static/images/grace/app-home.webp)

La fenêtre comporte trois parties : le **panneau de contrôle** à gauche, la **carte** en haut à droite et le **panneau du graphique** sous la carte.
Faites glisser les trois points situés entre la carte et le graphique pour agrandir l’un ou l’autre ; double-cliquez dessus pour rétablir la
répartition par défaut.

## Panneau de contrôle { #control-panel }

![Le panneau de contrôle](../../static/images/grace/app-panel.webp){ align=right width="260" }

De haut en bas :

- **Regions / Global.** Bascule entre la vue régionale, qui affiche les contours des régions et analyse une région à la fois, et la
  [vue globale](global-view.md), qui anime le monde entier. Cliquer sur **Regions** lorsqu’une région est ouverte ramène à la vue d’ensemble.
- **Upload.** Charge votre propre limite de région depuis un fichier GeoJSON (voir [Vue Régionale](regional-view.md#uploading-a-region)).
- **Settings.** Paramètres d’affichage, décrits plus bas.
- **Dataset.** Lequel des deux jeux de données d’eau souterraine concerne le panneau, la carte et le graphique :
  **GRACE + GLDAS 2.1**, dont les eaux souterraines sont obtenues en retranchant trois modèles de surface terrestre de la mesure GRACE, et
  **GLDAS 2.2**, dont les eaux souterraines sont lues dans un modèle qui assimile GRACE (voir
  [Calcul du Stockage des Eaux Souterraines](../gldas/deriving-groundwater.md)). Une ligne sous le contrôle indique comment ce jeu de données
  obtient les eaux souterraines et à quelle résolution. Changer de jeu de données conserve la même grandeur sélectionnée et la même région
  ouverte : la comparaison est à un clic.
- **Displayed layer.** La composante du stockage affichée sur la carte et tracée dans le graphique : Groundwater Storage Anomaly (GWSa,
  anomalie de stockage des eaux souterraines, par défaut), Total Water Storage Anomaly (TWSa, anomalie de stockage total en eau), Soil Moisture
  Anomaly (SMa, anomalie d’humidité du sol), Snow Water Equivalent Anomaly (SWEa, anomalie d’équivalent en eau de la neige) et Canopy Water
  Storage Anomaly (CANa, anomalie de stockage d’eau de la canopée). Le menu déroulant donne les noms complets ; les abréviations sont ce
  qu’utilisent la légende du graphique et le CSV.
- **Time series.** Cochez d’autres composantes pour les ajouter au graphique à des fins de comparaison. La couche affichée est toujours tracée
  (voir [Vue Régionale](regional-view.md#the-time-series-chart)).
- **Also show …** Trace aussi sur le graphique les mêmes grandeurs de l’autre jeu de données, pour pouvoir lire l’un en regard de l’autre. Il
  reprend ce qui est coché au-dessus au lieu de proposer une seconde série de cases, et ne change rien sur la carte. L’une des mesures de
  comparaison de **Color by** a besoin des deux séries : la choisir coche cette case et l’y maintient jusqu’à ce que vous choisissiez autre chose.
- **Gap filling.** Ce que fait le graphique aux mois sans données GRACE. **None** interrompt la courbe à chaque lacune, **Straight line** relie
  les mois situés de part et d’autre, et **Seasonal model** comble les lacunes avec des valeurs estimées à partir du reste de la série, tracées en
  tirets avec des marqueurs creux (voir [Lacunes et Comblement des Lacunes](../mission/gap-filling.md)). Ce réglage ne modifie que le graphique, jamais le
  fichier CSV téléchargé. GLDAS 2.2 n’a aucun mois manquant, et ce contrôle est donc masqué tant que ce jeu de données est sélectionné.
- **Color ramp.** Six palettes. Viridis, Cividis, Brown-Teal et Purple-Green sont adaptées aux personnes ayant un trouble de la vision des
  couleurs.
- **Layer opacity.** Atténue les mailles d’anomalie pour laisser voir le fond de carte.
- **Cell boundaries / Mascon boundaries.** Affiche le contour des mailles de la grille, ou des mascons GRACE de 3° qui déterminent la
  résolution réelle des données. Les mascons appartiennent à la mesure GRACE, et ce contrôle est donc masqué sous GLDAS 2.2.
- **Region names.** Affiche le nom des régions une fois le zoom suffisant.
- **Light mode.** Bascule entre le thème clair et le thème sombre.
- **Regions.** Choisissez un jeu de régions, filtrez-le par nom et cliquez sur un nom pour analyser cette région.

<div style="clear: both;"></div>

Trois de ces contrôles sont masqués plutôt que grisés tant que **GLDAS 2.2** est sélectionné, parce qu’ils décrivent des choses que ce jeu de
données n’a pas : **Gap filling** (son enregistrement n’a pas de lacunes), **Mascon boundaries** (c’est un modèle et non une solution de
mascons) et la bande d’incertitude sur le graphique (c’est une simulation unique, sans ensemble dont tirer une dispersion). Un contrôle grisé
invite à se demander comment l’activer : il est donc retiré.

## Carte { #map }

La carte comporte des boutons de zoom et un menu de fonds de carte (l’icône des couches sous les boutons de zoom) proposant les fonds
OpenStreetMap, topographique, imagerie, rues, gris clair, gris foncé et relief. Une barre d’échelle se trouve en bas à droite. La barre de
couleurs en haut à droite donne l’échelle des mailles d’anomalie, toujours centrée sur zéro ; la légende de l’analyse apparaît au-dessus
lorsqu’une classification est affichée.

Le **contrôle temporel** en bas de la carte permet de parcourir les mois :

![Le contrôle temporel](../../static/images/grace/app-time-control.webp){ width="410" }

Appuyez sur lecture pour lancer l’animation, ou faites glisser le curseur. Sur le jeu de données GRACE, le curseur ne s’arrête que sur les mois
disposant de données GRACE ; GLDAS 2.2 a une valeur à chaque mois depuis février 2003, et le curseur les parcourt donc tous. Le mois en cours
est aussi repéré sur le graphique par une ligne rouge en tirets.

## Barre d’en-tête { #header-bar }

![La barre d’en-tête : fil d’Ariane à gauche, contrôles d’analyse à droite](../../static/images/grace/app-header.webp){ width="800" }

Le fil d’Ariane à gauche indique où vous vous trouvez : **Home** (la vue d’ensemble), un nom de région, **Global map** ou les coordonnées d’une
maille sélectionnée. Cliquez sur **Home** pour revenir à la vue d’ensemble. À droite, **Analyze / Hide** active ou désactive la classification de
la carte, **Color by** choisit ce qui est classé — la tendance de la couche affichée, ou l’une de trois comparaisons entre les deux jeux de
données — et le sélecteur **Window** fixe la période sur laquelle une tendance est calculée. Voir
[Analyse des Tendances et des Écarts](trends.md) et [Explorer les écarts dans l’application](../compare/exploring.md).

## Paramètres { #settings }

![La boîte de dialogue Display Settings](../../static/images/grace/app-settings.webp){ width="510" }

- **GRACE Mascon Footprints** et **Anomaly Cell Boundaries :** un curseur **Boundary width** pour chacune des deux couches de contours. La
  section des mascons porte en outre une note expliquant pourquoi une grille plus fine n’est pas une mesure plus fine.
- **Show color bar on map :** masque ou affiche la barre de couleurs.
- **Dynamic scale (fit to data) :** lorsque cette option est activée, l’échelle de couleurs s’ajuste aux données affichées, de sorte que les
  petites anomalies restent visibles. Elle va jusqu’au 95e centile des valeurs absolues sur les mailles affichées et sur tous les mois, dans une
  région comme dans la vue globale, de sorte que quelques mailles extrêmes saturent au lieu d’aplatir tout le reste. Désactivez-la pour utiliser
  une échelle fixe de −30 à +30 cm, préférable pour comparer des captures d’écran de différentes régions.
- **Clear cached data :** supprime la copie des données que l’application conserve dans votre navigateur. La visite suivante télécharge à
  nouveau l’ensemble des données. Utilisez cette option si l’application se comporte de façon anormale après une mise à jour des données.

Les paramètres sont conservés jusqu’à la fermeture de la page. Le thème clair ou sombre et la taille du panneau du graphique sont mémorisés d’une
visite à l’autre.
