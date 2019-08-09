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
   CI = p +/- 1.96 * sqrt( p(1-p)/n ) under normal approximation with np > 5.
```

**Geometric**
```
   Parameters: p
   Geometric(p) = p (1-p)^(x-1)
   Mean = 1/p and variance = (1-p) / p^2
   p = Probability of getting 1-st success in x trials.
```

**Negative Binomial**
```
   Parameters: k, p
   NegBinomial(k, p) = (x-1)C(k-1) p^k (1-p)^(x-k)
   Mean = k / p and variance = k(1-p) / p^2
   p = Probability of getting k successes in x trials.
```

**Poisson**
```
   Parameters: lam
   Poisson(lam) = e^(-lam) lam^k / k!
   Mean = lam and variance = lam
   CI = lam +/- 1.96 * sqrt( lam/n ) under normal approximation.
   The number of events occur in a given time duration follows Poisson distribution.
```

**Exponential**
```
   Parameters: lam
   Exponential(lam) = lam * e^(-lam*x)
   Mean = 1/lam and variance = 1/lam^2
   The amount of time to wait until an event first occurs follow an exponential distribution.
```
Note: If the occurrence of events in a time duration T = t2-t1 can be modeled as Poisson process, the in inter-event-intervals can be modeled using exponential distribution, i.e. the times taken between two consecutive events are exponential distributed.

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
   Gamma(alpha, beta) = beta^alpha / GAMM(alpha) * x^(alpha-1) * e^(-beta * x)
   Mean = alpha/beta and variance = alpha/beta^2
```

**Beta**
```
   Parameters: alpha, beta
   Beta(alpha, beta) = x^(alpha-1) * (1-x)^(beta-1) / B(alpha,beta), where B(alpha,beta) = GAMM(alpha) * GAMM(beta) / gamma_func(alpha+beta)
   Mean = alpha/(alpha+beta) and variance = alpha*beta / ( (alpha+beta)^2 * (alpha + beta + 1) )
```

**Conjugate priors**
```
Prior - Likelihood pairs:
Beta - Binomial            Gamma - Poisson         Normal - Normal(sigma=known)        Pareto - Uniform
Beta - Geometric           Gamma - Exponential     Inverse Gamma - Normal(mu=known)
```

**Gamma-Beta identities**
```
INT(0, inf){ x^(t-1) * e^(-x) }dx = GAMM(t)
INT(0,1){ x^(a-1) * (1-x)^(b-1) }dx = GAMM(a)*GAMM(b)/GAMM(a+b)
GAMM(a) = (a-1)! and GAMM(1+a) = a*GAMM(a)
```


**Exercise Problems (collection continuing from different sources!)**

* There are four people in a room that haven’t met before. They are told to shake hands, exactly once, of every other person in the room so that they all meet each other. If each of these people shake their hands with every other person exactly once then how many handshakes are going to occur?
```
There are 4C2 ways to select 2 people from 4.
```

* You have 8 coins in a bag. 3 of them are unfair and they have 60% chance of coming up with head when flipped. You randomly chose one coin from the bag and flip it two times. What is the probability of getting two heads?
```
8--|U--3/8--|--HH--0.6*0.6 √
   |        |--HT--0.6*0.4
   |        |--TH--0.4*0.6
   |        |--TT--0.4*0.4
   |F--5/8--|--HH--0.5*0.5 √
   |        |--HT--0.5*0.5
   |        |--TH--0.5*0.5
   |        |--TT--0.5*0.5
Law of total probability:
p(HH) = p(HH|U) + p(HH|F) = 3/8 * 0.36 + 5/8 * 0.25
```

* Find the probability of rolling doubles on two six-sided dice numbered from 1 to 6
 ```
Imagine the sample space of the two rolls; 
the diagonal will form the doubles (same outcome in the both rolls). 
So, the probability of rolling doubles is 6/36 = 1/6
```

* There are 26 letters in english. 1) can you tell me # of possible combinations of creating 3 letter words when we can use the each letter as many time as we want 2) and when we can use each letter only once?
```
1) Each position can be filled with 26 ways, so for 3 letter words: 26*26*26 = 26^3
2) Total choice: 26C3
```

* Software tester a found 80 bugs. Software tester b found 60 bugs. And they found 40 bugs that were common between them. Can you estimate the total number of bugs in the system?
```
n(Bugs) = n(a) + n(b) - n(a and b) = 80 + 60 - 40 = 100
```

* Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 o spring, respectively. Each of Bobo’s descendants also has the same probabilities. What is the probability that Bobo’s lineage dies out?
```
p = probability of Bobo's lineage dies out.
Bobo--|--0--1/4.p^0
      |--1--1/4.p^1
      |--2--1/2.p^2
Total probability:
p = 1/4 + 1/4 p + 1/2 p^2
p = 1, 1/2
```

* In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the probability that you see at least one shooting star in the period of an hour?
```
Number of occurance in a given (time) interval follows a Poisson distribution.
For 15-minute duration:
          inf
          ---
p = 0.2 = \    exp(-lambda) lambda^k / k!
          /
          ---
          i=1
=> 0.2 = 1-exp(-lambda) => exp(-lambda) = 0.8 => lambda = ln(1/0.8) = ln(5/4)

For 1 hour duration:
lambda = 60/15 * lambda = 4 ln(5/4)
p = 1 - exp(-lambda) = 1 - exp(-4 ln(5/4))
```

* How can you generate a random number between 1 and 7 with only a die?
```
Let's roll twice, which will give 36 possible unique outcomes. For equal proabiblity,
consider the first 35 outcomes (maximum integer of 7) and ignore the rolls with outcomes 6,6.

Let's denote the outcomes in the first and second rolls: x1 and x2
Random number between 1 and 7 with the outcomes in two rolls: (6*(x1-1) + x2)%7 + 1

A % B denotes the remainder when A is divided by B.

In general, with a n-sided dice (or anything that gives n possible unique outputs),
and with r rolls, to generate random numbers between 1 and D, use the following equation:

.----                       ----.
|  r-1                           |
|  ---                           |
|  \  n^(r-1) * (x_i - 1) + x_r  | % D + 1
|  /                             |
|  ---                           |
|  i=i                           |
'----                       ----'
For n = 6 and r = 4: [6^3*(x1-1) + 6^2*(x2-1) + 6*(x3-1) + x4] % D + 1

Based on the value of D, we need to find the value of r and ignore some of the outcomes.
```

* How can you get a fair coin toss if someone hands you a coin that is weighted to come up heads more often than tails?
```
Let's probability of getting heads = p. Toss twice:
prob(HH) = p.p
prob(HT) = p(1-p)
prob(TH) = (1-p)p
prob(TT) = (1-p)(1-p)
So, ignore if the outcomes are HH or TT, and call HT as heads and TH as tails, which have equal proababilities.
```

* You have an 50-50 mixture of two normal distributions with the same standard deviation. How far apart do the means need to be in order for this distribution to be bimodal?
```
|mu1-mu2| > 2*sigma
```

* Given draws from a normal distribution with known parameters, how can you simulate draws from a uniform distribution?
```
Put the draws into the CDF of the normal distribution, 
which will give the draws from a uniform distribution between 0 and 1.
This is the universality of uniform distribution.
```

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

* In a class of 30 students, approximately what is the probability that two of the students have their birthday on the same day (defined by same day and month) (assuming it’s not a leap year)?

* Consider the following probability density function: f(x) = 1/8 e^(-x/8), x > 0. What is the probability for X≤6 i.e. P(x≤6)

* There are a total of 8 bows of 2 each of green, yellow, orange & red. In how many ways can you select 1 bow?

* A coin of diameter 1-inches is thrown on a table covered with a grid of lines each two inches apart. What is the probability that the coin lands inside a square without touching any of the lines of the grid? You can assume that the person throwing has no skill in throwing the coin and is throwing it randomly.

* Suppose you were interviewed for a technical role. 50% of the people who sat for the first interview received the call for second interview. 95% of the people who got a call for second interview felt good about their first interview. 75% of people who did not receive a second call, also felt good about their first interview. If you felt good after your first interview, what is the probability that you will receive a second interview call?

* Consider 3 situations as follows: (1) At least one 6, when 6 dice are rolled. (2) At least 2 sixes when 12 dice are rolled. (3) At least 3 sixes when 18 dice are rolled. Which of the following events is most likely?

* A jar contains 4 marbles: 3 red and 1 white. Two marbles are drawn with replacement after each draw. What is the probability that the same color marble is drawn twice?

* Some test scores follow a normal distribution with a mean of 18 and a standard deviation of 6. What proportion of test takers have scored between 18 and 24?

* A roulette wheel has 38 slots, 18 are red, 18 are black, and 2 are green. You play five games and always bet on red. (1) How many games can you expect to win? (2) What is the probability that you win all the 5 games?

* Cross-fertilizing a red and a white flower produces red flowers 25% of the time. Now we cross-fertilize five pairs of red and white flowers and produce five offspring. What is the probability that there are no red flower plants in the five offspring?

* Suppose you’re in the final round of “Let’s make a deal” game show and you are supposed to choose from three doors – 1, 2 & 3. One of the three doors has a car behind it and other two doors have goats. Let’s say you choose Door 1 and the host opens Door 3, which has a goat behind it. To assure the probability of your win, which of the following options would you choose?

* When an event A independent of itself?

* Suppose a life insurance company sells a $240,000 one year term life insurance policy to a 25-year old female for $210. The probability that the female survives the year is .999592. Find the expected value of this policy for the insurance company.

* We have two coins, A and B. For each toss of coin A, the probability of getting head is 1/2 and for each toss of coin B, the probability of getting Heads is 1/3. All tosses of the same coin are independent. We select a coin at random and toss it till we get a head. The probability of selecting coin A is ¼ and coin B is 3/4. What is the expected number of tosses to get the first heads?

* A group of 60 students is randomly split into 3 classes of equal size. All partitions are equally likely. Jack and Jill are two students belonging to that group. What is the probability that Jack and Jill will end up in the same class?

* 18 people are randomly divided into 3 groups of size 5, 6 and 7. Among the 18 are John, Jack and James. What is the probability that: (1) what is the probability that both Jack and James are included in the 6-persons group? (2) What is the probability that John, Jack and James are each in a different group? (3) What is the probability that two of the three are in the same group and the third is in a different group?

* A fair six-sided die is rolled 6 times. What is the probability of getting all outcomes as unique?

* A player is randomly dealt a sequence of 13 cards from a deck of 52-cards. All sequences of 13 cards are equally likely. In an equivalent model, the cards are chosen and dealt one at a time. When choosing a card, the dealer is equally likely to pick any of the cards that remain in the deck. If you dealt 13 cards, what is the probability that the 13th card is a King?

* Anita randomly picks 4 cards from a deck of 52-cards and places them back into the deck ( Any set of 4 cards is equally likely ). Then, Babita randomly chooses 8 cards out of the same deck ( Any set of 8 cards is equally likely). Assume that the choice of 4 cards by Anita and the choice of 8 cards by Babita are independent. What is the probability that all 4 cards chosen by Anita are in the set of 8 cards chosen by Babita?

* Consider a tetrahedral die and roll it twice. What is the probability that the number on the first roll is strictly higher than the number on the second roll?

* A fair six-sided die is rolled twice. What is the probability of getting 2 on the first roll and not getting 4 on the second roll?

* Alice has 2 kids and one of them is a girl. What is the probability that the other child is also a girl?

* Let A and B be events on the same sample space, with P (A) = 0.6 and P (B) = 0.7. Can these two events be disjoint?

* You are playing a lottery game where you must pick 2 numbers from 0 to 9 followed by an English alphabet (from 26-letters). You may choose the same number both times. If his ticket matches the 2 numbers and 1 letter drawn in order, you win the grand prize and receive $10405. If just his letter matches but one or both of the numbers do not match, you win $100. Under any other circumstance, you win nothing. The game costs you $5 to play. Suppose you have chosen 04R to play. What is the expected net profit from playing this ticket?

* A coin is tossed for 1000 times and 560 heads appeared. Is the coin fair?

* In general, 20% m&m are red. You pick 100 of them and found 15 red. Is this usual?

* You’re about to get on a plane to Seattle. You want to know if you should bring an umbrella. You call 3 random friends of yours who live there and ask each independently if it’s raining. Each of your friends has a 2/3 chance of telling you the truth and a 1/3 chance of messing with you by lying. All 3 friends tell you that “Yes” it is raining. What is the probability that it’s actually raining in Seattle?

* There’s one box - has 12 black and 12 red cards, 2nd box has 24 black and 24 red; if you want to draw 2 cards at random from one of the 2 boxes, which box has the higher probability of getting the same color? Can you tell intuitively why the 2nd box has a higher probability?

* An HIV test has a sensitivity of 99.7% and a specificity of 98.5%. A subject from a population of prevalence 0.1% receives a positive test result. What is the precision of the test (i.e the probability he is HIV positive)?

* Infection rates at a hospital above a 1 infection per 100 person days at risk are considered high. An hospital had 10 infections over the last 1787 person days at risk. Give the p-value of the correct one-sided test of whether the hospital is below the standard.

* You roll a biased coin (p(head)=0.8) five times. What’s the probability of getting three or more heads?

* A random variable X is normal with mean 1020 and standard deviation 50. Calculate P(X>1200)

* Consider the number of people that show up at a bus station is Poisson with mean 2.5/h. What is the probability that at most three people show up in a four-hour period?

* You are running for office and your pollster polled hundred people. Sixty of them claimed they will vote for you. Can you relax?

* Geiger counter records 100 radioactive decays in 5 minutes. Find an approximate 95% interval for the number of decays per hour.

* The homicide rate in Scotland fell last year to 99 from 115 the year before. Is this reported change really noteworthy?

* Consider influenza epidemics for two parent heterosexual families. Suppose that the probability is 17% that at least one of the parents has contracted the disease. The probability that the father has contracted influenza is 12% while the probability that both the mother and father have contracted the disease is 6%. What is the probability that the mother has contracted influenza?

* Suppose that diastolic blood pressures (DBPs) for men aged 35-44 are normally distributed with a mean of 80 (mm Hg) and a standard deviation of 10. About what is the probability that a random 35-44 year old has a DBP less than 70?

* In a population of interest, a sample of 9 men yielded a sample average brain volume of 1,100cc and a standard deviation of 30cc. What is a 95% Student’s T confidence interval for the mean brain volume in this new population?

* A diet pill is given to 9 subjects over six weeks. The average difference in weight (follow up - baseline) is -2 pounds. What would the standard deviation of the difference in weight have to be for the upper endpoint of the 95% T confidence interval to touch 0?

* An oil company conducts a geological study that indicates that an exploratory oil well should have a 20% chance of striking oil. (1) What is the probability that the first strike comes on the third well drilled? (2) What is the probability that the third strike comes on the seventh well drilled? (3) What is the mean and variance of the number of wells that must be drilled if the oil company wants to set up three producing wells?

* A representative from the National Football League's Marketing Division randomly selects people on a random street in Kansas City. The probability that he succeeds in finding such a person, equal 0.20. (1) What is the probability that the marketing representative must select 4 people before he finds one who attended the last home football game? (2) What is the probability that the marketing representative must select more than 6 people before he finds one who attended the last home football game? (3) How many people should we expect (that is, what is the average number) the marketing representative needs to select before he finds one who attended the last home football game? And, while we're at it, what is the variance?

* You have a group of couples that decide to have children until they have their first girl, after which they stop having children. (1) What is the expected number of children each couple will have? (2) What is the expected gender ratio of the children that are born?

* The number of typos on a printed page with a mean of 3 typos per page. (1) What is the probability that a randomly selected page has at least one typo on it? (2) What is the probability that a randomly selected page has at most one typo on it? (3) What is the probability that a randomly selected page has four typos on it? (4) What is the probability that three randomly selected pages have more than eight typos on it?

* Students arrive at a local bar and restaurant according to an approximate Poisson process at a mean rate of 30 students per hour. What is the probability that the bouncer has to wait more than 3 minutes to card the next student?
```
Times between events, whose occurances can be modeled as Poisson process, can be modeled using exponential distribution.
mu = 1/lam = 30 /hour = 1/2 /minute
P(x>3) = int(3,inf) 2 exp(-2x) = exp(-6)
```

* The number of miles that a particular car can run before its battery wears out is exponentially distributed with an average of 10,000 miles. The owner of the car needs to take a 5000-mile trip. What is the probability that he will be able to complete the trip without having to replace the car battery?
```
Assume that the car hasn't been driven, i.e. the battery is fully charged before the starting of the journey.
mu = 1/lam = 10000 miles
P(x>5000) = int(5000,inf) 1/1000 exp(-x/10000) = exp(-1/2)
```

* A shuttle train at a busy airport completes a circuit between two terminals in 5 minutes. What is the probability that a passenger needs to wait more than 3 minutes in a terminal?
```
a=0, b=5, U(a,b)=1/(b-a) = 1/5
P(x>3) = int(3,5) 1/5 dx = 2/5 = 0.4
```
