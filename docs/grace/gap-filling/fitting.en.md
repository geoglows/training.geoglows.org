# Fitting the Model

## Least squares for fixed breakpoints

For a given set of breakpoints, the slopes *β* and *γ*<sub>j</sub> and the twelve levels *α*<sub>m</sub> are found by ordinary least squares
over the observed months only. Missing months take no part in the fit. Each calendar month must be observed at least twice, or its level
can't be estimated reliably and the app leaves the series unfilled.

After the fit, the levels are shifted so that the seasonal cycle averages zero over the year, and the trend is shifted up by the same amount:

$$
S(m) = \alpha_m - \bar{\alpha}, \qquad T(t) = \beta \, t + \sum_{j} \gamma_j \max(t - b_j,\, 0) + \bar{\alpha}, \qquad
\bar{\alpha} = \frac{1}{12} \sum_{m} \alpha_m
$$

The sum *T* + *S* is unchanged. With the shift, *T* gives the long-term level and *S* gives each month's departure from it.

## Placing the breakpoints

For a given number of breakpoints *k*, the app chooses their positions to minimize the residual sum of squares (RSS) of the fit. Breakpoints
are limited to keep each part of the trend meaningful:

- at least 48 months (four years) from either end of the record, so an end segment is not fitted to a few months
- at least 36 months (three years) apart, so every segment between two breakpoints spans several seasonal cycles

The search runs in two steps. First, candidate breakpoints are placed every three months, and every valid combination of *k* candidates is
fitted. The combination with the lowest RSS is kept. Then each breakpoint in turn is moved one month earlier or later, and the move is kept
if it lowers the RSS. This repeats until no one-month move improves the fit, so each breakpoint ends up at the best month near the best
three-month candidate.

## Choosing the number of breakpoints

More breakpoints always fit the observed months at least as well, so the number is chosen with the Bayesian information criterion (BIC),
which adds a penalty for each parameter:

$$
\text{BIC} = n \ln\!\left(\frac{\text{RSS}}{n}\right) + p \ln n, \qquad p = 1 + 2k + 12
$$

where *n* is the number of observed months and *p* counts the parameters: the first slope, a slope change and a position for each breakpoint,
and the twelve monthly levels.

The app fits the best model with 0, 1, 2 and 3 breakpoints. Starting from the straight trend, it moves to a model with more breakpoints only if
that model's BIC is at least 10 lower than the BIC of the model chosen so far. A drop of 10 is strong evidence that the extra bend is real
rather than a fit to noise, so the trend bends only where the record clearly changes direction.
