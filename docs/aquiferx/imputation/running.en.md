# Running an Imputation

**Impute Gaps** is at the top right once an aquifer is open and water table elevation is the data type. It fills the wells of that
one aquifer and saves the result in it, so the region has to be in My Data. On a Sample Data region the button explains that Sample
Data is read-only and offers **Copy to My Data**, which copies the region and opens the copy (see
[Sample Data and My Data](../start/my-data.md#copying-a-sample-region)); open the aquifer in the copy and click **Impute Gaps** again.

The wizard, **Impute WTE Gaps**, has two steps, **Wells & Options** and **Title & Run**. Everything runs in the browser, so it needs
no internet connection.

![The first step of the Impute Gaps wizard on Escalante Valley-Beryl-Enterprise](../../static/images/aquiferx/impute-wizard.webp)

## Wells and options

At the top of the first step, **Water levels** draws the PCHIP curve of every well with two or more readings on one set of axes, the
wells that will be filled in color and the rest in gray, and its title counts both. **Wells read in each half-year** under it counts
the wells with at least one reading in each half year: orange for wells that will be filled, gray for the others. On Escalante
Valley-Beryl-Enterprise the first chart reads 213 wells to fill of 364 with 2 or more readings, and from about 1980 nearly all the wells
were read once a year, in March: the bars stand in the first half of each year, with a few wells in the second.

### The options

- **Min Observations / Well** and **Min Time Span / Well (years)**, 5 and 5 to start with, choose the wells to fill: those with at
  least that many readings, spread over at least that many years. They are the same two settings Spatial Analysis uses to choose the
  wells for its maps (Part 5). The line under them counts the wells that will be filled and those left out; on Escalante, 213 and
  500.
- **Fill beyond each record for up to (years)**, 10 to start with, is how far each well is filled before its first reading and after
  its last, whether by MC+LNN or by holding the reading. Past it the well has no value. Set it to 0 to fill only inside each record.
- **Check: hide 5 years of each well and fill them again**, ticked to start with, adds the hidden-readings check to the run (see
  [How MC+LNN Works](method.md#the-hidden-readings-check)). It about doubles the time a run takes.

The note at the bottom gives the months the model covers, from the aquifer's first reading to its last (January 1940 to October 2026
on Escalante), and how each gap is filled: PCHIP across gaps under 6 months; MC+LNN across longer gaps and before and after each
record; PCHIP and held readings for a well with fewer than 12 months of readings or no neighbors that track it.

### Choosing the options

The two well settings decide which wells get a series, and so which wells a map made from the model can use. MC+LNN takes its
neighbors from every well of the aquifer with readings in at least 10 months, whether or not that well is filled, so raising the
settings leaves out wells from the result without taking them away as neighbors. A well with five readings spread over five years
gets a series, but with fewer than 12 months of readings it is filled with PCHIP and held readings only.

A longer limit beyond each record keeps more wells on the maps in the years before they were first read and after they were last
read. The tests in [Gaps in Well Records](gaps.md#how-close-the-filled-values-come) covered up to 10 years past the record, and the
values further out rest on the neighbors alone, or on a reading held for decades.

## Title and run

The second step asks for a **Title**: letters, numbers, spaces, hyphens and underscores. It starts as `mc_lnn`, or `mc_lnn_2` and so on
when the aquifer already has a model by that name. Under it is the file the model will be saved in, such as
`escalante_valley_beryl_enterprise/model_wte_mc_lnn.json`, with *Name already exists* if the title is taken. **Options Summary**
repeats the settings: the months, the wells, PCHIP for gaps under 6 months, MC+LNN for longer gaps, the limit beyond each record and
the check.

**Run Imputation** starts the run, and a progress bar and a log follow it. The log opens with the months and the number of wells to
fill and to use as neighbors, then gives a line for each well: how it was filled, with its number of neighbors, R² and RMSE (see
[How MC+LNN Works](method.md#the-fit-statistics)), how many of its months came from PCHIP, MC+LNN and held readings, and the result
of its check. The fills run in the background, several at once on a computer with several cores, so the page stays responsive;
Escalante's 213 wells, with the check, took about a minute on a laptop. **Cancel** stops the run and goes back to the first step
without saving anything.

When the run ends, the wizard reports how many wells were filled and how many of them by MC+LNN, the hidden-readings check for the
aquifer, the months and the aquifer, with the log under **Processing Log**. For Escalante it reads 213 wells filled, 155 by MC+LNN
and 58 by PCHIP and held readings only, and *MC+LNN was closer than PCHIP at 87 of 109 wells (median RMSE 1.47 vs 2.39)*.
**View Results** opens the model on the chart (see [Reading the Results](results.md)).
