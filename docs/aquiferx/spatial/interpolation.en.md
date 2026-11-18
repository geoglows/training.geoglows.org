# Interpolation Methods

Each map is a grid of cells over the aquifer, and every cell whose center lies inside the outline gets a value interpolated from the
wells' values on the map's date. The grid has the number of columns set by **Resolution**, square cells, and as many rows as the
outline's height takes (see [Running a Spatial Analysis](running.md#spatial)). Spatial Analysis offers two interpolation methods,
ordinary kriging and inverse distance weighting (IDW). Both use every well with a value on the date, and both go through the same
steps before and after.

## The wells on each date

A well is one point on a map, at its location, with its value on the map's date: from its readings by PCHIP or a moving average, held
beyond its record, or from a gap-filling model (see [Running a Spatial Analysis](running.md#temporal)). A well with no value on a date
is left out of that map. Wells at one place were narrowed to one in the wizard (see [Wells at One Place](places.md)); any wells still
closer together than the place distance are averaged into one point, at their mean location with their mean value. A map with one
point is that point's value everywhere, and a date with no points gives no map.

## Kriging

Kriging treats the water table as a surface whose values are more alike the closer together they are, and it weights each well by how
closely its value is expected to agree with the cell's, given the distances between the cell and the wells and among the wells
themselves. The app uses ordinary kriging, which takes the surface's mean as unknown and constant across the aquifer.

### The covariance

How alike two values are at a distance *h* apart is set by the covariance:

$$
C(0) = \sigma^2, \qquad C(h) = (\sigma^2 - c_0)\, \rho(h / a) \quad \text{for } h > 0
$$

with *σ*² the sill, *c*<sub>0</sub> the nugget, *a* the range, and *ρ* the correlation chosen by **Variogram Model**:

| Model | *ρ*(*q*), *q* = *h* / *a* |
|---|---|
| Exponential | e<sup>−*q*</sup> |
| Spherical | 1 − 1.5 *q* + 0.5 *q*<sup>3</sup> for *q* < 1, and 0 beyond the range |
| Gaussian | e<sup>−*q*²</sup> |

At the range, the exponential and Gaussian correlations have fallen to 0.37, and the spherical one to zero, so wells farther apart
than the range are unrelated under the spherical model. Near zero distance the exponential correlation falls steeply and the Gaussian
one barely falls at all, which makes Gaussian maps smooth and sensitive to wells close together. A variogram, the half mean square
difference between values *h* apart, is the same model written the other way: *γ*(*h*) = *σ*² − *C*(*h*).

The app sets the three parameters from the wells, without fitting them to the data:

- **Sill**: the variance of the wells' mean values, each well's mean taken over the map dates on which it has a value.
- **Range**: with **Auto (1/3 diagonal)**, a third of the diagonal of the rectangle around the wells; with **Custom (meters)**, the
  distance you give; with **Percentage**, that share of the diagonal. Escalante Valley-Beryl-Enterprise's 209 mapped wells span a
  rectangle 58 km across its diagonal, so the range is 19 km. Wells there stand a median 0.8 km from their nearest neighbor.
- **Nugget**: with **Enable nugget**, 5% of the sill; without it, 0.01% of the sill (at least 0.001), a trace that keeps the
  equations solvable.

Distances are measured along the earth's surface, in meters. One covariance serves every map of the run. Because the nugget is a
fixed share of the sill, the sill drops out of the weights below, and the maps depend on the model, the range and whether the nugget
is on.

### The weights

At each cell *x*<sub>0</sub> the weights *λ*<sub>i</sub> of the *n* wells solve

$$
\sum_{j=1}^{n} \lambda_j\, C(x_i - x_j) + \mu = C(x_i - x_0), \quad i = 1, \dots, n, \qquad \sum_{j=1}^{n} \lambda_j = 1
$$

with *μ* a Lagrange multiplier that holds the weights to a sum of one, and the cell's value is

$$
\hat z(x_0) = \sum_{i=1}^{n} \lambda_i z_i
$$

The matrix on the left depends only on the wells, so it is factored once per map and each cell costs one back-substitution. Every
well takes part at every cell.

Wells that agree with each other share their weight, so a cluster of wells counts for less than the same number spread out, and wells
behind a nearer one get little weight or a small negative one. Negative weights let the map rise a little above the highest well or
fall below the lowest. Away from the wells the map flattens toward a weighted mean of all of them.

### The nugget

The nugget is the gap between *C*(0) and the covariance just beyond zero distance: it says how much two readings at almost the same
place can differ, from measuring error or from conditions too local to map. Without it, the map passes through the wells: the value
at a well's location is the well's value. With it, the map smooths across the wells and can miss each one by several feet.

### Why exponential without a nugget

The default comes from a leave-one-out test of the six combinations of model and nugget, with the range on Auto, in 45 aquifers of
seven regions: the three Sample Data regions and four others in the Caribbean, the Middle East and West Africa. For each aquifer the
test made maps from the measurements on January 1 of each year, with the wells of at least 5 readings over at least 5 years, 2,201
maps in all. On each map with at least 10 wells it left out each well in turn, made the map from the rest and read it at the missing
well (Dubrule, 1983). The RMSE over all the wells left out, as a share of that of the Gaussian model with a nugget, which was the app's
default before, came out:

| Setting | RMSE against Gaussian with nugget, median over the aquifers |
|---|--:|
| Exponential with nugget | 0.93 |
| Exponential without nugget | 0.95 |
| Spherical without nugget | 1.00 |
| Spherical with nugget | 1.01 |
| Gaussian without nugget | 1.42 |

Exponential, with or without the nugget, came closer to the wells left out than the old default in 60 to 62% of the aquifers, and
the old default came out best in 16 of the 45. At the wells themselves, in the aquifers measured in feet, the maps missed by a median
0.01 ft without the nugget, 3.5 ft with it, and 11.9 ft for Gaussian with the nugget. Exponential without the nugget comes about as close to the wells left out as with
it, and it keeps each map true to the readings, so it is the default. Turn the nugget on where the readings at nearby wells disagree
by more than the map should show, for example where wells of slightly different depths stand side by side.

## Inverse distance weighting

IDW takes each cell's value as a weighted average over the wells, the nearer ones weighted more. The app uses Shepard's method with
the weights of Franke and Nielson (1980):

$$
\hat z(x) = \frac{\sum_i w_i\, Q_i(x)}{\sum_i w_i}, \qquad w_i = \left( \frac{R - h_i}{R\, h_i} \right)^{p}
$$

with *h*<sub>i</sub> the distance from the cell to well *i*, *p* the **Exponent** (2 to start with), and *R* the distance to the
farthest well used for that cell. That well, at *h* = *R*, gets no weight. **Neighbors** sets the wells used: **All Wells**, or
**Nearest N**, the N nearest to each cell (12 to start with). Distances are in meters, from coordinates projected about the wells'
center. A larger exponent gives the nearest wells more of the weight and the map flat patches around them; a smaller one blends the
wells more evenly.

*Q*<sub>i</sub>, the nodal function, is what well *i* says the value is at the cell:

- **Classic**: the well's value, *Q*<sub>i</sub> = *z*<sub>i</sub>. The map is then an average of the wells' values, so it stays
  between the lowest and highest well, and with an exponent above 1 it levels off at each well.
- **Gradient Plane**: a plane through the well, *Q*<sub>i</sub>(*x*, *y*) = *z*<sub>i</sub> + *a*<sub>i</sub>(*x* − *x*<sub>i</sub>) +
  *b*<sub>i</sub>(*y* − *y*<sub>i</sub>), so each well carries the slope of the water table around it.
- **Quadratic**: a quadratic surface through the well, adding (*x* − *x*<sub>i</sub>)², (*x* − *x*<sub>i</sub>)(*y* − *y*<sub>i</sub>)
  and (*y* − *y*<sub>i</sub>)² terms, so it carries the bending as well. Where its fit fails, the well falls back to a plane.

The coefficients of each well's plane or quadratic are fitted by weighted least squares to the values of its nearest wells: the number in
**Nearest N**, 12 to start with, whichever Neighbors is chosen, but at least 5 for a plane and 8 for a quadratic, weighted by the same formula with *R* the distance to the
farthest of them. With Nearest N, a quadratic needs at least 6 neighbors. The planes and quadratics let the map continue a slope past
the outermost wells and rise above the highest well or fall below the lowest, which suits a water table sloping steadily across an
aquifer and can mislead near the edge.

The tests above did not cover IDW.

## After either method

- With **Log Interpolation**, the wells' values are replaced by their natural logarithms before interpolating, and each cell's result
  is turned back with the exponential. A well with a value of zero or less is left out of that date.
- **Truncate Low** and **Truncate High** then clip each cell to the values given.
- Each value is rounded to three decimals and saved.

The maps' statistics (see [Viewing the Maps](maps.md#raster-statistics)) come from the wells' values in the data's own units, with or
without the logarithm.

## References

Dubrule, O. (1983). Cross validation of kriging in a unique neighborhood. *Journal of the International Association for Mathematical
Geology*, 15(6), 687–699.

Franke, R., and Nielson, G. (1980). Smooth interpolation of large sets of scattered data. *International Journal for Numerical
Methods in Engineering*, 15(11), 1691–1704.

Isaaks, E. H., and Srivastava, R. M. (1989). *An Introduction to Applied Geostatistics*. Oxford University Press.

Shepard, D. (1968). A two-dimensional interpolation function for irregularly-spaced data. *Proceedings of the 1968 23rd ACM National
Conference*, 517–524.
