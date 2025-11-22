# titanic-eda

## What I Cleaned

1. Updated column '2urivied" to "Survived".
2. Filled in missing values in 'Embarked' with the Mode as this dataset uses 0,1,2 format to inform on which port.

## What I Learned

1. Avoid 'inplace=True'
1.1 it disrupts method chaining: You cannot stack multiple operations in one line if one returns None (which inplace=True does). 
1.2 Also, No performance gain: Under the hood, Pandas usually copies the data anyway, so it rarely saves memory.
(Fix) Just put the modified dataframe back into the same variable: data = data.rename({'x':'y'})

2. Remember 'index=False'
2.1 When saving: data.to_csv('./titanic.csv', index=False) recall that pandas by default adds in its own index column.


