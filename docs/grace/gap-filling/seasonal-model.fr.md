# Le Modèle Saisonnier

L'option **Seasonal model** estime chaque mois manquant à partir d'un modèle de la série propre à la région, ajusté sur ses mois observés,
selon l'approche de Barbosa et al. (2022) (voir [Lacunes dans les Données](gaps.md)). Cette page présente le modèle, son ajustement, le calcul
des valeurs comblées et leur précision.

## Tendance, cycle saisonnier et résidu { #trend-seasonal-cycle-and-residual }

La série est décomposée en une tendance à long terme, un cycle saisonnier qui se répète chaque année, et un résidu :

$$
y(t) = T(t) + S(m) + r(t)
$$

où *y*(*t*) est GWSa (ou TWSa) au mois *t*, *m* est le mois calendaire de *t* (janvier à décembre), *T* est la tendance, *S* le cycle
saisonnier et *r* le résidu, c'est-à-dire la part de la valeur de chaque mois que la tendance et le cycle saisonnier n'expliquent pas.

Pour le Northern Midwest Aquifer System, le modèle sépare le GWSa en ces trois parties, la lacune entre les missions étant grisée :

![GWSa du Northern Midwest Aquifer System séparé en tendance, cycle saisonnier et résidu](../../static/images/grace/seasonal-decomposition.png){ width="800" }

La tendance porte la hausse et la baisse lentes du stockage sur l'ensemble de la série, le cycle saisonnier répète la même oscillation annuelle
chaque année, et le résidu contient le reste : les années humides et sèches, et le bruit des données GRACE.

### La tendance { #the-trend }

La tendance est une droite continue par morceaux comportant jusqu'à trois points de rupture *b*<sub>1</sub>, …, *b*<sub>k</sub>, où sa pente change :

$$
T(t) = \beta \, t + \sum_{j=1}^{k} \gamma_j \max(t - b_j,\, 0)
$$

Le temps *t* est compté en mois à partir du premier mois observé. Chaque terme charnière max(*t* − *b*<sub>j</sub>, 0) est nul avant son point de rupture et
augmente d'une unité par mois ensuite ; la pente vaut donc *β* avant le premier point de rupture, *β* + *γ*<sub>1</sub> après celui-ci, et ainsi de suite. La droite s'infléchit à chaque
point de rupture sans saut. Une série avec *k* = 0 a une tendance rectiligne unique.

### Le cycle saisonnier { #the-seasonal-cycle }

Le cycle saisonnier a un niveau pour chaque mois calendaire, *α*<sub>Jan</sub>, …, *α*<sub>Dec</sub>. Le modèle complet pour un mois observé *i*
s'écrit

$$
y_i = \beta \, t_i + \sum_{j=1}^{k} \gamma_j \max(t_i - b_j,\, 0) + \alpha_{m_i} + \varepsilon_i
$$

Les douze niveaux tiennent aussi lieu d'ordonnée à l'origine ; il n'y a donc pas de terme constant séparé. Les niveaux sont les mêmes d'une année à l'autre : le modèle a un
seul cycle annuel moyen, et une année humide apparaît dans le résidu et non dans *S*.

Pour le Northern Midwest Aquifer System, les niveaux, décalés pour avoir une moyenne nulle comme décrit dans [Ajustement du modèle](#fitting-the-model),
vont de −4.3 cm en mars à +3.8 cm en août :

![Les douze niveaux mensuels du cycle saisonnier du Northern Midwest Aquifer System](../../static/images/grace/seasonal-levels.png){ width="700" }

## Ajustement du modèle { #fitting-the-model }

### Moindres carrés à points de rupture fixés { #least-squares-for-fixed-breakpoints }

Pour un ensemble donné de points de rupture, les pentes *β* et *γ*<sub>j</sub> et les douze niveaux *α*<sub>m</sub> sont obtenus par moindres carrés ordinaires
sur les seuls mois observés. Les mois manquants ne participent pas à l'ajustement. Chaque mois calendaire doit être observé au moins deux fois ; sinon son niveau
ne peut pas être estimé de façon fiable et l'application laisse la série sans comblement.

Après l'ajustement, les niveaux sont décalés de sorte que le cycle saisonnier ait une moyenne nulle sur l'année, et la tendance est relevée de la même quantité :

$$
S(m) = \alpha_m - \bar{\alpha}, \qquad T(t) = \beta \, t + \sum_{j} \gamma_j \max(t - b_j,\, 0) + \bar{\alpha}, \qquad
\bar{\alpha} = \frac{1}{12} \sum_{m} \alpha_m
$$

La somme *T* + *S* reste inchangée. Avec ce décalage, *T* donne le niveau à long terme et *S* l'écart de chaque mois par rapport à ce niveau.

### Placement des points de rupture { #placing-the-breakpoints }

Pour un nombre donné *k* de points de rupture, l'application choisit leurs positions de façon à minimiser la somme des carrés des résidus (RSS) de l'ajustement. Les points de rupture
sont contraints pour que chaque segment de la tendance ait un sens :

- au moins 48 mois (quatre ans) de chaque extrémité de la série, pour qu'un segment terminal ne soit pas ajusté sur quelques mois
- au moins 36 mois (trois ans) d'écart entre eux, pour que chaque segment entre deux points de rupture couvre plusieurs cycles saisonniers

La recherche se fait en deux étapes. D'abord, des points de rupture candidats sont placés tous les trois mois, et chaque combinaison valide de *k* candidats est
ajustée. La combinaison de plus faible RSS est retenue. Ensuite, chaque point de rupture est tour à tour déplacé d'un mois plus tôt ou plus tard, et le déplacement est conservé
s'il réduit la RSS. Cela se répète jusqu'à ce qu'aucun déplacement d'un mois n'améliore l'ajustement ; chaque point de rupture se retrouve ainsi au meilleur mois proche du meilleur
candidat trimestriel.

### Choix du nombre de points de rupture { #choosing-the-number-of-breakpoints }

Davantage de points de rupture ajustent toujours les mois observés au moins aussi bien ; le nombre est donc choisi avec le critère d'information bayésien (BIC),
qui ajoute une pénalité pour chaque paramètre :

$$
\text{BIC} = n \ln\!\left(\frac{\text{RSS}}{n}\right) + p \ln n, \qquad p = 1 + 2k + 12
$$

où *n* est le nombre de mois observés et *p* compte les paramètres : la première pente, un changement de pente et une position pour chaque point de rupture,
et les douze niveaux mensuels.

L'application ajuste le meilleur modèle à 0, 1, 2 et 3 points de rupture. En partant de la tendance rectiligne, elle ne passe à un modèle comportant plus de points de rupture que si
le BIC de ce modèle est inférieur d'au moins 10 à celui du modèle retenu jusque-là. Une baisse de 10 constitue une forte indication que l'inflexion supplémentaire est réelle
et ne résulte pas d'un ajustement au bruit ; la tendance ne s'infléchit donc que là où la série change nettement de direction.

Pour le Northern Midwest Aquifer System, chaque point de rupture supplémentaire abaisse le BIC de plus de 10 (de 12, puis 113, puis 44), si bien
que l'application conserve les trois :

![La meilleure tendance avec 0, 1, 2 et 3 points de rupture pour le Northern Midwest Aquifer System, avec le BIC de chacune](../../static/images/grace/seasonal-breakpoints.png)

## Comblement des lacunes { #filling-the-gaps }

Une lacune est une suite d'un ou plusieurs mois manquants entre deux mois observés, *a* avant et *c* après. Le modèle seul, *T* + *S*, ne
rejoindrait les valeurs observées à aucune des extrémités de la lacune, car chaque mois observé a son propre résidu. La valeur comblée ajoute une correction
du résidu interpolée linéairement à travers la lacune :

$$
\hat{y}_g = T(t_g) + S(m_g) + r_a + \frac{t_g - t_a}{t_c - t_a}\,(r_c - r_a), \qquad r_a = y_a - T(t_a) - S(m_a), \quad r_c = y_c - T(t_c) - S(m_c)
$$

pour chaque mois manquant *g* de la lacune.

La correction donne au comblement une forme cohérente quelle que soit la longueur de la lacune :

- Pour un seul mois manquant, la variation saisonnière d'un mois au suivant est faible ; la valeur comblée est donc proche d'une droite entre
  ses deux voisins.
- Pour une longue lacune, comme les 11 mois entre les missions, les mois comblés suivent la tendance et le cycle saisonnier, montant et descendant
  au rythme habituel des saisons, tandis que la correction les décale pour rejoindre les valeurs observées aux deux extrémités.

Les deux résidus qui fixent la correction proviennent de mois différents, et rien ne lie l'un à l'autre. Dans la lacune entre les missions du
Northern Midwest Aquifer System, ils sont presque égaux (−0.38 cm en juin 2017 et −0.53 cm en juin 2018), si bien que la correction place chaque
mois comblé juste sous le modèle seul :

![La correction du résidu dans la lacune entre GRACE et GRACE-FO pour le Northern Midwest Aquifer System](../../static/images/grace/seasonal-gap-correction.png){ width="720" }

Dans la Vallée Centrale de Californie, la même lacune commence 5.55 cm au-dessus du modèle et se termine 3.64 cm en dessous. La correction
diminue de 9.2 cm d'un bout à l'autre de la lacune, si bien que les mois comblés commencent bien au-dessus du modèle seul et finissent en dessous :

![La correction du résidu dans la lacune entre GRACE et GRACE-FO pour la Vallée Centrale de Californie](../../static/images/grace/seasonal-gap-correction-cv.png){ width="720" }

Les mois observés ne sont jamais modifiés. Les mois antérieurs à la première observation ou postérieurs à la dernière restent vides, car il n'y a pas de valeur observée
de l'autre côté à laquelle ancrer une correction.

GWSa et TWSa sont chacun comblés à partir de leur propre série, avec leur propre tendance et leur propre cycle saisonnier. Une valeur comblée de GWSa n'est donc pas exactement la
valeur comblée de TWSa moins les termes GLDAS de ce mois. Les couches GLDAS n'ont pas de lacunes et ne sont jamais comblées.

### Exemple : le Northern Midwest Aquifer System { #example-the-northern-midwest-aquifer-system }

Pour le Northern Midwest Aquifer System, le BIC retient trois points de rupture, en septembre 2006, mai 2013 et octobre 2017, qui divisent la série
en quatre segments de tendance de +1.3, −0.7, +2.9 et −0.5 cm/an :

![GWSa observé du Northern Midwest Aquifer System avec la tendance à quatre segments et les mois comblés en rouge](../../static/images/grace/gap-filling-example.png)

Les mois manquants isolés entre 2011 et 2017 restent proches de leurs voisins. Sur la lacune de 11 mois entre les missions, les valeurs comblées
montent à 12.8 cm en septembre 2017 et redescendent à 4.8 cm en mars 2018 avant de rejoindre le premier mois GRACE-FO, prolongeant le cycle annuel
de la région. L'application affiche les mêmes valeurs avec **Gap filling** réglé sur **Seasonal model** (voir
[Lacunes dans les Données](gaps.md#the-gap-filling-control)).

## Précision du comblement { #fill-accuracy }

Le comblement a été testé sur des mois qui disposent de données. Certains mois observés sont masqués, le modèle est réajusté sans eux, et les valeurs comblées
sont comparées aux valeurs réelles. Il y a deux tests :

- **Mois isolés :** 10 % des mois observés (26 mois), choisis au hasard sur l'ensemble de la série, sont masqués ensemble.
- **Longues lacunes :** un bloc de 11 mois est masqué, pour reproduire la lacune entre les missions. L'opération est répétée pour six blocs répartis sur la
  série.

Chaque test compare le modèle saisonnier à deux comblements plus simples : la tendance et le cycle saisonnier sans la correction du résidu, et l'interpolation
linéaire entre les mois observés voisins. Le tableau donne l'erreur quadratique moyenne (RMSE) de chacun, en cm, avec l'incertitude GRACE médiane ±1σ
de la région à titre de comparaison :

**Mois isolés** (RMSE, cm) :

| Région | ±1σ | Modèle saisonnier | Tendance + saisonnier | Linéaire |
|---|---|---|---|---|
| Northern Midwest Aquifer System | 4.4 | 1.3 | 2.4 | 1.1 |
| Bassin de la Volta | 3.9 | 1.6 | 2.5 | 2.0 |
| Iullemeden-Irhazer Aquifer System | 1.9 | 0.9 | 1.1 | 0.8 |
| Vallée Centrale de Californie | 3.4 | 3.1 | 5.3 | 3.3 |

**Blocs de 11 mois** (RMSE, cm) :

| Région | ±1σ | Modèle saisonnier | Tendance + saisonnier | Linéaire |
|---|---|---|---|---|
| Northern Midwest Aquifer System | 4.4 | 1.5 | 2.3 | 4.7 |
| Bassin de la Volta | 3.9 | 2.6 | 2.4 | 5.1 |
| Iullemeden-Irhazer Aquifer System | 1.9 | 1.4 | 1.4 | 1.7 |
| Vallée Centrale de Californie | 3.4 | 4.2 | 4.8 | 5.2 |

Trois résultats se dégagent :

- Pour les mois isolés, le modèle saisonnier vaut à peu près l'interpolation linéaire, comme prévu : sur un seul mois, la correction du résidu rend
  les deux presque identiques.
- Pour les lacunes de 11 mois, l'interpolation linéaire coupe en ligne droite tout un cycle saisonnier, et son erreur est deux à trois fois celle du
  modèle saisonnier dans les régions à cycle marqué (4.7 contre 1.5 cm pour le Northern Midwest).
- Dans les trois premières régions, l'erreur du modèle saisonnier est nettement inférieure à l'incertitude GRACE. La Vallée Centrale de Californie se comble
  moins bien, avec des erreurs supérieures à l'incertitude, car son stockage est gouverné par des sécheresses et des années humides pluriannuelles qu'aucun cycle saisonnier moyen
  ne peut prévoir à l'intérieur d'une longue lacune.

L'erreur d'une valeur comblée provient du modèle et non de GRACE ; l'application ne trace donc pas la bande d'incertitude pour les mois comblés. Dans une
région comme la Vallée Centrale, traitez avec une prudence accrue les résultats qui dépendent de mois comblés, par exemple la recharge des années que
l'[Analyse de la Recharge](../recharge/results.md#the-table) signale comme utilisant des mois comblés.

## Référence { #reference }

Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). Evaluating groundwater storage change and
recharge using GRACE data: A case study of aquifers in Niger, West Africa. *Remote Sensing*, 14(7), 1532.
[doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}
