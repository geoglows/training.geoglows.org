# Jusqu’où cela est validé

[Lequel utiliser](which-one-to-use.md) formule des recommandations. Cette page dit sur quoi elles reposent, afin que vous puissiez juger du poids
à accorder à chacune.

## Ce qu’établit la comparaison de ces pages { #what-the-comparison-on-these-pages-establishes }

Les chiffres de [Pourquoi les deux jeux de données diffèrent](why-they-differ.md) et de [À quoi ressemblent les écarts](examples.md) proviennent
de la comparaison des deux jeux de données publiés entre eux. Cela établit comment ils diffèrent, de combien, et par quel terme. Cela ne tranche
rien quant à savoir lequel est le plus proche de la nappe, car aucun des deux n’y est confronté à des niveaux d’eau mesurés.

Que deux jeux de données divergent indique qu’au moins l’un des deux se trompe. Cela ne dit pas lequel.

## Là où des puits ont réellement été consultés { #where-wells-have-actually-been-consulted }

Deux études ont comparé ces jeux de données à des niveaux d’eau souterraine observés. Toutes deux sont l’œuvre de notre groupe avec des
collaborateurs, toutes deux sont publiées, et toutes deux portent sur une seule région.

### La Central Valley de Californie { #californias-central-valley }

Stevens et al. (2025) ont construit un enregistrement de stockage à partir de puits des bases de l’USGS et du California Department of Water
Resources, comblé par un schéma d’apprentissage automatique et converti en stockage à l’aide de la carte de porosité efficace du Central Valley
Hydrologic Model de l’USGS. Au seuil de 75 mois d’enregistrement (572 puits), la courbe fondée sur les puits s’accordait étroitement à ce modèle
calibré, à r² = 0,87 et RMSE 9,04 km³.

Face à cet enregistrement, l’eau souterraine GRACE de l’application suivait bien le calendrier — r² = 0,725 sur 2002–2021 — tout en étant
plusieurs fois trop faible. L’étude a calibré un facteur d’échelle d’environ 5 (± 1,0) pour l’aligner. GLDAS 2.2, qui perd 6 cm sur
l’enregistrement là où la voie GRACE en perd 32, est le plus éloigné des trois de ce que montrent les puits.

Voir [Central Valley](../case-studies/central-valley.md) pour la méthode et les figures.

### Le bassin de la Volta { #the-volta-basin }

Barbosa et al. (2025) ont estimé la recharge par la méthode de fluctuation de la nappe à partir des deux jeux de données et ont comparé le
résultat à des puits :

| Source | Recharge |
|:---|:---:|
| Voie GRACE, méthode WTF 1 | 5,8 cm/an |
| Voie GRACE, méthode WTF 2 | 10,7 cm/an |
| Puits du sous-bassin de Nasia, porosité efficace 0,05 | 10,4 cm/an |
| Obuobie et al. (2012), estimation indépendante antérieure | 8,6 cm/an |
| GLDAS 2.2, méthode WTF 1 | 17,4 cm/an |
| GLDAS 2.2, méthode WTF 2 | 36,1 cm/an |

La voie GRACE encadre le chiffre issu des puits. GLDAS 2.2 se situe bien au-dessus de toutes les autres estimations. Cette étude est le fondement
de la recommandation d’employer GRACE pour la recharge.

Voir [Bassin de la Volta](../case-studies/volta.md), qui montre aussi que le lac Volta représente environ la moitié du signal de stockage du
bassin.

## Les éléments derrière chaque recommandation { #the-evidence-behind-each-recommendation }

### 2.2 aplatit les tendances { #22-flattens-trends }

Le soutien le plus fort vient de l’équipe qui a construit GLDAS 2.2. Li et al. (2019) ont validé l’assimilation sur des données in situ
d’environ 4 000 puits et ont trouvé qu’elle améliorait le modèle seul : erreurs réduites de 36 % et corrélation améliorée de 16 % à l’échelle
régionale, 10 % et 22 % en des points individuels. Ils en énoncent aussi la limite sans détour — l’assimilation **ne peut pas compenser l’absence
d’un schéma de prélèvement d’eau souterraine dans le modèle Catchment dans les zones de pompage intensif.** C’est le mécanisme derrière chaque
ligne du tableau des tendances, énoncé par les auteurs mêmes du produit.

Scanlon et al. (2018) ont trouvé le même déficit pour les modèles en général : sept modèles mondiaux de surface terrestre et de ressources en eau
face à GRACE sur 186 bassins fluviaux, 2002–2014, les médianes des modèles sous-estimant largement aussi bien les fortes tendances à la baisse
que voit GRACE (≤ −0,5 km³/an) que les fortes tendances à la hausse (≥ 0,5 km³/an). Sommés sur les bassins, les modèles donnaient une tendance
négative du stockage continental là où GRACE en donnait une positive.

Ce que cela n’établit pas, c’est la valeur de la tendance correcte. Cela justifie de préférer GRACE à 2.2 pour un rythme de variation ; cela ne
dit pas que le chiffre GRACE est le bon. La Central Valley est le seul endroit où des puits ont été consultés, et là GRACE lui-même était
plusieurs fois trop faible.

### La méthode résiduelle est structurellement fragile { #the-residual-method-is-structurally-shaky }

Getirana, Kumar et Rodell (2025) examinent l’hypothèse qui sous-tend la voie GRACE : que les réservoirs d’humidité du sol, de neige et de canopée
d’un modèle de surface terrestre sont des compartiments distincts et physiquement signifiants contenant exactement l’eau que leurs noms
suggèrent. Ils soutiennent que les simplifications et les conventions de nomenclature des modèles rompent cette hypothèse, et recommandent des
modèles représentant la subsurface plus complètement avec assimilation de données — ce qui décrit GLDAS 2.2.

C’est un argument tiré de la construction des modèles, non une mesure face à des puits. Le motif du rapport d’humidité du sol sur 299 aquifères
dans [À quoi ressemblent les écarts](examples.md) y est cohérent, mais la cohérence n’est pas une confirmation : aucun enregistrement de puits
n’établit que le calendrier saisonnier de 2.2 soit le bon dans l’un quelconque de ces aquifères.

### Les deux solutions GRACE concordent à l’échelle du bassin et divergent sur les tendances { #the-two-grace-solutions-agree-at-basin-scale-and-diverge-on-trends }

Scanlon et al. (2016) ont comparé les produits mascon du CSR et du JPL sur 176 bassins fluviaux et ont trouvé que leurs enregistrements d’eau
totale se suivaient de près, les tendances à long terme restant la part qui diverge. C’est pourquoi la différence de construction compte le plus
pour les tendances et le moins pour le calendrier, et les deux jeux de données de cette application se comportent de même.

### Comparer tout cela à des puits est plus difficile qu’il n’y paraît { #comparing-any-of-this-against-wells-is-harder-than-it-sounds }

Chen, Famiglietti, Scanlon et Rodell (2016) notent que convertir des niveaux de puits en stockage exige une porosité efficace par puits,
elle-même incertaine même là où le réseau de suivi est dense. Bhanja et al. (2016) ont mené une telle comparaison à travers l’Inde. Les études de
la Central Valley et de la Volta dépendent toutes deux d’une porosité efficace, de sorte que leur accord en porte l’incertitude.

## Quel poids porte chaque recommandation { #how-much-weight-each-recommendation-carries }

| Recommandation | Repose sur | Force |
|:---|:---|:---|
| Employer GRACE pour l’ampleur d’une tendance | Li et al. (2019) sur le schéma de prélèvement manquant, Scanlon et al. (2018) sur 186 bassins, et les rapports mesurés ici | forte sur la direction, faible sur la magnitude |
| Employer GRACE pour la recharge | Barbosa et al. (2025) face à des puits dans un bassin | une région, une méthode |
| Préférer 2.2 pour la forme saisonnière là où l’humidité du sol oscille autant que l’eau totale | Getirana et al. (2025) sur la construction, et le motif sur 299 aquifères | mécanisme bien argumenté, aucun enregistrement de puits ne confirme quel calendrier est le bon |
| Employer 2.2 pour les petites régions et les séries continues | les grilles publiées et les périodes d’enregistrement | un fait sur les produits, non un résultat |
| Rapporter les deux quand cela compte | — | une pratique, non un résultat |

## Ce qui reste non validé { #what-is-still-unvalidated }

Aucune des études ci-dessus n’a évalué ces deux jeux de données de l’application l’un par rapport à l’autre, et aucune n’a utilisé cette
application. La validation directe par les puits atteint la Central Valley et le bassin de la Volta et s’arrête là — deux régions sur les
centaines que couvre l’application, toutes deux issues des travaux d’un seul groupe.

En particulier, rien ici n’établit :

- lequel des deux jeux de données a le bon calendrier saisonnier dans un aquifère à nappe peu profonde
- si le problème d’échelle de la voie GRACE dans la Central Valley se généralise à d’autres aquifères étroits
- comment l’un ou l’autre se comporte sous les tropiques humides, en zone de pergélisol, ou partout où l’eau de surface représente une grande
  part du signal
- une incertitude pour GLDAS 2.2, puisque la NASA n’en publie aucune et qu’il s’agit d’une unique simulation et non d’un ensemble

Traitez les recommandations comme un raisonnement fondé sur la construction de chaque jeu de données et sur un comportement mesuré, étayé par la
littérature sur chaque mécanisme, plutôt que comme un classement validé. Là où vous disposez de puits, servez-vous-en : cette comparaison
l’emporte sur tout ce que contient cette page.

## Références { #references }

- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
- Bhanja, S. N., Mukherjee, A., Saha, D., Velicogna, I., et Famiglietti, J. S. (2016). Validation of GRACE based groundwater storage anomaly
  using in-situ groundwater level measurements in India. *Journal of Hydrology*, 543, 729–738.
  [doi:10.1016/j.jhydrol.2016.10.042](https://doi.org/10.1016/j.jhydrol.2016.10.042){:target="_blank"}
- Chen, J., Famiglietti, J. S., Scanlon, B. R., et Rodell, M. (2016). Groundwater Storage Changes: Present Status from GRACE Observations.
  *Surveys in Geophysics*, 37, 397–417. [doi:10.1007/s10712-015-9332-4](https://doi.org/10.1007/s10712-015-9332-4){:target="_blank"}
- Getirana, A., Kumar, S., et Rodell, M. (2025). Inconsistencies in GRACE-Based Groundwater Storage Estimation — A Call for a Proper Use of
  Land Surface Models. *Geophysical Research Letters*, 52, e2025GL119197.
  [doi:10.1029/2025GL119197](https://doi.org/10.1029/2025GL119197){:target="_blank"}
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE Data Assimilation for Groundwater
  and Drought Monitoring: Advances and Challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., et Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
- Stevens, M. D., Ramirez, S. G., Martin, E.-M. H., Jones, N. L., Williams, G. P., Adams, K. H., Ames, D. P., et Pulla, S. T. (2025).
  Groundwater storage loss in the Central Valley analysis using a novel method based on in situ data compared to GRACE-derived data.
  *Environmental Modelling & Software*, 186, 106368.
  [doi:10.1016/j.envsoft.2025.106368](https://doi.org/10.1016/j.envsoft.2025.106368){:target="_blank"}
