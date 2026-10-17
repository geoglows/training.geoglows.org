# Pourquoi les deux jeux de données diffèrent

L’application sert deux enregistrements d’eau souterraine pour le même mois et la même maille, et ils ne concordent pas. Cette page traite de
l’origine du désaccord. [Quand se fier à chacun](trusting-each-one.md) traite de celui qu’il faut croire, et
[Artefacts connus](known-artifacts.md) rassemble les endroits où l’un des deux se trompe tout simplement.

[Calcul du stockage d’eau souterraine](../gldas/deriving-groundwater.md) donne les deux constructions en entier. En bref :

- **La voie GRACE.** Le JPL mesure le stockage total d’eau. L’application retranche l’humidité du sol, la neige et l’eau de la canopée de
  GLDAS 2.1, et lit le reste comme de l’eau souterraine.
- **La voie GLDAS 2.2.** La NASA fait tourner le modèle de surface terrestre Catchment avec GRACE assimilé dedans, et le modèle rapporte
  directement un état d’eau souterraine. Rien n’est retranché.

## Ce qui diffère déjà avant de compter la moindre goutte { #what-already-differs-before-any-water-is-counted }

| | Voie GRACE | GLDAS 2.2 |
|---|---|---|
| Solution GRACE | mascons du JPL, RL06.3 v04 CRI | mascons du CSR, RL06 |
| Empreinte GRACE native | calottes de 3° à surface égale | 1° à surface égale à l’équateur |
| Grille servie | 1° | 0.25°, moyennée à 1° pour la grille globale |
| Début de l’enregistrement | avril 2002 | février 2003 |
| Mois manquants | les lacunes de GRACE, comblées ou signalées | aucun ; le modèle les traverse sans correction |
| Facteurs de gain | ceux du JPL, appliqués | aucun |
| Couches d’incertitude | publiées par maille | aucune |
| Mailles de terre sur la grille à 1° | 15 159 | 17 346 |

Le début de l’enregistrement et le masque de terre relèvent de la comptabilité, et apparaissent comme des données manquantes plutôt que comme un
désaccord. Toutes les autres lignes changent les chiffres.

## Deux groupes, une paire de satellites { #two-groups-one-pair-of-satellites }

GRACE n’a jamais mesuré d’eau. Il a mesuré la distance entre deux satellites, à quelques microns près, pendant qu’ils tombaient autour de la Terre
et que la masse située en dessous les tirait. Reconstituer une carte des masses à partir de cet enregistrement est sous-déterminé — bien des
répartitions de masse différentes s’accordent avec les mêmes orbites — et chaque centre de traitement impose donc des hypothèses supplémentaires
pour aboutir à une réponse unique. Le JPL et le CSR en imposent de différentes.

| | JPL | CSR |
|---|---|---|
| Résolu sur | calottes sphériques de 3° à surface égale | grille géodésique à surface égale, 1° à l’équateur |
| Livré en | 0.5° | 0.25° |
| Régularisation | contrainte informée par un modèle de surface terrestre | contrainte tirée des seules données GRACE, paramètre choisi par une L-ribbon |
| Côtes | un filtre CRI sépare terre et océan à l’intérieur d’un mascon à cheval | les tuiles côtières sont coupées en deux le long de la côte |
| Facteurs d’échelle | publiés, et le JPL recommande de les appliquer | le CSR indique que ses mascons n’en ont pas besoin |

Scanlon et al. (2016) ont comparé les mascons du CSR et du JPL entre eux et aux harmoniques sphériques remises à l’échelle sur 176 bassins
fluviaux, et ont trouvé des séries d’eau totale corrélant pour la plupart au-dessus de 0.9, les tendances restant la part qui diverge. Cela
correspond à ce que font ici les deux jeux de données : sur les 37 bassins WHYMAP, les séries de TWSa corrèlent à une médiane de 0.87, et 15 des
37 dépassent 0.9. L’accord se dégrade à mesure que la région rétrécit, et maille par maille sur tout le globe la corrélation médiane de TWSa vaut
0.75.

## Répartir l’écart entre ses deux causes { #splitting-the-difference-into-its-two-causes }

Les deux jeux de données satisfont le même bilan hydrique, TWSa = GWSa + SMa + SWEa + CANa. En notant REST tout ce qui n’est pas de l’eau
souterraine, l’écart entre les deux séries d’eau souterraine est donc fixé par deux autres écarts :

$$ d_{GW} = d_{TWS} - d_{REST} $$

Chaque terme se mesure. Maille par maille, médianes pondérées par la surface entre 2003-02 et 2026-06 :

| | RMS | part médiane de la variance de d<sub>GW</sub> |
|---|---:|---:|
| d<sub>GW</sub>, l’écart d’eau souterraine que l’on voit | 6.42 cm | — |
| d<sub>TWS</sub>, les deux solutions GRACE en désaccord | 5.73 cm | 0.85 |
| d<sub>REST</sub>, la colonne partagée autrement | 3.38 cm | 0.32 |

Les parts dépassent 1 ensemble parce que les deux écarts sont en partie corrélés.

Moyenné sur un bassin, l’équilibre se déplace. Les médianes par bassin valent 0.72 pour d<sub>TWS</sub> et 0.32 pour d<sub>REST</sub>, et dans 11
des 37 bassins le partage est le plus grand des deux. La moyenne annule une bonne part du bruit de maille des solutions GRACE tout en laissant
l’écart systématique dans la façon de diviser la colonne : plus la région est grande, plus le désaccord porte sur le partage et moins sur JPL
contre CSR.

L’eau souterraine diverge partout plus que l’eau totale. Maille par maille, les médianes valent 0.42 pour la GWSa contre 0.75 pour la TWSa ; par
bassin, 0.61 contre 0.87. Plus une grandeur s’éloigne de la mesure brute, plus les deux constructions s’écartent.

## Ce que dit la littérature sur la soustraction { #what-the-literature-says-about-the-subtraction }

Getirana, Kumar et Rodell (2025) soutiennent que la méthode du résidu — retrancher de la TWS de GRACE l’humidité du sol, la neige et l’eau de la
canopée modélisées, puis lire le reste comme de l’eau souterraine — repose sur une hypothèse qui ne tient pas : que les modèles représentent
chaque réservoir autre que l’eau souterraine dans des compartiments séparés et physiquement signifiants. Ils demandent aux utilisateurs de peser
ce que les simplifications et les conventions des modèles font au résultat, et recommandent l’assimilation de données et des modèles dotés d’une
représentation plus complète du sous-sol.

Cette critique vise la voie GRACE de cette application, et les sections sur les cycles saisonniers de
[Quand se fier à chacun](trusting-each-one.md) chiffrent un cas précis. Elle ne rend pas la voie GRACE inutile. Scanlon et al. (2018) ont comparé
sept modèles globaux à trois solutions GRACE sur 186 bassins fluviaux et ont trouvé que les modèles sous-estiment gravement les grandes tendances
décennales que voit GRACE, dans les deux sens, ce qui est une raison de garder la mesure dans le tableau plutôt que de confier la question à un
modèle. Les deux articles pointent dans le même sens : prendre le partage du modèle le mieux posé et l’ampleur du changement de la mesure.

## Références { #references }

- Getirana, A., Kumar, S., et Rodell, M. (2025). Inconsistencies in GRACE-Based Groundwater Storage Estimation — A Call for a Proper Use of
  Land Surface Models. *Geophysical Research Letters*, 52, e2025GL119197.
  [doi:10.1029/2025GL119197](https://doi.org/10.1029/2025GL119197){:target="_blank"}
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE Data Assimilation for Groundwater
  and Drought Monitoring: Advances and Challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
- Save, H., Bettadpur, S., et Tapley, B. D. (2016). High-resolution CSR GRACE RL05 mascons. *Journal of Geophysical Research: Solid Earth*,
  121, 7547–7569. [doi:10.1002/2016JB013007](https://doi.org/10.1002/2016JB013007){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., et Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
