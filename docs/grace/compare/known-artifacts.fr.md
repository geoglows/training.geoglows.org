# Artefacts connus

Certains des plus grands écarts entre les deux jeux de données se trouvent là où l’un d’eux, le plus souvent la voie GRACE, rapporte de l’eau qui
n’est pas de l’eau souterraine. L’application dessine ces mailles comme toutes les autres. Cette page les nomme pour que vous en reconnaissiez une
au premier coup d’œil plutôt que de la lire comme un résultat.

## Calottes glaciaires et glaciers { #ice-sheets-and-glaciers }

Les douze mailles à 1° où les deux enregistrements d’eau souterraine diffèrent le plus sont toutes de la glace :

| Maille | Écart typique | Corrélation | Neige moyenne |
|:---|:---:|:---:|:---:|
| 66.5°N, 36.5°O (Groenland oriental) | 1019 cm | −0.03 | 327 cm |
| 66.5°N, 35.5°O | 805 cm | 0.02 | 283 cm |
| 66.5°N, 37.5°O | 777 cm | 0.02 | 330 cm |
| 76.5°N, 67.5°O (Ellesmere et Baffin) | 739 cm | 0.13 | 9 cm |
| 78.5°N, 15.5°E (Svalbard) | 734 cm | 0.39 | 24 cm |
| 76.5°N, 68.5°O | 729 cm | 0.19 | 6 cm |

GRACE mesure la calotte qui perd de la masse, année après année. Aucun modèle GLDAS ne porte de glaciers ni de calottes : aucun ne rapporte donc
cette perte comme de la neige, et la soustraction n’a nulle part où la mettre sinon dans l’eau souterraine. Le résultat, ce sont des variations
d’eau souterraine de l’ordre du mètre dans des mailles sans le moindre aquifère. 2.2 contourne l’arithmétique sans échapper au problème : son
modèle Catchment n’a pas de glace non plus, et la correction GRACE qu’il reçoit se répartit entre tous les réservoirs du modèle, si bien qu’il
rapporte un chiffre bien plus petit, pour la raison même qui l’amène à aplatir les tendances ailleurs. Ni l’une ni l’autre série ne signifie quoi
que ce soit comme eau souterraine ici.

![Les enregistrements d’eau souterraine d’une seule maille de 1° au Groenland oriental, où la voie GRACE rapporte une perte de 19 mètres](../../static/images/grace/compare-artifact-ice.png)

Une seule maille suffit à le montrer. À 66.5°N 36.5°O, la voie GRACE rapporte une eau souterraine qui baisse de 19 mètres sur la période, en une
droite interrompue par le seul trou entre les missions, dans un lieu sans aquifère et sans eau souterraine à perdre. Cette droite, c’est la
calotte du Groenland. 2.2 reste à zéro parce que son modèle n’a pas non plus de glace à perdre, et parce que sa correction GRACE se répartit
entre des réservoirs incapables de recevoir cette perte.

Deux bassins fluviaux des jeux de l’application elle-même, Alsek et Santa Cruz, portent une GWSa très grande pour cette raison (voir
[Calcul du stockage d’eau souterraine](../gldas/deriving-groundwater.md)).

**Comment le reconnaître.** Basculez la couche affichée sur la neige (SWEa). Là où elle atteint des centaines de centimètres, ou là où la région
repose sur une calotte à n’importe quelle latitude, la couche d’eau souterraine rapporte de la glace.

## L’eau de surface que les modèles ne portent pas { #surface-water-the-models-do-not-carry }

En Amazonie, l’eau souterraine de GRACE oscille de 40.8 cm au fil de l’année contre 18.1 pour 2.2, et sa tendance vaut +0.31 cm/an contre −0.40
pour 2.2 : les deux jeux de données ne s’accordent même pas sur le sens. L’essentiel du cycle de l’eau amazonien se joue dans les chenaux et sur
la plaine d’inondation, et aucun modèle GLDAS ne représente l’un ni l’autre. Sur la voie GRACE, cette eau n’a nulle part où aller dans la
soustraction : elle finit donc dans l’eau souterraine. Le Congo se comporte de même.

![Les cycles d’eau souterraine du bassin amazonien dans les deux jeux de données, celui de GRACE étant plus de deux fois plus ample](../../static/images/grace/compare-artifact-amazon.png)

Le calendrier n’est pas en cause : les deux cycles corrèlent à 0.99 et culminent tous deux en mai avec la crue. L’ampleur, si : la voie GRACE
oscille de 40.8 cm contre 18.1 cm, et l’eau en trop est le fleuve lui-même, qui monte et descend sur la plaine d’inondation sans nulle part
ailleurs où aller dans la soustraction. Les tendances pointent alors en sens opposés : qui demande si l’eau souterraine amazonienne gagne ou perd
obtient une réponse différente de chaque jeu de données.

Tout bassin où un grand fleuve monte et descend au fil des saisons sur une large plaine d’inondation en fera une version.

**Comment le reconnaître.** Un cycle d’eau souterraine GRACE bien plus ample que celui de 2.2, dans un bassin humide traversé par un fleuve
important, est en général de l’eau de surface.

## Neige et sol gelé aux hautes latitudes { #snow-and-frozen-ground-at-high-latitude }

Écart typique entre les deux enregistrements d’eau souterraine, par bande de latitude :

| Bande | Écart typique | Neige moyenne | Mailles |
|:---|:---:|:---:|:---:|
| 60°S–30°S | 5.92 cm | 0.33 cm | 540 |
| 30°S–0° | 8.48 cm | 0.01 cm | 2 428 |
| 0°–30°N | 7.41 cm | 0.02 cm | 3 094 |
| 30°N–60°N | 6.49 cm | 2.12 cm | 5 397 |
| 60°N–90°N | 7.75 cm | 18.91 cm | 3 700 |

La bande la plus septentrionale porte la neige, et les bassins sibériens montrent la voie GRACE oscillant bien plus fort au fil de l’année : la
Petchora à 12.1 cm contre 3.3 pour 2.2, la Sibérie occidentale à 14.0 contre 4.6. Deux choses finissent là-bas dans l’eau souterraine GRACE : la
masse de neige que la couche de neige du modèle n’égale pas, et l’eau emprisonnée dans un sol saisonnièrement gelé, qu’aucun modèle GLDAS ne
garde comme réservoir distinct.

La bande tropicale est la pire des bandes libres de glace, et il s’agit de l’eau de plaine d’inondation évoquée plus haut, non de quoi que ce
soit de gelé.

## Nappes peu profondes { #shallow-water-tables }

Là où la nappe est proche de la surface, une partie de ce que les modèles GLDAS 2.1 comptent comme humidité du sol est en réalité de l’eau
souterraine, si bien que la soustraire retire deux fois le signal souterrain. Le cas le plus net est le Northern Atlantic Coastal Plain, où le
cycle d’eau souterraine de GRACE finit décalé de quatre mois par rapport à celui de 2.2. [Quand se fier à chacun](trusting-each-one.md) donne la
vérification à faire et les aquifères concernés.

## Les régions où il se passe peu de chose { #regions-where-little-happens }

Sur les mailles à 1° où l’eau souterraine GRACE bouge à peine — moins de 5 cm de variation typique —, les deux jeux de données corrèlent à une
médiane de 0.19. Deux petits signaux qui ne parviennent pas à s’aligner donnent ce chiffre, que quelque chose cloche ou non. Avant de lire une
corrélation faible comme un problème, regardez quelle quantité d’eau bouge réellement : la même comparaison donne 0.77 dans les mailles qui
varient de plus de 15 cm.

## Une courte liste de contrôle { #a-short-checklist }

Avant de traiter un grand écart comme un résultat :

1. Tracez la neige (SWEa). La glace et la neige expliquent la plupart des extrêmes.
2. Tracez l’eau totale (TWSa) des deux jeux de données. Là où les totaux s’accordent et où seule l’eau souterraine diverge, les deux jeux
   partagent la colonne différemment ; la mesure satellitaire elle-même n’est pas en cause.
3. Comparez l’oscillation saisonnière de l’humidité du sol (SMa) à celle de l’eau totale (TWSa). Là où elles sont voisines, méfiez-vous du
   calendrier du cycle d’eau souterraine GRACE.
4. Regardez quelle quantité d’eau bouge avant de lire quoi que ce soit dans une corrélation.
5. Demandez-vous si un fleuve, une plaine d’inondation ou un réservoir pourrait rendre compte de l’eau.
