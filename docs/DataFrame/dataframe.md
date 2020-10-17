
## DataFrame Introduction

In this notebook, we will learn to load the data and look at top row of the data, shape (i.e., number of rows and columns) of the data, list of name of columns, list of name of index and summary of data statistics (e.g., mean, standard deviation, median).


```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.set()
```

#### 1. Creating DataFrame by loading data

- To load data to pandas DataFrame from ```csv``` file, we can use ```read_csv()``` functionality. Pandas ```DataFrame``` is an object. When we load data, ```DataFrame``` holds the data with extra functionality integrated into the ```DataFrme``` object. Once the data is loaded, we can set up one column as the index by ```set_index()``` function. Following is the defult setting of data upload with ```read_csv()```:

```pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None,...)```


```python
titanic = pd.read_csv('data/titanic.csv')
titanic = titanic.set_index('Name')
```

- To see top 3 row of data in the ```DataFrame```.


```python
titanic.head(3)
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
    </tr>
  </tbody>
</table>
</div>



- To know shape of the ```DataFrame```:


```python
titanic.shape
```




    (891, 11)



- To find the list of column names:


```python
titanic.columns
```




    Index(['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch',
           'Ticket', 'Fare', 'Cabin', 'Embarked'],
          dtype='object')



- To find the list of index name:


```python
titanic.index
```




    Index(['Braund, Mr. Owen Harris',
           'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
           'Heikkinen, Miss. Laina',
           'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
           'Allen, Mr. William Henry', 'Moran, Mr. James',
           'McCarthy, Mr. Timothy J', 'Palsson, Master. Gosta Leonard',
           'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
           'Nasser, Mrs. Nicholas (Adele Achem)',
           ...
           'Markun, Mr. Johann', 'Dahlberg, Miss. Gerda Ulrika',
           'Banfield, Mr. Frederick James', 'Sutehall, Mr. Henry Jr',
           'Rice, Mrs. William (Margaret Norton)', 'Montvila, Rev. Juozas',
           'Graham, Miss. Margaret Edith',
           'Johnston, Miss. Catherine Helen "Carrie"', 'Behr, Mr. Karl Howell',
           'Dooley, Mr. Patrick'],
          dtype='object', name='Name', length=891)



- To find preliminary satatistics of the each column of the ```DataFrame```.


```python
titanic.describe().T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>PassengerId</th>
      <td>891.0</td>
      <td>446.000000</td>
      <td>257.353842</td>
      <td>1.00</td>
      <td>223.5000</td>
      <td>446.0000</td>
      <td>668.5</td>
      <td>891.0000</td>
    </tr>
    <tr>
      <th>Survived</th>
      <td>891.0</td>
      <td>0.383838</td>
      <td>0.486592</td>
      <td>0.00</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>1.0</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>Pclass</th>
      <td>891.0</td>
      <td>2.308642</td>
      <td>0.836071</td>
      <td>1.00</td>
      <td>2.0000</td>
      <td>3.0000</td>
      <td>3.0</td>
      <td>3.0000</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>714.0</td>
      <td>29.699118</td>
      <td>14.526497</td>
      <td>0.42</td>
      <td>20.1250</td>
      <td>28.0000</td>
      <td>38.0</td>
      <td>80.0000</td>
    </tr>
    <tr>
      <th>SibSp</th>
      <td>891.0</td>
      <td>0.523008</td>
      <td>1.102743</td>
      <td>0.00</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>1.0</td>
      <td>8.0000</td>
    </tr>
    <tr>
      <th>Parch</th>
      <td>891.0</td>
      <td>0.381594</td>
      <td>0.806057</td>
      <td>0.00</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0</td>
      <td>6.0000</td>
    </tr>
    <tr>
      <th>Fare</th>
      <td>891.0</td>
      <td>32.204208</td>
      <td>49.693429</td>
      <td>0.00</td>
      <td>7.9104</td>
      <td>14.4542</td>
      <td>31.0</td>
      <td>512.3292</td>
    </tr>
  </tbody>
</table>
</div>



- Styling data sample visualization:


```python
cm = sns.light_palette("green", as_cmap=True)
s = titanic[0:5].style.background_gradient(cmap=cm)
s
```




<style  type="text/css" >
    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col0 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col1 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col2 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col4 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col5 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col6 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col8 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col0 {
            background-color:  #acdfac;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col1 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col2 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col4 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col5 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col6 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col8 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col0 {
            background-color:  #72bf72;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col1 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col2 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col4 {
            background-color:  #acdfac;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col5 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col6 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col8 {
            background-color:  #e4fee4;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col0 {
            background-color:  #399f39;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col1 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col2 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col4 {
            background-color:  #2a972a;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col5 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col6 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col8 {
            background-color:  #41a441;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col0 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col1 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col2 {
            background-color:  #008000;
            color:  #f1f1f1;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col4 {
            background-color:  #2a972a;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col5 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col6 {
            background-color:  #e5ffe5;
            color:  #000000;
        }    #T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col8 {
            background-color:  #e3fee3;
            color:  #000000;
        }</style><table id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >PassengerId</th>        <th class="col_heading level0 col1" >Survived</th>        <th class="col_heading level0 col2" >Pclass</th>        <th class="col_heading level0 col3" >Sex</th>        <th class="col_heading level0 col4" >Age</th>        <th class="col_heading level0 col5" >SibSp</th>        <th class="col_heading level0 col6" >Parch</th>        <th class="col_heading level0 col7" >Ticket</th>        <th class="col_heading level0 col8" >Fare</th>        <th class="col_heading level0 col9" >Cabin</th>        <th class="col_heading level0 col10" >Embarked</th>    </tr>    <tr>        <th class="index_name level0" >Name</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96level0_row0" class="row_heading level0 row0" >Braund, Mr. Owen Harris</th>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col0" class="data row0 col0" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col1" class="data row0 col1" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col2" class="data row0 col2" >3</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col3" class="data row0 col3" >male</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col4" class="data row0 col4" >22</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col5" class="data row0 col5" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col6" class="data row0 col6" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col7" class="data row0 col7" >A/5 21171</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col8" class="data row0 col8" >7.25</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col9" class="data row0 col9" >nan</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row0_col10" class="data row0 col10" >S</td>
            </tr>
            <tr>
                        <th id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96level0_row1" class="row_heading level0 row1" >Cumings, Mrs. John Bradley (Florence Briggs Thayer)</th>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col0" class="data row1 col0" >2</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col1" class="data row1 col1" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col2" class="data row1 col2" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col3" class="data row1 col3" >female</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col4" class="data row1 col4" >38</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col5" class="data row1 col5" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col6" class="data row1 col6" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col7" class="data row1 col7" >PC 17599</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col8" class="data row1 col8" >71.2833</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col9" class="data row1 col9" >C85</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row1_col10" class="data row1 col10" >C</td>
            </tr>
            <tr>
                        <th id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96level0_row2" class="row_heading level0 row2" >Heikkinen, Miss. Laina</th>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col0" class="data row2 col0" >3</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col1" class="data row2 col1" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col2" class="data row2 col2" >3</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col3" class="data row2 col3" >female</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col4" class="data row2 col4" >26</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col5" class="data row2 col5" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col6" class="data row2 col6" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col7" class="data row2 col7" >STON/O2. 3101282</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col8" class="data row2 col8" >7.925</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col9" class="data row2 col9" >nan</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row2_col10" class="data row2 col10" >S</td>
            </tr>
            <tr>
                        <th id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96level0_row3" class="row_heading level0 row3" >Futrelle, Mrs. Jacques Heath (Lily May Peel)</th>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col0" class="data row3 col0" >4</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col1" class="data row3 col1" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col2" class="data row3 col2" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col3" class="data row3 col3" >female</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col4" class="data row3 col4" >35</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col5" class="data row3 col5" >1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col6" class="data row3 col6" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col7" class="data row3 col7" >113803</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col8" class="data row3 col8" >53.1</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col9" class="data row3 col9" >C123</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row3_col10" class="data row3 col10" >S</td>
            </tr>
            <tr>
                        <th id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96level0_row4" class="row_heading level0 row4" >Allen, Mr. William Henry</th>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col0" class="data row4 col0" >5</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col1" class="data row4 col1" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col2" class="data row4 col2" >3</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col3" class="data row4 col3" >male</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col4" class="data row4 col4" >35</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col5" class="data row4 col5" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col6" class="data row4 col6" >0</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col7" class="data row4 col7" >373450</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col8" class="data row4 col8" >8.05</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col9" class="data row4 col9" >nan</td>
                        <td id="T_ee022e9c_100c_11eb_9d23_3052cb51cf96row4_col10" class="data row4 col10" >S</td>
            </tr>
    </tbody></table>



- To drop a column from a ```DataFrame```:


```python
titanic = titanic.drop('Ticket', axis=1)
titanic.head(2)
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
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>



- To drop the row data if there is ```NaN``` value:


```python
titanic = titanic.dropna(axis=0)
titanic.head(2)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cumings, Mrs. John Bradley (Florence Briggs Thayer)</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
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
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



- To fill the ```NaN``` value with 0.


```python
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list('ABCD'))
df = df.fillna(0)
df
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
      <th>0</th>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



- To invert or transpose the ```DataFrame```:


```python
df.T
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>B</th>
      <td>2.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



### References:
1. [Pydata document for Styling DataFrame visualization](https://pandas.pydata.org/docs/user_guide/style.html)
2. [Pandas API References](https://pandas.pydata.org/docs/reference/index.html)
