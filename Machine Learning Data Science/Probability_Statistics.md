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



**Exercise Problems**

* Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 o spring, respectively. Each of Bobo’s descendants also has the same probabilities. What is the probability that Bobo’s lineage dies out?

* In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the probability that you see at least one shooting star in the period of an hour?

* How can you generate a random number between 1 and 7 with only a die?

* How can you get a fair coin toss if someone hands you a coin that is weighted to come up heads more often than tails?

* You have an 50-50 mixture of two normal distributions with the same standard deviation. How far apart do the means need to be in order for this distribution to be bimodal?

* Given draws from a normal distribution with known parameters, how can you simulate draws from a uniform distribution?

* A certain couple tells you that they have two children, at least one of which is a girl. What is the probability that they have two girls?

* You have a group of couples that decide to have children until they have their first girl, after which they stop having children. What is the expected gender ratio of the children that are born? What is the expected number of children each couple will have?

* How many ways can you split 12 people into 3 teams of 4?

* Your hash function assigns each object to a number between 1:10, each with equal probability. With 10 objects, what is the probability of a hash collision? What is the expected number of hash collisions? What is the expected number of hashes that are unused.

* You call 2 UberX’s and 3 Lyfts. If the time that each takes to reach you is IID, what is the probability that all the Lyfts arrive first? What is the probability that all the UberX’s arrive first?

* I write a program should print out all the numbers from 1 to 300, but prints out Fizz instead if the number is divisible by 3, Buzz instead if the number is divisible by 5, and FizzBuzz if the number is divisible by 3 and 5. What is the total number of numbers that is either Fizzed, Buzzed, or FizzBuzzed?

* On a dating site, users can select 5 out of 24 adjectives to describe themselves. A match is declared between two users if they match on at least 4 adjectives. If Alice and Bob randomly pick adjectives, what is the probability that they form a match?

* A lazy high school senior types up application and envelopes to n different colleges, but puts the applications randomly into the envelopes. What is the expected number of applications that went to the right college?

* Let’s say you have a very tall father. On average, what would you expect the height of his son to be? Taller, equal, or shorter? What if you had a very short father?

* What’s the expected number of coin flips until you get two heads in a row? What’s the expected number of coin flips until you get two tails in a row?

* Let’s say we play a game where I keep flipping a coin until I get heads. If the first time I get heads is on the nth coin, then I pay you 2n-1 dollars. How much would you pay me to play this game?

* You have two coins, one of which is fair and comes up heads with a probability 1/2, and the other which is biased and comes up heads with probability 3/4. You randomly pick coin and flip it twice, and get heads both times. What is the probability that you picked the fair coin?

* You have a 0.1% chance of picking up a coin with both heads, and a 99.9% chance that you pick up a fair coin. You flip your coin and it comes up heads 10 times. What’s the chance that you picked up the fair coin, given the information that you observed?

