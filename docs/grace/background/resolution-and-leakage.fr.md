# Résolution, Fuite du Signal et Petites Régions

## Ce que GRACE peut résoudre { #what-grace-can-resolve }

GRACE détecte la masse par la gravité, et la gravité s’atténue avec la distance. Depuis une orbite située à plusieurs centaines de kilomètres
d’altitude, deux masses distantes de moins de quelques centaines de kilomètres se confondent en une seule. La solution mascon du JPL reflète cette
limite : elle calcule une valeur par calotte de 3°, d’environ 330 km de diamètre, et les grilles de 0.5° et 1° de l’application répètent ou
moyennent ces valeurs. Elles facilitent le stockage et la cartographie des données, mais n’ajoutent aucun détail.

![Tailles de grille comparées à la taille des régions, et fuite du signal](../../static/images/grace/grace-resolution-leakage.png)

Le panneau A compare les grilles à deux régions. Le bassin fluvial s’étend sur plusieurs mascons ; sa moyenne s’appuie donc sur plusieurs mesures
indépendantes. L’aquifère est plus petit qu’un mascon. Sa valeur reflète essentiellement le comportement du mascon dans lequel il se trouve, y
compris les variations de stockage à l’extérieur de l’aquifère.

En règle générale, les résultats de GRACE sont fiables pour des régions d’environ 200 000 km² ou plus (environ 4° × 4° près de l’équateur),
utilisables avec précaution jusqu’à la taille d’un mascon (environ 100 000 km²), et de plus en plus incertains en deçà. La GWSa varie bien d’une
maille de 1° à l’autre à l’intérieur d’un mascon, mais uniquement parce que les termes GLDAS varient ; la part GRACE de chaque maille est la
valeur du mascon.

## Fuite du signal { #leakage }

Comme GRACE étale la masse sur quelques centaines de kilomètres, une variation de stockage concentrée sur une petite zone apparaît dans les
données comme une variation plus faible répartie sur une zone plus étendue (panneau B). Le signal **fuit** hors de la région où il s’est produit,
vers les régions voisines. L’inverse se produit aussi : les variations de stockage juste à l’extérieur d’une région y pénètrent.

La fuite du signal pèse le plus lorsque la variation de stockage à l’intérieur de la région diffère de celle des alentours. Le cas le plus
défavorable est celui d’un pompage intensif dans une vallée irriguée entourée de montagnes : la baisse est concentrée dans la vallée, et GRACE
l’étale aussi sur les montagnes. Une moyenne calculée sur la seule vallée sous-estime alors la perte réelle, parfois d’un facteur de plusieurs
unités. Là où le stockage évolue de façon similaire à l’intérieur et à l’extérieur de la région, comme dans un grand bassin sédimentaire sous un
climat uniforme, les fuites entrantes et sortantes s’équilibrent à peu près et la moyenne régionale est proche de la réalité.

Le filtre côtier du JPL limite la fuite entre continents et océans. La fuite entre zones continentales voisines n’est pas corrigée dans les
données de l’application.

## Travailler avec de petites régions { #working-with-small-regions }

Si votre région d’intérêt est plus petite qu’un mascon, ou s’il s’agit d’un centre de pompage entouré de zones au comportement différent, les
approches suivantes sont utiles :

**Analyser l’unité hydrologique plus grande.** Lancez l’analyse sur le bassin fluvial ou le système aquifère qui contient votre zone, à l’aide de
l’un des jeux de régions prédéfinis ou d’une limite importée. Si la quasi-totalité de la variation de stockage se produit dans la zone plus
petite (par exemple, si le pompage est concentré dans l’aquifère), le volume de variation de l’unité plus grande approche celui de la zone plus
petite :

```text
ΔV ≈ GWSa_basin × Area_basin
```

Cela fonctionne parce qu’un volume sommé sur une surface suffisamment grande récupère l’essentiel du signal qui a fui, alors qu’une moyenne sur
une petite surface ne le récupère pas.

**Étalonner à l’aide des puits.** Là où des piézomètres fournissent une estimation indépendante de la variation de stockage sur une partie de la
période GRACE, le rapport entre les estimations issues des puits et celles issues de GRACE donne un facteur d’échelle empirique qui corrige la
fuite du signal dans cette région. Ce facteur est propre à la région et à la période utilisée pour le calculer. Stevens et al. (2025) l’ont fait
pour la Vallée Centrale de Californie ([étude de cas](../case-studies/central-valley.md)).

**Interpréter une maille isolée avec prudence.** Dans la vue globale, vous pouvez cliquer sur une maille pour afficher sa série temporelle. C’est
rapide et utile pour l’exploration, mais deux aquifères voisins situés dans le même mascon donneront des résultats presque identiques, car ils
sont mesurés par la même valeur de 3°.

![Vallée Centrale de Californie : un aquifère étroit et fortement exploité, entouré de montagnes, proche du cas le plus défavorable pour la fuite du signal](../../static/images/grace/app-central-valley.webp)

## Autres limites { #other-limitations }

- **Du stockage, pas des niveaux.** La GWSa est une variation de la masse d’eau. La convertir en variation du niveau de la nappe nécessite un
  rendement spécifique (porosité de drainage) de l’aquifère, qui varie fortement et est souvent mal connu.
- **Aucun détail vertical.** GRACE ne peut pas distinguer les aquifères superficiels des aquifères profonds, ni les nappes captives des nappes
  libres.
- **Erreur des modèles.** Les erreurs des termes GLDAS d’humidité du sol, de neige et de canopée se reportent directement sur la GWSa. C’est
  surtout problématique dans les régions enneigées et humides, où ces termes sont importants.
- **Eaux de surface.** Les variations des réservoirs, des lacs et des plaines inondables sont comptabilisées comme eaux souterraines (voir
  [Calcul du Stockage des Eaux Souterraines](deriving-groundwater.md)).

Malgré ces limites, GRACE offre une vision cohérente et indépendante de la variation du stockage sur des systèmes aquifères entiers, souvent la
seule disponible. Utilisez-le pour les tendances régionales et comparez-le aux données locales chaque fois que possible.

## Références { #references }

- Stevens, M. D., et al. (2025). Groundwater storage loss in the Central Valley analysis using a novel method based on in situ data compared
  to GRACE-derived data. *Environmental Modelling & Software*, 186, 106368.
  [doi:10.1016/j.envsoft.2025.106368](https://doi.org/10.1016/j.envsoft.2025.106368){:target="_blank"}

- Rodell, M., and Famiglietti, J. S. (1999). Detectability of variations in continental water storage from satellite observations of the time
  dependent gravity field. *Water Resources Research*, 35, 2705–2723.
  [doi:10.1029/1999WR900141](https://doi.org/10.1029/1999WR900141){:target="_blank"}
- Longuevergne, L., Scanlon, B. R., and Wilson, C. R. (2010). GRACE hydrological estimates for small basins: Evaluating processing approaches on
  the High Plains Aquifer, USA. *Water Resources Research*, 46, W11517.
  [doi:10.1029/2009WR008564](https://doi.org/10.1029/2009WR008564){:target="_blank"}
