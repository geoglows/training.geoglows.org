# Analyse des Tendances

## Classification des tendances { #trend-classification }

**Analyze trends** colore chaque contour de région (dans la vue régionale) ou chaque maille (dans la vue globale) selon le rythme auquel la
couche affichée augmente ou diminue. Les tendances sont activées à l’ouverture de l’application ; cliquez sur **Hide trends** pour les
désactiver.

![Aquifères du jeu Global Aquifers classés selon la tendance du stockage des eaux souterraines sur les cinq dernières années](../../static/images/grace/app-home.webp)

Dans la vue régionale, ci-dessus, chaque aquifère ou bassin reçoit une tendance unique calculée à partir de la moyenne de ses mailles (voir
[Vue Régionale](regional-view.md#the-landing-page)). C’est le meilleur indicateur pour un aquifère donné.

![Tendance du stockage des eaux souterraines sur les cinq dernières années pour chaque maille de 1°, dans la vue globale](../../static/images/grace/app-global-trends.webp)

La vue globale, ci-dessus, classe les 15 159 mailles continentales : elle montre donc où le stockage évolue, indépendamment des limites des
aquifères. Il augmente dans le Sahel et en Afrique de l’Est, et diminue dans une grande partie du Moyen-Orient, le nord de l’Inde et le Brésil.

La tendance est la pente d’une droite ajustée par moindres carrés sur les valeurs mensuelles de la fenêtre de tendance, en cm par an. Les mois
sans données GRACE sont ignorés, et non comblés. Une région ou une maille doit disposer d’au moins 24 mois de données dans la fenêtre pour être
classée ; sinon, elle apparaît comme **Insufficient data**.

| Classe | Tendance (cm/an) |
|---|---|
| Extreme decline (baisse extrême) | inférieure à −2 |
| Decline (baisse) | −2 à −0.5 |
| Static (stable) | −0.5 à +0.5 |
| Increase (hausse) | +0.5 à +2 |
| Extreme increase (hausse extrême) | supérieure à +2 |

La légende compte les régions ou les mailles de chaque classe. À titre de repère, une tendance de −2 cm/an maintenue sur 100 000 km² correspond
à une perte de 2 km³ d’eau par an.

## La fenêtre de tendance { #the-trend-window }

Le sélecteur **Window** de l’en-tête fixe la période couverte par l’ajustement, en remontant depuis le mois le plus récent : 5, 10, 15 ou 20 ans,
ou **All** pour l’ensemble de la série depuis 2002. La classification et la légende se mettent à jour lorsque vous la modifiez.

Dans la plupart des régions, le stockage oscille entre années humides et années sèches ; une fenêtre courte peut donc ne saisir qu’une
oscillation au lieu de l’évolution de long terme. Dans la Vallée Centrale de Californie, le stockage des eaux souterraines a diminué de 2002
jusqu’à la sécheresse de 2021–2022, puis s’est partiellement rétabli après l’hiver très humide de 2022–2023. La tendance sur 5 ans est une hausse ;
la tendance sur 20 ans est une baisse. Les deux sont exactes pour leur fenêtre. Examinez la série temporelle avant de tirer des conclusions d’une
classe de tendance, et comparez plusieurs fenêtres.

## Droite de tendance sur le graphique { #trend-line-on-the-chart }

Lorsqu’une région ou une maille est sélectionnée et que les tendances sont activées, le graphique ajoute la droite ajustée en tirets sur la
fenêtre de tendance, et la légende indique la pente, par exemple « GWSa trend +2.25 cm/yr (last 5 yr) ». Chaque composante tracée reçoit sa
propre droite de tendance.

## Calcul de la classification des régions { #how-the-region-classification-is-computed }

Pour classer d’un coup toutes les régions d’un jeu, l’application fait la moyenne des mailles dont le centre se trouve dans chaque région,
pondérée par le cosinus de la latitude. Cette méthode est plus rapide que la moyenne pondérée par recouvrement utilisée pour le graphique d’une
région sélectionnée (voir [Vue Régionale](regional-view.md#which-cells-are-averaged)), et les deux peuvent différer légèrement pour les régions
petites ou étroites. La tendance indiquée dans la légende du graphique est celle calculée à partir de la série du graphique. Une région trop
petite pour contenir le centre d’une maille est classée à partir de la maille située en son centre.
