# Les Modèles de Surface Terrestre GLDAS

Tout ce que l’application affiche qui n’est pas une mesure de gravité vient de GLDAS. Le jeu de données GRACE + GLDAS 2.1 utilise trois modèles
GLDAS pour retirer la neige, l’eau du couvert végétal et l’humidité du sol de ce que mesurent les satellites. Le jeu de données GLDAS 2.2 lit
les eaux souterraines directement dans une quatrième simulation GLDAS. Cette page traite de ce que sont ces modèles et de ce qu’ils peuvent ou
non représenter ; [Calcul du Stockage des Eaux Souterraines](deriving-groundwater.md) donne les deux calculs en entier.

## Ce qu’est GLDAS { #what-gldas-is }

Le Global Land Data Assimilation System de la NASA produit des champs globaux d’états et de flux de la surface terrestre en forçant des modèles
de surface terrestre avec la météorologie observée (Rodell et al., 2004). Les modèles tournent **hors couplage**, c’est-à-dire sans être
couplés à une atmosphère : la météorologie est une donnée d’entrée, et le travail du modèle est de suivre où vont l’eau et l’énergie une fois
qu’elles atteignent le sol. GLDAS les exécute à travers le Land Information System (Kumar et al., 2006).

Les produits que lit l’application couvrent de 60°S à 90°N et toutes les longitudes, sur des grilles à 1° et 0.25°. L’Antarctique est en dehors
du domaine, et c’est pourquoi la carte globale s’arrête à 60°S. GLDAS publie des sorties toutes les 3 heures et quotidiennes, ainsi que des
moyennes mensuelles construites à partir de celles-ci ; l’application utilise les moyennes mensuelles.

La version 2 de GLDAS se décline en trois parties, et les différences entre elles comptent pour la manière dont l’application traite chacune :

| | Forçage | Modèles | Période | Observations assimilées |
|---|---|---|---|---|
| **GLDAS-2.0** | jeu météorologique de Princeton | Noah, VIC, Catchment | 1948–2014 | aucune |
| **GLDAS-2.1** | NOAA GDAS, GPCP, AGRMET | Noah, VIC, Catchment | 2000–présent | aucune |
| **GLDAS-2.2** | analyse IFS du CEPMMT | Catchment seulement | 2003–présent | stockage total de l’eau de GRACE |

GLDAS-2.0 s’arrête en 2014 et l’application ne l’utilise pas, sinon que les deux autres versions sont parties de son état et non de zéro.
GLDAS-2.0 et 2.1 sont en **boucle ouverte** : les modèles tournent avec leur seul forçage et aucune observation ne les corrige en chemin.
GLDAS-2.2 est le seul produit de la famille qui assimile des données.

## Ce que calcule un modèle de surface terrestre { #what-a-land-surface-model-computes }

Le bilan ci-dessous est le même dans toutes les versions de GLDAS. Ce qui change entre elles, c’est quels réservoirs existent et lesquels
l’application retient, et le bas de la figure l’indique pour chacune.

![Les réservoirs et les flux qu’un modèle de surface terrestre GLDAS porte pour chaque maille, et ce que chaque version de GLDAS apporte à l’application](../../static/images/grace/gldas-water-cycle.png)

Pour chaque maille et chaque pas de temps, le modèle prend la météorologie au-dessus de la surface et résout un bilan d’eau et d’énergie en
dessous. La pluie et la neige arrivent. Une partie de la pluie est retenue par les feuilles et s’évapore aussitôt ; la neige s’accumule puis
fond ; ce qui atteint le sol s’infiltre, descend dans le sol et en ressort par évaporation, transpiration, ruissellement de surface ou drainage.
Ce qui n’est pas parti à la fin du pas de temps est du stock, et il est reporté au pas suivant.

Les quatre réservoirs sont ce sur quoi l’application est bâtie : l’eau du couvert végétal, l’équivalent en eau de la neige, l’humidité du sol et
les eaux souterraines. Les trois premiers existent dans tous les modèles GLDAS et les deux jeux de données de l’application les utilisent. Les
eaux souterraines n’existent que dans le modèle Catchment, et c’est pourquoi elles n’atteignent l’application que par GLDAS 2.2. Chaque
réservoir est rapporté comme une hauteur d’eau liquide en kg/m², ce qui équivaut à un millimètre, soit un dixième de centimètre ;
l’application les convertit tous en centimètres pour pouvoir les ajouter à GRACE et les en retrancher.

Ce que les modèles laissent de côté se retrouve dans les eaux souterraines de l’application :

**Ni pompage ni irrigation.** GLDAS simule le cycle naturel de l’eau. Rien dans le modèle ne prélève d’eau dans un aquifère, de sorte qu’une
simulation GLDAS seule ne peut pas produire l’épuisement qui est tout le sujet de cette application. C’est pourquoi la voie 2.1 retranche les
modèles d’une mesure et la voie 2.2 doit en assimiler une.

**Pas d’eaux de surface.** Il n’y a ni rivières, ni lacs, ni réservoirs. Dans un bassin où un grand réservoir se remplit et se vide, cette
variation est comptée ailleurs, ce qui en pratique veut dire dans les eaux souterraines.

**Ni glaciers ni calottes glaciaires.** Aucun des modèles GLDAS n’en comporte, de sorte qu’au Groenland, dans certaines parties de l’Arctique et
dans les sols perpétuellement gelés de l’Himalaya, l’équivalent en eau de la neige s’accumule sans limite. La documentation de la NASA pour
GLDAS version 2 le dit clairement et conseille de masquer ces mailles.

[À quoi ressemblent les écarts](../compare/examples.md) montre ce que chacune de ces trois absences produit sur la carte.

### Les données de forçage { #the-forcing-data }

Un modèle de surface terrestre ne calcule rien de la météorologie ; la météorologie lui est fournie et il détermine ce que le sol en fait.
GLDAS fournit sept champs à chaque pas de temps :

| Champ | Variable | Unités |
|---|---|---|
| Taux de précipitation totale | `Rainf_f_tavg` | kg m⁻² s⁻¹ |
| Température de l’air | `Tair_f_inst` | K |
| Humidité spécifique | `Qair_f_inst` | kg kg⁻¹ |
| Pression de surface | `Psurf_f_inst` | Pa |
| Vitesse du vent | `Wind_f_inst` | m s⁻¹ |
| Rayonnement de courtes longueurs d’onde descendant | `SWdown_f_tavg` | W m⁻² |
| Rayonnement de grandes longueurs d’onde descendant | `LWdown_f_tavg` | W m⁻² |

La précipitation est ce qui compte le plus pour le stockage, et c’est le champ que chaque version de GLDAS traite différemment :

| | Champs atmosphériques | Précipitation | Rayonnement |
|---|---|---|---|
| **GLDAS-2.0** | jeu de forçage global de Princeton (Sheffield et al., 2006) | Princeton | Princeton |
| **GLDAS-2.1** | analyse GDAS de la NOAA (Derber et al., 1991) | GPCP v1.3 quotidien, désagrégé à 3 heures | AGRMET, désormais GALWEM |
| **GLDAS-2.2** | analyse opérationnelle IFS du CEPMMT | IFS du CEPMMT | IFS du CEPMMT |

La source de rayonnement de 2.1 a changé sous les pieds de l’application : AGRMET reposait sur le World-Wide Merged Cloud Analysis de l’armée
de l’air américaine, qui a cessé d’être produit le 8 juin 2025, de sorte que depuis le 9 juin 2025 GLDAS 2.1 est forcé avec le rayonnement
GALWEM du Met Office britannique. Les mois antérieurs et postérieurs à cette date ont été produits avec des entrées de rayonnement différentes,
ce qui est une raison de plus pour que la bande d’incertitude soit la dispersion entre modèles plutôt qu’une erreur publiée.

Deux autres conséquences du forçage à garder à l’esprit en lisant les données. GLDAS 2.1 a tourné avec GDAS et GPCP seuls de janvier 2000
jusqu’à l’ajout d’AGRMET le 1er mars 2001, de sorte que ses premiers mois ne sont pas forcés comme le reste ; l’enregistrement de l’application
commence en avril 2002 et en est exempt. Et comme le forçage de 2.2 est celui du CEPMMT, dont la licence n’autorise pas la NASA à le
redistribuer, le produit 2.2 ne publie aucun champ météorologique : on peut voir ce que le modèle a fait, mais pas ce qu’on lui a dit.

Les modèles ne portent pas non plus de routage entre mailles. Noah et VIC traitent chaque maille comme une colonne indépendante. Le modèle
Catchment est l’exception à l’intérieur d’une maille : il divise la terre en bassins hydrologiques délimités à partir de données d’élévation et
redistribue l’eau dans chacun selon la topographie (Koster et al., 2000 ; Ducharne et al., 2000).

## Les trois modèles de GLDAS 2.1 { #the-three-models-of-gldas-21 }

GLDAS 2.1 a démarré le 1er janvier 2000 depuis l’état de GLDAS-2.0, forcé comme le décrit le tableau ci-dessus. Il exécute trois modèles, qui
diffèrent surtout par la façon dont ils portent l’eau du sol :

| Modèle | Grille | Humidité du sol utilisée par l’application |
|---|---|---|
| Noah 3.6 | 0.25° | quatre couches, 0–200 cm |
| VIC 4.1.2 | 1° | trois couches, profondeurs variables selon le lieu |
| Catchment (CLSM-F2.5) | 1° | zone racinaire, 0–100 cm |

Aucun des trois ne porte un réservoir d’eau souterraine utilisable par l’application. Noah et VIC n’en ont aucun : l’eau qui draine sous la
couche inférieure quitte la colonne en débit de base et le modèle cesse de la suivre. Le modèle Catchment porte bien des eaux souterraines,
mais tournant en boucle ouverte il n’a aucun moyen de connaître le pompage, de sorte que ses eaux souterraines suivent la pluie et peu d’autre
chose.

Les trois modèles sont souvent en désaccord, et c’est sur l’humidité du sol profond que le désaccord est le plus fort. L’application en fait la
moyenne plutôt que d’en choisir un, ce qui impose de travailler sur la plus grossière des trois grilles, celle à 1°
([comment](deriving-groundwater.md#the-gldas-terms)).

### Pourquoi le modèle Catchment demande un traitement à part { #why-the-catchment-model-needs-separate-handling }

Noah et VIC rapportent l’humidité du sol par couche de profondeur, et l’application additionne donc les couches. Le modèle Catchment n’a pas de
couches. Il rapporte trois réservoirs, et la documentation de la NASA pour GLDAS version 2 est explicite : ils sont imbriqués, le profil
contenant la zone racinaire et la zone racinaire contenant la surface.

| Réservoir | Profondeur | Variable |
|---|---|---|
| Surface | 0–2 cm | `SoilMoist_S_inst` |
| Zone racinaire | 0–100 cm | `SoilMoist_RZ_inst` |
| Profil | jusqu’au substratum rocheux, variable d’une maille à l’autre | `SoilMoist_P_inst` |

Le réservoir de profil descend sous la nappe, et il contient donc les eaux souterraines du modèle en même temps que son humidité du sol. La NASA
définit les eaux souterraines du modèle Catchment à partir de ce fait :

$$
\mathrm{GWS} = \mathrm{TWS} - \mathrm{RootZone} - \mathrm{SWE} - \mathrm{CanopInt}
$$

Le stockage total de l’eau du modèle est l’eau de son profil plus la neige plus le couvert végétal, ce qui se ferme à 5×10⁻⁴ mm sur les fichiers
publiés. En y substituant cela, les eaux souterraines apparaissent comme l’écart entre les deux réservoirs :

$$
\mathrm{GWS} = \mathrm{SoilMoist\_P} - \mathrm{RootZone}
$$

Sur l’ensemble de la surface terrestre, cet écart contient une médiane de 746 mm d’eau, soit plus du triple de ce que contient la zone racinaire
elle-même.

L’application prend donc la zone racinaire pour le modèle Catchment et laisse le profil de côté. Verser le profil dans le terme d’humidité du
sol confierait les eaux souterraines du modèle au mauvais côté du bilan hydrique : elles seraient retranchées de ce que GRACE a mesuré, alors
que les eaux souterraines sont précisément la quantité cherchée. Il suffit qu’un tiers de l’ensemble porte des eaux souterraines dans son terme
d’humidité du sol pour amortir le résultat partout.

Cela aligne aussi les deux jeux de données l’un sur l’autre. La voie 2.2 part du même modèle et retranche ses eaux souterraines du profil, et
par l’identité ci-dessus `SoilMoist_P − GWS` *est* la zone racinaire. Les couches d’humidité du sol des deux jeux de données décrivent donc le
même réservoir du même modèle.

Ce que le changement ne règle pas, c’est la profondeur. Noah somme 0–200 cm, la zone racinaire de Catchment s’arrête à 100 cm et les deux
couches inférieures de VIC varient selon le lieu : l’ensemble moyenne donc toujours trois colonnes de sol différentes. C’est un désaccord
ordinaire entre modèles, du genre que la dispersion entre eux est là pour exprimer, et c’est autre chose que de compter les eaux souterraines
comme de l’humidité du sol.

## GLDAS 2.2 et la correction par GRACE { #gldas-22-and-the-grace-correction }

![En quoi les voies 2.1 et 2.2 vers les eaux souterraines diffèrent](../../static/images/grace/gldas-2.1-vs-2.2.png)

GLDAS 2.2 est un seul produit quotidien : le modèle Catchment à 0.25°, démarré le 1er février 2003 depuis l’état Catchment de GLDAS-2.0.

Ce qui le distingue, c’est que l’anomalie de stockage total de l’eau mesurée par GRACE est assimilée dans la simulation (Li et al., 2019), au
moyen de la machinerie d’assimilation du Land Information System (Kumar et al., 2016). Le modèle Catchment a été retenu pour cela en raison de
sa façon de traiter l’eau sous la surface : il suit un déficit en eau du bassin qui tient lieu de profondeur de la nappe, de sorte que les eaux
souterraines sont un état que le modèle propage plutôt qu’une quantité déduite après coup. C’est ce qui donne à l’assimilation un endroit où
déposer une correction.

GRACE mesure toute la colonne et ne peut pas voir à quel réservoir appartient un écart : le schéma répartit donc la correction de chaque mois
entre les réservoirs du modèle, dont les eaux souterraines. L’épuisement dû au pompage n’atteint l’état d’eau souterraine de 2.2 que par cette
voie. La physique du modèle ne comporte toujours pas de puits.

La solution GRACE assimilée dans 2.2 est le produit de mascons du **CSR** (Save et al., 2012, 2016), tandis que les couches GRACE de
l’application elle-même utilisent les mascons du **JPL**. Les deux voies vers les eaux souterraines ne reposent donc pas sur la même solution
GRACE, et elles ne concorderont pas exactement, même là où toutes deux fonctionnent bien.


## La sortie, et où l’application la prend { #output-and-where-the-app-gets-it }

GLDAS publie à des pas de 3 heures et quotidiens, avec des moyennes mensuelles construites à partir des fichiers de 3 heures. Ce qui existe
diffère selon la version, et l’application retient la valeur mensuelle dans les deux cas :

| | Publié comme | Résolutions | L’application lit |
|---|---|---|---|
| **GLDAS-2.0** | 3 heures, quotidien, mensuel | 1°, 0.25° | rien |
| **GLDAS-2.1** | 3 heures, mensuel | 1°, 0.25° | les fichiers mensuels |
| **GLDAS-2.2** | quotidien seulement | 0.25° | les fichiers quotidiens, moyennés sur les mois calendaires |

Les fichiers de 2.1 viennent de l’archive GES DISC au format NetCDF-4, un fichier par modèle et par mois : `GLDAS_NOAH025_M.2.1`,
`GLDAS_VIC10_M.2.1` et `GLDAS_CLSM10_M.2.1`. Un compte Earthdata Login est nécessaire pour les télécharger, et ils sont aussi accessibles par
Earthdata Search, OPeNDAP, THREDDS et le subsetter de GES DISC.

GLDAS 2.2 n’a pas de produit mensuel, et l’application en construit donc un. Elle lit la collection quotidienne `GLDAS_CLSM025_DA1_D.2.2` à
travers Google Earth Engine, qui porte les mêmes champs, moyenne chaque mois calendaire et stocke le résultat. C’est aussi pourquoi
l’enregistrement 2.2 dans l’application est mensuel comme tout le reste et non quotidien.

Les deux versions sont en retard sur le présent : le flux de production principal de 2.1 de trois à quatre mois, celui de 2.2 de deux à six,
puisqu’il attend le champ GRACE qu’il assimile. Chacune a en plus un flux précoce à environ 1.5 mois, ce qui pour 2.2 signifie aucune
assimilation GRACE. L’application lit les flux principaux : le mois le plus récent qu’elle affiche a donc quelques mois, et tous les mois 2.2
qu’elle contient ont été corrigés.

## Exactitude, et mélange des versions { #accuracy-and-mixing-versions }

La NASA énumère quatre sources d’erreur dans les estimations GLDAS : l’incertitude du forçage météorologique, qui est la pire aux hautes
latitudes, en altitude et là où les stations météorologiques sont rares ; les représentations simplifiées de processus complexes dans les
modèles ; les erreurs sur les paramètres de surface décrivant la végétation, les sols et l’élévation ; et la calibration insuffisante des
paramètres des modèles. Aucune n’est rapportée sous forme de nombre à côté des données, et c’est pourquoi la bande d’incertitude de
l’application pour la voie 2.1 est construite à partir de la dispersion entre les trois modèles plutôt qu’à partir de quoi que ce soit que
publie la NASA.

La NASA met aussi en garde contre l’assemblage des versions de GLDAS en une seule série temporelle : leurs jeux de forçage sont biaisés les uns
par rapport aux autres, et l’assimilation modifie aussi bien les états que les flux dans 2.2. L’application ne les raccorde jamais. Chaque jeu
de données est son propre enregistrement d’un bout à l’autre, et lorsque les deux sont affichés sur un même graphique ils sont tracés comme des
séries distinctes. Ils partagent bien la période de référence 2004–2009, ce qui les place sur un zéro commun et rend la comparaison lisible ; ce
sont les enregistrements qui restent séparés, pas la période de référence.

## Références { #references }

- Rodell, M., Houser, P. R., Jambor, U., Gottschalck, J., Mitchell, K., Meng, C.-J., et al. (2004). The Global Land Data Assimilation System.
  *Bulletin of the American Meteorological Society*, 85(3), 381–394.
  [doi:10.1175/BAMS-85-3-381](https://doi.org/10.1175/BAMS-85-3-381){:target="_blank"}

- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE data assimilation for groundwater
  and drought monitoring: Advances and challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
  L’étude dont GLDAS 2.2 est issu, et la référence sur ce que l’assimilation fait aux eaux souterraines.

- Kumar, S. V., Zaitchik, B. F., Peters-Lidard, C., Rodell, M., Reichle, R., Li, B., et al. (2016). Assimilation of gridded GRACE terrestrial
  water storage estimates in the North American Land Data Assimilation System. *Journal of Hydrometeorology*, 17(7), 1951–1972.
  [doi:10.1175/JHM-D-15-0157.1](https://doi.org/10.1175/JHM-D-15-0157.1){:target="_blank"}

- Koster, R. D., Suarez, M. J., Ducharne, A., Stieglitz, M., and Kumar, P. (2000). A catchment-based approach to modeling land surface processes
  in a general circulation model: 1. Model structure. *Journal of Geophysical Research*, 105(D20), 24809–24822.
  [doi:10.1029/2000JD900327](https://doi.org/10.1029/2000JD900327){:target="_blank"}

- Ducharne, A., Koster, R. D., Suarez, M. J., Stieglitz, M., and Kumar, P. (2000). A catchment-based approach to modeling land surface processes
  in a general circulation model: 2. Parameter estimation and model demonstration. *Journal of Geophysical Research*, 105(D20), 24823–24838.
  [doi:10.1029/2000JD900328](https://doi.org/10.1029/2000JD900328){:target="_blank"}

- Rui, H., and Beaudoing, H. (2025). *README Document for NASA GLDAS Version 2 Data Products*. NASA GES DISC.
  [hydro1.gesdisc.eosdis.nasa.gov](https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_CLSM025_DA1_D.2.2/doc/README_GLDAS2.pdf){:target="_blank"}
  La documentation propre de la NASA pour les produits GLDAS, et la source du forçage, des périodes d’enregistrement, des versions des modèles
  et des mises en garde de cette page. Sa section « Data Interpretation » est d’où viennent l’imbrication des trois réservoirs d’humidité du sol
  du modèle Catchment et la définition de son stockage d’eau souterraine.

- Données GLDAS au NASA GES DISC : [Noah](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_M_2.1/summary){:target="_blank"},
  [VIC](https://disc.gsfc.nasa.gov/datasets/GLDAS_VIC10_M_2.1/summary){:target="_blank"},
  [CLSM](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM10_M_2.1/summary){:target="_blank"},
  [Catchment GRACE-DA1 2.2](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM025_DA1_D_2.2/summary){:target="_blank"}
