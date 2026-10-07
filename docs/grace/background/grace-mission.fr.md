# La Mission GRACE

## Deux satellites qui pèsent l’eau { #two-satellites-that-weigh-water }

GRACE (Gravity Recovery and Climate Experiment) est une paire de satellites identiques qui volent l’un derrière l’autre sur la même orbite
polaire, à environ 220 km l’un de l’autre et à quelque 500 km d’altitude. La NASA et le Centre aérospatial allemand ont lancé la première paire en
mars 2002. GRACE Follow-On (GRACE-FO), lancée en mai 2018, poursuit la mesure avec la même conception.

![Géométrie de la mission GRACE : altitude, séparation, mesure de distance, suivi GPS et accéléromètres](../../static/images/grace/grace-mission-geometry.png)

Les satellites ne prennent pas d’images de la surface. Ils mesurent en continu la distance qui les sépare, avec un système de mesure de distance
par micro-ondes précis à environ un micromètre près, une fraction de l’épaisseur d’un cheveu. (GRACE-FO embarque aussi un instrument
expérimental de mesure de distance par laser, plus précis encore.) Des récepteurs GPS suivent la position de chaque satellite, et des
accéléromètres embarqués mesurent les forces non gravitationnelles, principalement le frottement atmosphérique, afin de pouvoir les retirer. Ce
qui reste des variations de cette distance révèle les variations de la gravité terrestre le long de la trajectoire.

![Comment GRACE détecte une anomalie de masse](../../static/images/grace/grace-ranging.png)

Lorsque la paire s’approche d’une région présentant un excédent de masse, par exemple un aquifère qui s’est rempli après une saison humide, le
satellite de tête ressent l’attraction supplémentaire en premier et accélère légèrement, si bien que l’écart entre les deux augmente. Une fois que
le satellite de tête a dépassé la masse, il est freiné tandis que le satellite suiveur est attiré vers l’avant, et l’écart diminue. Au passage du
satellite suiveur, l’écart augmente de nouveau avant de revenir à la normale.

L’orbite couvre l’ensemble du globe environ une fois par mois. Le Jet Propulsion Laboratory (JPL) de la NASA, le Center for Space Research de
l’Université du Texas (CSR) et le Centre allemand de recherche en géosciences (GFZ) transforment chacun un mois de mesures de distance en une carte
du champ de gravité terrestre. En soustrayant un champ moyen de long terme, on obtient l’anomalie de gravité du mois.

## De la gravité à l’eau { #from-gravity-to-water }

Sur des périodes allant d’un mois à quelques années, la quasi-totalité des variations du champ de gravité terrestre au-dessus des continents
provient des déplacements de l’eau : accumulation et fonte de la neige, humidification et assèchement des sols, montée et baisse des rivières et
des lacs, remplissage des aquifères ou prélèvements par pompage. L’anomalie de gravité peut donc être convertie en variation de la masse d’eau
stockée dans une colonne qui s’étend du sommet de la végétation jusqu’aux aquifères. Ce total est appelé **stockage total en eau (TWS)**, et son
écart à la moyenne de long terme est l’**anomalie de stockage total en eau (TWSa)**.

La TWSa est exprimée en hauteur d’**équivalent en eau liquide (LWE)** en centimètres : l’épaisseur de la lame d’eau qui expliquerait la
variation de masse si elle était répartie uniformément sur la surface. Une TWSa de −10 cm sur une région signifie que la région contient 10 cm
d’eau de moins que sa moyenne de long terme, ce qui revient à retirer une lame d’eau de 10 cm sur toute sa surface. Comme il s’agit déjà d’une
hauteur d’eau, une valeur LWE se convertit en volume en la multipliant par la surface : −10 cm sur 50 000 km² représentent −5 km³.

!!! note "Des anomalies, pas des quantités"
    GRACE mesure des variations de stockage, pas la quantité stockée. Une GWSa nulle signifie que le stockage est égal à sa moyenne 2004–2009,
    et non que l’aquifère est vide. L’anomalie peut vous indiquer combien de stockage a été perdu ou gagné entre deux dates, mais pas combien
    d’eau il reste.

## La solution mascon utilisée par l’application { #the-mascon-solution-used-by-the-app }

L’application utilise la solution **mascon** du JPL (RL06.3, avec le filtre Coastline Resolution Improvement). Au lieu de décrire le champ de
gravité par une série mathématique lisse, le JPL divise la surface de la Terre en 4 551 calottes de même superficie, d’environ 3° (soit environ
330 km) de diamètre, et calcule directement la variation de masse de chaque calotte. Le filtre côtier scinde les calottes qui chevauchent une
côte afin que les variations de masse océaniques ne contaminent pas les valeurs continentales.

Le JPL distribue les valeurs des mascons sur une grille de 0.5° par commodité. Les mailles de 0.5° situées à l’intérieur d’un mascon reprennent
toutes la valeur de ce mascon : la résolution réelle de la TWSa est donc le mascon de 3°, et non la maille de 0.5°. Vous pouvez le constater dans
l’application : choisissez TWSa comme couche affichée, zoomez et activez **Show mascon boundaries** (afficher les limites des mascons). Les
mailles TWSa ne changent de valeur qu’au franchissement d’une limite de mascon.

La TWSa du JPL est calculée par rapport à la moyenne de janvier 2004 à décembre 2009. La même période de référence est utilisée pour toutes les
couches de l’application.

## La série et ses lacunes { #the-record-and-its-gaps }

![La série de données GRACE et GRACE-FO](../../static/images/grace/grace-timeline.png)

La série commence en avril 2002 et est mise à jour à mesure que le JPL publie de nouveaux mois GRACE-FO, généralement avec quelques mois de
décalage. Elle présente deux types de lacunes :

- **Des mois manquants isolés.** Quelques mois manquent en 2002–2003, pendant la mise en service de la mission. À partir de 2011, les batteries
  vieillissantes de GRACE ne pouvaient plus alimenter les instruments sur toutes les portions de l’orbite ; ceux-ci ont donc été éteints environ
  un mois sur cinq ou six. GRACE-FO a manqué deux mois supplémentaires, août et septembre 2018, peu après son lancement.
- **L’intervalle entre les missions.** GRACE a cessé ses opérations scientifiques en juin 2017, et GRACE-FO a commencé à fournir des données en
  juin 2018, laissant 11 mois sans mesures.

L’application affiche les mois manquants comme des lacunes dans la série temporelle et les saute dans l’animation de la carte. La page
[Le Modèle Saisonnier](../gap-filling/seasonal-model.md) montre comment les estimer lorsqu’une analyse nécessite une série mensuelle complète.

## Références { #references }

- Tapley, B. D., Bettadpur, S., Watkins, M., and Reigber, C. (2004). The gravity recovery and climate experiment: Mission overview and early
  results. *Geophysical Research Letters*, 31, L09607. [doi:10.1029/2004GL019920](https://doi.org/10.1029/2004GL019920){:target="_blank"}
- Watkins, M. M., Wiese, D. N., Yuan, D.-N., Boening, C., and Landerer, F. W. (2015). Improved methods for observing Earth's time variable mass
  distribution with GRACE using spherical cap mascons. *Journal of Geophysical Research: Solid Earth*, 120, 2648–2671.
  [doi:10.1002/2014JB011547](https://doi.org/10.1002/2014JB011547){:target="_blank"}
- Wiese, D. N., Landerer, F. W., and Watkins, M. M. (2016). Quantifying and reducing leakage errors in the JPL RL05M GRACE mascon solution.
  *Water Resources Research*, 52, 7490–7502. [doi:10.1002/2016WR019344](https://doi.org/10.1002/2016WR019344){:target="_blank"}
- Landerer, F. W., et al. (2020). Extending the global mass change data record: GRACE Follow-On instrument and science data performance.
  *Geophysical Research Letters*, 47, e2020GL088306. [doi:10.1029/2020GL088306](https://doi.org/10.1029/2020GL088306){:target="_blank"}
- Données mascon GRACE et GRACE-FO du JPL :
  [grace.jpl.nasa.gov/data/get-data/jpl_global_mascons](https://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/){:target="_blank"}
