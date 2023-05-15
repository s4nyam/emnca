# This folder contains answers to the questions below:

## 1. All elementary CA runs of 256 rules: HD fine grained CA vs CG CA with a block of 2x1. Having 2x1 coarse graining on Elementary CA.

## 2. Vary with 6 types of initialisations:
### 2.1 Centre of 1% initialisation.
### 2.2 Probabilistic 10% random initialisation
### 2.3 Probabilistic 20% random initialisation
### 2.4 Probabilistic 30% random initialisation
### 2.5 Probabilistic 40% random initialisation
### 2.6 Probabilistic 50% random initialisation

## 3. Pipeline should be:

--> Run 256 CA for each different rules.

--> 256 results of elementary CA with 6 different initialisations.

--> Store them and perform analysis.

--> Perform FHCG analysis.

## 4. Analysis should have 
4.1. Test multiple block sizes of coarse graining = 2x1, 3x1, etc
4.2. Test multiple thresholds (need to figure out threshold value based on initial experiments as alpha value is unknown in the paper too (Hugo et. al.))

## Summary

All elementary CA runs of 256 rules: HD/Fine grained CA vs CG CA with a block of 2x1. Having 2x1 coarse grianing on Elementary CA.
Vary with 6 types of initial states Single active cell 1% Active cells with 10%, 20%, 30%, 40% and 50% chances. (Probabilistic initialization as we have in 2D CA) 

Pipeline should be: 256 CA runs on each rules ⇒ 256 results of elementary CA  x 6 (different initializations) ⇒ store them ⇒ Perform Analysis. Performing analysis should have following steps:
Test multiple block sizes of coarse graining (2x1, 3x1 etc)
Test multiple thresholds (need to figure out the threshold values based on initial experiments, as alpha value is unknown in the paper too!)
