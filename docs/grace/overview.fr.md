# Vue d’ensemble de GRACE Regional Analyst

## Ce que fait l’application { #what-the-app-does }

GRACE Regional Analyst suit l’évolution du stockage des eaux souterraines depuis 2002 dans n’importe quelle région du monde. Elle rapporte une
anomalie de stockage des eaux souterraines : la quantité d’eau stockée dans le sous-sol au cours d’un mois donné, en plus ou en moins par rapport
à la moyenne 2004–2009, exprimée en hauteur d’eau liquide en centimètres.

Elle atteint ce nombre par deux chemins différents, et porte les deux.

**GRACE + GLDAS 2.1** part de la colonne d’eau totale pesée par les satellites GRACE et GRACE Follow-On de la NASA et en retranche la neige,
l’eau du couvert végétal et l’humidité du sol estimées par trois modèles de surface terrestre. Ce qui reste est l’eau souterraine.
L’enregistrement commence en avril 2002, et la partie qui compte le plus — la variation du stockage elle-même — est mesurée et non modélisée.

**GLDAS 2.2** lit les eaux souterraines dans un seul modèle de surface terrestre, le modèle Catchment de la NASA, qui porte les eaux souterraines
comme un état à part entière et est corrigé chaque mois par assimilation de GRACE. L’enregistrement commence en février 2003, ne comporte aucun
mois manquant et est servi à 0.25° à l’intérieur d’une région, quatre fois plus fin dans chaque direction que l’autre jeu de données, ce qui rend
les bassins plus petits exploitables.

Aucun des deux n’est la bonne réponse partout, et ils divergent de manière instructive : l’application trace donc les deux sur un même graphique.
[Calcul du Stockage des Eaux Souterraines](gldas/deriving-groundwater.md) donne les deux calculs en entier et dit où chacun mérite confiance.

La plupart des aquifères comptent trop peu de piézomètres, ou des piézomètres aux séries trop lacunaires, pour dire avec certitude si le stockage
augmente ou diminue à l’échelle de l’ensemble du système. GRACE observe chaque aquifère de la planète, chaque mois, avec le même instrument. Sa
résolution est grossière, environ 300 km : elle convient donc aux aquifères, aux bassins et aux pays plutôt qu’aux champs captants individuels,
mais à cette échelle elle fournit un enregistrement cohérent de la variation du stockage là où il n’existe guère d’autres données.

![GRACE Regional Analyst, vue régionale du Système Aquifère d’Iullemeden-Irhazer](../static/images/grace/app-region.webp)

L’application est gratuite et s’exécute dans un navigateur web à l’adresse
[apps.geoglows.org/grace-anomalies](https://apps.geoglows.org/grace-anomalies){:target="_blank"}. Elle vous permet de :

- passer d’un jeu de données à l’autre, ou tracer les deux sur le même graphique pour les comparer
- animer les cartes mensuelles des anomalies de stockage des eaux souterraines, de l’eau totale, de l’humidité du sol, de la neige et de l’eau
  de la canopée pour l’ensemble du globe
- choisir un aquifère ou un bassin fluvial dans l’un des cinq jeux de régions publiés, importer votre propre limite au format GeoJSON ou en
  dessiner une sur la carte
- tracer la série temporelle moyennée sur la surface de cette région, avec sa bande d’incertitude lorsque le jeu de données en possède une, et
  comparer les composantes du stockage
- classer les régions ou les mailles selon la tendance du stockage sur les 5, 10, 15 ou 20 dernières années, ou sur l’ensemble de la série
- combler les mois qui manquent à GRACE avec un modèle saisonnier ajusté à l’enregistrement propre de la région
- estimer la recharge annuelle des eaux souterraines par la méthode de fluctuation de la nappe
- télécharger les valeurs mensuelles de n’importe quelle région ou maille dans un fichier CSV pour vos propres analyses

## Contenu de cette formation { #what-this-training-covers }

**Partie 1, La Mission GRACE,** porte sur la mesure : ce qu’elle est, jusqu’où on peut la pousser, et où elle est trouée :

- [Comment GRACE Mesure le Stockage de l'Eau](mission/measuring-water-storage.md) : comment deux satellites mesurent les variations de la
  gravité terrestre, et ce qu’est une anomalie mensuelle de stockage d’eau.
- [Résolution, Fuite du Signal et Petites Régions](mission/resolution-and-leakage.md) : ce que GRACE peut et ne peut pas résoudre, et comment
  travailler avec des régions plus petites que son empreinte.
- [Lacunes et Comblement des Lacunes](mission/gap-filling.md) : les 35 mois qui manquent à la série, les options de l’application et le modèle
  saisonnier derrière l’option **Seasonal model** : comment il est ajusté, comment les valeurs comblées sont calculées et quelle est leur
  précision.

**Partie 2, GLDAS,** porte sur les modèles, qui fournissent tout ce que l’application affiche qui n’est pas une mesure de gravité :

- [Les Modèles de Surface Terrestre GLDAS](gldas/land-surface-models.md) : ce qu’est GLDAS, ce que calcule un modèle de surface terrestre, les
  trois modèles derrière le jeu de données 2.1, et ce que change l’assimilation de GRACE dans 2.2.
- [Calcul du Stockage des Eaux Souterraines](gldas/deriving-groundwater.md) : les deux voies vers les eaux souterraines, les facteurs de gain
  appliqués aux données GRACE, et la façon dont l’incertitude est estimée.

**Partie 3, Utilisation de l’Application,** présente l’interface : [la disposition](app/interface.md), [la vue régionale](app/regional-view.md),
[la vue globale](app/global-view.md), [l’analyse des tendances](app/trends.md) et
[le téléchargement des données](app/downloading-data.md).

**Partie 4, Analyse de la Recharge,** estime la recharge annuelle des eaux souterraines par la méthode de fluctuation de la nappe (WTF) :
[la méthode](recharge/wtf-method.md) appliquée aux données GRACE, puis [l’ouverture de l’analyse](recharge/opening.md) et la vérification de
la série, [les années hydrologiques et le choix des points](recharge/picks.md), et [les résultats](recharge/results.md).

**Partie 5, Études de Cas,** résume trois études publiées par l’équipe de l’Université Brigham Young qui a développé l’application et son
prédécesseur, le GRACE Groundwater Subsetting Tool (GGST). Chacune combine le bilan hydrique GRACE et GLDAS de l’application avec d’autres
données : [l’estimation de la recharge au Niger](case-studies/niger.md), où les puits sont rares, [la prise en compte d’un grand réservoir dans
le bassin de la Volta](case-studies/volta.md), et [la correction de la fuite du signal dans la Vallée Centrale de Californie](case-studies/central-valley.md),
une vallée étroite et fortement exploitée par pompage.

## Historique { #history }

GRACE Regional Analyst remplace le GRACE Groundwater Subsetting Tool (GGST), une application Tethys Platform développée à l’Université Brigham
Young dans le cadre du projet NASA SERVIR Afrique de l’Ouest (2019–2023) et utilisée lors d’ateliers de formation en Afrique de l’Ouest, en
Jordanie et en Palestine. La nouvelle application conserve la méthode de GGST pour séparer les eaux souterraines du stockage total en eau, et
ajoute la classification des tendances, les limites d’aquifères et de bassins publiées, les régions dessinées par l’utilisateur, l’analyse de la
recharge et le jeu de données GLDAS 2.2 à côté du précédent. Elle s’exécute entièrement dans le navigateur et lit les données traitées
directement depuis le stockage cloud ; aucun compte ni identifiant n’est donc nécessaire.

## Pour aller plus loin { #further-reading }

Ces articles ont établi GRACE comme outil de suivi du stockage des eaux souterraines dans les grands aquifères :

- Rodell, M., Velicogna, I., and Famiglietti, J. S. (2009). Satellite-based estimates of groundwater depletion in India. *Nature*, 460,
  999–1002. [doi:10.1038/nature08238](https://doi.org/10.1038/nature08238){:target="_blank"}
- Famiglietti, J. S., et al. (2011). Satellites measure recent rates of groundwater depletion in California's Central Valley. *Geophysical
  Research Letters*, 38, L03403. [doi:10.1029/2010GL046442](https://doi.org/10.1029/2010GL046442){:target="_blank"}
- Famiglietti, J. S. (2014). The global groundwater crisis. *Nature Climate Change*, 4, 945–948.
  [doi:10.1038/nclimate2425](https://doi.org/10.1038/nclimate2425){:target="_blank"}
- Thomas, A. C., Reager, J. T., Famiglietti, J. S., and Rodell, M. (2014). A GRACE-based water storage deficit approach for hydrological
  drought characterization. *Geophysical Research Letters*, 41, 1537–1545.
  [doi:10.1002/2014GL059323](https://doi.org/10.1002/2014GL059323){:target="_blank"}
