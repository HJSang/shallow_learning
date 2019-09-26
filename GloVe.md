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
<img src="http://latex.codecogs.com/gif.latex?J=\sum_{i,j=1}^V f(X_{ij}) (w_i^T\tilde{w}_j + b_i+\tilde{b}_j - \log{X_{ij}})^2" border="0"/>

* <img src="http://latex.codecogs.com/gif.latex?f(X)" border="0"/> is a weighting function. <img src="http://latex.codecogs.com/gif.latex?f(x) = (x/x_{max})^{\alpha} \quad \text{if} \quad x< x_{max}" border="0"/>, otherwise f(x)=1.
* <img src="http://latex.codecogs.com/gif.latex? b_i" border="0"/> is a bias for <img src="http://latex.codecogs.com/gif.latex? w_i" border="0"/>.

