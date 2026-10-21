# Vue Régionale

## La page d’accueil { #the-landing-page }

L’application s’ouvre sur la vue régionale, qui affiche les contours de toutes les régions du jeu de régions actif. Le jeu par défaut est Global
Aquifers. Chaque contour est coloré selon la tendance du stockage des eaux souterraines sur les cinq dernières années, et la légende en haut à
droite compte les régions de chaque classe de tendance (voir [Analyse des Tendances et des Écarts](trends.md)). **Color by** dans l’en-tête
change ce selon quoi les contours sont colorés, et **Hide** affiche de simples contours.

![La vue régionale à l’ouverture, avec le jeu Global Aquifers classé selon la tendance du stockage des eaux souterraines](../../static/images/grace/app-home.webp)

À partir de là, vous pouvez :

- déplacer la carte et zoomer ; les noms des régions apparaissent une fois le zoom suffisant (désactivez-les avec **Region names**)
- passer à un autre jeu de régions, ou filtrer la liste des noms, dans la section **Regions** du panneau de contrôle
- modifier la couche affichée (**Displayed layer**) ou la fenêtre (**Window**) pour reclasser toutes les régions d’un coup, par exemple pour
  voir quels aquifères ont perdu du stockage total en eau au cours des 20 dernières années
- modifier **Color by** pour classer chaque région selon l’ampleur du désaccord entre les deux jeux de données à cet endroit, en tendance, en
  concordance d’un mois à l’autre ou en taille du cycle saisonnier (voir
  [Explorer les écarts dans l’application](../compare/exploring.md))
- ouvrir une région pour l’analyser, comme décrit ci-dessous

Sur cette page, le fil d’Ariane de l’en-tête indique **Home**. Après avoir ouvert une région, cliquez sur **Home** ou sur le bouton **Regions**
pour revenir.

## Choisir une région { #choosing-a-region }

Il existe trois façons d’ouvrir une région pour l’analyser :

1. Cliquer sur son contour sur la carte, ou sur son nom dans la liste du panneau de contrôle.
2. Importer une limite depuis un fichier GeoJSON.
3. Dessiner un polygone sur la carte.

### Jeux de régions prédéfinis { #preset-region-sets }

Choisissez un jeu dans la liste déroulante sous **Regions**. Saisissez du texte dans **Filter regions…** pour restreindre la liste.

| Jeu de régions | Régions | Source |
|---|---|---|
| Global Aquifers | 99 | Compilé par l’équipe GEOGLOWS à partir de plusieurs sources, complété par les jeux WHYMAP et IGRAC ci-dessous |
| Large Aquifer Systems (WHYMAP) | 37 | Large Aquifer Systems of the World, WHYMAP (BGR/UNESCO) |
| Transboundary Aquifers (IGRAC) | 155 | Transboundary Aquifers of the World 2025, UNESCO-IHP / IGRAC (CC BY-SA 3.0 IGO) |
| Principal Aquifers, USA (USGS) | 31 | Principal Aquifers of the United States, U.S. Geological Survey |
| Major River Basins (GRDC) | 456 | Major River Basins of the World, Global Runoff Data Centre (usage non commercial uniquement) |
| My Regions | les vôtres | Les régions que vous avez importées |

L’attribution du jeu actif est indiquée sous la liste. Citez-la si vous publiez des résultats fondés sur ce jeu.

### Importer une région { #uploading-a-region }

Cliquez sur **Upload**, choisissez ou faites glisser un fichier GeoJSON (`.geojson` ou `.json`, jusqu’à 50 MB), donnez un nom à la région et
cliquez sur **Analyze**.

![La boîte de dialogue Upload Region](../../static/images/grace/app-upload.webp){ width="510" }

Le fichier doit contenir des entités Polygon ou MultiPolygon en longitude et latitude WGS 84, conformément à la norme GeoJSON. S’il contient
plusieurs entités, elles sont fusionnées en une seule région. Les trous des polygones sont ignorés.

!!! tip "Convertir un shapefile"
    L’application ne lit que le GeoJSON. Pour convertir un shapefile, ouvrez-le dans QGIS, faites un clic droit sur la couche, choisissez
    **Export → Save Features As…**, puis réglez le format sur GeoJSON et le SCR sur EPSG:4326. [mapshaper.org](https://mapshaper.org){:target="_blank"}
    fait la même chose dans un navigateur : importez ensemble les fichiers `.shp`, `.dbf` et `.prj`, puis exportez en GeoJSON. Simplifier au
    préalable une limite très détaillée réduit la taille du fichier sans changer le résultat, puisque les mailles de la grille font 1° de côté.

![Un rectangle GeoJSON sur le Pendjab et l’Haryana, analysé comme sa propre région](../../static/images/grace/app-upload-result.webp)

La région est analysée dès qu’elle est importée, comme une région publiée, et le fil d’Ariane prend le nom que vous lui avez donné. L’exemple
ci-dessus est un simple rectangle sur le Pendjab et l’Haryana, où la baisse des eaux souterraines est assez marquée pour être évidente au premier
coup d’œil.

Les régions importées sont enregistrées dans **My Regions**, où vous pouvez les rouvrir ou les supprimer avec le × à côté du nom. Elles sont
stockées uniquement dans votre navigateur : elles ne sont partagées avec personne et n’apparaîtront ni sur un autre ordinateur ni dans un autre
navigateur.

### Dessiner une région { #drawing-a-region }

Sélectionnez **My Regions** dans la liste déroulante des jeux de régions, puis cliquez sur **Draw a polygon** sur la carte. Cliquez pour placer
chaque sommet et double-cliquez pour terminer. L’application analyse le polygone immédiatement. Les polygones dessinés ne sont pas enregistrés ;
importez un fichier si vous souhaitez conserver une région.

## Lire les résultats { #reading-the-results }

Lorsque vous ouvrez une région, la carte zoome sur celle-ci et affiche les mailles d’anomalie de la couche affichée à l’intérieur de sa limite,
et le graphique présente la série temporelle moyenne de la région (voir [Le graphique des séries temporelles](#the-time-series-chart)).

![L’Aquifère d’Ogallala analysé, avec ses mailles sur la carte et sa série temporelle moyenne en dessous](../../static/images/grace/app-region-result.webp)

L’Ogallala, ci-dessus, montre à quoi ressemble un résultat régional. Les mailles se situent au-dessus de la moyenne 2004–2009 sur la moitié nord
de l’aquifère et près d’elle au sud : les couleurs ne sont donc pas uniformes, même à l’intérieur d’une seule région. La série moyenne reste à
peu près stable pendant les années 2010 puis baisse à partir de 2020 environ, ce qui produit le −1.70 cm/an de la légende des tendances : ce
chiffre est la pente des cinq dernières années, et non celle de toute la série. Modifier le sélecteur **Window** le change (voir
[Analyse des Tendances et des Écarts](trends.md#the-analysis-window)).

### Mailles prises en compte dans la moyenne { #which-cells-are-averaged }

La moyenne régionale utilise toutes les mailles de la grille dont au moins 35 % de la surface se trouve dans la région, et pondère chacune par la
surface de recouvrement. Les mailles situées en majeure partie hors de la région sont exclues ; les mailles en bordure comptent au prorata de leur
part située à l’intérieur.

![Comment l’application calcule la moyenne des mailles sur une région](../../static/images/grace/grace-region-averaging.png)

Laquelle de ces grilles dépend du jeu de données. Sur **GRACE + GLDAS 2.1**, la TWSa est moyennée sur sa grille de 0.5° et les autres couches
sur leur grille de 1°, chacune avec ses propres poids de recouvrement. Sur **GLDAS 2.2**, toutes les couches sont moyennées sur la grille native
du modèle, à 0.25° : une région reçoit donc seize fois plus de mailles et la règle des 35 % en exclut beaucoup moins. C’est la principale raison
pratique de se tourner vers 2.2 sur un petit bassin.

Une région plus petite qu’environ 35 % d’une maille peut n’avoir aucune maille éligible ; utilisez alors une région plus grande, passez à
GLDAS 2.2 pour sa grille plus fine, ou cliquez sur la maille dans la [vue globale](global-view.md).

### Afficher la grille { #showing-the-grid }

Activez **Cell boundaries** et **Mascon boundaries** pour voir comment la région se situe par rapport à la grille et à la résolution
réelle de GRACE :

![Limites des mailles et des mascons sur le Système Aquifère d’Iullemeden-Irhazer](../../static/images/grace/app-region-boundaries.webp)

Ici, la région couvre des parties de plusieurs mascons (en violet) ; sa moyenne s’appuie donc sur plusieurs valeurs GRACE indépendantes. Une
région située à l’intérieur d’un seul mascon est sujette à la [fuite du signal](../mission/resolution-and-leakage.md) décrite dans la Partie 1.

Les mascons appartiennent à la solution GRACE, et **Mascon boundaries** est donc masqué sous GLDAS 2.2. La mise en garde qui l’accompagne n’a pas
disparu : 2.2 assimile GRACE, et la correction qui fait entrer le pompage dans ses eaux souterraines arrive donc à la résolution de GRACE,
quelque fine que soit la grille du modèle.

## Le graphique des séries temporelles { #the-time-series-chart }

Le graphique sous la carte trace la moyenne de la région pour chaque mois en cm d’équivalent en eau liquide, avec le zéro (la moyenne 2004–2009)
représenté par une ligne continue. Faites glisser le séparateur entre la carte et le graphique pour agrandir le graphique.

![Le graphique des séries temporelles de GWSa pour le Northern Midwest Aquifer System, avec les lacunes comblées par le modèle saisonnier et la tendance sur 5 ans](../../static/images/grace/app-recharge-button.webp)

Survolez le graphique pour lire les valeurs d’un mois. La ligne rouge en tirets repère le mois affiché sur la carte et se déplace lorsque vous
avancez ou lancez la lecture avec le contrôle temporel.

### Incertitude { #uncertainty }

Sur **GRACE + GLDAS 2.1**, une bande ombrée indique ±1σ lorsqu’une seule composante est tracée. La bande est moyennée sur les mailles de la même
façon que les valeurs, ce qui revient à considérer les erreurs des mailles voisines comme entièrement corrélées. C’est le choix prudent : des
erreurs qui se compensent en partie d’une maille à l’autre donneraient une bande plus étroite. La bande est masquée lorsque plusieurs composantes
sont tracées, pour que le graphique reste lisible.

**GLDAS 2.2 n’a pas de bande.** C’est une simulation unique : il n’y a donc pas d’ensemble dont tirer une dispersion, et la NASA ne publie aucune
incertitude mensuelle pour lui. L’absence de bande signifie qu’aucune estimation n’était disponible, jamais que les valeurs sont plus sûres que
celles qui en ont une — en général c’est le contraire, puisqu’une simulation porte toutes les sources d’erreur énumérées dans
[Les Modèles de Surface Terrestre GLDAS](../gldas/land-surface-models.md#accuracy-and-mixing-versions) sans que rien ne les rapporte.

### Comparer les composantes { #comparing-components }

Le graphique trace toujours la couche affichée (**Displayed layer**). Cochez d’autres composantes sous **Time series** dans le panneau de contrôle
pour les ajouter sur les mêmes axes :

| Composante | Sur GRACE + GLDAS 2.1 | Sur GLDAS 2.2 | Ce qu’elle représente |
|---|---|---|---|
| TWSa | mesurée par GRACE | le total propre du modèle | toute l’eau de la colonne : eaux souterraines, humidité du sol, neige, canopée et eaux de surface |
| GWSa | TWSa moins les trois couches GLDAS | un état du modèle, corrigé par GRACE | eaux souterraines, eaux de surface incluses |
| SMa | moyenne de trois modèles GLDAS 2.1 | profil Catchment, moins les eaux souterraines | humidité du sol |
| SWEa | moyenne de trois modèles GLDAS 2.1 | Catchment | équivalent en eau de la neige |
| CANa | moyenne de trois modèles GLDAS 2.1 | Catchment | eau retenue par la canopée végétale |

Les mêmes cinq noms désignent les mêmes grandeurs physiques dans les deux jeux de données, ce qui les rend comparables, mais on y parvient
différemment et ils ne concorderont pas exactement.
[Calcul du Stockage des Eaux Souterraines](../gldas/deriving-groundwater.md) explique comment les couches s’articulent dans chacun.

Cocher **Also show GLDAS 2.2** (ou **Also show GRACE + GLDAS 2.1**, selon le jeu de données sélectionné) ajoute la version de l’autre jeu de
données de ce qui est déjà tracé, dans un second jeu de couleurs. Là où les deux séries d’eau souterraine concordent, le résultat repose sur une
mesure et sur un modèle construits indépendamment l’un de l’autre, ce qui est une preuve plus forte que l’un ou l’autre seul. Là où elles
divergent, regardez les composantes pour voir dans quel terme se trouve le désaccord ; les études de cas en déroulent des exemples.

![GWSa comparée à TWSa et SMa pour le Système Aquifère d’Iullemeden-Irhazer](../../static/images/grace/app-chart-compare.webp)

La comparaison des composantes montre ce qui détermine le signal des eaux souterraines. Dans l’exemple ci-dessus, l’humidité du sol (en vert)
présente un fort cycle saisonnier mais aucune tendance de long terme, tandis que le stockage total en eau (en orange) et les eaux souterraines
(en bleu) augmentent ensemble à partir de 2010 environ : la hausse du stockage total correspond donc aux eaux souterraines.

### Comblement des lacunes { #gap-filling }

GRACE ne fournit aucune donnée pour 35 mois de la série ; sur le jeu de données GRACE, la TWSa et la GWSa présentent donc des lacunes, alors que
ses couches GLDAS, et toutes les couches de GLDAS 2.2, ont une valeur chaque mois. Le contrôle **Gap filling** détermine comment le graphique
trace les lacunes, et il est entièrement masqué sous GLDAS 2.2 :

- **None** interrompt la courbe à chaque lacune.
- **Straight line** relie les mois situés de part et d’autre de chaque lacune.
- **Seasonal model** estime les mois manquants à partir d’une tendance et d’un cycle saisonnier ajustés sur la série propre à la région, et les
  trace en tirets avec des marqueurs creux, comme dans le graphique ci-dessus.

Ce réglage ne modifie que le graphique. [Lacunes et Comblement des Lacunes](../mission/gap-filling.md) compare les trois options, puis présente
la méthode complète.

### Droites de tendance { #trend-lines }

Lorsqu’une tendance est affichée (**Analyze** dans l’en-tête), chaque composante tracée reçoit sa droite de tendance ajustée, en tirets, sur la
fenêtre, et la légende indique sa pente, par exemple « GWSa trend −0.29 cm/yr (last 5 yr) ». Sous l’une des mesures de comparaison, le graphique
rapporte à la place le nombre de cette région sous son titre, les deux jeux de données étant tracés. Voir
[Analyse des Tendances et des Écarts](trends.md).

### Analyse de la recharge { #recharge-analysis }

La méthode de fluctuation de la nappe a besoin d’une valeur à chaque mois : un bouton **Recharge Analysis** apparaît donc au-dessus du graphique
dès que la série en a une, c’est-à-dire avec **Seasonal model** sélectionné sur le jeu de données GRACE, et toujours sur GLDAS 2.2, dont
l’enregistrement n’a pas de lacunes à combler. Il ouvre une page qui estime la recharge annuelle des eaux souterraines à partir de la série GWSa.
L’analyse utilise toujours la GWSa, quelle que soit la couche affichée. La Partie 4 la décrit, en commençant par
[La Méthode WTF](../recharge/wtf-method.md).

Pouvoir la lancer sur 2.2 ne veut pas dire que la réponse est juste. Barbosa et al. (2025) ont lancé les deux dans le Bassin de la Volta et ont
trouvé que 2.2 donnait une recharge de 1.7 à 3.5 fois l’estimation fondée sur les puits, selon la variante de la méthode WTF, et ne l’ont pas
recommandé du tout pour la recharge, tout en le recommandant pour le suivi des tendances (voir
[Bassin de la Volta](../case-studies/volta.md)). Lisez un chiffre de recharge issu de 2.2 en regard d’un chiffre issu de 2.1 avant de
l’utiliser.

### Télécharger les données { #downloading-the-data }

**Download CSV** enregistre les valeurs mensuelles des cinq composantes pour la région, quelles que soient les composantes tracées et l’option
de comblement sélectionnée, ainsi que les bornes ±1σ et les séries comblées lorsque le jeu de données en possède. Avec la comparaison cochée, les
colonnes de l’autre jeu de données viennent aussi. [Téléchargement des Données](downloading-data.md) décrit les colonnes et montre comment
convertir les valeurs en volumes.
