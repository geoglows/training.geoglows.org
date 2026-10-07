# La Méthode WTF

## La recharge à partir de la remontée de la nappe { #recharge-from-a-rising-water-table }

La méthode de fluctuation de la nappe (WTF) estime la recharge des eaux souterraines à partir de la remontée des niveaux piézométriques qui suit une saison humide (Healy et
Cook, 2002). Sous un climat comportant une saison sèche et une saison humide par an, le stockage diminue pendant les mois secs à mesure que les eaux souterraines se déchargent vers
les cours d'eau, les sources, les puits et l'évapotranspiration. Quand la pluie ou la fonte des neiges atteint la nappe, le stockage remonte. L'ampleur de cette remontée
mesure la quantité d'eau entrée dans l'aquifère.

Sur l'hydrogramme d'un puits, la remontée est une variation de charge, Δh, et la recharge est le produit du rendement spécifique de l'aquifère par cette remontée :

$$
R = S_y \, \Delta h
$$

Le rendement spécifique est rarement bien connu, et il varie au sein d'un aquifère ; c'est donc souvent la principale source d'erreur d'une estimation fondée sur des puits.
GRACE supprime cette étape. GWSa est déjà une hauteur d'eau, la variation du stockage des eaux souterraines moyennée sur la région ; appliquée à GWSa, la
méthode donne donc directement la recharge en centimètres par an, sans rendement spécifique :

$$
R = \Delta \text{GWSa}
$$

Barbosa et al. (2022) ont appliqué la méthode de cette façon aux bassins des Iullemeden et du Tchad au Niger, en utilisant la série GRACE des eaux souterraines à la place
des hydrogrammes de puits (voir [Études de Cas](../case-studies/niger.md)).
La page Recharge Analysis de l'application suit leur approche.

## Une année hydrologique { #one-water-year }

La méthode travaille une année hydrologique à la fois. Une année hydrologique comprend une saison sèche suivie d'une saison humide ; elle commence donc au mois où
le stockage est habituellement le plus bas. Pour chaque année hydrologique, la méthode a besoin de quatre valeurs de GWSa :

![La méthode de fluctuation de la nappe appliquée à une année hydrologique](../../static/images/grace/wtf-concept.png)

- **S<sub>A</sub>**, le pic de la saison humide précédente, où commence la récession de saison sèche
- **S<sub>B</sub>**, le creux, le stockage le plus bas avant la remontée de l'année
- **S<sub>P</sub>**, le pic atteint pendant cette saison humide
- **S<sub>L</sub>**, le stockage que l'aquifère aurait atteint au moment du pic s'il avait continué à se vider sans recharge

La droite de récession donne S<sub>L</sub>. Une droite est ajustée sur GWSa de S<sub>A</sub> jusqu'à S<sub>B</sub>, ce qui donne le rythme auquel
le stockage se vide sans recharge. Cette pente est ensuite prolongée de S<sub>B</sub> jusqu'au mois du pic :

$$
S_L = S_B + m \, (t_P - t_B)
$$

où *m* est la pente de la droite ajustée (cm par mois), et *t*<sub>B</sub> et *t*<sub>P</sub> sont les mois du creux et du pic.

## Deux estimations de la recharge { #two-estimates-of-recharge }

La remontée visible du creux au pic est

$$
R_S = S_P - S_B
$$

L'aquifère continue de se vider pendant qu'il est rechargé ; une partie de l'eau arrivée pendant la saison humide repart donc avant le pic
et n'apparaît jamais dans la remontée. La droite de récession estime cette perte comme la baisse supplémentaire qu'aurait montrée le stockage sans recharge :

$$
R_D = S_B - S_L
$$

Ensemble, elles donnent deux estimations, que l'application présente sous les noms R1 et R2 :

$$
\begin{aligned}
R_1 &= R_S = S_P - S_B \\
R_2 &= R_S + R_D = S_P - S_L
\end{aligned}
$$

R1 ne compte que la remontée visible ; c'est donc une estimation basse. R2 réintègre le drainage pendant la remontée, mais il repose sur le prolongement de la
droite de récession sur des mois où elle n'a pas été ajustée, et le rythme de drainage ralentit généralement à mesure que le stockage baisse ; R2 est donc une estimation haute.
Barbosa et al. (2022) les appellent Method 1 et Method 2 et présentent les deux. La recharge réelle se situe très probablement entre elles.

Lorsque le stockage était stable ou en hausse avant le creux, il n'y a pas de drainage à corriger : l'application pose S<sub>L</sub> = S<sub>B</sub>, et R2
est égal à R1.

## Application de la méthode aux données GRACE { #applying-the-method-to-grace-data }

Les données GRACE diffèrent d'une série de puits sur plusieurs points, et l'application traite chacun d'eux.

**Lacunes.** La méthode a besoin d'une valeur pour chaque mois : un mois manquant au pic ou au creux modifie le résultat de l'année. L'analyse de la recharge n'est
disponible qu'avec le comblement **Seasonal model**, et elle s'exécute sur la série comblée (voir [Lacunes dans les Données](../gap-filling/gaps.md)). Les années dont
les points choisis ou la droite de récession tombent sur des mois comblés sont signalées dans les résultats.

**Tendances à long terme.** De nombreuses régions présentent une baisse ou une hausse régulière du stockage sur l'ensemble de la série. Sur la série brute, une forte baisse
repousserait le mois le plus haut de chaque année au début de l'année hydrologique et son mois le plus bas à la fin. L'application choisit les mois du pic et du creux sur
la série dont la tendance à long terme a été retirée (la tendance du modèle saisonnier), puis lit S<sub>P</sub>, S<sub>B</sub> et la droite de récession
sur la série comblée elle-même.

**L'année hydrologique.** L'application repère le mois de plus faible valeur dans le cycle saisonnier moyen et fait commencer chaque année hydrologique à ce mois. Vous pouvez
choisir un autre mois de début (voir [Années Hydrologiques et Choix des Points](picks.md)).

**Les points choisis.** Dans chaque année hydrologique, S<sub>P</sub> est le mois le plus haut de la série sans tendance. S<sub>B</sub> est le mois sans tendance le plus bas
entre le pic de l'année précédente et celui de l'année en cours. S<sub>A</sub> est le pic de l'année précédente. La première année hydrologique de la série n'a pas de
pic précédent ; son S<sub>A</sub> est donc le mois sans tendance le plus haut avant son creux.

**La droite de récession.** La droite est un ajustement par moindres carrés sur la GWSa comblée de S<sub>A</sub> à S<sub>B</sub>. Lorsque le creux survient moins
de quatre mois après S<sub>A</sub>, l'ajustement utilise à la place les quatre mois qui se terminent au creux, de sorte qu'une pente n'est jamais ajustée sur deux ou trois
points.

**Unités.** GWSa est exprimé en centimètres d'eau ; R1 et R2 sont donc en cm par an, moyennés sur la région. Multipliés par la superficie de la région,
ils donnent un volume :

$$
V\,[\text{km}^3/\text{an}] = R\,[\text{cm/an}] \times 10^{-5} \times A\,[\text{km}^2]
$$

## Domaine d'application de la méthode { #where-the-method-applies }

La méthode interprète la remontée de chaque année comme la recharge de cette année ; elle exige donc un cycle annuel net avec une seule saison de recharge par an. Elle fonctionne le mieux
lorsque :

- le stockage monte et descend une fois par an, à peu près à la même époque chaque année
- l'amplitude saisonnière est grande par rapport à l'incertitude ±1σ d'une valeur mensuelle GRACE
- la baisse de saison sèche correspond à un drainage naturel et non à des pompages

Elle ne s'applique pas lorsque la recharge a lieu toute l'année sans remontée nette, dans les régions arides à faible recharge saisonnière, ni lorsque des périodes humides
et sèches pluriannuelles dominent la série. L'application vérifie ces conditions sur chaque série avant d'exécuter la méthode (voir
[Ouverture de l'Analyse](opening.md)).

## Références { #references }

- Healy, R. W., and Cook, P. G. (2002). Using groundwater levels to estimate recharge. *Hydrogeology Journal*, 10, 91–109.
  [doi:10.1007/s10040-001-0178-0](https://doi.org/10.1007/s10040-001-0178-0){:target="_blank"}
- Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). Evaluating groundwater storage change and
  recharge using GRACE data: A case study of aquifers in Niger, West Africa. *Remote Sensing*, 14(7), 1532.
  [doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}
