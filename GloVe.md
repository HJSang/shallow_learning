# GloVe: Global Vectors for Word Representation

[Paper](https://nlp.stanford.edu/pubs/glove.pdf)

The result is a new global log-bilinear regression model that combines the advantages of the two major model families: **global matrix factorization** and **local context window** methods.

## Notation
* Let the matrix of word-word co-occurrence counts be denoted by **X**. 
* **X_{ij}** is the number of times word j occurs in the context of word i. 
* Let **X_i=\sum_{k} X_{ik}** be the number of times any word appears in the context of word i..
* Let **P_{ij} = P(j|i) = X_{ij}/ X_i** be the probability that word j appear in the context of word i.
* Suggest that the appropriate starting point for word vector learning should be with ratios of co-occurrence probabilities rather than the probabilities themselves.
* w: word vector
* \tilde{w}: separate context word vector

## Objective Function
<img src="http://latex.codecogs.com/gif.latex?1+sin(x)" border="0"/>
