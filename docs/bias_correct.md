### Bias Correction

#### Introduction

Global model predictions often exhibit biases at 
local scales or specific locations, where the 
magnitude of flood events may differ from actual 
flows despite correct timing and general 
parameters. These biases hinder the local utility 
of such models, potentially undermining confidence
in decision-making processes.

To address this issue, a bias correction method, 
inspired by Farmer et al. (2018), has been 
proposed for correcting biases in GEOGLoWS ECMWF
simulated streamflow. This method utilizes flow 
duration curves, which represent the cumulative 
percent of time that a given discharge was exceeded
during a specific period. By comparing simulated 
and observed flow duration curves, the method 
estimates the non-exceedance probability of 
simulated values and identifies corresponding 
observed streamflow values. Subsequently, 
simulated values are adjusted by replacing them 
with equivalent observed streamflow values 
at the same non-exceedance probability. This 
correction process aims to improve the accuracy 
of simulated flood events, enhancing the 
reliability of model predictions for 
decision-makers.

> Here is a [presentation][1] about bias correction.
> #this needs more explanation

>The [Google Colab notebook][2] outlines the steps to
> run the bias correction method in python, using the geoglows package.

[![image(https://training.geoglows.org/en/latest/_images/forecasts.png)]]
> #it would be good to create a link to the Hydroviewer tutorial 
> for uniformity's sake
> 


[1]: https://byu.sharepoint.com/:p:/r/sites/BYUHydroinformaticsLaboratory/Shared%20Documents/geoglows-training/GEOGLOWS%20Master%20Training%20Materials/Retrospective%20Validation/GEOGloWS%20-%20BiasCorrection.pptx?d=w84cc417ccfae43f5bae9222655db3728&csf=1&web=1&e=5PBsfY
[2]: https://colab.research.google.com/drive/15MUTx3lb5P93BLUv8Uehv0gTudc43qkX?usp=sharing