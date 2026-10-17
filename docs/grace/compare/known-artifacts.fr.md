# Artefacts connus

Certains des plus grands écarts entre les deux jeux de données se trouvent là où l’un d’eux, le plus souvent la voie GRACE, rapporte de l’eau qui
n’est pas de l’eau souterraine. L’application dessine ces mailles comme toutes les autres. Cette page les nomme pour que vous en reconnaissiez une
au premier coup d’œil plutôt que de la lire comme un résultat.

## Calottes glaciaires et glaciers { #ice-sheets-and-glaciers }

Les douze mailles à 1° où les deux enregistrements d’eau souterraine diffèrent le plus sont toutes de la glace :

| Maille | écart RMS | corrélation | \|SWEa\| moyen |
|---|---:|---:|---:|
| 66.5°N, 36.5°O (Groenland oriental) | 1019 cm | −0.03 | 327 cm |
| 66.5°N, 35.5°O | 805 cm | 0.02 | 283 cm |
| 66.5°N, 37.5°O | 777 cm | 0.02 | 330 cm |
| 76.5°N, 67.5°O (Ellesmere et Baffin) | 739 cm | 0.13 | 9 cm |
| 78.5°N, 15.5°E (Svalbard) | 734 cm | 0.39 | 24 cm |
| 76.5°N, 68.5°O | 729 cm | 0.19 | 6 cm |

GRACE mesure la calotte qui perd de la masse. Aucun modèle GLDAS ne porte de glaciers ni de calottes, si bien que la SWEa ne peut pas absorber
cette perte et que la soustraction la remet à l’eau souterraine, produisant des GWSa métriques dans des mailles sans le moindre aquifère. 2.2
évite l’arithmétique mais pas le problème de fond : sa simulation Catchment n’a pas de glace non plus, et l’incrément GRACE qu’elle reçoit se
répartit entre les réservoirs du modèle, si bien qu’elle rapporte un chiffre bien plus petit, pour la raison même qui l’amène à aplatir les
tendances ailleurs. Ni l’une ni l’autre série ne signifie quoi que ce soit comme eau souterraine ici.

Deux bassins fluviaux des jeux de l’application elle-même, Alsek et Santa Cruz, portent une GWSa très grande pour cette raison (voir
[Calcul du stockage d’eau souterraine](../gldas/deriving-groundwater.md)).

**Comment le reconnaître.** Basculez la couche affichée sur la SWEa. Là où la SWEa absolue moyenne atteint des centaines de centimètres, ou là où
la région repose sur une calotte à n’importe quelle latitude, la couche d’eau souterraine rapporte de la glace.

## L’eau de surface que les modèles ne portent pas { #surface-water-the-models-do-not-carry }

En Amazonie, l’amplitude saisonnière de la GWSa de GRACE vaut 40.8 cm contre 18.1 pour 2.2, et la tendance GRACE vaut +0.31 cm/an contre −0.40
pour 2.2. Le cycle d’eau totale de l’Amazone est dominé par le stockage dans les chenaux et les plaines d’inondation, qu’aucun modèle GLDAS ne
représente. Sur la voie GRACE, ce stockage n’a nulle part où aller dans la soustraction et finit dans l’eau souterraine ; le Congo se comporte de
même, et les deux jeux de données divergent sur le signe de la tendance dans les deux cas.

Tout bassin où un grand fleuve monte et descend au fil des saisons sur une large plaine d’inondation en fera une version.

**Comment le reconnaître.** Un cycle saisonnier de GWSa sur la voie GRACE bien plus ample que celui de 2.2, dans un bassin humide traversé par un
fleuve important, est en général de l’eau de surface.

## Neige et sol gelé aux hautes latitudes { #snow-and-frozen-ground-at-high-latitude }

Écart RMS entre les deux enregistrements d’eau souterraine, par bande de latitude :

| Bande | écart RMS | \|SWEa\| moyen | mailles |
|---|---:|---:|---:|
| 60°S–30°S | 5.92 cm | 0.33 cm | 540 |
| 30°S–0° | 8.48 cm | 0.01 cm | 2 428 |
| 0°–30°N | 7.41 cm | 0.02 cm | 3 094 |
| 30°N–60°N | 6.49 cm | 2.12 cm | 5 397 |
| 60°N–90°N | 7.75 cm | 18.91 cm | 3 700 |

La bande la plus septentrionale porte la neige, et les bassins sibériens montrent la voie GRACE avec l’amplitude saisonnière la plus grande : la
Petchora à 12.1 cm contre 3.3 pour 2.2, la Sibérie occidentale à 14.0 contre 4.6. La masse de neige que la SWEa du modèle n’égale pas, et l’eau
retenue dans un sol saisonnièrement gelé qu’aucun modèle ne traite comme un réservoir distinct, finissent toutes deux dans le résidu GRACE.

La bande tropicale est la pire des bandes libres de glace, et il s’agit du stockage de plaine d’inondation évoqué plus haut, non de quoi que ce
soit de gelé.

## Nappes peu profondes { #shallow-water-tables }

Là où la nappe est proche de la surface, une partie de ce que GLDAS 2.1 compte comme humidité du sol est en réalité de l’eau souterraine, et la
soustraire retire deux fois le signal d’eau souterraine. Le cas le plus net est le Northern Atlantic Coastal Plain, où le cycle saisonnier de la
GWSa de GRACE finit déphasé de quatre mois par rapport à celui de 2.2. [Quand se fier à chacun](trusting-each-one.md) donne le diagnostic et les
aquifères concernés.

## Les régions où il se passe peu de chose { #regions-where-little-happens }

Sur les mailles à 1° dont l’écart-type de GWSa GRACE est inférieur à 5 cm, la corrélation médiane entre les deux jeux de données vaut 0.19. Deux
petits signaux qui ne parviennent pas à s’aligner donnent ce chiffre, que quelque chose cloche ou non. Avant de lire une corrélation faible comme
un problème, regardez quelle quantité d’eau bouge : la même comparaison donne 0.77 dans les mailles dont la variabilité dépasse 15 cm.

## Une courte liste de contrôle { #a-short-checklist }

Avant de traiter un grand écart comme un résultat :

1. Tracez la SWEa. La glace et la neige expliquent la plupart des extrêmes.
2. Tracez la TWSa des deux jeux de données. Si elles s’accordent et que seule l’eau souterraine diverge, le problème est dans le partage et non
   dans la mesure.
3. Comparez l’ampleur saisonnière de la SMa à celle de la TWSa. Là où elles sont voisines, méfiez-vous de la phase de l’eau souterraine GRACE.
4. Regardez la taille du signal avant de lire quoi que ce soit dans une corrélation.
5. Demandez-vous si un fleuve, une plaine d’inondation ou un réservoir pourrait rendre compte de l’eau.
