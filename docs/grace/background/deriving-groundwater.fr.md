# Calcul du Stockage des Eaux Souterraines

## Le bilan hydrique { #the-water-balance }

GRACE mesure la variation totale de l’eau stockée dans une colonne de la Terre. Pour isoler les eaux souterraines, l’application soustrait les
parties de ce total qui peuvent être estimées par d’autres moyens :

![Composantes du stockage d’eau terrestre](../../static/images/grace/grace-water-balance.png)

La TWSa est la somme des anomalies de tous les réservoirs de la colonne : équivalent en eau de la neige (SWEa), eau retenue par la canopée
végétale (CANa), humidité du sol (SMa), eaux souterraines (GWSa) et eaux de surface des rivières, lacs et réservoirs. Les modèles de surface
terrestre estiment bien les trois premiers termes. En les retirant, il reste les eaux souterraines :

$$
\mathrm{GWSa} = \mathrm{TWSa} - (\mathrm{SWEa} + \mathrm{CANa} + \mathrm{SMa})
$$

L’application ne fait pas figurer les eaux de surface dans le bilan : toute variation du stockage des eaux de surface se retrouve donc dans la
GWSa. Dans la majeure partie du monde, les variations des eaux de surface sont faibles par rapport aux autres termes. Dans les régions comportant
de grands réservoirs, des zones humides ou des fleuves aux crues importantes (l’Amazone, le Gange et le Brahmapoutre, la mer Caspienne, le lac
Victoria, le lac Volta), la GWSa inclut ces variations et surestime l’amplitude saisonnière des eaux souterraines. Dans le bassin de la Volta, par exemple, le lac représente environ la moitié
du signal total de stockage ([étude de cas](../case-studies/volta.md)).

## Les modèles de surface terrestre GLDAS { #gldas-land-surface-models }

Le Global Land Data Assimilation System (GLDAS) de la NASA fait tourner des modèles de surface terrestre forcés par les précipitations, le
rayonnement et les données météorologiques observés afin d’estimer la quantité d’eau stockée chaque mois à la surface des terres. L’application
utilise trois modèles GLDAS version 2.1, qui diffèrent par leur représentation des couches de sol et du ruissellement :

| Modèle | Grille | Humidité du sol utilisée |
|---|---|---|
| Noah | 0.25° | quatre couches, 0–200 cm |
| VIC (Variable Infiltration Capacity) | 1° | trois couches, profondeurs variables selon le lieu |
| CLSM (Catchment Land Surface Model) | 1° | profil de sol complet |

De chaque modèle, l’application extrait l’équivalent en eau de la neige, le stockage par interception de la canopée et l’humidité du sol, les
convertit de kg/m² en cm d’eau et place les trois modèles sur la même grille de 1° (Noah est moyenné de 0.25° à 1°). L’anomalie de chaque modèle
est sa valeur moins la moyenne 2004–2009 de la maille, soit la même période de référence que GRACE.

Les trois modèles sont souvent en désaccord, en particulier sur l’humidité du sol en profondeur. Plutôt que d’en choisir un, l’application en fait
la moyenne : SWEa, CANa et SMa sont chacun la moyenne des trois modèles, et la dispersion entre les modèles (leur écart-type) sert d’incertitude
pour chaque terme.

## Chaîne de traitement { #processing-chain }

![Chaîne de traitement de GRACE Regional Analyst](../../static/images/grace/grace-processing.png)

La TWSa de GRACE est moyennée de 0.5° à 1° et combinée à l’ensemble de modèles pour obtenir la GWSa sur une grille de 1°. L’application fournit
cinq couches : GWSa, SMa, SWEa et CANa à 1°, et TWSa à 0.5° telle que la distribue le JPL. L’utilisation de 1° pour les couches dérivées suit la
pratique courante qui consiste à combiner GRACE et les données de modèles sur la plus grossière des deux grilles ; fournir la GWSa à 0.5°
donnerait une impression de détail qu’aucun des deux jeux de données ne possède.

Aucune lacune n’est comblée. Chaque valeur mensuelle de l’application est la valeur publiée par le JPL, mise à l’échelle comme décrit ci-dessous,
combinée à l’ensemble GLDAS du même mois.

### Facteurs de gain { #gain-factors }

La solution mascon est nativement à 3°, et le fichier à 0.5° répète la valeur de chaque mascon sur ses 36 mailles : la grille publiée ne porte
donc à elle seule aucun détail plus fin qu’un mascon. Le JPL distribue dans le même fichier une grille de **facteurs de gain** destinée à
récupérer une partie de ce détail. Ils sont obtenus en faisant passer le modèle de surface terrestre CLM par le même traitement que subit GRACE,
puis en estimant maille par maille le multiplicateur qui rétablit l’amplitude initiale du modèle. La correction est une simple multiplication, le
facteur étant constant dans le temps :

$$
g'(x,y,t) = g(x,y,t) \times s(x,y)
$$

Le JPL n’applique pas cette mise à l’échelle avant de distribuer les données ; le GRACE-FO Level-3 Handbook précise qu’il revient aux
utilisateurs de l’appliquer, et son propre exemple consacré aux eaux souterraines suit la même approche TWSa moins GLDAS que cette application,
en indiquant la multiplication comme étape de prétraitement. L’application applique les facteurs à la TWSa à 0.5°, avant que celle-ci ne soit
moyennée à 1°, car la structure qu’ils ajoutent est plus fine qu’une maille de 1°.

La plupart des facteurs sont proches de 1 : environ 83 % se situent entre 0.5 et 1.5. Une maille conserve la valeur du mascon non mise à
l’échelle dans deux cas.

**Là où le JPL ne publie aucun facteur.** Il s’agit de l’océan, que le masque continental de GLDAS retire de toute façon, et de la glace : toute
l’Antarctique et 18 % des terres au nord de 60°N. Les facteurs ne sont pas destinés à la glace, car CLM ne représente ni les calottes glaciaires
ni les glaciers de montagne. Cela concerne 5.6 % des mailles que dessine l’application.

**Là où le facteur est implausible**, c’est-à-dire nul ou négatif, ou supérieur à 3. Cela représente 1 604 mailles sur la grille à 0.5°, soit
0.74 % du total, et c’est une règle de l’application et non du JPL : le fichier déclare valide l’ensemble de sa plage et ne fixe aucune borne.

Ce que ces mailles ont en commun, c’est que la régression produisant le facteur disposait de très peu de signal : sa pente est donc instable.
Elles sont côtières environ trois fois plus souvent que les mailles conservées (51 % à moins de deux mailles de l’eau, contre 19 %) et portent de
la neige toute l’année treize fois plus souvent (18.5 % contre 1.4 %). Près de la moitié ne relève ni de l’un ni de l’autre et se situe dans des
intérieurs arides — le Kalahari, l’intérieur australien, le Karoo, l’Atacama — où la variation de stockage de CLM est suffisamment faible pour
que l’ajustement divise par presque rien. Glace, littoral et désert sont la même défaillance dans trois contextes : c’est pourquoi une borne sur
le facteur les détecte là où un masque de glaciers seul n’y parviendrait pas.

Dans ces mailles, les facteurs vont jusqu’à 24 et −1.35. Un facteur négatif inverse le signe de l’anomalie ; un facteur de 24 a transformé
−292 cm en −7048 cm sur l’île d’Ellesmere. Dans les bassins arides, l’exclusion est sans conséquence dans un sens comme dans l’autre — quatre des
806 mailles du Grand Bassin Artésien, pour un déplacement de 0.00 cm de sa série — car une petite anomalie multipliée par un mauvais facteur
reste petite.

Elle compte en revanche dans au moins un endroit qu’un utilisateur remarquerait. Une de ces mailles tombe dans le **bassin du Caucase du Nord**,
un aquifère des jeux de régions de l’application. Appliquer tous les facteurs a doublé la série des eaux souterraines de ce bassin : l’écart-type
de sa moyenne est passé de 13.3 cm sans mise à l’échelle à 23.5 cm, et s’établit à 13.6 cm dès lors que les mailles implausibles sont laissées
telles quelles. Presque toute cette amplitude apparente venait d’une poignée de mailles dégénérées, et non du signal. Le gain que les facteurs
servent à rétablir survit à la règle : la Vallée Centrale de Californie le conserve entièrement, de 10.2 cm à 12.4 cm, et le Congo presque
entièrement, de 7.6 cm sans mise à l’échelle à 7.9 cm, contre 8.1 cm avec tous les facteurs appliqués.

Deux bassins glaciaires des jeux de bassins fluviaux, l’Alsek et le Santa Cruz, présentent une GWSa très élevée quoi qu’on fasse des facteurs de
gain. GRACE y détecte la perte de masse glaciaire et GLDAS ne modélise pas les glaciers : le bilan hydrique l’attribue donc aux eaux
souterraines. Ces valeurs sont un artefact de la méthode, non de la mise à l’échelle.

Ce que les facteurs ne font pas, c’est transformer la grille à 0.5° en 36 mesures indépendantes. Le mascon sous-jacent reste une estimation
unique, et les facteurs redistribuent son amplitude selon l’idée qu’un modèle se fait de la variation du stockage en son sein. Le handbook est
explicite : les modèles qui les sous-tendent comportent des biais et « n’incluent typiquement ni les eaux souterraines ni les activités humaines
dans leurs simulations ». Un aquifère intensément pompé est donc précisément l’endroit où la redistribution est la moins informée par ce que
l’on mesure.

## Incertitude { #uncertainty }

Chaque couche de l’application est accompagnée d’une incertitude à un écart-type (1σ), que le graphique des séries temporelles trace sous forme
de bande autour de la courbe :

- **TWSa :** l’incertitude publiée par le JPL pour chaque mascon et chaque mois, multipliée par le même facteur de gain que les données, afin
  que la bande reste proportionnelle à la valeur qu’elle décrit.
- **SWEa, CANa, SMa :** l’écart-type entre les trois modèles GLDAS.
- **GWSa :** les quatre combinées, en les supposant indépendantes :

$$
\sigma_{\mathrm{GWSa}} = \sqrt{\sigma_{\mathrm{TWSa}}^2 + \sigma_{\mathrm{SWEa}}^2 + \sigma_{\mathrm{CANa}}^2 + \sigma_{\mathrm{SMa}}^2}
$$

La bande d’incertitude rend compte de l’erreur de mesure de GRACE et du désaccord entre les modèles. Elle ne rend pas compte des erreurs
communes aux trois modèles, de l’effet de l’omission des eaux de surface, de la fuite du signal provenant de l’extérieur d’une région (voir
[Résolution, Fuite du Signal et Petites Régions](resolution-and-leakage.md)), ni de l’incertitude des facteurs de gain eux-mêmes, que le JPL ne
publie pas : l’incertitude réelle est donc plus grande que ne l’indique la bande.

Une précaution sur leur combinaison : l’incertitude TWSa du JPL est une erreur de mesure, tandis que les trois termes GLDAS correspondent à la
dispersion entre Noah, VIC et CLSM, qui mesure l’ampleur du désaccord entre les modèles plutôt que celle de leur erreur. Les additionner en
quadrature traite les deux comme comparables. Sur la plupart des bassins, la dispersion entre modèles domine : dans le Congo, 3.1 cm pour GRACE
contre 5.7 cm au total.

## À quoi sert la GWSa { #what-gwsa-is-good-for }

La GWSa est surtout utile pour répondre à des questions régionales de sens et de rythme d’évolution : le stockage de cet aquifère diminue-t-il, à
quelle vitesse, et la baisse a-t-elle ralenti après un changement de politique ou une série d’années humides ? Elle ne convient pas aux décisions
à l’échelle d’un champ captant ou d’un périmètre irrigué, et elle n’apporte aucune information sur les niveaux piézométriques ni sur la qualité
de l’eau. Là où des piézomètres existent, comparez la tendance GRACE avec la variation de stockage estimée à partir des puits ; l’accord entre les
deux renforce l’une et l’autre.

## Références { #references }

- Rodell, M., et al. (2004). The Global Land Data Assimilation System. *Bulletin of the American Meteorological Society*, 85, 381–394.
  [doi:10.1175/BAMS-85-3-381](https://doi.org/10.1175/BAMS-85-3-381){:target="_blank"}
- Données GLDAS au NASA GES DISC : [Noah](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_M_2.1/summary){:target="_blank"},
  [VIC](https://disc.gsfc.nasa.gov/datasets/GLDAS_VIC10_M_2.1/summary){:target="_blank"},
  [CLSM](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM10_M_2.1/summary){:target="_blank"}
