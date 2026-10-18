# Pourquoi les deux jeux de données diffèrent

L’application sert deux enregistrements d’eau souterraine pour le même mois et la même maille, et ils ne concordent pas. Cette page traite de
l’origine du désaccord. [Quand se fier à chacun](trusting-each-one.md) traite de celui qu’il faut croire, et
[Artefacts connus](known-artifacts.md) rassemble les endroits où l’un des deux se trompe tout simplement.

[Calcul du stockage d’eau souterraine](../gldas/deriving-groundwater.md) donne les deux constructions en entier. En bref :

- **La voie GRACE.** Le JPL mesure le stockage total d’eau. L’application retranche l’humidité du sol, la neige et l’eau de la canopée de
  GLDAS 2.1, et lit le reste comme de l’eau souterraine.
- **La voie GLDAS 2.2.** La NASA fait tourner le modèle de surface terrestre Catchment avec GRACE assimilé dedans, et le modèle rapporte
  directement un état d’eau souterraine. Rien n’est retranché.

Ces pages emploient partout les noms des couches de l’application. **TWSa** est l’eau totale stockée : toutes les formes d’eau retenues dans la
colonne à cet endroit — humidité du sol, neige, eau sur les feuilles, eau de surface et eau souterraine. **GWSa** en est la part souterraine,
**SMa** l’humidité du sol, **SWEa** la neige et **CANa** l’eau retenue par la végétation. Le *a* de chacune signifie anomalie : chaque valeur est
un écart à la moyenne 2004–2009 de la maille elle-même, en centimètres d’eau répartis uniformément sur la maille. Zéro signifie des conditions
moyennes pour ce lieu, jamais un aquifère vide.

## Ce qui diffère déjà avant de compter la moindre goutte { #what-already-differs-before-any-water-is-counted }

| | Voie GRACE | GLDAS 2.2 |
|:---|:---|:---|
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

GRACE n’a jamais mesuré d’eau. Deux satellites volaient en formation, l’un devant l’autre, et l’instrument placé entre eux mesurait leur
séparation à quelques microns près. La masse supplémentaire du sol en dessous — de l’eau, pour l’essentiel — attire d’abord le satellite de tête,
puis celui de queue un instant plus tard, ce qui modifie très légèrement cette séparation. Des mois de ces mesures se retraduisent en une carte
des gains et des pertes de masse.

Cette conversion n’a pas de réponse unique. Beaucoup de répartitions différentes de l’eau au sol correspondent aussi bien au même enregistrement
orbital, si bien que chaque centre de traitement ajoute ses propres hypothèses pour n’en retenir qu’une. Le JPL et le CSR ajoutent des hypothèses
différentes. Tous deux publient le résultat sous forme de **mascons** : des blocs de la surface terrestre, chacun recevant une valeur d’eau par
mois.

| | JPL | CSR |
|:---|:---|:---|
| Blocs sur lesquels la solution est calculée | calottes d’égale surface de 3°, environ 300 km | tuiles d’égale surface de 1° à l’équateur, environ 110 km |
| Grille de diffusion des fichiers | 0.5° | 0.25° |
| Ce qui oriente la réponse là où GRACE seul est ambigu | un modèle de surface continentale | les seules données GRACE |
| Blocs à cheval sur une côte | un filtre sépare la part terrestre de la part océanique | le bloc est coupé en deux le long du trait de côte |
| Facteurs de correction | le JPL publie des facteurs de gain et recommande de les appliquer | le CSR indique que ses mascons n’en ont pas besoin |

Les deux grilles sont plus fines que ce que GRACE peut réellement voir. Les satellites résolvent des structures de quelques centaines de
kilomètres, quel que soit le centre qui les traite : la grille est la façon d’emballer une réponse, pas la quantité de détail qu’elle contient.

Scanlon et al. (2016) ont comparé les produits des deux centres sur 176 bassins fluviaux et trouvé que leurs enregistrements d’eau totale se
suivent de près, les tendances de long terme restant la part qui diverge. Les deux jeux de données de cette application se comportent de la même
façon.

L’accord, dans ces pages, se mesure par une **corrélation** : un seul nombre entre −1 et 1 qui dit avec quelle fidélité deux enregistrements
mensuels montent et descendent ensemble. À 1 ils bougent à l’unisson, à 0 il n’y a aucune relation, à −1 l’un monte chaque fois que l’autre
descend. Une corrélation ne dit rien sur le fait que les deux s’accordent sur la quantité d’eau, seulement sur le calendrier et la forme des
hausses et des baisses.

Chaque corrélation porte ici sur les 281 mois que les deux jeux fournissent, de février 2003 à juin 2026. Pour un bassin, chaque jeu est d’abord
moyenné sur le bassin — la série que trace la vue régionale de l’application — et ces deux moyennes sont comparées. Les tendances y restent, de
sorte qu’une baisse que les deux jeux voient compte en faveur de leur accord.

Sur les 37 bassins WHYMAP, les deux enregistrements d’eau totale corrèlent à une médiane de 0.87, et 15 des 37 dépassent 0.9. L’accord faiblit à
mesure que la surface diminue : maille de 1° par maille de 1°, la médiane tombe à 0.75, car moyenner sur un bassin annule le bruit d’un mois à
l’autre qu’une seule maille porte à elle seule.

Le Système aquifère Guarani montre à quoi ressemble un bon accord :

![Les enregistrements d’eau souterraine de la voie GRACE et de GLDAS 2.2 sur le Système aquifère Guarani, mois par mois et en cycle saisonnier moyen](../../static/images/grace/compare-agreement.png)

Les deux jeux de données suivent les années humides jusqu’en 2016 et tous deux s’infléchissent à la baisse après 2020. Leurs enregistrements
mensuels d’eau souterraine corrèlent à 0.85, leurs cycles saisonniers à 0.96, et leurs oscillations saisonnières diffèrent d’un centimètre. Rien
de ce qu’un gestionnaire de l’eau conclurait sur cet aquifère ne change avec le choix du jeu de données.

Le reste de cette page porte sur les bassins où ce n’est pas le cas, et [Où faire confiance à chacun](trusting-each-one.md) en parcourt
quatre.
## D’où vient l’écart { #where-the-difference-comes-from }

Aucun des deux jeux de données ne mesure l’eau souterraine. Tous deux y parviennent par soustraction : on part de l’eau totale stockée dans la
colonne, puis on retranche l’eau retenue sous forme d’humidité du sol, de neige et d’eau de la canopée. Ce qui reste est appelé eau souterraine.

Les deux séries d’eau souterraine peuvent donc diverger de deux façons, et d’aucune autre.

1. **Elles partent d’un total différent.** Les couches GRACE de l’application portent la solution du JPL et GLDAS 2.2 intègre celle du CSR. Là où
   ces deux solutions sont en désaccord sur l’eau totale, l’eau souterraine qu’elles impliquent hérite intégralement de ce désaccord.
2. **Elles retranchent une quantité différente.** Les trois modèles GLDAS 2.1 que la route GRACE moyenne, et le modèle Catchment au cœur de 2.2,
   retiennent des quantités différentes d’humidité du sol et de neige pour le même lieu au même mois. Retrancher davantage laisse moins d’eau
   souterraine.

Rien d’autre n’intervient, de sorte que les trois écarts sont liés exactement : l’écart d’eau souterraine est égal à l’écart d’eau totale moins
l’écart de la soustraction. En notant d « l’écart entre les deux jeux de données », TWS l’eau totale et REST tout ce qui, dans la colonne, n’est
pas de l’eau souterraine,

$$ d_{GW} = d_{TWS} - d_{REST} $$

Les trois se mesurent, ce qui tranche la question de la cause dominante selon les endroits.

Le **RMS** est la taille typique d’un écart, en centimètres d’eau : on prend la différence entre les deux jeux de données à chaque mois, on
l’élève au carré, on moyenne sur la période, on prend la racine carrée. Le décalage fixe propre à chaque maille est retiré d’abord, si bien que
le RMS mesure le désaccord qui évolue dans le temps plutôt qu’une distance constante entre les deux.

La **part** dit quelle fraction de l’écart d’eau souterraine une seule cause pourrait expliquer. Chaque écart oscille d’une certaine ampleur
autour de sa propre moyenne, et la part compare l’ampleur de cette oscillation à celle de l’écart d’eau souterraine.

Les deux sont des médianes sur les mailles terrestres communes aux deux jeux, de février 2003 à juin 2026, chaque maille comptant
proportionnellement à sa surface, de sorte qu’une maille large à l’équateur pèse plus qu’une maille étroite près d’un pôle.

| L’écart entre les deux jeux de données sur | RMS | Part de l’écart d’eau souterraine |
|:---|:---:|:---:|
| l’eau souterraine, ce qui s’affiche à l’écran | 6.42 cm | — |
| l’eau totale, JPL contre CSR | 5.73 cm | 0.85 |
| la soustraction : sol, neige et canopée | 3.38 cm | 0.32 |

Les deux parts totalisent plus de 1 parce que les écarts évoluent en partie ensemble : elles ne répartissent donc pas la responsabilité en
pourcentages nets. À lire comme un classement : dans une maille typique de 1°, le désaccord entre le JPL et le CSR explique l’essentiel de
l’écart d’eau souterraine, et la soustraction environ un tiers.

Moyenner sur un bassin déplace cet équilibre. La moyenne annule une bonne part du bruit de maille des solutions GRACE tout en laissant l’écart
systématique dans la façon de diviser la colonne : plus la région est grande, plus le désaccord provient de la soustraction. Les parts par bassin
atteignent une médiane de 0.72 pour l’eau totale et de 0.32 pour la soustraction, et dans 11 des 37 bassins la soustraction est la cause la plus
importante.

L’eau souterraine diverge partout plus que l’eau totale. Maille par maille, les séries d’eau souterraine des deux jeux corrèlent à une médiane de
0.42, contre 0.75 pour l’eau totale ; par bassin, 0.61 contre 0.87. Chaque pas qui éloigne de la mesure brute ajoute un choix de modélisation que
les deux jeux de données font différemment.

## Ce que dit la littérature sur la soustraction { #what-the-literature-says-about-the-subtraction }

Getirana, Kumar et Rodell (2025) mettent en cause la méthode qui sous-tend la route GRACE. Retrancher l’humidité du sol et la neige d’un modèle à
un total GRACE ne donne de l’eau souterraine que si les compartiments de sol et de neige du modèle contiennent exactement l’eau que ces
étiquettes suggèrent, ce qui n’est pas le cas dans beaucoup de modèles. Les couches de sol s’arrêtent à une profondeur fixe, ce qui se trouve en
dessous est traité par convention, et là où la nappe est peu profonde l’eau qu’un modèle classe en humidité du sol est celle qu’un hydrologue
appellerait eau souterraine. En la retranchant, on emporte le signal recherché. Ils recommandent des modèles dotés d’un sous-sol plus complet et
assimilant GRACE, ce qui décrit GLDAS 2.2.

La critique s’applique à la route GRACE de cette application. Les sections sur les cycles saisonniers de [Où faire confiance à
chacun](trusting-each-one.md) chiffrent un cas précis : sur la plaine côtière atlantique, où les nappes sont peu profondes, la route GRACE place
son maximum d’eau souterraine à la mauvaise saison.

Cela ne rend pas la route GRACE inutile. Scanlon et al. (2018) ont confronté sept modèles globaux de surface continentale à trois solutions GRACE
sur 186 bassins fluviaux et trouvé les modèles systématiquement trop plats : là où GRACE voit un gain ou une perte importante sur plusieurs
années, les modèles en montrent une moindre, dans les deux sens. Un modèle est le meilleur guide pour savoir comment la colonne se partage entre
sol, neige et eau souterraine ; les satellites sont le meilleur guide pour savoir de combien le total a changé.

Les deux articles appuient le partage que recommandent ces pages : prendre de 2.2 la forme du cycle et le partage de la colonne, et de GRACE
l’ampleur d’un gain ou d’une perte de long terme.
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
