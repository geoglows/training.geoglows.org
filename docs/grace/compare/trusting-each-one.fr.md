# Quand se fier à chacun

Aucun des deux jeux de données ne l’emporte partout. [Pourquoi les deux jeux de données diffèrent](why-they-differ.md) rend compte du désaccord ;
cette page dit quelle série citer pour quelle question, et donne le diagnostic à mener quand vous voulez trancher vous-même dans une région que
les tableaux ci-dessous ne couvrent pas.

## L’accord suit la taille du signal { #agreement-follows-the-size-of-the-signal }

En regroupant les mailles de terre à 1° selon l’ampleur réelle des mouvements de l’eau souterraine de GRACE :

| Écart-type de la GWSa de GRACE | corrélation médiane | écart RMS médian | mailles |
|---|---:|---:|---:|
| moins de 5 cm | 0.19 | 4.58 cm | 5 854 |
| 5–15 cm | 0.51 | 8.32 cm | 7 110 |
| plus de 15 cm | 0.77 | 27.32 cm | 2 171 |

Une maille calme qui corrèle à 0.2, ce sont deux petits signaux qui ne parviennent pas à s’aligner, et cela ne dit rien sur la solidité de l’un ou
l’autre jeu de données. Les aquifères que l’on analyserait se trouvent dans la dernière ligne. Lisez la corrélation à côté de la quantité d’eau en
jeu, jamais seule.

## Pour l’ampleur d’une tendance, utilisez GRACE { #for-the-size-of-a-trend-use-grace }

Moyennée sur les 37 grands bassins d’eau souterraine WHYMAP, la tendance de GWSa de 2.2 vaut environ le quart de celle de GRACE : un rapport médian
de 0.26 sur les bassins qui perdent du stockage et de 0.33 sur ceux qui en gagnent, l’aplatissement joue donc dans les deux sens :

| Bassin | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|---|---:|---:|---:|
| Gange-Brahmapoutre | −1.53 | −0.44 | 0.29 |
| Indus | −1.45 | −0.21 | 0.14 |
| Vallée centrale de Californie | −1.37 | −0.24 | 0.18 |
| Caucase du Nord | −1.03 | −0.68 | 0.66 |
| Plaine de Chine du Nord | −0.67 | −0.25 | 0.38 |
| Arabique | −0.65 | −0.10 | 0.16 |
| Tarim | −0.55 | −0.06 | 0.11 |
| Ogallala (High Plains) | −0.45 | −0.22 | 0.49 |
| Sahara septentrional | −0.44 | −0.10 | 0.23 |

Tendances en cm/an, moyennées par surface sur chaque bassin, de février 2003 à juin 2026.

Le pompage est absent de la physique de Catchment : l’épuisement n’atteint donc le stock d’eau souterraine de 2.2 que par la correction mensuelle
GRACE, et cette correction se répartit entre les réservoirs de surface, de zone racinaire et de profil au lieu de tomber dans la seule eau
souterraine. Entre deux corrections, le modèle se relâche vers son propre bilan hydrique.

Scanlon et al. (2018) ont trouvé le même aplatissement dans des modèles en boucle ouverte, en comparant sept d’entre eux à trois solutions GRACE
sur 186 bassins fluviaux et sur 2002–2014 : les modèles sous-estiment gravement les grandes tendances décennales que voit GRACE, dans les deux
sens, ce qu’ils attribuent à l’irrigation et aux autres usages humains, extérieurs à la physique des modèles. 2.2 est un modèle avec GRACE
assimilé et non une simulation en boucle ouverte, si bien que la correction le ramène en partie, et les rapports ci-dessus sont ce qui reste.

Trois bassins divergent sur le signe — l’Amazone, le Congo et la Petchora —, tous des endroits où la tendance est faible devant le cycle
saisonnier.

## Pour la forme du cycle saisonnier, comparez d’abord la SMa à la TWSa { #for-the-shape-of-the-seasonal-cycle-check-sma-against-twsa-first }

Les deux jeux de données peuvent différer par l’ampleur de l’oscillation saisonnière et par son calendrier. Sur les 37 bassins WHYMAP, l’amplitude
saisonnière de 2.2 vaut une médiane de 1.23 fois celle de GRACE ; sur les 31 aquifères principaux de l’USGS, 1.52. À quelques endroits elle est
plusieurs fois plus grande :

| Aquifère | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|---|---:|---:|---:|
| Willamette Lowland | 4.8 | 33.3 | 7.0 |
| Bassin parisien | 3.0 | 17.3 | 5.7 |
| Denver Basin | 1.2 | 4.7 | 4.0 |
| Northern Atlantic Coastal Plain | 2.9 | 9.9 | 3.4 |
| Bassin sénégalo-mauritanien | 5.8 | 18.7 | 3.2 |

Du pic au creux de la climatologie de GWSa en cm, tendance retirée, de février 2003 à juin 2026.

Le calendrier peut lui aussi se séparer. Dans le Northern Atlantic Coastal Plain, la GWSa de GRACE culmine en juin et celle de 2.2 en février,
quatre mois d’écart, et les deux cycles saisonniers corrèlent à −0.54. Le Sahara septentrional est décalé d’une demi-année ; l’Indus oppose mars à
septembre.

Comparer l’ampleur saisonnière de la SMa à celle de la TWSa indique quelles régions feront cela. Sur les bassins WHYMAP, le rapport entre ces deux
amplitudes corrèle à −0.65 avec la concordance des deux cycles d’eau souterraine, et à −0.83 sur les aquifères de l’USGS. Toute région dont les
cycles saisonniers tournent à l’envers a une humidité du sol qui oscille autant que l’eau totale, ou davantage :

| Aquifère | amplitude de TWSa | amplitude de SMa | SMa / TWSa | r saisonnier |
|---|---:|---:|---:|---:|
| Ogaden-Juba | 2.0 | 3.3 | 1.70 | −0.74 |
| Upper carbonate | 7.2 | 9.9 | 1.37 | −0.60 |
| Sahara septentrional | 0.5 | 0.7 | 1.35 | −0.83 |
| Cambrian-Ordovician | 9.9 | 11.4 | 1.15 | −0.38 |
| Indus | 5.7 | 6.3 | 1.11 | −0.39 |
| Northern Atlantic Coastal Plain | 7.9 | 8.4 | 1.06 | −0.54 |

Les régions où les deux s’accordent se situent entre 0.4 et 0.6.

La GWSa de la voie GRACE vaut TWSa − SMa − SWEa − CANa. Là où le cycle d’humidité du sol du modèle est aussi grand que le cycle mesuré d’eau totale
et presque en phase avec lui, le reste culmine quand l’humidité du sol est au plus sec, et le cycle d’eau souterraine qui subsiste est la petite
différence de deux grands nombres voisins. Dans le Northern Atlantic Coastal Plain, cela place le pic GRACE quatre mois après le moment où la nappe
est réellement la plus haute, tandis que le pic de février de 2.2 tombe là où la recharge de fin d’hiver le placerait. La cause probable est une
nappe peu profonde : une partie de ce que GLDAS 2.1 compte comme humidité du sol est de l’eau souterraine, et la soustraire retire le signal deux
fois. Getirana, Kumar et Rodell (2025) formulent la version générale de cet argument : les compartiments des modèles ne sont pas les réservoirs
physiquement séparés que la soustraction suppose.

**Préférer 2.2 pour la forme saisonnière là où la SMa oscille autant que la TWSa.** La vérification se fait dans l’application : tracez la SMa et
la TWSa de la région et comparez la hauteur de leurs cycles saisonniers.

## Pour la recharge, utilisez GRACE { #for-recharge-use-grace }

Barbosa et al. (2025) ont appliqué la méthode de fluctuation de la nappe aux deux jeux de données dans le Bassin de la Volta et ont obtenu 17.4 et
36.1 cm/an avec 2.2 contre 5.8 et 10.7 cm/an avec GRACE, les puits donnant une médiane de 10.4. Ils recommandent 2.2 pour les tendances et non
pour la recharge (voir [Bassin de la Volta](../case-studies/volta.md)). Un cycle saisonnier déphasé est une seconde raison d’aboutir à la même
conclusion : la méthode lit un creux et un pic sur la série, et si leurs mois sont faux, l’estimation de recharge l’est avec eux.

## Résumé { #summary }

| Ce que vous cherchez | Utilisez | Parce que |
|---|---|---|
| Un taux d’épuisement ou de reconstitution, en cm/an ou km³/an | GRACE | 2.2 aplatit les tendances à environ un quart |
| La forme et le calendrier du cycle saisonnier | 2.2 là où la SMa oscille autant que la TWSa, sinon l’un ou l’autre | la soustraction peut inverser la phase |
| Une région large de quelques mailles | 2.2 | moyennée à 0.25° là où l’autre est à 1° |
| Une série mensuelle sans interruption | 2.2 | le modèle traverse les lacunes de GRACE |
| La recharge par la méthode WTF | GRACE | Barbosa et al. (2025), plus le risque de phase |
| Un chiffre d’incertitude par maille | GRACE | 2.2 n’en publie aucun |
| Tout ce qui précède février 2003 | GRACE | l’enregistrement de 2.2 commence là |
| Un résultat que vous comptez publier | les deux | en disant où ils s’accordent et où ils divergent |

Deux réponses indépendantes qui concordent sont difficiles à écarter. Là où elles divergent, tracez les composantes : une divergence qui vit dans
la SMa est un autre problème qu’une divergence qui vit dans la TWSa.

## Jusqu’où tout cela est validé { #how-far-any-of-this-is-validated }

Les chiffres de cette page viennent de la comparaison des deux jeux de données publiés entre eux, ce qui établit comment et pourquoi ils diffèrent,
et ne règle rien quant à celui qui serre de plus près la nappe. Le soutien indépendant des recommandations est indirect :

- **Les modèles sous-estiment les tendances.** Scanlon et al. (2018), sept modèles globaux contre trois solutions GRACE sur 186 bassins.
- **La méthode du résidu est structurellement fragile.** Getirana, Kumar et Rodell (2025), sur le fait que les réservoirs des modèles ne sont pas
  les compartiments séparables dont la soustraction a besoin.
- **Les deux solutions mascon s’accordent à l’échelle du bassin et divergent sur les tendances.** Scanlon et al. (2016), CSR et JPL sur 176
  bassins.
- **La comparaison in situ est plus difficile qu’il n’y paraît.** Chen, Famiglietti, Scanlon et Rodell (2016) notent que convertir des niveaux de
  puits en stockage demande un coefficient d’emmagasinement par puits, lui-même incertain même là où le réseau de suivi est dense. Bhanja et al.
  (2016) ont mené une telle comparaison à l’échelle de l’Inde.

Aucune de ces études n’a évalué ces deux jeux de données l’un contre l’autre, et aucune n’a utilisé cette application. La validation directe par
les puits ne va ici que jusqu’à la [Vallée centrale](../case-studies/central-valley.md) et aux puits de la Volta de Barbosa et al. Prenez les
recommandations ci-dessus comme un raisonnement tiré de la construction et du comportement mesuré, appuyé par la littérature sur chaque mécanisme,
et non comme un classement validé.

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
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., et Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
