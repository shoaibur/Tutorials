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

**Gamma**
```
   Parameters: alpha, beta
   Gamma(alpha, beta) = beta^alpha / gamma_func(alpha) * x^(alpha-1) * e^(-beta * x)
   Mean = alpha/beta and variance = alpha/beta^2
```

**Beta**
```
   Parameters: alpha, beta
   Gamma(alpha, beta) = x^(alpha-1) * (1-x)^(beta-1) / B(alpha,beta), where B(alpha,beta) = gamma_func(alpha) * gamma_func(beta) / gamma_func(alpha+beta)
   Mean = alpha/(alpha+beta) and variance = alpha*beta / ( (alpha+beta)^2 * (alpha + beta + 1) )
```

**Conjugate priors**
```
Prior - Likelihood pairs:
Beta - Binomial            Gamma - Poisson         Normal - Normal(sigma=known)        Pareto - Uniform
Beta - Geometric           Gamma - Exponential     Inverse Gamma - Normal(mu=known)
```


**Exercise Problems (collection continuing from different sources!)**

* There are four people in a room that haven’t met before. They are told to shake hands, exactly once, of every other person in the room so that they all meet each other. If each of these people shake their hands with every other person exactly once then how many handshakes are going to occur?

* You have 8 coins in a bag. 3 of them are unfair and they have 60% chance of coming up with head when flipped. You randomly chose one coin from the bag and flip it two times. What is the probability of getting two heads?

* Find the probability of rolling doubles on two six-sided dice numbered from 1 to 6

* There are 26 letters in english. 1) can you tell me # of possible combinations of creating 3 letter words when we can use the each letter as many time as we want 2) and when we can use each letter only once?

* Software tester a found 80 bugs. Software tester b found 60 bugs. And they found 40 bugs that were common between them. Can you estimate the total number of bugs in the system?

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

* A fly has a life between 4-6 days. What is the probability that the fly will die at exactly 5 days?

* Jack is having two coins in his hand. Out of the two coins, one is a real coin and the second one is a faulty one with Tails on both sides. He blindfolds himself to choose a random coin and tosses it in the air. The coin falls down with Tails facing upwards. What is the probability that this tail is shown by the faulty coin?

* Rob has fever and the doctor suspects it to be typhoid. To be sure, the doctor wants to conduct the test. The test results positive when the patient actually has typhoid 80% of the time. The test gives positive when the patient does not have typhoid 10% of the time. If 1% of the population has typhoid, what is the probability that Rob has typhoid provided he tested positive?

* About 30% of human twins are identical, and the rest are fraternal. Identical twins are necessarily the same sex, half are males and the other half are females. One-quarter of fraternal twins are both males, one-quarter both female, and one-half are mixed: one male, one female. You have just become a parent of twins and are told they are both girls. Given this information, what is the probability that they are identical?

* While it is said that the probabilities of having a boy or a girl are the same, let’s assume that the actual probability of having a boy is slightly higher at 0.51. Suppose a couple plans to have 3 children. What is the probability that exactly 2 of them will be boys?

* The students of a particular class were given two tests for evaluation. Twenty-five percent of the class cleared both the tests and forty-five percent of the students were able to clear the first test. Calculate the percentage of students who passed the second test given that they were also able to pass the first test.

* Hospital records show that 75% of patients suffering from a disease die due to that disease. What is the probability that 4 out of the 6 randomly selected patients recover?

* The prior probability of anyone having HIV is 0.00148. The true positive rate for Elisa is 93% and the true negative rate is 99%. What is the probability that a recruit has HIV, given he tested positive on first Elisa test? What is the probability of having HIV, given he tested positive on Elisa the second time as well?

* Assume you sell sandwiches. 70% people choose egg, and the rest choose chicken. What is the probability of selling 2 egg sandwiches to the next 3 customers?

