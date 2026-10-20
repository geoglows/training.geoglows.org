# Lequel utiliser

Aucun des deux jeux de données ne l’emporte partout. [À quoi ressemblent les écarts](examples.md) montre les cas d’où vient ce conseil, et
[Jusqu’où cela est validé](validation.md) dit quel poids il peut porter.

## La réponse courte { #the-short-answer }

| Ce que vous cherchez | Utilisez | Parce que |
|:---|:---|:---|
| Un taux d’épuisement ou de reconstitution, en cm/an ou km³/an | GRACE | 2.2 aplatit les tendances à environ un quart |
| La forme et le calendrier du cycle saisonnier | 2.2 là où l’humidité du sol oscille autant que l’eau totale ; sinon l’un ou l’autre | la soustraction peut inverser le calendrier |
| Une région de quelques cellules | 2.2 | moyenné à 0,25° là où l’autre est à 1° |
| Une série mensuelle sans interruption | 2.2 | le modèle tourne à travers les lacunes de GRACE |
| La recharge par la méthode WTF | GRACE | Barbosa et al. (2025), plus le risque d’une saison inversée |
| Une incertitude par cellule | GRACE | 2.2 n’en publie aucune |
| Quoi que ce soit avant février 2003 | GRACE | l’enregistrement de 2.2 commence là |
| Un résultat destiné à publication | les deux | en disant où ils concordent et où ils divergent |

Deux réponses indépendantes qui concordent sont difficiles à écarter. Là où elles divergent, tracez les composantes : un écart qui réside dans
l’humidité du sol est un autre problème qu’un écart qui réside dans l’eau totale.

## La vérification à faire avant de se fier à un cycle saisonnier { #the-check-to-run-before-trusting-a-seasonal-cycle }

Une seule comparaison indique si le calendrier saisonnier de la voie GRACE est fiable dans votre région, et elle prend une minute dans
l’application.

1. Ouvrez votre région et tracez **SMa** et **TWSa** pour le jeu de données GRACE.
2. Comparez la hauteur de leurs cycles saisonniers, du mois le plus bas au plus haut.
3. Si l’humidité du sol oscille environ moitié moins que l’eau totale ou moins encore, le cycle souterrain GRACE a une forme propre. L’un ou
   l’autre jeu de données convient pour les questions saisonnières.
4. Si l’humidité du sol oscille autant que l’eau totale ou davantage, la soustraction annule l’essentiel du signal. Préférez 2.2 pour la forme et
   le calendrier du cycle, et ne lisez pas le mois du maximum GRACE comme le mois où la nappe est la plus haute.

Sur 299 aquifères, ce rapport prédit la concordance entre les deux cycles saisonniers à une corrélation de −0,75. En dessous de 0,7 la
concordance médiane vaut 0,93 ; au-dessus de 1,0 elle vaut −0,39.

## Avant de traiter un grand écart comme un résultat { #before-treating-a-large-difference-as-a-result }

1. Tracez la neige (**SWEa**). La glace et la neige expliquent la plupart des extrêmes, et un cycle souterrain ayant la forme du cycle de neige
   inversé est le terme de neige.
2. Tracez l’eau totale (**TWSa**) pour les deux jeux de données. Là où les totaux concordent et où seule l’eau souterraine diverge, les deux
   découpent la colonne différemment et la mesure satellitaire elle-même n’est pas en cause.
3. Comparez l’amplitude saisonnière de l’humidité du sol (**SMa**) à celle de l’eau totale, comme ci-dessus.
4. Vérifiez quelle quantité d’eau bouge réellement. En dessous d’environ 5 cm de variation, les deux jeux de données corrèlent à une médiane de
   0,19, et ce nombre ne dit rien sur l’un ni sur l’autre.
5. Demandez-vous si un fleuve, une plaine d’inondation, un lac ou un réservoir pourrait expliquer cette eau.

## À quoi sert la GWSa, dans l’un comme dans l’autre { #what-gwsa-is-good-for-in-either-dataset }

Les deux jeux de données répondent à des questions régionales de direction et de rythme : le stockage de cet aquifère baisse-t-il, à quelle
vitesse, et la baisse a-t-elle ralenti après un changement de politique ou une suite d’années humides ? Aucun ne convient à des décisions à
l’échelle d’un champ de captage ou d’un seul périmètre irrigué, et aucun ne dit quoi que ce soit sur les niveaux ni sur la qualité de l’eau. Tous
deux moyennent la variation de stockage sur une surface bien plus grande qu’un champ de captage, et tous deux versent l’eau de surface dans le
terme souterrain.

Là où des piézomètres existent, comparez la tendance à la variation de stockage estimée à partir des puits. Cette comparaison est la vérification
la plus forte disponible pour l’un comme pour l’autre, et leur accord renforce les deux.

## Références { #references }

- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
