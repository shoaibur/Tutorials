**Linear Regression**
```
```
**Logistic Regression**
* Link function for logistic regression: sigmoid, i.e. y = sigmoid( -(w^Tx + b) ) = 1 / 1 + exp( -(w^Tx +b) )
* Log-odds are linearly related to the predictors, i.e. log(p/(1-p)) = w^T x + b, where p = prob(y=1|X,w)
* Estimate parameters using MLE, or equivalently minimizing the cost: J = y log(p) + (1-y) log(1-p)
* Assumptions: (1) Independent observations, (2) Logodds-predictors linear relationships, (3) No or minimal multicolinearity, (4) Samples represent population.
* Algorithms:
 * initialize W and b
 * Forward propabation
  * Linear transformation, Z = W^T * X + b
  * Activation, A = sigmoid(Z)
 * Compute cost, J = Y log(A) + (1-Y) log(1-P)
 * Backpropagation
  * dZ = A - Y
  * dW = 1/m * np.dot(dZ.T, X)
  * db = 1/m sum( dZ )
 * Update parameters
  * W = W - learning_rate * dW
  * b = b - learning_rate * db
