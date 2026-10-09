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

Aucun facteur de gain ou d’échelle n’est appliqué aux données GRACE, et aucune lacune n’est comblée. Chaque valeur mensuelle de l’application est
la valeur publiée par le JPL combinée à l’ensemble GLDAS du même mois.

## Incertitude { #uncertainty }

Chaque couche de l’application est accompagnée d’une incertitude à un écart-type (1σ), que le graphique des séries temporelles trace sous forme
de bande autour de la courbe :

- **TWSa :** l’incertitude publiée par le JPL pour chaque mascon et chaque mois.
- **SWEa, CANa, SMa :** l’écart-type entre les trois modèles GLDAS.
- **GWSa :** les quatre combinées, en les supposant indépendantes :

$$
\sigma_{\mathrm{GWSa}} = \sqrt{\sigma_{\mathrm{TWSa}}^2 + \sigma_{\mathrm{SWEa}}^2 + \sigma_{\mathrm{CANa}}^2 + \sigma_{\mathrm{SMa}}^2}
$$

La bande d’incertitude rend compte de l’erreur de mesure de GRACE et du désaccord entre les modèles. Elle ne rend pas compte des erreurs communes
aux trois modèles, de l’effet de l’omission des eaux de surface, ni de la fuite du signal provenant de l’extérieur d’une région (voir
[Résolution, Fuite du Signal et Petites Régions](resolution-and-leakage.md)) : l’incertitude réelle est donc plus grande que ne l’indique la bande.

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
