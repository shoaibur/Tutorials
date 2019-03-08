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


* In R:
  * 1-sample, 2-sample (independent, paired) t-test
    * Parametric: t.test(x, y=NULL, var.equal=T, paired=F)
    * Nonparametric: wilcoxon.test(x, y=NULL, var.equal=T, paired=F)
  * z-test: library(BSDA)
    * z.test(x, y, mu = 0, sigma.x = 1, sigma.y = 1, conf.level = 0.95)
  * z-test vs. t-test
    * z-test is used for comparing proportions, while t-test is used for comparing means.
    * z = (p - p0) / sigma, where p=sample proportion, p0=assumed proportion at H0, sigma = sqrt((1-p0)/p0)
    * t = (mu-mu0) / sigma, where mu=sample mean, mu0=assumed mean at H0, sigma = sigma_sample/sqrt(n)

