# Calcul du Stockage des Eaux Souterraines

L’application atteint les eaux souterraines par deux chemins. Le jeu de données GRACE + GLDAS 2.1 retranche le stockage modélisé d’une mesure de
gravité. Le jeu de données GLDAS 2.2 lit un état de modèle que GRACE a corrigé. Les deux rapportent la même grandeur sur la même période de
référence, et les deux sont donnés ici, suivis de ce que couvre l’incertitude et de quand préférer l’un à l’autre.

## Le bilan hydrique { #the-water-balance }

Le stockage total de l’eau est la somme de tous les réservoirs d’une colonne de la Terre : l’équivalent en eau de la neige (SWEa), l’eau retenue
par le couvert végétal (CANa), l’humidité du sol (SMa), les eaux souterraines (GWSa) et les eaux de surface des rivières, des lacs et des
réservoirs.

![Composantes du stockage terrestre de l’eau](../../static/images/grace/grace-water-balance.png)

Les deux jeux de données de l’application reposent sur cette identité, et tous deux en laissent les eaux de surface de côté :

$$
\mathrm{TWSa} = \mathrm{SWEa} + \mathrm{CANa} + \mathrm{SMa} + \mathrm{GWSa}
$$

Toute variation du stockage des eaux de surface se retrouve donc dans la GWSa, dans l’un comme dans l’autre jeu de données : aucun modèle GLDAS
ne porte davantage de rivières, de lacs ou de réservoirs. Dans la plus grande partie du monde, les variations des eaux de surface sont faibles
devant les autres termes. Dans les régions avec de grands réservoirs, des zones humides ou des rivières à fortes crues (l’Amazone, le Gange et
le Brahmapoutre, la mer Caspienne, le lac Victoria, le lac Volta), la GWSa inclut ces variations et exagère l’oscillation saisonnière des eaux
souterraines. Dans le Bassin de la Volta, par exemple, le lac représente environ la moitié du signal total de stockage
([étude de cas](../case-studies/volta.md)).

Ce qui sépare les deux voies, c’est quel terme est mesuré et lequel est cherché. La voie 1 mesure la TWSa avec GRACE et réarrange l’identité pour
obtenir la GWSa. La voie 2 lit la GWSa dans un modèle, et la TWSa est le total propre de ce même modèle.

## Voie 1 : GRACE moins GLDAS 2.1 { #route-1-grace-minus-gldas-21 }

GRACE mesure la variation totale de l’eau stockée dans la colonne, et les modèles de surface terrestre estiment les trois termes qui ne sont pas
souterrains assez bien pour qu’on les retranche. En réarrangeant l’identité ci-dessus, les eaux souterraines apparaissent comme le résidu :

$$
\mathrm{GWSa} = \mathrm{TWSa} - (\mathrm{SWEa} + \mathrm{CANa} + \mathrm{SMa})
$$

Rien dans cette voie ne modélise les eaux souterraines. Tout ce que GRACE a pesé et que les trois termes des modèles n’expliquent pas est
rapporté comme eau souterraine, ce qui fait la force de la méthode là où ces termes sont petits et sa faiblesse là où ils ne le sont pas.

### Les termes GLDAS { #the-gldas-terms }

L’application prend l’équivalent en eau de la neige, le stockage par interception du couvert végétal et l’humidité du sol dans chacun des trois
modèles GLDAS 2.1 — Noah, VIC et le modèle Catchment, décrits dans
[Les Modèles de Surface Terrestre GLDAS](land-surface-models.md) —, les convertit de kg/m² en cm d’eau et place les trois sur la même grille à 1°
(Noah est moyenné de 0.25° à 1°). L’anomalie de chaque modèle est sa valeur moins la moyenne de cette maille pour 2004–2009, la même période de
référence que GRACE.

L’humidité du sol désigne la somme des couches pour Noah et VIC, et le réservoir de la zone racinaire pour le modèle Catchment, dont le
réservoir de profil publié entraînerait avec lui les eaux souterraines du modèle lui-même
([pourquoi](land-surface-models.md#why-the-catchment-model-needs-separate-handling)).

Les trois modèles sont souvent en désaccord, en particulier sur l’humidité du sol profond. Plutôt que d’en choisir un, l’application en fait la
moyenne : SWEa, CANa et SMa sont chacune la moyenne des trois modèles, et la dispersion entre les modèles (leur écart-type) sert d’incertitude
pour chaque terme.

### Chaîne de traitement { #processing-chain }

![La chaîne de traitement GRACE + GLDAS 2.1, des entrées publiées aux cinq couches servies par l’application](../../static/images/grace/grace-processing.png)

La TWSa de GRACE est mise à l’échelle par les facteurs de gain à 0.5°, moyennée à 1°, puis combinée à l’ensemble de modèles pour donner la GWSa
sur une grille à 1°. L’application sert cinq couches : GWSa, SMa, SWEa et CANa à 1°, et TWSa à 0.5°, sur la grille telle que le JPL la
distribue. Utiliser 1° pour les couches dérivées suit la pratique habituelle qui consiste à combiner GRACE et les données de modèles sur la plus
grossière des deux grilles ; rapporter la GWSa à 0.5° donnerait une impression de détail qu’aucun des deux jeux de données ne possède.

Aucune lacune n’est comblée. Chaque valeur mensuelle dans l’application est la valeur publiée par le JPL, mise à l’échelle comme décrit
ci-dessous, combinée à l’ensemble GLDAS pour ce mois. Les 35 mois qui manquent à GRACE manquent aussi ici, et le comblement des lacunes de
l’application n’agit sur eux que dans le graphique (voir [Lacunes et Comblement des Lacunes](../mission/gap-filling.md)).

### Facteurs de gain { #gain-factors }

La solution mascon est nativement à 3°, et le fichier à 0.5° répète la valeur de chaque mascon dans toutes les mailles qu’il contient — 36 à
l’équateur, une médiane de 42 sur les terres, et davantage vers les pôles, où un mascon de même surface couvre plus de longitude : la grille
publiée ne porte donc à elle seule aucun détail plus fin qu’un mascon. Le JPL distribue dans le même fichier une grille de **facteurs de gain**
destinée à récupérer une partie de ce détail. Ils sont obtenus en faisant passer le modèle de surface terrestre CLM par le même traitement que
GRACE et en estimant, maille par maille, le multiplicateur qui restitue l’amplitude originale du modèle. La correction est une simple
multiplication, le facteur étant constant dans le temps :

$$
g'(x,y,t) = g(x,y,t) \times s(x,y)
$$

Le JPL n’applique pas cette mise à l’échelle avant de distribuer les données ; le GRACE-FO Level-3 Handbook indique que c’est aux utilisateurs
de l’appliquer, et son propre exemple sur les eaux souterraines suit la même approche TWSa moins GLDAS que cette application, en inscrivant la
multiplication comme étape de prétraitement. L’application applique les facteurs à la TWSa à 0.5°, avant que la TWSa ne soit moyennée à 1°,
puisque la structure qu’ils ajoutent est plus fine qu’une maille de 1°.

La plupart des facteurs sont proches de 1 : 84 % des mailles qui en reçoivent un tombent entre 0.5 et 1.5. L’application dessine 60 064 mailles
à 0.5°, et une maille conserve la valeur du mascon non mise à l’échelle dans deux cas.

**Là où le JPL ne publie aucun facteur.** Soit 3 365 mailles, 5.6 % de la grille, dont 84 % se trouvent au nord de 60°N. Les facteurs ne sont pas
faits pour la glace, car CLM ne représente ni les calottes glaciaires ni les glaciers de montagne. Le JPL laisse aussi l’océan non mis à
l’échelle, que le masque terrestre de GLDAS retire de toute façon de l’application. L’Antarctique ne se pose jamais : GLDAS court de 60°S vers le
nord, et l’application n’a donc aucune maille antarctique.

**Là où le facteur est implausible**, c’est-à-dire nul ou négatif, supérieur à 3 ou inférieur à 1/3. Soit 790 mailles, 1.3 % de la grille, et
c’est une règle de l’application et non du JPL : le fichier marque toute son étendue comme valide et ne fixe aucune borne.

Ce que ces mailles ont en commun, c’est que la régression qui produit le facteur n’avait presque aucun signal sur lequel travailler, de sorte que
sa pente est instable. Elles sont côtières environ trois fois plus souvent que les mailles conservées (51 % à moins de deux mailles de l’eau,
contre 19 %) et portent de la neige toute l’année treize fois plus souvent (18.5 % contre 1.4 %). Près de la moitié ne sont ni l’un ni l’autre et
se situent dans des intérieurs arides — le Kalahari, l’intérieur australien, le Karoo, l’Atacama — où la variation de stockage de CLM est assez
faible pour que l’ajustement divise par presque rien. Glace, littoral et désert sont la même défaillance dans trois décors, et c’est pourquoi une
borne sur le facteur les attrape là où un masque de glaciers seul n’y parviendrait pas.

Les facteurs dans ces mailles vont jusqu’à 24 et −1.35. Un facteur négatif inverse le signe de l’anomalie ; un facteur de 24 a transformé −292 cm
en −7048 cm sur l’île d’Ellesmere. Dans les bassins arides, l’exclusion est inoffensive de toute façon — quatre des 806 mailles du Grand Bassin
Artésien, déplaçant sa série de 0.00 cm — parce qu’une petite anomalie multipliée par un mauvais facteur reste petite.

Cela compte en au moins un endroit qu’un utilisateur remarquerait. Une de ces mailles tombe dans le **Bassin du Caucase du Nord**, un aquifère
des jeux de régions de l’application elle-même. Appliquer tous les facteurs a doublé la série d’eau souterraine de ce bassin : l’écart-type de sa
moyenne est passé de 13.3 cm sans mise à l’échelle à 23.5 cm, et s’établit à 13.6 cm lorsque les mailles implausibles sont laissées
tranquilles. Presque toute cette amplitude apparente venait d’une poignée de mailles dégénérées, et non du signal. Le gain que les facteurs
existent pour restituer survit à la règle : la Vallée Centrale de Californie le conserve entièrement, de 10.2 cm à 12.4 cm, et le Congo presque
entièrement, de 7.6 cm sans mise à l’échelle à 7.9 cm contre 8.1 cm avec tous les facteurs appliqués.

Deux bassins glaciaires des jeux de bassins versants, l’Alsek et la Santa Cruz, portent une GWSa très importante quoi qu’on fasse des facteurs de
gain. GRACE y détecte la perte de masse glaciaire et GLDAS ne modélise pas les glaciers : le bilan hydrique l’attribue donc aux eaux
souterraines. Ces nombres sont un artefact de la méthode, non de la mise à l’échelle.

Ce que les facteurs ne font pas, c’est transformer la grille à 0.5° en 36 mesures indépendantes. Le mascon sous-jacent reste une seule
estimation, et les facteurs redistribuent son amplitude en s’appuyant sur l’idée qu’un modèle se fait de la variation du stockage à l’intérieur.
Le handbook est explicite : les modèles qui les sous-tendent comportent des biais et « n’incluent typiquement ni les eaux souterraines ni les
activités humaines dans leurs simulations », de sorte qu’un aquifère fortement pompé est précisément là où la redistribution est la moins
informée par ce que l’on mesure.

## Voie 2 : les eaux souterraines depuis GLDAS 2.2 { #route-2-groundwater-from-gldas-22 }

Le modèle Catchment porte les eaux souterraines comme un état à part entière, et la simulation GLDAS 2.2 corrige cet état chaque mois en
assimilant l’anomalie de stockage total de l’eau de GRACE. Les eaux souterraines arrivent donc comme une variable publiée, `GWS_tavg`, et le
calcul est une seule soustraction :

$$
\mathrm{GWSa}_{22} = \mathrm{GWS} - \overline{\mathrm{GWS}}_{2004\text{–}2009}
$$

La même période de référence 2004–2009 que GRACE : les anomalies des deux jeux de données sont donc autour du même zéro et peuvent être tracées
sur un seul axe.

La NASA publie 2.2 sous forme de champs quotidiens ; l’application les moyenne sur les mois calendaires pour s’accorder au reste. Tout est
converti de kg/m² en cm. Le magasin à 0.25° conserve les valeurs au centième de centimètre, parce que cette grille existe pour les petites
régions où un demi-centimètre fait partie du signal et où il n’y a pas de dispersion d’ensemble où le dissimuler. Un magasin à 1°, moyenné
depuis les mêmes mailles que celles des magasins GRACE, alimente la carte globale au dixième de centimètre, ce qui fait descendre la première
vue d’une couche mondiale de 10.5 Mo à 7.1 Mo.

### L’humidité du sol, et pourquoi ce n’est pas celle que publie la NASA { #soil-moisture-and-why-it-is-not-what-nasa-publishes }

L’humidité du sol publiée du modèle Catchment contient déjà les eaux souterraines. `SoilMoist_P_tavg` est tout le profil depuis la surface vers
le bas, et `SoilMoist_P − GWS` est positif partout : une médiane de 277 mm d’eau située au-dessus de la nappe. Le bilan propre du produit se
ferme sur trois termes :

$$
\mathrm{TWS} = \mathrm{SoilMoist\_P} + \mathrm{SWE} + \mathrm{CanopInt}
$$

Servie ainsi, la SMa du jeu de données 2.2 signifierait autre chose que la SMa du jeu de données GRACE, et les cinq couches ne s’additionneraient
pas dans le graphique. L’application stocke donc la SMa de 2.2 comme l’anomalie de `SoilMoist_P − GWS`, c’est-à-dire l’humidité du sol au-dessus
de la nappe. D’après la définition que la NASA donne elle-même des eaux souterraines du modèle, cette différence est le réservoir de la zone
racinaire, qui est ce que l’ensemble de modèles du jeu de données GRACE prend au même modèle — voir
[pourquoi le modèle Catchment demande un traitement à part](land-surface-models.md#why-the-catchment-model-needs-separate-handling). Avec cette
substitution, les cinq couches se ferment exactement :

$$
\mathrm{TWSa}_{22} = \mathrm{SWEa}_{22} + \mathrm{CANa}_{22} + \mathrm{SMa}_{22} + \mathrm{GWSa}_{22}
$$

Mesuré sur le magasin publié à 0.25°, le plus grand résidu de tout l’enregistrement est de 0.02 cm, soit deux unités de son propre arrondi.

### Ce que l’assimilation fait et ne fait pas { #what-the-assimilation-does-and-does-not-do }

GRACE voit toute la colonne et ne peut pas dire à quel réservoir appartient un écart : le schéma répartit donc la correction de chaque mois entre
les états du modèle, dont les eaux souterraines. Le pompage est absent de la physique du modèle et n’atteint l’état d’eau souterraine que par
cette correction.

Cela a des conséquences pour la lecture d’une série 2.2.

L’enregistrement commence en février 2003, dix mois après l’avril 2002 de GRACE, parce que c’est à ce moment-là que la simulation assimilatrice a
été démarrée.

Il n’y a aucun mois manquant. Là où GRACE a une lacune, le modèle continue de tourner ; il reste simplement non corrigé pour ce mois-là, de sorte
que la série est continue et que rien ne marque l’endroit où la correction s’est interrompue.

La grille est plus fine que la correction. Une maille de 0.25° est une maille du modèle, et l’information GRACE qui l’a atteinte venait d’un
mascon CSR, de 1° à surface égale à l’équateur : les mailles voisines diffèrent donc par ce que dit le modèle et non par ce qui a été mesuré — la même mise en garde que les
facteurs de gain sur l’autre voie, arrivant par un autre chemin.

## Incertitude { #uncertainty }

Chaque couche du jeu de données GRACE est accompagnée d’une incertitude à un écart-type (1σ), que le graphique de séries temporelles trace en
bande autour de la ligne :

- **TWSa :** l’incertitude publiée par le JPL pour chaque mascon et chaque mois, multipliée par le même facteur de gain que les données, afin
  que la bande reste proportionnelle à la valeur qu’elle décrit.
- **SWEa, CANa, SMa :** l’écart-type entre les trois modèles GLDAS.
- **GWSa :** les quatre combinées, traitées comme indépendantes :

$$
\sigma_{\mathrm{GWSa}} = \sqrt{\sigma_{\mathrm{TWSa}}^2 + \sigma_{\mathrm{SWEa}}^2 + \sigma_{\mathrm{CANa}}^2 + \sigma_{\mathrm{SMa}}^2}
$$

La bande d’incertitude rend compte de l’erreur de mesure de GRACE et du désaccord entre les modèles. Elle ne rend pas compte des erreurs que les
trois modèles partagent, de l’effet de l’omission des eaux de surface, de la fuite du signal depuis l’extérieur d’une région (voir
[Résolution, Fuite du Signal et Petites Régions](../mission/resolution-and-leakage.md)), ni de l’incertitude des facteurs de gain eux-mêmes, que le JPL ne
publie pas. L’incertitude réelle est plus grande que ce que montre la bande.

Une mise en garde sur leur combinaison : l’incertitude de la TWSa du JPL est une erreur de mesure, tandis que les trois termes GLDAS sont la
dispersion entre Noah, VIC et CLSM, qui mesure l’ampleur du désaccord entre les modèles et non celle de leur erreur. Les additionner en
quadrature traite les deux comme comparables. Sur la plupart des bassins, c’est la dispersion entre modèles qui domine : dans le Congo, 3.1 cm
pour GRACE contre 5.7 cm combinés.

GLDAS 2.2 ne porte aucune incertitude. C’est une simulation unique et non un ensemble : il n’y a donc pas de dispersion à prendre, et la NASA ne
publie aucune erreur mensuelle pour le produit. Le graphique ne trace aucune bande pour lui. Ce silence est l’absence d’une estimation ; tout ce
qui, dans [Les Modèles de Surface Terrestre GLDAS](land-surface-models.md#accuracy-and-mixing-versions), rend un modèle de surface terrestre
inexact s’applique encore, sans que rien ne le rapporte.

## Lequel utiliser { #which-one-to-use }

Aucun des deux jeux de données ne l’emporte partout, et la bonne habitude est de tracer les deux et de regarder où ils se séparent.

**C’est sur la voie GRACE qu’il faut s’appuyer pour savoir de combien le stockage a changé.** Ses eaux souterraines reposent sur une mesure de
masse, et les modèles n’entrent que comme les termes retranchés. Là où les termes GLDAS sont faibles devant le signal d’eau souterraine — la
plupart des aquifères arides et semi-arides —, très peu de la réponse dépend de la justesse des modèles.

**C’est la voie 2.2 qu’il faut saisir sur une petite région**, parce qu’elle est moyennée sur une grille à 0.25° là où l’autre est à 1° : un
bassin large de quelques mailles est donc décrit par seize fois plus de mailles. Son enregistrement continu en fait aussi la série la plus facile
à travailler année par année. Ce qu’elle achète, c’est de l’échantillonnage et non de la résolution : l’information GRACE qu’elle contient est
tout de même arrivée à 3°.

**Préférer la voie GRACE pour la recharge.** Barbosa et al. (2025) ont appliqué la méthode de fluctuation de la nappe aux deux jeux de données
dans le Bassin de la Volta et ont obtenu 17.4 et 36.1 cm/an avec 2.2 contre 5.8 et 10.7 cm/an avec GRACE, les puits donnant une médiane de 10.4.
Ils recommandent 2.2 pour les tendances et non pour la recharge (voir [Bassin de la Volta](../case-studies/volta.md)).

**Leur accord vaut plus que l’un ou l’autre seul.** Une mesure et un modèle construit indépendamment qui disent la même chose sont difficiles à
écarter. Là où ils divergent, tracez les composantes : une divergence qui vit dans la SMa est un autre problème qu’une divergence qui vit dans la
TWSa.

L’enregistrement de 2.2 commence dix mois plus tard que celui de GRACE, en février 2003, et la solution GRACE derrière 2.2 est celle du CSR
tandis que les couches GRACE de l’application elle-même sont celles du JPL. Ni l’un ni l’autre n’est un défaut des données ; tous deux
apparaîtront chaque fois que les deux seront superposés.

## À quoi sert la GWSa { #what-gwsa-is-good-for }

La GWSa sert surtout à répondre à des questions régionales de direction et de rythme : le stockage de cet aquifère diminue-t-il, à quelle
vitesse, et la baisse a-t-elle ralenti après un changement de politique ou une suite d’années humides ? Elle ne convient pas à des décisions à
l’échelle d’un champ de captage ou d’un seul district d’irrigation, et elle ne dit rien des niveaux d’eau ni de la qualité de l’eau. Là où des
puits de suivi existent, comparez la tendance au changement de stockage estimé à partir des puits ; l’accord entre les deux renforce les deux.

Cela vaut pour l’un comme pour l’autre jeu de données. Tous deux sont un changement de stockage moyenné sur une surface bien plus grande qu’un
champ de captage, tous deux incluent les eaux de surface dans le terme souterrain, et une comparaison avec des puits est la vérification la plus
solide dont on dispose pour l’un comme pour l’autre.

## Références { #references }

- Rodell, M., et al. (2004). The Global Land Data Assimilation System. *Bulletin of the American Meteorological Society*, 85, 381–394.
  [doi:10.1175/BAMS-85-3-381](https://doi.org/10.1175/BAMS-85-3-381){:target="_blank"}
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE data assimilation for groundwater
  and drought monitoring: Advances and challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
  La simulation GLDAS 2.2 que lit la seconde voie.
- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
  La comparaison des estimations de recharge des deux jeux de données ; voir [Bassin de la Volta](../case-studies/volta.md).
- Données GLDAS au NASA GES DISC : [Noah](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_M_2.1/summary){:target="_blank"},
  [VIC](https://disc.gsfc.nasa.gov/datasets/GLDAS_VIC10_M_2.1/summary){:target="_blank"},
  [CLSM](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM10_M_2.1/summary){:target="_blank"},
  [Catchment GRACE-DA1 2.2](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM025_DA1_D_2.2/summary){:target="_blank"}
