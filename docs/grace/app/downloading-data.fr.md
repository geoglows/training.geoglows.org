# Téléchargement des Données

## Télécharger un CSV { #downloading-a-csv }

Une fois une région ou une maille sélectionnée, cliquez sur **Download CSV** en haut à droite du panneau du graphique. Le fichier contient les
valeurs mensuelles des cinq couches du jeu de données sélectionné pour cette région ou cette maille, qu’elles soient tracées ou non, ainsi que
les cinq de l’autre jeu de données si la comparaison est cochée. Il est nommé `grace_gwsa_data.csv` pour une région (la partie centrale
correspond à la couche affichée) ou `grace_cell_<lat>_<lon>_data.csv` pour une maille.

| Colonne | Contenu |
|---|---|
| `Date` | Premier jour du mois, `YYYY-MM-DD` |
| `GWSa`, `TWSa`, `SMa`, `SWEa`, `CANa` | Anomalie moyenne pondérée par la surface pour le mois, en cm d’équivalent en eau liquide |
| `GWSa_22`, `TWSa_22`, `SMa_22`, `SWEa_22`, `CANa_22` | Les mêmes cinq, issues de GLDAS 2.2 |
| `<layer>_upper`, `<layer>_lower` | La moyenne plus et moins 1σ ; couches GRACE seulement, puisque GLDAS 2.2 n’a pas d’incertitude |
| `GWSa_filled`, `TWSa_filled` | La même série avec ses lacunes comblées par le modèle saisonnier ; égale à la valeur observée tous les autres mois |
| `GWSa_is_filled`, `TWSa_is_filled` | 1 pour les mois comblés par le modèle saisonnier, 0 sinon |

Seules les couches présentes dans le fichier reçoivent des colonnes : un téléchargement fait avec GLDAS 2.2 sélectionné et la comparaison
désactivée comporte les cinq colonnes `_22` et rien d’autre. Les paires `_filled` et `_is_filled` appartiennent aux deux couches dérivées de
GRACE, les seules à présenter des lacunes.

Par exemple, le début de l’intervalle entre les missions pour le Northern Midwest Aquifer System :

```text
Date,GWSa,GWSa_upper,GWSa_lower,GWSa_filled,GWSa_is_filled,TWSa,...
2017-06-01,14.408,18.786,10.030,14.408,0,14.699,...
2017-07-01,,,,13.941,1,,...
2017-08-01,,,,13.354,1,,...
```

Le fichier comporte une ligne pour chaque mois où l’une de ses colonnes a une valeur : d’avril 2002 pour les couches GRACE, de février 2003 pour
celles de GLDAS 2.2, de sorte qu’un fichier contenant les deux a des cellules `_22` vides dans ses dix premières lignes. Pour les mois sans
données GRACE, les cellules `GWSa` et `TWSa` sont vides, tandis que les couches GLDAS (`SMa`, `SWEa`, `CANa`, et les cinq colonnes `_22`) ont
toujours des valeurs, car les modèles de surface terrestre tournent chaque mois.
Les colonnes `_filled` fournissent une valeur pour ces mois (voir [Lacunes et Comblement des Lacunes](../mission/gap-filling.md)). Elles sont écrites quel que
soit le réglage **Gap filling** : le fichier est donc le même, quelle que soit la façon dont le graphique est tracé.

Excel, Google Sheets, Python et R lisent tous le fichier directement, et les dates ISO ne nécessitent aucune conversion (avec pandas, utilisez
`pd.read_csv(path, parse_dates=["Date"])`). Pour
retrouver l’incertitude σ à partir des bornes, calculez `(upper − lower) / 2`.

## Conversion en volume { #converting-to-volume }

Les anomalies sont des hauteurs d’eau moyennées sur la région. Multipliez-les par la surface de la région pour obtenir un volume :

```text
ΔV (km³) = GWSa (cm) × Area (km²) / 100,000
```

Par exemple, une GWSa de −12 cm sur un aquifère de 400 000 km² correspond à 12 × 400 000 / 100 000 = 48 km³ (48 000 millions de m³) d’eau en
moins que la moyenne 2004–2009. La variation entre deux dates est la différence de leurs anomalies multipliée par la surface, et une tendance en
cm/an multipliée par la surface donne un rythme de perte ou de gain en km³/an.

Utilisez la surface de la région telle que vous l’avez définie. Pour une région importée, un SIG peut indiquer la surface du polygone ;
calculez-la dans une projection équivalente (à conservation des surfaces), et non en degrés.

## Pour aller plus loin { #what-to-do-next }

Le CSV est le point de départ d’analyses en dehors de l’application. Pour estimer la recharge, utilisez l’[analyse de la recharge](../recharge/opening.md)
de l’application, qui applique la méthode de fluctuation de la nappe à la série comblée et propose son propre téléchargement CSV.
[Lacunes et Comblement des Lacunes](../mission/gap-filling.md#filling-the-gaps) décrit comment les colonnes `GWSa_filled` et `TWSa_filled` sont estimées.
