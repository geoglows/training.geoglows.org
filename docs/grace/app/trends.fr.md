# Analyse des Tendances et des Écarts

## Ce que fait l’analyse { #what-the-analysis-does }

**Analyze**, dans l’en-tête, colore chaque contour de région, dans la vue régionale, ou chaque maille, dans la vue globale, par un seul nombre
qui résume l’enregistrement entier, à la place de la valeur du mois choisi sur le contrôle de temps. L’analyse est active à l’ouverture de
l’application ; **Hide** la désactive et rend à la carte l’anomalie mensuelle.

**Color by**, à côté du bouton, choisit ce nombre. Une mesure travaille sur le jeu de données sélectionné, et trois comparent les deux jeux entre
eux :

| Color by | Ce qu’elle calcule | Les deux jeux | S’ouvre sur |
|:---|:---|:---:|:---:|
| Trend in GWSa | la pente par moindres carrés des valeurs mensuelles, en cm/an | non | les 5 dernières années |
| GRACE vs GLDAS 2.2: trend difference | la pente GRACE moins la pente 2.2 | oui | l’enregistrement entier |
| GRACE vs GLDAS 2.2: agreement | la corrélation de Pearson des deux séries mensuelles | oui | l’enregistrement entier |
| GRACE vs GLDAS 2.2: seasonal swing | l’amplitude saisonnière GRACE divisée par celle de 2.2 | oui | l’enregistrement entier |

L’entrée de tendance nomme ce qui est affiché : elle se lit **Trend in GWSa** sur la couche par défaut et **Trend in SMa** sur l’humidité du sol.
Les trois comparaisons n’apparaissent que lorsque l’eau souterraine (GWSa) est affichée, car c’est la seule grandeur que les deux jeux produisent
en propre : l’humidité du sol, la neige et l’eau du couvert de la voie 2.1 viennent des trois modèles de surface terrestre, sans GRACE dedans,
si bien qu’appeler « GRACE vs GLDAS 2.2 » une comparaison avec elles nommerait un jeu de données qui n’y figure pas.

Toute mesure a besoin d’au moins 24 mois de données dans la fenêtre, et les trois comparaisons de 24 mois rapportés par les deux jeux ; une
région ou une maille qui en compte moins apparaît comme **Insufficient data**. [Explorer les écarts dans
l’application](../compare/exploring.md) couvre ce que signifient les trois comparaisons, les limites de leurs classes et la façon de les lire.
Le reste de cette page porte sur la tendance.

## Classification des tendances { #trend-classification }

Sous **Trend in GWSa**, ou la tendance de ce qui est affiché, chaque région ou maille est colorée selon le rythme auquel cette couche augmente
ou diminue.

![Aquifères du jeu Global Aquifers classés selon la tendance du stockage des eaux souterraines sur les cinq dernières années](../../static/images/grace/app-home.webp)

Dans la vue régionale, ci-dessus, chaque aquifère ou bassin reçoit une tendance unique calculée à partir de la moyenne de ses mailles (voir
[Vue Régionale](regional-view.md#the-landing-page)). C’est le meilleur indicateur pour un aquifère donné.

![Tendance du stockage des eaux souterraines sur les cinq dernières années pour chaque maille de 1°, dans la vue globale](../../static/images/grace/app-global-trends.webp)

La vue globale, ci-dessus, classe toutes les mailles continentales — 15 159 sur la grille à 1° du jeu de données GRACE et 17 346 sur celle de
GLDAS 2.2, qui porte un masque terrestre un peu plus large : elle montre donc où le stockage évolue, indépendamment des limites des aquifères.
Il augmente dans le Sahel et en Afrique de l’Est, et diminue dans une grande partie du Moyen-Orient, le nord de l’Inde et le Brésil.

La tendance est la pente d’une droite ajustée par moindres carrés sur les valeurs mensuelles de la fenêtre, en cm par an. Les mois sans données
GRACE sont ignorés plutôt que comblés, ce qui ne concerne que le jeu de données GRACE ; GLDAS 2.2 a une valeur à chaque mois.

Les tendances sont calculées sur le jeu de données sélectionné : la classification change donc quand vous en changez. Deux différences comptent
quand on compare les deux cartes. GLDAS 2.2 commence en février 2003 contre avril 2002 pour GRACE, et la fenêtre **All** couvre donc dix mois de
moins. Et une tendance 2.2 est une tendance dans un état de modèle que GRACE corrige chaque mois, qui hérite de la résolution de GRACE quelque
fine que paraisse la grille du modèle.

| Classe | Tendance (cm/an) |
|---|---|
| Extreme decline (baisse extrême) | inférieure à −2 |
| Decline (baisse) | −2 à −0.5 |
| Static (stable) | −0.5 à +0.5 |
| Increase (hausse) | +0.5 à +2 |
| Extreme increase (hausse extrême) | supérieure à +2 |

La légende compte les régions ou les mailles de chaque classe. À titre de repère, une tendance de −2 cm/an maintenue sur 100 000 km² correspond
à une perte de 2 km³ d’eau par an.

### Facteurs de gain et amplitude des tendances { #gain-factors-and-trend-magnitudes }

Cette section porte sur le jeu de données GRACE. GLDAS 2.2 n’est pas concerné : aucun facteur de gain ne lui est appliqué, et la solution GRACE
qui y est assimilée est celle du CSR et non celle du JPL.

La TWSa servie par l’application a les facteurs de gain du JPL appliqués (voir
[Calcul du Stockage des Eaux Souterraines](../gldas/deriving-groundwater.md#gain-factors)), et ces facteurs se répercutent directement sur
les tendances, car un multiplicateur constant appliqué à une série temporelle multiplie sa pente. Le JPL assortit cet usage d’une mise en garde :
les facteurs sont dominés par le cycle annuel, et le GRACE-FO Level-3 Handbook indique qu’ils « peuvent introduire des biais dans des bandes de
fréquence autres que la composante annuelle, en particulier pour les tendances de long terme », pour lesquelles il faudrait des facteurs dérivés
par noyau de moyennage. Aucun facteur de ce type n’est publié pour ce produit : l’application applique donc partout les facteurs standard et
fournit une seule valeur de GWSa, plutôt qu’un chiffre pour la carte et un autre pour la tendance.

En pratique, cela déplace très peu la plupart des tendances. Sur la fenêtre de cinq ans par laquelle s’ouvre l’application, la tendance des eaux
souterraines de la maille médiane se déplace de 0.12 cm/an et l’amplitude médiane des tendances passe de 0.95 à 0.93 cm/an ; sur l’ensemble de la
série, le déplacement médian est de 0.05 cm/an. Environ 15 % des mailles franchissent une limite de classe sur cinq ans, et 10 % sur l’ensemble
de la série — presque toutes des mailles déjà proches des seuils de ±0.5 ou ±2 cm/an, où une faible variation de pente change l’étiquette. Les
exceptions sont les mailles englacées, au Svalbard, en Nouvelle-Zemble et dans les champs de glace de Patagonie, où un facteur élevé s’applique à
un signal glaciaire énorme et où la tendance peut se déplacer de plusieurs dizaines de cm par an. Ces mailles n’ont jamais représenté des eaux
souterraines. Traitez une classe comme un résumé et non comme une mesure, et lisez ensemble l’amplitude de la tendance et la série temporelle.

## La fenêtre d’analyse { #the-analysis-window }

Le sélecteur **Window** de l’en-tête fixe la période couverte par l’ajustement, en remontant depuis le mois le plus récent : 5, 10, 15 ou 20 ans,
ou **All** pour l’ensemble de la série depuis 2002. La classification et la légende se mettent à jour lorsque vous la modifiez.

La concordance et l’amplitude saisonnière utilisent toujours l’enregistrement entier : le sélecteur s’estompe donc sous ces deux mesures. Une
corrélation sur cinq ans pose une autre question qu’une corrélation sur vingt ans, et un cycle saisonnier estimé sur cinq ans repose sur cinq
valeurs par mois du calendrier. Le réglage est conservé pendant que le sélecteur est estompé et revient dès que vous retournez à une tendance.

L’écart de tendance, lui, utilise bien le sélecteur, mais il s’ouvre sur l’enregistrement entier et non sur les cinq ans par lesquels s’ouvre une
tendance, parce que les limites de ses classes ont été tracées à partir de la dispersion sur l’enregistrement entier : ±0,25 et ±1 cm/an
signalent comme extrême environ un dixième des régions sur l’enregistrement entier et environ un tiers sur cinq ans. Déplacer la fenêtre reste le
bon geste si vous voulez savoir si les deux jeux de données ont commencé à diverger récemment, et une fois le sélecteur déplacé rien ne le
ramène.

La tendance garde la fenêtre courte par défaut, et ce sont ses propres limites qui l’expliquent. Sur l’enregistrement entier, ±0,5 et ±2 cm/an
placent 59 des 99 contours de Global Aquifers dans **Static** et laissent **Extreme increase** vide, car une pente ajustée sur 24 ans gomme les
retournements sur lesquels porte généralement la question d’un gestionnaire. Sur cinq ans, ces mêmes 99 se répartissent en 11/22/34/28/4.

Dans la plupart des régions, le stockage oscille entre années humides et années sèches ; une fenêtre courte peut donc ne saisir qu’une
oscillation au lieu de l’évolution de long terme. Dans la Vallée Centrale de Californie, le stockage des eaux souterraines a diminué de 2002
jusqu’à la sécheresse de 2021–2022, puis s’est partiellement rétabli après l’hiver très humide de 2022–2023. La tendance sur 5 ans est une
hausse ;
la tendance sur 20 ans est une baisse. Les deux sont exactes pour leur fenêtre. Examinez la série temporelle avant de tirer des conclusions d’une
classe de tendance, et comparez plusieurs fenêtres.

## Droites ajustées sur le graphique { #fitted-lines-on-the-chart }

Lorsqu’une région ou une maille est sélectionnée et qu’une tendance est affichée, le graphique ajoute la droite ajustée en pointillé sur la
fenêtre, et la légende donne sa pente, par exemple « GWSa trend +2.25 cm/yr (last 5 yr) ». Chaque composante tracée reçoit sa propre droite de
tendance.

L’écart de tendance trace les deux ajustements, un par jeu de données, et rapporte sous le titre du graphique le nombre avec lequel la carte a
été colorée. La concordance et l’amplitude saisonnière n’ont pas de droite à tracer : le graphique n’en montre aucune et rapporte la mesure sous
son titre.

## Calcul de la classification des régions { #how-the-region-classification-is-computed }

Pour classer d’un coup toutes les régions d’un jeu, sous l’une quelconque des quatre mesures, l’application fait la moyenne des mailles dont
le centre se trouve dans chaque région,
pondérée par le cosinus de la latitude. Cette méthode est plus rapide que la moyenne pondérée par recouvrement utilisée pour le graphique d’une
région sélectionnée (voir [Vue Régionale](regional-view.md#which-cells-are-averaged)), et les deux peuvent différer légèrement pour les régions
petites ou étroites. La tendance indiquée dans la légende du graphique, et la mesure sous le titre du graphique, sont calculées à partir de
la série du graphique
lui-même. Une région trop
petite pour contenir le centre d’une maille est classée à partir de la maille située en son centre.
