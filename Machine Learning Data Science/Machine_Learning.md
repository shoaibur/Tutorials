**Linear Regression**
```
```
**Logistic Regression**
* Link function for logistic regression: sigmoid, i.e. y = sigmoid( -(w^Tx + b) ) = 1 / 1 + exp( -(w^Tx +b) )
* Log-odds are linearly related to the predictors, i.e. log(p/(1-p)) = w^T x + b, where p = prob(y=1|X,w)
* Estimate parameters using MLE, or equivalently minimizing the cost: J = p log(y) + (1-p) log(1-y)
* Assumptions: (1) Independent observations, (2) Logodds-predictors linear relationships, (3) No or minimal multicolinearity, (4) Samples represent population.
