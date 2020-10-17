
## Data Operation: ```concat(), merge(), join()```

This notebook will provide a walkthrough for data ```concat, merge and join``` functionality for combining multiple DataFrame objects.

Some part of this notebook are taken from Pydata tutorials. Read more about these functionality from [Pandas Pydata Document about concat, merge, join](https://pandas.pydata.org/docs/user_guide/merging.html)[1].



```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.set()
```

#### 1. Concatanation of data frames by index:
 Here we create three seperate Dataframe with same column names (e.g., ```col A, col B, col C, col D```) and create a final dataframe with concatenating these dataframes. Read more from [pydata](https://pandas.pydata.org/docs/user_guide/merging.html)
 
 The defult setting is: ```pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None,
          levels=None, names=None, verify_integrity=False, copy=True)```
 

![img](https://pandas.pydata.org/docs/_images/merging_concat_basic.png)

<center> Image courtesy : Pydata </center>


```python
df1 = pd.DataFrame({'col A': ['A0', 'A1', 'A2', 'A3'],
                    'col B': ['B0', 'B1', 'B2', 'B3'],
                    'col C': ['C0', 'C1', 'C2', 'C3'],
                    'col D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
 

df2 = pd.DataFrame({'col A': ['A4', 'A5', 'A6', 'A7'],
                    'col B': ['B4', 'B5', 'B6', 'B7'],
                    'col C': ['C4', 'C5', 'C6', 'C7'],
                    'col D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])
     

df3 = pd.DataFrame({'col A': ['A8', 'A9', 'A10', 'A11'],
                    'col B': ['B8', 'B9', 'B10', 'B11'],
                    'col C': ['C8', 'C9', 'C10', 'C11'],
                    'col D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])
     

frames = [df1, df2, df3]
result = pd.concat(frames, sort=False)
result
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
      <th>col A</th>
      <th>col B</th>
      <th>col C</th>
      <th>col D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>



- Concatenating different dataframes with different column names with defult ```join="outer"```.


```python
df4 = pd.DataFrame({'colE': ['E4', 'E5', 'E6', 'E7'],
                    'colF': ['F4', 'F5', 'F6', 'F7'],
                    'colG': ['G4', 'G5', 'G6', 'G7'],
                    'colH': ['H4', 'H5', 'H6', 'H7']},
                    index=[4, 5, 6, 7])
     

df5 = pd.DataFrame({'colA': ['A8', 'A9', 'A10', 'A11'],
                    'colE': ['E8', 'E9', 'E10', 'E11'],
                    'colC': ['C8', 'C9', 'C10', 'C11'],
                    'colH': ['H8', 'H9', 'H10', 'H11']},
                    index=[8, 9, 10, 11])
     

frames = [df1, df2, df3]
result = pd.concat(frames, sort=False)
result
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
      <th>colA</th>
      <th>colB</th>
      <th>colC</th>
      <th>colD</th>
      <th>colE</th>
      <th>colF</th>
      <th>colG</th>
      <th>colH</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>E4</td>
      <td>F4</td>
      <td>G4</td>
      <td>H4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>E5</td>
      <td>F5</td>
      <td>G5</td>
      <td>H5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>E6</td>
      <td>F6</td>
      <td>G6</td>
      <td>H6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>E7</td>
      <td>F7</td>
      <td>G7</td>
      <td>H7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>NaN</td>
      <td>C8</td>
      <td>NaN</td>
      <td>E8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>H8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>NaN</td>
      <td>C9</td>
      <td>NaN</td>
      <td>E9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>H9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>NaN</td>
      <td>C10</td>
      <td>NaN</td>
      <td>E10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>H10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>NaN</td>
      <td>C11</td>
      <td>NaN</td>
      <td>E11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>H11</td>
    </tr>
  </tbody>
</table>
</div>



- Concatenating different dataframes with different column names with defult ```join="inner"``` and ```axis =0```.


```python
frames = [df1, df5]
result = pd.concat(frames, sort=False, join = "inner")
result
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
      <th>colA</th>
      <th>colC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>C0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>C1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>C2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>C3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>C8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>C9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>C10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>C11</td>
    </tr>
  </tbody>
</table>
</div>




<center> axis = 1</center>
<img src="https://miro.medium.com/max/875/1*LoUq8uZrbg_tO3t4tqZfqg.png" width="400" height="400"></img>

----------

<center> axis = 0</center>
<img src="https://miro.medium.com/max/875/1*bQ3Bl6_N_V4er6XZxVxIZA.png" width="400" height="400"></img>

------
<center> Image Courtesy www.towardsdatascience.com </center> 

#### 2. Merge dataframe

Two ```DataFrame``` object can be merged on specific ```key```.

Defult setting : ```pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)```

![img](https://pandas.pydata.org/docs/_images/merging_merge_on_key.png)
<center> Image courtesy : Pydata </center>



```python
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                          'B': ['B0', 'B1', 'B2', 'B3']})
     

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
     

result = pd.merge(left, right, on='key')
result
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
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




    
<img src="https://datascience.quantecon.org/assets/_static/merge_files/merge_venns.png" width="400" height="300"></img>


<center> Image Courtesy www.datascience.quantecon.org </center> 

#### 3. Join DataFrame

Joining two ```DataFrame``` objects with ```join``` operation. Defult setting is ```join='inner'```.
![img](![image.png](attachment:image.png)
<center> Image courtesy : Pydata </center>


```python
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                          'B': ['B0', 'B1', 'B2']},
                         index=['K0', 'K1', 'K2'])
     

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                           'D': ['D0', 'D2', 'D3']},
                          index=['K0', 'K2', 'K3'])
     

result = left.join(right)
result
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
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
  </tbody>
</table>
</div>



<img src="https://miro.medium.com/max/7360/1*-I_1qa5TIiB5eNYxnodfAA.png" width="600" height="500"></img>


<center> Image Courtesy www.towardsdatascience.com </center> 

### References:
1. [Pandas Pydata Document](https://pandas.pydata.org/docs/user_guide/merging.html)
2. [Python Pandas DataFrame Join, Merge, and Concatenate](https://towardsdatascience.com/python-pandas-dataframe-join-merge-and-concatenate-84985c29ef78)
3. [Merge, concat, Join in pandas](https://datascience.quantecon.org/pandas/merge.html)
