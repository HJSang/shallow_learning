# KD Tree
* [Wiki Source](https://en.wikipedia.org/wiki/K-d_tree) for summary.
* [geeksforgeeks](https://www.geeksforgeeks.org/k-dimensional-tree/) for implementation.

## k-d tree
* A k-d tree is a space partitioning data structure for organizing points in a k-dimensional space.
* Useful for range searches and nearest neighbor searhes.

## Construction 
```
function kdtree (list of points pointList, int depth)
{
    // Select axis based on depth so that axis cycles through all valid values
    var int axis := depth mod k;

    // Sort point list and choose median as pivot element
    select median by axis from pointList;

    // Create node and construct subtree
    node.location := median;
    node.leftChild := kdtree(points in pointList before median, depth+1);
    node.rightChild := kdtree(points in pointList after median, depth+1);
    return node;
}
```

## Adding elements
* First, traverse the tree, starting from the root and moving to either the left or the right child depending on whether the point to be inserted is on the "left" or "right" side of the splitting plane.
* Once you get to the node under which the child should be located, add the new point as either the left or right child of the leaf node, again depending on which side of the node's splitting plane contains the new node.

## Removing elements
Find a replacement for the point removed. First, find the node R that contains the point to be removed. For the base case where R is a leaf node, no replacement is required. For the general case, find a replacement point, say p, from the subtree rooted at R. Replace the point stored at R with p. Then, recursively remove p.

For finding a replacement point, if R discriminates on x (say) and R has a right child, find the point with the minimum x value from the subtree rooted at the right child. Otherwise, find the point with the maximum x value from the subtree rooted at the left child.

## Nearest neighbour search
Searching for a nearest neighbour in a k-d tree proceeds as follows:

* Starting with the root node, the algorithm moves down the tree recursively, in the same way that it would if the search point were being inserted.
* Once the algorithm reaches a node, it checks that node point and if the distance is better, that node point is saved as the "current best".
* The algorithm unwinds the recursion of the tree, performing the following steps at each node:
  * If the current node is closer than the current best, then it becomes the current best.
  * The algorithm checks whether there could be any points on the other side of the splitting plane that are closer to the search point than the current best. 
  * If the hypersphere crosses the plane, there could be nearer points on the other side of the plane, so the algorithm must move down the other branch of the tree from the current node looking for closer points, following the same recursive process as the entire search.
  * If the hypersphere doesn't intersect the splitting plane, then the algorithm continues walking up the tree, and the entire branch on the other side of that node is eliminated.
* When the algorithm finishes this process for the root node, then the search is complete.



