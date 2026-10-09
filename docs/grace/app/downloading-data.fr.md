# Téléchargement des Données

## Télécharger un CSV { #downloading-a-csv }

Une fois une région ou une maille sélectionnée, cliquez sur **Download CSV** en haut à droite du panneau du graphique. Le fichier contient les
valeurs mensuelles des cinq couches pour cette région ou cette maille, quelles que soient les couches tracées. Il est nommé
`grace_gwsa_data.csv` pour une région (la partie centrale correspond à la couche affichée) ou `grace_cell_<lat>_<lon>_data.csv` pour une maille.

| Colonne | Contenu |
|---|---|
| `Date` | Premier jour du mois, `YYYY-MM-DD` |
| `GWSa`, `TWSa`, `SMa`, `SWEa`, `CANa` | Anomalie moyenne pondérée par la surface pour le mois, en cm d’équivalent en eau liquide |
| `<layer>_upper`, `<layer>_lower` | La moyenne plus et moins 1σ |
| `GWSa_filled`, `TWSa_filled` | La même série avec ses lacunes comblées par le modèle saisonnier ; égale à la valeur observée tous les autres mois |
| `GWSa_is_filled`, `TWSa_is_filled` | 1 pour les mois comblés par le modèle saisonnier, 0 sinon |

Par exemple, le début de l’intervalle entre les missions pour le Northern Midwest Aquifer System :

```text
Date,GWSa,GWSa_upper,GWSa_lower,GWSa_filled,GWSa_is_filled,TWSa,...
2017-06-01,9.529,14.913,4.146,9.529,0,12.536,...
2017-07-01,,,,11.146,1,,...
2017-08-01,,,,12.694,1,,...
```

Le fichier comporte une ligne par mois, d’avril 2002 à la dernière publication. Pour les mois sans données GRACE, les cellules `GWSa` et `TWSa` sont
vides, tandis que les couches GLDAS (`SMa`, `SWEa`, `CANa`) ont toujours des valeurs, car les modèles de surface terrestre tournent chaque mois.
Les colonnes `_filled` fournissent une valeur pour ces mois (voir [Lacunes dans les Données](../gap-filling/gaps.md)). Elles sont écrites quel que
soit le réglage **Gap filling** : le fichier est donc le même, quelle que soit la façon dont le graphique est tracé.

Excel, Google Sheets, Python et R lisent tous le fichier directement, et les dates ISO ne nécessitent aucune conversion (avec pandas, utilisez
`pd.read_csv(path, parse_dates=["Date"])`). Pour
retrouver l’incertitude σ à partir des bornes, calculez `(upper − lower) / 2`.

## Conversion en volume { #converting-to-volume }

Les anomalies sont des hauteurs d’eau moyennées sur la région. Multipliez-les par la surface de la région pour obtenir un volume :

```text
ΔV (km³) = GWSa (cm) × Area (km²) / 100,000
```

Par exemple, une GWSa de −12 cm sur un aquifère de 400 000 km² correspond à 12 × 400 000 / 100 000 = 4.8 km³ (4 800 millions de m³) d’eau en
moins que la moyenne 2004–2009. La variation entre deux dates est la différence de leurs anomalies multipliée par la surface, et une tendance en
cm/an multipliée par la surface donne un rythme de perte ou de gain en km³/an.

Utilisez la surface de la région telle que vous l’avez définie. Pour une région importée, un SIG peut indiquer la surface du polygone ;
calculez-la dans une projection équivalente (à conservation des surfaces), et non en degrés.

## Pour aller plus loin { #what-to-do-next }

Le CSV est le point de départ d’analyses en dehors de l’application. Pour estimer la recharge, utilisez l’[analyse de la recharge](../recharge/opening.md)
de l’application, qui applique la méthode de fluctuation de la nappe à la série comblée et propose son propre téléchargement CSV.
[Le Modèle Saisonnier](../gap-filling/seasonal-model.md#filling-the-gaps) décrit comment les colonnes `GWSa_filled` et `TWSa_filled` sont estimées.
