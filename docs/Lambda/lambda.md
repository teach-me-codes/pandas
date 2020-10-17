
## Apply and Lambda Transformation

In this notebook we will learn to perform the column data operation through implementation of ```apply()``` and ```lambda``` functionality.


```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```

####  Load data


```python
titanic = pd.read_csv('data/titanic.csv')
df1 = titanic.set_index('Name')
df1.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Braund, Mr. Owen Harris</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>Cumings, Mrs. John Bradley (Florence Briggs Thayer)</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>



#### 1. Implementation of ```Apply ()``` with ```lambda()``` function

- Apply ```lambda``` functionality to ```age``` column.


```python
df1['remaining-age'] = df1['Age'].apply(lambda x: 100-x).head(5)
df1.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
      <th>remaining-age</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Braund, Mr. Owen Harris</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
      <td>78.0</td>
    </tr>
    <tr>
      <th>Cumings, Mrs. John Bradley (Florence Briggs Thayer)</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>Heikkinen, Miss. Laina</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
      <td>74.0</td>
    </tr>
    <tr>
      <th>Futrelle, Mrs. Jacques Heath (Lily May Peel)</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>Allen, Mr. William Henry</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
      <td>65.0</td>
    </tr>
  </tbody>
</table>
</div>



- Apply ```lambda``` functionality to ```Fare``` column to transform it to new value.


```python
df1['Fare'].apply(lambda x: (10*x**2 + 2*x +4)/10).head(5)
```




    Name
    Braund, Mr. Owen Harris                                  54.412500
    Cumings, Mrs. John Bradley (Florence Briggs Thayer)    5095.965519
    Heikkinen, Miss. Laina                                   64.790625
    Futrelle, Mrs. Jacques Heath (Lily May Peel)           2830.630000
    Allen, Mr. William Henry                                 66.812500
    Name: Fare, dtype: float64



- Let us write a new function to supply inside the ```apply()``` function.


```python
def newfeature(x):
    return 10 + x/3 + x**2
```


```python
df1['Fare'].apply(newfeature).head(4)
```




    Name
    Braund, Mr. Owen Harris                                  64.979167
    Cumings, Mrs. John Bradley (Florence Briggs Thayer)    5115.069959
    Heikkinen, Miss. Laina                                   75.447292
    Futrelle, Mrs. Jacques Heath (Lily May Peel)           2847.310000
    Name: Fare, dtype: float64



#### 2. Column Operation with Lambda function

- Lets create a new random dataframe to play around.


```python
dates = pd.date_range('1/1/2000', periods=100)
df = pd.DataFrame(np.random.randn(100, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.656738</td>
      <td>-0.461095</td>
      <td>-0.259647</td>
      <td>0.890244</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.652611</td>
      <td>0.906148</td>
      <td>-0.527606</td>
      <td>-0.106089</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.067463</td>
      <td>1.407429</td>
      <td>1.414694</td>
      <td>-1.266369</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>0.301058</td>
      <td>0.624163</td>
      <td>-0.144190</td>
      <td>-1.177690</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.557796</td>
      <td>-1.497422</td>
      <td>0.545636</td>
      <td>-1.006319</td>
    </tr>
  </tbody>
</table>
</div>



- We can directly add, multiply, substract etc among columns if they have same data types.


```python
df['E'] = (df['A'] + df['B'])/df['C']
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.656738</td>
      <td>-0.461095</td>
      <td>-0.259647</td>
      <td>0.890244</td>
      <td>4.305207</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.652611</td>
      <td>0.906148</td>
      <td>-0.527606</td>
      <td>-0.106089</td>
      <td>-2.954399</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.067463</td>
      <td>1.407429</td>
      <td>1.414694</td>
      <td>-1.266369</td>
      <td>0.947177</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>0.301058</td>
      <td>0.624163</td>
      <td>-0.144190</td>
      <td>-1.177690</td>
      <td>-6.416660</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.557796</td>
      <td>-1.497422</td>
      <td>0.545636</td>
      <td>-1.006319</td>
      <td>0.110649</td>
    </tr>
  </tbody>
</table>
</div>



- One can use ```lambda``` functions to transform the columns before the column operation.


```python
df['F'] = df['A'].apply(lambda x : 10+x) + df['E'].apply(lambda x: x+20 if x>0 else x)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.656738</td>
      <td>-0.461095</td>
      <td>-0.259647</td>
      <td>0.890244</td>
      <td>4.305207</td>
      <td>33.648469</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.652611</td>
      <td>0.906148</td>
      <td>-0.527606</td>
      <td>-0.106089</td>
      <td>-2.954399</td>
      <td>7.698212</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.067463</td>
      <td>1.407429</td>
      <td>1.414694</td>
      <td>-1.266369</td>
      <td>0.947177</td>
      <td>30.879714</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>0.301058</td>
      <td>0.624163</td>
      <td>-0.144190</td>
      <td>-1.177690</td>
      <td>-6.416660</td>
      <td>3.884397</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.557796</td>
      <td>-1.497422</td>
      <td>0.545636</td>
      <td>-1.006319</td>
      <td>0.110649</td>
      <td>31.668445</td>
    </tr>
  </tbody>
</table>
</div>



### References:
1. [Pydata document for Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)
