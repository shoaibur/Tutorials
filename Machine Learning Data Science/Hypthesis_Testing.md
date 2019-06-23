**T-tests**
* In Python: from scipy import stats
  * 1-sample t-test
    * Parametric: ```stats.ttest_1samp(a=data)```
    * Nonparametric: ```stats.wilcoxon(x=data, y=None)```
  * 2-sample paired t-test
    * Parametric: ```stats.ttest_rel(a=data1, b=data2)```
    * Nonparametric: ```stats.wilcoxon(x=data1, y=data2)```
  * 2-sample independent t-test
    * Parametric: ```stats.ttest_ind(a=data1, b=data2, equal_var=True)```
    * Nonparametric: ```stats.mannwhitneyu(x=data1, y=data2)```
  
###########################################################################

* In R:
  * 1-sample, 2-sample (independent, paired) t-test
    * Parametric: ```t.test(x, y=NULL, var.equal=T, paired=F)```
    * Nonparametric: ```wilcoxon.test(x, y=NULL, var.equal=T, paired=F)```
  * z-test: library(BSDA)
    * ```z.test(x, y, mu = 0, sigma.x = 1, sigma.y = 1, conf.level = 0.95)```
  * z-test vs. t-test
    * z-test is used for comparing proportions, while t-test is used for comparing means.
    * ```z = (p - p0) / sigma``` where p=sample proportion, p0=assumed proportion at H0, sigma = sqrt((1-p0)/p0)
    * ```t = (mu-mu0) / sigma``` where mu=sample mean, mu0=assumed mean at H0, sigma = sigma_sample/sqrt(n)

  * Chi-squre test (for goodness-of-fit and independence)
    * ```chisq.test(x, y)```
  
  * ANOVA
    * One-way: ```fit = aov(y ~ A, df)```, or non-parametric: ```kruskal.test(y ~ A, df)```
    * Two-way
      * Randomized block design: ```fit = aov(y ~ A + B, df)```, or non-parametric: ```friedman.test(y ~ A + B, df)```
      * Factorial design: ```fit = aov(y ~ A + B + A:B, df)```
      * Repeated measures: ```fit = aov(y ~ A * B + Error(subj/(A*B)), df)```
       
  * ANCOVA: ```fit = aov(y ~ A + B + x1 + x2, df)```, A,B: Categorical and x1,x2: Continuous
  
  * Linear model: ```fit = lm(y ~ x1 + x2, df)```
  * Liner mixed-effect model: library(lme4)
    * ```fit = lmer(y ~ x1 + x2 + (1|g1), df)``` where x1 and x2 are fixed, g1 is random

###########################################################################

**Power analysis:**
```power.t.test(n, delta, sd, power, sig.level, alternative)```

###########################################################################

**Confidence interval**
```95% CI: With repeated samples, the method/experiment will produce intervals that capture/overlap the population parameter (e.g. mean) in 95% of the samples.```

**p-value**
```Probability of getting data as extreme or more extreme than the calculated statistic given the null the hypothesis.```
```Probability of getting extreme data by chance given the null hypothesis.```
###########################################################################

**A/B testing**
* Step 1. Form hypotheses
  * H0: mu = 20 min before the change
  * H1 > 20 min after the change
* Step 2. Pick a significant level
  * alpha = 0.05
* Step 3. Calculate sample statistic
  * Take samples (after change), n = 100
  * Estimate mean (x_bar = 25 min), sd (s = 3 min), etc.
* Step 4. Compute p-value: 
  * P(x_bar >= 25 | H0 true)
* Step 5. Compare p-value with significance level
  * If p < alpha --> Reject H0 in favour of H1
  * If p >= alpha --> Do not reject H0

**Statistical Power:** ```Ability to correctly reject the null hypothesis, measured as power = 1 - beta```

**Tests of assumptions of normal distribution and equal variance:**
* Noramality tests
  * ```stats.shapiro(x)```
  * ```stats.kstest(x, 'norm')```
  * ```stats.normalitytest(x)```  
* Equal variance tests
  * ```stats.levene(x, y)```
  * ```stats.bartlett(x, 'norm')```
  * ```stats.flinger(x) -- non-parametric```

**Parametric vs. non-parametric tests**
* No assumption of distribution of data is required for non-parametric tests.
* Non-parametric tests have less statistical power, i.e. are high succeptible to give type-II error.
* Less statistical power specifically when the sample size is small, because non-parametric tests look for ranks, e.g.
```
With actual values:                |         With ranks:
Control-----------Treatment        |         Control-----------Treatment
  1.4               100.1          |           2                 4
  1.5               107.5          |           3                 6
  1.1               103.4          |           1                 5
```
