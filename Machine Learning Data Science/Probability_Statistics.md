# Probability distributions

**Bernoulli**
```
   Parameters: p
   Bernoulli(p) = p^x (1-p)^(1-x)
   Mean = p and variance = p(1-p)
```    

**Binomial**
```
   Parameters: p, n
   Binomial(p, n) = nCx p^x (1-p)^(n-x)
   Mean = np and variance = np(1-p)
```

**Geometric**
```
   Parameters: p
   Geometric(p) = p (1-p)^(x-1)
   Mean = 1/p and variance = (1-p) / p^2
```

**Negative Binomial**
```
   Parameters: k, p
   NegBinomial(k, p) = (x-1)C(k-1) p^k (1-p)^(x-k)
   Mean = k / p and variance = k(1-p) / p^2
```

**Poisson**
```
   Parameters: lam
   Poisson(lam) = e^(-lam) lam^k / k!
   Mean = lam and variance = lam
```

**Exponential**
```
   Parameters: lam
   Exponential(lam) = lam * e^(-lam*x)
   Mean = 1/lam and variance = 1/lam^2
```

**Uniform**
```
   Parameters: a, b
   Uniform(a,b) = 1 / (b - a)
   Mean = (a+b)/2 and variance = (b-a)^2 / 12
```

**Normal**
```
   Parameters: mu, sigma
   Normal(mu, sigma) = 1/sqrt(2*pi*sigma^2) * e^(-(x-mu)^2 / (2*sigma^2))
   Mean = mu and variance = sigma^2
```
