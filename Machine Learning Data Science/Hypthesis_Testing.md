**T-tests**
* In Python: from scipy import stats
  * 1-sample t-test
    * Parametric: ```stats.ttest_1samp(a=data)```
    * Nonparametric: ```stats.wilcoxon(x=data, y=None)```
  * 2-sample independent t-test
    * Parametric: ```stats.ttest_ind(a=data1, b=data2, equal_var=True)```
    * Nonparametric: ```stats.mannwhitneyu(x=data2, y=data2)```
  * 2-sample paired t-test
    * Parametric: ```stats.ttest_rel(a=data1, b=data2)```
    * Nonparametric: ```stats.wilcoxon(x=data, y=data2)```

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
  * ANOVA
    * One-way: ```fit = aov(y ~ A, df)```, or non-parametric: ```kruskal.test(y ~ A, df)```
    * Two-way
      * Randomized block design: ```fit = aov(y ~ A + B, df)```, or non-parametric: ```friedman.test(y ~ A + B, df)```
      * Factorial design: ```fit = aov(y ~ A + B + A:B, df)```
      * Repeated measured: ```fit = aov(y ~ A + Error(subj/A), df)```
  * ANCOVA: ```fit = aov(y ~ A + B + x1 + x2, df)```, A,B: Categorical and x1,x2: Continuous

###########################################################################

**Power analysis:**
```power.t.test(n, delta, sd, power, sig.level, alternative)```

###########################################################################

**Confidence interval**
```95% CI: With repeated samples, the method/experiment will produce intervals that capture/overlap the population parameter (e.g. mean) in 95% of the samples.```

###########################################################################

**A/B testing and p-value**
* Step 1. Hypothesis
  * H0: mu = 20 min after the change
  * H1 > 20 min after the change
* Step 2. Significant level
  * alpha = 0.05
* Step 3. Calculate sample statistic
  * Take samples (after change), n = 100
  * Estimate mean (x_bar = 25 min), sd (s = 3 min), etc.
* Step 4. p-value: 
  * P(x_bar >= 25 | H0 true)
  * Probability of getting data as extreme or more extreme than the calculated statistic given the null the hypothesis.
* Step 5. Compare p-value with significance level
  * If p < alpha --> Reject H0 in favour of H1
  * If p >= alpha --> Do not reject H0
