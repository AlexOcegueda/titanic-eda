# titanic-eda

## What I Cleaned

1. Updated column '2urivied" to "Survived".
2. Filled in missing values in 'Embarked' with the Mode as this dataset uses 0,1,2 format to inform on which port.
3. Filled in missing values in 'Age' with the Median.
4. Removed all 'zero' columns that was used for machine learning.

## What I Learned (Pandas)

1. Avoid 'inplace=True'
1.1 it disrupts method chaining: You cannot stack multiple operations in one line if one returns None (which inplace=True does). 
1.2 Also, No performance gain: Under the hood, Pandas usually copies the data anyway, so it rarely saves memory.
(Fix) Just put the modified dataframe back into the same variable: data = data.rename({'x':'y'})

2. Remember 'index=False'
2.1 When saving: data.to_csv('./titanic.csv', index=False) recall that pandas by default adds in its own index column.

3. How to drop columns with df.drop(columns={})

4. How to fill in missing data with .fillna()

## Key Findings: Titanic Survival Factors

This analysis explores the primary factors that influenced passenger survival using both statistical correlation and predictive modeling (Linear and Logistic Regression).

### Correlations

Sex,+0.404,Strong Positive,"Strongest factor measured. The positive correlation indicates that the encoded female value is highly associated with survival, confirming the priority given to women."

Pclass,-0.245,Moderate Negative,"A moderate negative relationship exists, meaning as the class number increases (moving from 1st → 3rd), the survival rate significantly decreases."

Fare,+0.174,Weak Positive,"A weak but noticeable positive association, suggesting that higher ticket prices (often linked to higher class) offered a slight advantage for survival."

Age,-0.056,Very Weak Negative,"A negligible linear relationship. The slight negative lean suggests that, generally, older passengers had a marginally reduced chance of survival compared to younger ones."

Parch (Parents/Children),+0.055,Very Weak Positive,"A negligible relationship, slightly positive due to the higher survival rate of children."

SibSp (Siblings/Spouses),-0.014,Very Weak Negative,Virtually no linear relationship. The impact of having a sibling or spouse was not a significant factor on survival probability.

### Logistic vs Linear Regression
My analysis showed that Sex was the strongest predictor of survival. The Logistic Regression model confirms that being female significantly increased the odds of survival, while Fare had a smaller, but still statistically significant, positive impact on survival probability.

(Linear R2≈0.030, Logit R2≈0.147) Logistic Regression (0.147) was a much better fit for the binary survival outcome than Linear Regression (0.030).

![Image](https://github.com/AlexOcegueda/titanic-eda/blob/main/imgs/age_distribution.png)
![Image](https://github.com/AlexOcegueda/titanic-eda/blob/main/imgs/pclass-barchart.png)
![Image](https://github.com/AlexOcegueda/titanic-eda/blob/main/imgs/sex-survival-barchart.png)
![Image](https://github.com/AlexOcegueda/titanic-eda/blob/main/imgs/corr_heatmap.png)
