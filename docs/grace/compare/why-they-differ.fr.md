# Pourquoi les deux jeux de données diffèrent

L’application propose deux enregistrements d’eau souterraine pour le même mois et la même cellule, et ils ne concordent pas. Cette page traite de
l’origine du désaccord. [À quoi ressemblent les écarts](examples.md) en montre les cas, [Lequel utiliser](which-one-to-use.md) indique quelle
série citer pour quelle question, et [Jusqu’où cela est validé](validation.md) dit quel poids ce conseil peut porter.

[Calcul du stockage d’eau souterraine](../gldas/deriving-groundwater.md) donne les deux constructions en entier. En bref :

- **La voie GRACE.** Le JPL mesure le stockage total d’eau. L’application soustrait l’humidité du sol, la neige et l’eau de la canopée de
  GLDAS 2.1, et lit le reste comme de l’eau souterraine.
- **La voie GLDAS 2.2.** La NASA fait tourner le modèle de surface Catchment avec GRACE assimilé, et le modèle rapporte directement un état d’eau
  souterraine. Rien n’est soustrait.

Ces pages emploient les noms de couches de l’application. **TWSa** est le stockage total d’eau : toute forme d’eau retenue dans la colonne à cet
endroit — humidité du sol, neige, eau sur les feuilles, eau de surface et eau souterraine réunies. **GWSa** en est la part souterraine, **SMa**
l’humidité du sol, **SWEa** la neige et **CANa** l’eau retenue par la végétation. Le *a* de chacune signifie anomalie : chaque valeur est un écart
à la moyenne 2004–2009 de la cellule elle-même, en centimètres d’eau répartis uniformément sur elle. Zéro signifie des conditions moyennes pour ce
lieu, jamais un aquifère vide.

## Ce qui diffère déjà avant de compter la moindre goutte { #what-already-differs-before-any-water-is-counted }

| | Voie GRACE | GLDAS 2.2 |
|:---|:---|:---|
| Solution GRACE | mascons du JPL, RL06.3 v04 CRI | mascons du CSR, RL06 |
| Empreinte GRACE native | calottes équisurfaciques de 3° | 1° équisurfacique à l’équateur |
| Grille servie | 1° | 0,25°, moyennée à 1° pour la grille mondiale |
| Début de l’enregistrement | avril 2002 | février 2003 |
| Mois manquants | les lacunes de GRACE, comblées ou signalées | aucun ; le modèle tourne sans correction |
| Facteurs de gain | ceux du JPL, appliqués | aucun |
| Couches d’incertitude | publiées par cellule | aucune |
| Cellules terrestres sur la grille 1° | 15 159 | 17 346 |

Le début de l’enregistrement et le masque terrestre relèvent de la comptabilité, et apparaissent comme des données manquantes plutôt que comme un
désaccord. Toutes les autres lignes changent les chiffres.

## Deux groupes, une paire de satellites { #two-groups-one-pair-of-satellites }

GRACE n’a jamais mesuré d’eau. Deux satellites volaient en formation, l’un devant l’autre, et l’instrument entre eux mesurait leur séparation à
quelques microns près. La masse supplémentaire au sol en dessous — de l’eau, surtout — tire d’abord sur le satellite de tête puis, un instant plus
tard, sur celui de queue, modifiant cette séparation d’une quantité infime. Des mois de ces mesures peuvent être retraduits en une carte des
gains et des pertes de masse.

Cette conversion n’a pas de réponse unique. De nombreuses répartitions différentes de l’eau au sol s’accordent aussi bien avec le même
enregistrement orbital, si bien que chaque centre de traitement ajoute ses propres hypothèses pour en retenir une. Le JPL et le CSR ajoutent des
hypothèses différentes. Tous deux publient le résultat sous forme de **mascons** : des blocs de la surface terrestre, chacun doté d’une valeur
d’eau par mois.

| | JPL | CSR |
|:---|:---|:---|
| Blocs sur lesquels la réponse est résolue | calottes équisurfaciques de 3°, environ 300 km | tuiles équisurfaciques de 1° à l’équateur, environ 110 km |
| Grille de diffusion des fichiers | 0,5° | 0,25° |
| Ce qui oriente la réponse là où GRACE seul est ambigu | un modèle de surface terrestre | les seules données GRACE |
| Blocs à cheval sur une côte | un filtre sépare la part terrestre de la part océanique | le bloc est coupé en deux le long du littoral |
| Facteurs de correction | le JPL publie des facteurs de gain et recommande de les appliquer | le CSR affirme que ses mascons n’en ont pas besoin |

Les deux grilles sont plus fines que ce que GRACE peut réellement voir. Les satellites résolvent des structures de quelques centaines de
kilomètres, quel que soit le centre qui les traite, de sorte que la grille est une façon d’emballer une réponse plutôt qu’une mesure du détail
qu’elle contient.

Scanlon et al. (2016) ont comparé les produits des deux centres sur 176 bassins fluviaux et ont trouvé que leurs enregistrements d’eau totale se
suivaient de près, les tendances à long terme restant la part qui diverge. Les deux jeux de données de cette application se comportent de même.

## Comment la concordance est mesurée dans ces pages { #how-agreement-is-measured-on-these-pages }

La concordance se mesure par une **corrélation** : un nombre entre −1 et 1 indiquant à quel point deux enregistrements mensuels montent et
descendent ensemble. À 1 ils bougent à l’unisson, à 0 il n’y a aucune relation, à −1 l’un monte chaque fois que l’autre descend. Une corrélation
ne dit rien sur l’accord entre les deux quant à la quantité d’eau — seulement sur le moment et la forme des hausses et des baisses.

Chaque corrélation ici porte sur les 281 mois que fournissent les deux jeux de données, de février 2003 à juin 2026. Pour un bassin, chaque jeu
est d’abord moyenné sur le bassin, ce qui est la série que trace la vue régionale de l’application, et ces deux moyennes sont comparées. Les
tendances sont conservées, de sorte qu’une baisse que les deux perçoivent compte en faveur de leur concordance.

Sur les 37 bassins WHYMAP, les deux enregistrements d’eau totale corrèlent à une médiane de 0,87, et 15 des 37 dépassent 0,9. La concordance
faiblit quand la surface diminue : cellule de 1° par cellule, la médiane tombe à 0,75, car moyenner sur un bassin annule le bruit mensuel qu’une
cellule isolée porte seule.

## D’où vient l’écart { #where-the-difference-comes-from }

Aucun des deux jeux de données ne mesure l’eau souterraine. Tous deux y parviennent par soustraction : on part de l’eau totale stockée dans la
colonne, puis on retire l’eau retenue sous forme d’humidité du sol, de neige et de canopée. Ce qui reste est appelé eau souterraine.

Les deux séries peuvent donc diverger de deux façons, et d’aucune autre.

1. **Elles partent d’un total différent.** Les couches GRACE de l’application portent la solution du JPL et GLDAS 2.2 intègre celle du CSR. Partout
   où ces deux-là divergent sur l’eau totale, l’eau souterraine qu’elles impliquent hérite intégralement de ce désaccord.
2. **Elles retirent une quantité différente.** Les trois modèles GLDAS 2.1 que la voie GRACE moyenne, et le modèle Catchment au sein de 2.2,
   retiennent des quantités différentes d’humidité du sol et de neige pour le même lieu au même mois. Retirer davantage laisse moins d’eau
   souterraine.

Rien d’autre n’intervient, de sorte que les trois écarts sont liés exactement : l’écart sur l’eau souterraine vaut l’écart sur l’eau totale moins
l’écart sur la soustraction. En écrivant d pour « l’écart entre les deux jeux de données », TWS pour l’eau totale et REST pour tout ce qui, dans
la colonne, n’est pas de l’eau souterraine,

$$ d_{GW} = d_{TWS} - d_{REST} $$

Les trois sont mesurables, ce qui tranche la question de la cause dominante selon les lieux.

**RMS** est la taille typique d’un écart, en centimètres d’eau : on prend l’écart entre les deux jeux de données chaque mois, on l’élève au carré,
on moyenne sur l’enregistrement et on prend la racine carrée. Le décalage fixe de chaque cellule est retiré au préalable, si bien que le RMS
mesure un désaccord qui évolue dans le temps plutôt qu’une distance constante entre les deux.

**Part** indique quelle fraction de l’écart souterrain une cause pourrait expliquer à elle seule. Chaque écart oscille autour de sa propre moyenne
d’une certaine amplitude, et la part compare l’amplitude d’un écart à celle de l’écart souterrain.

Les deux sont des médianes sur les cellules terrestres communes aux deux jeux de données, de février 2003 à juin 2026, chaque cellule comptant à
proportion de sa surface, de sorte qu’une cellule large à l’équateur pèse plus qu’une étroite près d’un pôle.

| L’écart entre les deux jeux de données sur | RMS | Part de l’écart souterrain |
|:---|:---:|:---:|
| l’eau souterraine, ce qui s’affiche à l’écran | 6,42 cm | — |
| l’eau totale, JPL contre CSR | 5,73 cm | 0,85 |
| la soustraction : sol, neige et canopée | 3,38 cm | 0,32 |

Les deux parts totalisent plus de 1 parce que les écarts évoluent en partie ensemble, et ne répartissent donc pas la responsabilité en
pourcentages nets. Il faut les lire comme un ordre : dans une cellule de 1° typique, le désaccord entre le JPL et le CSR explique l’essentiel de
l’écart souterrain, et la soustraction environ un tiers.

Moyenner sur un bassin change cet équilibre. La moyenne annule une bonne part du bruit à l’échelle de la cellule dans les solutions GRACE tout en
laissant intacte la différence systématique de découpage de la colonne, de sorte que plus la région est grande, plus le désaccord provient de la
soustraction. Les parts par bassin atteignent une médiane de 0,72 pour l’eau totale et 0,32 pour la soustraction, et dans 11 des 37 bassins la
soustraction est la cause principale.

L’eau souterraine diverge partout plus que l’eau totale. Cellule par cellule, les séries souterraines des deux jeux de données corrèlent à une
médiane de 0,42, contre 0,75 pour l’eau totale ; par bassin, 0,61 contre 0,87. Chaque pas qui éloigne de la mesure brute ajoute un choix de
modélisation que les deux jeux de données font différemment.

## À quoi cela ressemble sur le terrain { #what-that-looks-like-on-the-ground }

Les deux causes ci-dessus produisent quatre motifs reconnaissables, et un cinquième qui n’est pas du tout un désaccord :

| Motif | Ce que l’on voit | Quelle cause |
|:---|:---|:---|
| Les deux concordent | les deux enregistrements montent et descendent ensemble, à un ou deux centimètres près | aucune ne domine |
| La tendance diffère | les mêmes années humides et sèches, sur des droites qui s’écartent | surtout la soustraction, par ce que 2.2 fait d’une correction |
| L’amplitude diffère | le même calendrier, un cycle plusieurs fois plus haut | la soustraction |
| Les cycles sont opposés | des maxima à des mois d’écart, une corrélation négative | la soustraction, là où l’humidité du sol égale presque l’eau totale |
| Un enregistrement n’est pas de l’eau souterraine | des mètres de variation, ou un cycle qui appartient à un fleuve | glace, eau de surface ou sol gelé, qu’aucun modèle ne porte |

[À quoi ressemblent les écarts](examples.md) parcourt chacun d’eux avec des aquifères nommés sur cinq continents.

## Références { #references }

- Save, H., Bettadpur, S., et Tapley, B. D. (2016). High-resolution CSR GRACE RL05 mascons. *Journal of Geophysical Research: Solid Earth*,
  121, 7547–7569. [doi:10.1002/2016JB013007](https://doi.org/10.1002/2016JB013007){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., et Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
