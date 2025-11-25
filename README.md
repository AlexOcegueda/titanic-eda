# titanic-eda

## What I Cleaned

1. Updated column '2urivied" to "Survived".
2. Filled in missing values in 'Embarked' with the Mode as this dataset uses 0,1,2 format to inform on which port.
3. Removed all 'zero' columns that was used for machine learning.

## What I Learned (Pandas)

1. Avoid 'inplace=True'
1.1 it disrupts method chaining: You cannot stack multiple operations in one line if one returns None (which inplace=True does). 
1.2 Also, No performance gain: Under the hood, Pandas usually copies the data anyway, so it rarely saves memory.
(Fix) Just put the modified dataframe back into the same variable: data = data.rename({'x':'y'})

2. Remember 'index=False'
2.1 When saving: data.to_csv('./titanic.csv', index=False) recall that pandas by default adds in its own index column.

3. How to drop columns with df.drop(columns={})

4. How to fill in missing data with .fillna()

## What I Learned (Titanic)

## Correlation
1. -0.0559 == Close to zero so no relation between age and surivival on the titanic. It is leaning towards a negative correlation which is interesting. I interpet this to mean the older you were the less likely you would be saved.
2. 0.1737862546525127 == Weak relation between fare and survival. It is leaning a positive correlation which is what i assumed but I expected it to be stronger. I thought bigger fare meant better position on boat or secure spot on a ship.
3. 0.40402003566536115 == stronger relation between your sex and survival rate. This is saying women where more likely to be saved than men.
4. -0.014375452914690471 == Weak relation with having a spouse or sibling on board and being saved.
5. 0.054908128447466 == weak positive relation with have a child or parent on board with survival.
6. -0.24468558861046874 == negative relation with class and survival rate.
