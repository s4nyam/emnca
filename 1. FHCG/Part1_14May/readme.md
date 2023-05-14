# This folder contains answers to the questions below:

## 1. Check simple life like rules. We need to improve coarse graining, may be I can try to use simple rules to check the working of the current coarse graining.
I understand, for a note, the purpose of coarse graining is to capture emerging behaviour, like gliders and eliminate the noise. Basically, remove noise and capture relevant features, features that appreared less is relevant and features that appeared more are irrelevant.

## 2. Should also check different levels of coarse graining using 
```python
block_size = 2
block_size = 3
```

## 3. Check the same on life like CA known rules of 2D CA. Try on 1nh CA for example GoL using moore neighborhood, 2nh CA or Multi-Neighbor CA.

## 4. Replace values from x-axis plots from probability with block types. For example, for 2x2 block we have 16 types of boolean combination of 0s and 1s i.e., 0000 to 1111

## 5. No need to run CA for every time. Just store CA for one run and then perform coarse graining with varying thresholds. In simpler words, just run CA for one time with a known life like rules, store data. Now perform coarse graining with varying thresholds. 
```python
# To overcome that, we have used 
import numpy as np
np.random.seed(seed_value)
```

## All imprveoments can be found under two notebooks namely:
### 1. bs2_100_100_10_Volumetric_VisMNCA_FHCG.ipynb for block size 2
### 2. bs3_198_198_10_Volumetric_VisMNCA_FHCG.ipynb for block size 3