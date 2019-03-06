**T-tests**
* In Python: from scipy import stats
  * 1-sample t-test
    * Parametric: stats.ttest_1samp(a=data)
    * Nonparametric: stats.wilcoxon(x=data, y=None)
  * 2-sample independent t-test
    * Parametric: stats.ttest_ind(a=data1, b=data2, equal_var=True)
    * Nonparametric: stats.mannwhitneyu(x=data2, y=data2)
  * 2-sample paired t-test
    * Parametric: stats.ttest_rel(a=data1, b=data2)
    * Nonparametric: stats.wilcoxon(x=data, y=data2)


* In R:
 * 1-sample t-test

