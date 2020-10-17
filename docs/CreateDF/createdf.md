
## DataFrame Creation

In this notebook, we will learn to create new ```DataFrame``` object from other data structures( e.g.,numpy array and dictionary) and convert data frame to numpy array and dictionary. The defult setting for pandas ```DataFrame``` is 

```pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)```


```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.set()
```

#### 1. To create new ```DataFrame``` from Numpy array. 

Let's create a random array of size(100,20) and random column names. We will use these array and column names to create the ```DataFrame``` in next step.


```python
import random as random
A = np.random.rand(100,10)
letter = ['A','B','C','D','E','F','G','H','X']

def namer(n):
    col_names = [ random.choice(letter)\
             +random.choice(letter)\
             +random.choice(letter)\
             +random.choice(letter) for i in range(n)]
    return col_names
```


```python
print(namer(A.shape[1]))
```

    ['HHEE', 'FEGD', 'BFHC', 'HXFC', 'CBDF', 'DEDH', 'CBCX', 'XGXB', 'GCBC', 'FDEE']
    


```python
df = pd.DataFrame(A, columns = col_names )
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
      <th>AAGF</th>
      <th>XBGA</th>
      <th>DXAC</th>
      <th>XEDB</th>
      <th>EDCG</th>
      <th>ABDH</th>
      <th>GFHX</th>
      <th>FAAB</th>
      <th>BBEC</th>
      <th>DGDC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.285058</td>
      <td>0.456733</td>
      <td>0.841292</td>
      <td>0.397957</td>
      <td>0.888982</td>
      <td>0.970782</td>
      <td>0.379687</td>
      <td>0.565177</td>
      <td>0.657939</td>
      <td>0.461385</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.725005</td>
      <td>0.432756</td>
      <td>0.037801</td>
      <td>0.020203</td>
      <td>0.590901</td>
      <td>0.590571</td>
      <td>0.623529</td>
      <td>0.166581</td>
      <td>0.179392</td>
      <td>0.454290</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.668743</td>
      <td>0.352332</td>
      <td>0.642905</td>
      <td>0.427461</td>
      <td>0.025124</td>
      <td>0.365414</td>
      <td>0.609983</td>
      <td>0.568686</td>
      <td>0.522738</td>
      <td>0.525048</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.807165</td>
      <td>0.827478</td>
      <td>0.542088</td>
      <td>0.628743</td>
      <td>0.616745</td>
      <td>0.386370</td>
      <td>0.632225</td>
      <td>0.387794</td>
      <td>0.618686</td>
      <td>0.786503</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.645945</td>
      <td>0.136078</td>
      <td>0.769546</td>
      <td>0.721885</td>
      <td>0.107891</td>
      <td>0.128859</td>
      <td>0.938451</td>
      <td>0.875492</td>
      <td>0.647702</td>
      <td>0.148635</td>
    </tr>
  </tbody>
</table>
</div>



- To save data from ```new DataFrame``` to a file:


```python
df.to_csv('data/test.csv')
```

#### 2. To create new  ```DataFrame``` from  list of dictionaries.

Here we will create a list with collection of dictionaries. Each of the dictionary will have keys and values. Using this list of dictionaries, we will create another ```DataFrame```. The keys of the dictionary will serve as the column names.


```python
LD = []
for i in range(100):
    LD.append({'Player' : namer(1)[0],\
               'game1' : random.uniform(0,1),\
               'game2' : random.uniform(0,1),\
               'game3' : random.uniform(0,1),
               'game4' : random.uniform(0,1),
               'game5' : random.uniform(0,1)})
```


```python
LD[0]
```




    {'Player': 'BGXB',
     'game1': 0.2965944756471328,
     'game2': 0.11334763879800447,
     'game3': 0.028543866127768824,
     'game4': 0.225405432495144,
     'game5': 0.05423542200055986}




```python
DF = pd.DataFrame(LD)
DF=DF.set_index("Player")
```


```python
DF.head(10)
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
      <th>game1</th>
      <th>game2</th>
      <th>game3</th>
      <th>game4</th>
      <th>game5</th>
    </tr>
    <tr>
      <th>Player</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BGXB</th>
      <td>0.296594</td>
      <td>0.113348</td>
      <td>0.028544</td>
      <td>0.225405</td>
      <td>0.054235</td>
    </tr>
    <tr>
      <th>DBDB</th>
      <td>0.047226</td>
      <td>0.107065</td>
      <td>0.801571</td>
      <td>0.816877</td>
      <td>0.556934</td>
    </tr>
    <tr>
      <th>AXXH</th>
      <td>0.862611</td>
      <td>0.439051</td>
      <td>0.083341</td>
      <td>0.389785</td>
      <td>0.258748</td>
    </tr>
    <tr>
      <th>BXED</th>
      <td>0.643533</td>
      <td>0.082176</td>
      <td>0.167241</td>
      <td>0.405304</td>
      <td>0.088063</td>
    </tr>
    <tr>
      <th>FXGE</th>
      <td>0.279076</td>
      <td>0.000998</td>
      <td>0.949414</td>
      <td>0.303408</td>
      <td>0.009342</td>
    </tr>
    <tr>
      <th>AHDC</th>
      <td>0.617194</td>
      <td>0.272401</td>
      <td>0.252663</td>
      <td>0.788798</td>
      <td>0.130996</td>
    </tr>
    <tr>
      <th>CXGA</th>
      <td>0.104552</td>
      <td>0.895106</td>
      <td>0.414877</td>
      <td>0.167643</td>
      <td>0.454175</td>
    </tr>
    <tr>
      <th>BDBA</th>
      <td>0.045650</td>
      <td>0.926742</td>
      <td>0.454097</td>
      <td>0.055006</td>
      <td>0.939082</td>
    </tr>
    <tr>
      <th>HBDC</th>
      <td>0.069192</td>
      <td>0.797224</td>
      <td>0.943648</td>
      <td>0.567334</td>
      <td>0.044285</td>
    </tr>
    <tr>
      <th>EBBX</th>
      <td>0.383365</td>
      <td>0.852788</td>
      <td>0.679330</td>
      <td>0.418570</td>
      <td>0.817291</td>
    </tr>
  </tbody>
</table>
</div>



#### 3. To create ```DataFrame``` from a List :


```python
A = [random.uniform(0,1)for i in range(10)]
B = [random.uniform(0,1)for i in range(10)]
C = [random.uniform(0,1)for i in range(10)]
D = [random.uniform(0,1)for i in range(10)]

df = pd.DataFrame()
df['A'],df['B'],df['C'],df['D'] = A,B,C,D
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
      <th>0</th>
      <td>0.816389</td>
      <td>0.212530</td>
      <td>0.705185</td>
      <td>0.225743</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.646496</td>
      <td>0.876869</td>
      <td>0.648350</td>
      <td>0.788687</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.869173</td>
      <td>0.832004</td>
      <td>0.516009</td>
      <td>0.917783</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.668866</td>
      <td>0.778850</td>
      <td>0.834528</td>
      <td>0.243842</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.742311</td>
      <td>0.984313</td>
      <td>0.872512</td>
      <td>0.451476</td>
    </tr>
  </tbody>
</table>
</div>



### References:
1. [Pydata document for Styling DataFrame visualization](https://pandas.pydata.org/docs/user_guide/style.html)
