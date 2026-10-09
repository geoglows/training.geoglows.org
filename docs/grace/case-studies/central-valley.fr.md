# Vallée Centrale de Californie : corriger GRACE avec des données de puits

!!! cite "Article"
    Stevens, M. D., Ramirez, S. G., Martin, E.-M. H., Jones, N. L., Williams, G. P., Adams, K. H., Ames, D. P., and Pulla, S. T. (2025).
    **Groundwater storage loss in the Central Valley analysis using a novel method based on in situ data compared to GRACE-derived data.**
    *Environmental Modelling & Software*, 186, 106368.
    [doi:10.1016/j.envsoft.2025.106368](https://doi.org/10.1016/j.envsoft.2025.106368){:target="_blank"}

## Contexte { #setting }

La Vallée Centrale de Californie mesure environ 700 km de long et 80 km de large, soit environ 52 000 km², et c'est l'un des systèmes aquifères les plus exploités par pompage au
monde. Elle est plus étroite qu'un seul mascon GRACE de 3° (environ 333 × 264 km à cette latitude), et la baisse due aux pompages est concentrée dans la vallée
tandis que les montagnes environnantes se comportent différemment. C'est donc un cas d'école de [fuite du signal](../background/resolution-and-leakage.md#leakage) :
moyenné sur la vallée, GRACE sous-estime la perte de stockage.

## Une estimation indépendante à partir des puits { #an-independent-estimate-from-wells }

L'étude a construit une série de stockage à partir des données de puits pour 1960–2020 :

![Analyse du stockage des eaux souterraines à partir de données in situ](../../static/images/grace/papers/cv-fig3-workflow.webp)

*Analyse du stockage des eaux souterraines à partir de données in situ. (a) les puits présentant des lacunes sont identifiés, (b) les lacunes sont imputées par un algorithme
d'apprentissage automatique en plusieurs étapes s'appuyant sur des observations de la Terre, (c) une interpolation temporelle puis spatiale produit des rasters de niveau d'eau
variables dans le temps, (d) les rasters de niveau d'eau sont combinés aux coefficients d'emmagasinement pour estimer la variation du stockage des eaux souterraines à chaque pas de temps.
Reproduit de Stevens et al. (2025), Fig. 3, © 2025 Elsevier, réutilisé en vertu des droits des auteurs.*

1. Les puits des bases de données de l'USGS et du California Department of Water Resources ont été sélectionnés selon la longueur de leur série ; l'étude a comparé des seuils de
   150, 75 et 50 mois d'observations (181, 572 et 921 puits).
2. Les lacunes de la série de chaque puits ont été comblées en deux étapes : un modèle d'apprentissage automatique (une extreme learning machine) piloté par le Palmer Drought
   Severity Index et l'humidité du sol GLDAS, puis un affinement itératif utilisant les trois puits voisins les mieux corrélés.
3. Les séries comblées ont été krigées en surfaces mensuelles de niveau d'eau sur une grille de 0.1°.
4. Les variations de niveau d'eau ont été converties en variations de stockage à l'aide de la carte de rendement spécifique du Central Valley Hydrologic Model (CVHM) de l'USGS.

Avec le seuil de 75 mois, la courbe de stockage issue des puits concorde étroitement avec le CVHM (r² = 0.87, RMSE 9.04 km³).

## Calibration de GRACE { #calibrating-grace }

La GWSa GRACE de la vallée, convertie en volume, suivait la courbe issue des puits dans sa chronologie mais était beaucoup plus faible. La multiplier par un facteur d'échelle
corrigeait la fuite du signal. Le meilleur facteur était d'environ 5 (± 1.0) ; avec ce facteur, GRACE et les puits concordaient avec r² = 0.725, une erreur moyenne de −14.4 km³
et une RMSE de 21.2 km³ sur 2002–2021.

![Comparaison de la courbe de stockage issue des puits avec GRACE multiplié par 5](../../static/images/grace/papers/cv-fig11-grace-75obs.webp)

*Comparaison de l'Iterative Well Imputation avec GRACE, sur le jeu de données au seuil de 75 mois d'observations. Reproduit de Stevens et al. (2025), Fig. 11,
© 2025 Elsevier, réutilisé en vertu des droits des auteurs.*

Avec ce facteur appliqué, les pertes de stockage GRACE concordent avec la plupart des estimations publiées pour les mêmes périodes :

| Étude publiée | Période | Perte publiée | GRACE × 5 dans cette étude |
|---|---|---|---|
| Famiglietti et al. (2011) | oct. 2003 – mars 2010 | 20.3 km³ | 26.7 km³ |
| Scanlon et al. (2012) | oct. 2006 – mars 2010 | 31 km³ | 31.1 km³ |
| Xiao et al. (2017) | avr. 2002 – sept. 2016 | 64.6 km³ | 70.7 km³ |
| Ojha et al. (2018) | déc. 2006 – janv. 2010 | 21.3 km³ | 53.2 km³ |

## Conclusions { #conclusions }

- Des séries de puits comblées peuvent produire un historique du stockage qui concorde avec un modèle régional calibré des eaux souterraines.
- Cet historique permet de calibrer directement un facteur d'échelle de fuite du signal pour GRACE, d'environ 5 pour la Vallée Centrale.
- Une fois calibré, GRACE peut suivre la variation du stockage dans la vallée à l'avenir, et la même approche pourrait s'appliquer aux régions pauvres en données disposant
  de quelques séries de puits.

**Pour les utilisateurs de l'application :** pour un aquifère petit ou étroit, la moyenne GRACE fournie par l'application restitue la chronologie et le sens de la variation du stockage mais peut
en sous-estimer l'ampleur de plusieurs fois. Un facteur d'échelle calibré sur des puits corrige ce biais, pour cet aquifère uniquement.
