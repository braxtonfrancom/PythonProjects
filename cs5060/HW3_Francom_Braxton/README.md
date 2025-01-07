----------------------------------------------------Part 1----------------------------------------------------
<br/>
I created a simulation that runs 5000 monte-carlo simulations around the described asset and returns the effective price. See below image:
<br/><br/>
![](Figure_1.png)
<br/><br/>
Based on this data, I found the price of the vanilla European Option to be $117.46. 
<br/>
<br/>
<br/>

----------------------------------------------------Part 2----------------------------------------------------

Below is the distribution for `stock1.csv`:
<br/>
![](distribution1.png)
<br/><br/>

Below is the distribution for `stock2.csv`:
<br/>
![](distribution2.png)
<br/><br/>


I then wanted to see what distribution and parameters gave the best fit for each stock. Below is the analysis for `stock1.csv`:
<br/><br/>
![](distributionAnalysis1.png)
<br/><br/>
The error values for each distribution for `stock1.csv` are as follows:
<br/><br/>
Fitted norm distribution with error=0.012594)<br/>
Fitted beta distribution with error=0.012476)<br/>
Fitted gamma distribution with error=0.012642)<br/>
Fitted lognorm distribution with error=0.012645)<br/>
Fitted burr distribution with error=0.016706)<br/>
<br/>
My findings showed that the distribution that best fit `stock1.csv` was the following:
<br/><br/>
{'beta': {'a': 8.79869504543807, 'b': 11.641039934834343, 'loc': -28.55044529458781, 'scale': 66.35206384896327}}

<br/><br/><br/>

Below is the analysis for `stock2-1.csv`:
<br/><br/>
![](distributionAnalysis2.png)
<br/><br/>
The error values for each distribution for `stock2-1.csv` are as follows:
<br/><br/>
Fitted norm distribution with error=0.010265)<br/>
Fitted gamma distribution with error=0.010431)<br/>
Fitted beta distribution with error=0.010425)<br/>
Fitted lognorm distribution with error=0.010433)<br/>
Fitted burr distribution with error=0.226903)<br/>
<br/>
My findings showed that the distribution that best fit `stock2-1.csv` was the following:
<br/><br/>
{'norm': {'loc': 0.05098900140562429, 'scale': 8.269809581146056}}

<br/><br/><br/>
Based on the analysis conducted on the stock price data from `stock1.csv` and `stock2-1.csv`, I employed the `Fitter` module from the `fitter` library to fit various probability distributions to the observed changes in stock prices. For each dataset, I initially computed the changes in stock prices from one day to the next and then used histograms to visualize the distributions of these changes.
<br/><br/>
I used the `Fitter` module to fit several probability distributions (including gamma, lognormal, beta, Burr, and normal distributions) to the observed data. To determine the goodness of fit, I utilized the sum of squared errors (sumsquare_error) metric.
<br/><br/>
For `stock1.csv`, the best-fitting distribution was identified as the beta distribution, with the following parameters:
- Shape parameter (a): 8.7987
- Shape parameter (b): 11.6410
- Location parameter (loc): -28.5504
- Scale parameter (scale): 66.3521
<br/><br/>
For `stock2-1.csv`, the best-fitting distribution was identified as the normal distribution, with the parameters inferred from the fitted distribution.
<br/><br/>
These distributions and parameters were determined based on the analysis of the observed data and the goodness of fit metrics provided by the `Fitter` module.
<br/><br/><br/>


<br/>
Assuming the same 1-year window of expiry, the cost of option for the average value of the two options is $118.78(using on a beta distribution).
<br/>

![](avg.png)

<br/>
With a normal distribution, the cost of option is $5.14.(See below)
<br/>

![](avg2.png)

<br/><br/><br/>

Assuming the same 1-year window of expiry, the cost of option for the max value of the two options is $120.82(using on a beta distribution).
<br/>

![](max.png)

<br/>
With a normal distribution, the cost of option is $6.11.(See below)
<br/>

![](max2.png)