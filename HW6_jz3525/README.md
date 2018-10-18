# PUI2018 HW 6 session 2 (evening)
## Assignment 1
### 1. Verify the Null and Alternate Hypothesis
I think it's really interesting to compare different types of customer. Personally, I've never thought about any possible difference on that. Very good point.
The only thing I have question about is the Null hypothesis and Alternate hypothesis states "biking on weekends" whereas the following project was made based on biking on weekdays. To make the project result clearer, I suggest to change the Null hypothesis to "The proportion of subsriber biking on weekdays is the same or higher than the proportion of customer biking on weekdays", and change the Alternative hypothesis to "The proportion of subscriber biking on weekdays is lower than the proportion of customer biking on weekdays".

### 2. Verify the Data Support the Project
As I mentioned above, the data calculated in the project doesn't match the Null hypothesis and Alternative hypothesis. If the two hypothesis were changed to statements based on biking on weekdays, the data match perfectly and were well pre-processed.
It's very well done to plot a normalized bar plot when the counts of two different types of users are significantly different to show the real difference.

### 3. Choose Appropriate Test
For the test, since the number of samples is really large (>30), I suggest conducting Z-test.
For this question, a Z-test could be applied with a one-tail two sample test, under 0.05 significance level, to show whether or not to reject the null hypothesis.


## Assignment 2
Group work with Asilayi Bahetibieke(ab8131), I did the ANOVA test and Correlation test while Asilayi finished the Logistic Regression test.
### ANOVA
| Statistical Analyses  | IV(s) | IV type(s) | DV(s) | DV type(s) | Control Var | Control Var type | Question to be answered | H0 | alpha | link to paper |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ANOVA  | 3, Player Level, (Professional level, Semi-profesisonal level, Non-professional level)  | Categorical  | 1, Motor Test  | Continuous  | None  | None  | Is the prognostic relevance of motor prognostic valid for identifying talents for potential players  | Players who reached APL1 had better scores in all motor test than the players who made it to the semi-professional or non-professional level  | 0.05  | [The influence of speed abilities and technical skills in early adolescence on adult success in soccer: A long-term prospective analysis using ANOVA and SEM approaches](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182211)  |

![journal pone 0182211 g002](https://user-images.githubusercontent.com/10840545/47044980-a713ef80-d15f-11e8-820b-b85f08c26d16.PNG)

### Correlation
| Statistical Analyses  | IV(s) | IV type(s) | DV(s) | DV type(s) | Control Var | Control Var type | Question to be answered | H0 | alpha | link to paper |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Correlation  | 1, The time spent on horses with different riders' postures  | Continuous  | 1, Number of horses with neck disorders  | Discrete  | 2, Riders' rein length and Riders' heel height  | Continuous  | Is the number of horses with neck disorders larger with more time spent on low hands positions than on positions in control gourps?  | Number of horses with neck disorders in low hands positions is smaller than that in control group | 0.05  | [Human Direct Actions May Alter Animal Welfare, a Study on Horses (Equus caballus)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010257)  |

![journal pone 0010257 t002](https://user-images.githubusercontent.com/10840545/47058446-10f9bc80-d193-11e8-9c7c-3888e040ffab.png)

### Logistic Regression
| Statistical Analyses  | IV(s) | IV type(s) | DV(s) | DV type(s) | Control Var | Control Var type | Question to be answered | H0 | alpha | link to paper |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Logistic Regression  | 1, BMI at 7 years  | Categorical  | 1, Odds Ratio for Obesity at 13 years  | Continuous  | 2, Birth Cohort, Gender  | Categorical  | Is the incident and persistance of obesity from age 7 to 13 causing the increasing prevalence of childhood obesity in Denmark?  | The increased persistence of obesity from 7 to 13 years old increase the prevalence of obesity at age 13 years old among boys and girls   | 0.05  | [Contributions of Incidence and Persistence to the Prevalence of Childhood Obesity during the Emerging Epidemic in Denmark](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0042521)  |

![journal pone 0042521 g005](https://user-images.githubusercontent.com/10840545/47058655-f96f0380-d193-11e8-8ed0-ed6e518bb152.png)

## Assignment 3
I worked with Asilayi to reproduce the analysis of the Hard to Employ program in NY and completed the Z-test and Chi-square test.

## Assignment 4
I worked with Asilayi to split the 201502 citibike dataset into trips during the day and night, and conducted three different tests (K-S test, Pearson's test and Spearman's test) to show whether there are statistical differences between the tripduration of them.
