# KNN algrorithm 
K-nearest neighbors algorithm (KNN) is a non-parameteric method.
* In KNN classification, an objecti is classified by a plurality vot of the neighbors.
* In KNN regression, the output is the property value for the object. This value is the average of the values of k nearest neighbors.


## Distance Metrics
* Euclidean distance for continuouse variables
* For discrete variables, we can use the **overlap metric**. [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) for text classification.
* The distance metric can be learned with specialized alhorithms. 
  * [Large Margin Nearest Neighbor](https://en.wikipedia.org/wiki/Large_margin_nearest_neighbor).
  * [Neighbourhood components analysis](https://en.wikipedia.org/wiki/Neighbourhood_components_analysis).

## How to select K
  * Larger values of K reduces effect of the noise but make boudaries between classes less distinct.
  * The accuracy of KNN ca be severely degraded by the presence of noisy or irrelavant fetaures. 
  * In binary classification case, it is helpful to choose K to be an odd number.

## The weighted nearest neighbour classifier
  * A common schema is to use **1/d**, d is the distance metric.

## Properties
  * KNN error converges to the Bayes error at the optimal (minimax) rate **O(n^{-4/(d+4)})**.

## Feature extraction & Dimension reduction
  * Dimension reduction and then KNN

## CNN for data reduction 
  * Condensed nearest neighbor (CNN) is an algroithm designed to reduce the data set for KNN.
  * CNN selects the se of prototypes U from the trainning data, such that 1NN with U can classify the examples as accurately as 1NN does with the whole data set.

