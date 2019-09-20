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

## [C++ implementation](https://www.geeksforgeeks.org/k-dimensional-tree/)
```
// A C++ program to demonstrate operations of KD tree 
#include<bits/stdc++.h> 
using namespace std; 

const int k = 2; 

// A structure to represent node of kd tree 
struct Node 
{ 
	int point[k]; // To store k dimensional point 
	Node *left, *right; 
}; 

// A method to create a node of K D tree 
struct Node* newNode(int arr[]) 
{ 
	struct Node* temp = new Node; 

	for (int i=0; i<k; i++) 
	temp->point[i] = arr[i]; 

	temp->left = temp->right = NULL; 
	return temp; 
} 

// Inserts a new node and returns root of modified tree 
// The parameter depth is used to decide axis of comparison 
Node *insertRec(Node *root, int point[], unsigned depth) 
{ 
	// Tree is empty? 
	if (root == NULL) 
	return newNode(point); 

	// Calculate current dimension (cd) of comparison 
	unsigned cd = depth % k; 

	// Compare the new point with root on current dimension 'cd' 
	// and decide the left or right subtree 
	if (point[cd] < (root->point[cd])) 
		root->left = insertRec(root->left, point, depth + 1); 
	else
		root->right = insertRec(root->right, point, depth + 1); 

	return root; 
} 

// Function to insert a new point with given point in 
// KD Tree and return new root. It mainly uses above recursive 
// function "insertRec()" 
Node* insert(Node *root, int point[]) 
{ 
	return insertRec(root, point, 0); 
} 

// A utility method to determine if two Points are same 
// in K Dimensional space 
bool arePointsSame(int point1[], int point2[]) 
{ 
	// Compare individual pointinate values 
	for (int i = 0; i < k; ++i) 
		if (point1[i] != point2[i]) 
			return false; 

	return true; 
} 

// Searches a Point represented by "point[]" in the K D tree. 
// The parameter depth is used to determine current axis. 
bool searchRec(Node* root, int point[], unsigned depth) 
{ 
	// Base cases 
	if (root == NULL) 
		return false; 
	if (arePointsSame(root->point, point)) 
		return true; 

	// Current dimension is computed using current depth and total 
	// dimensions (k) 
	unsigned cd = depth % k; 

	// Compare point with root with respect to cd (Current dimension) 
	if (point[cd] < root->point[cd]) 
		return searchRec(root->left, point, depth + 1); 

	return searchRec(root->right, point, depth + 1); 
} 

// Searches a Point in the K D tree. It mainly uses 
// searchRec() 
bool search(Node* root, int point[]) 
{ 
	// Pass current depth as 0 
	return searchRec(root, point, 0); 
} 

// Driver program to test above functions 
int main() 
{ 
	struct Node *root = NULL; 
	int points[][k] = {{3, 6}, {17, 15}, {13, 15}, {6, 12}, 
					{9, 1}, {2, 7}, {10, 19}}; 

	int n = sizeof(points)/sizeof(points[0]); 

	for (int i=0; i<n; i++) 
	root = insert(root, points[i]); 

	int point1[] = {10, 19}; 
	(search(root, point1))? cout << "Found\n": cout << "Not Found\n"; 

	int point2[] = {12, 19}; 
	(search(root, point2))? cout << "Found\n": cout << "Not Found\n"; 

	return 0; 
} 
```

## [Find Minimum](https://www.geeksforgeeks.org/k-dimensional-tree-set-2-find-minimum/)
 The operation is to find minimum in the given dimension. This is especially needed in delete operation.

 * If dimension of current level is same as given dimension, then required minimum lies on left side if there is left child. 
 * When dimension of current level is different, minimum may be either in left subtree or right subtree or current node may also be minimum. So we take minimum of three and return. This is different from Binary Search tree.

 ```
 // A C++ program to demonstrate find minimum on KD tree 
#include <bits/stdc++.h> 
using namespace std; 

const int k = 2; 

// A structure to represent node of kd tree 
struct Node { 
	int point[k]; // To store k dimensional point 
	Node *left, *right; 
}; 

// A method to create a node of K D tree 
struct Node* newNode(int arr[]) 
{ 
	struct Node* temp = new Node; 

	for (int i = 0; i < k; i++) 
		temp->point[i] = arr[i]; 

	temp->left = temp->right = NULL; 
	return temp; 
} 

// Inserts a new node and returns root of modified tree 
// The parameter depth is used to decide axis of comparison 
Node* insertRec(Node* root, int point[], unsigned depth) 
{ 
	// Tree is empty? 
	if (root == NULL) 
		return newNode(point); 

	// Calculate current dimension (cd) of comparison 
	unsigned cd = depth % k; 

	// Compare the new point with root on current dimension 'cd' 
	// and decide the left or right subtree 
	if (point[cd] < (root->point[cd])) 
		root->left = insertRec(root->left, point, depth + 1); 
	else
		root->right = insertRec(root->right, point, depth + 1); 

	return root; 
} 

// Function to insert a new point with given point in 
// KD Tree and return new root. It mainly uses above recursive 
// function "insertRec()" 
Node* insert(Node* root, int point[]) 
{ 
	return insertRec(root, point, 0); 
} 

// A utility function to find minimum of three integers 
int min(int x, int y, int z) 
{ 
	return min(x, min(y, z)); 
} 

// Recursively finds minimum of d'th dimension in KD tree 
// The parameter depth is used to determine current axis. 
int findMinRec(Node* root, int d, unsigned depth) 
{ 
	// Base cases 
	if (root == NULL) 
		return INT_MAX; 

	// Current dimension is computed using current depth and total 
	// dimensions (k) 
	unsigned cd = depth % k; 

	// Compare point with root with respect to cd (Current dimension) 
	if (cd == d) { 
		if (root->left == NULL) 
			return root->point[d]; 
		return min(root->point[d], findMinRec(root->left, d, depth + 1)); 
	} 

	// If current dimension is different then minimum can be anywhere 
	// in this subtree 
	return min(root->point[d], 
			findMinRec(root->left, d, depth + 1), 
			findMinRec(root->right, d, depth + 1)); 
} 

// A wrapper over findMinRec(). Returns minimum of d'th dimension 
int findMin(Node* root, int d) 
{ 
	// Pass current level or depth as 0 
	return findMinRec(root, d, 0); 
} 

// Driver program to test above functions 
int main() 
{ 
	struct Node* root = NULL; 
	int points[][k] = { { 30, 40 }, { 5, 25 }, 
	{ 70, 70 }, { 10, 12 }, { 50, 30 }, { 35, 45 } }; 

	int n = sizeof(points) / sizeof(points[0]); 

	for (int i = 0; i < n; i++) 
		root = insert(root, points[i]); 

	cout << "Minimum of 0'th dimension is " << findMin(root, 0) << endl; 
	cout << "Minimum of 1'th dimension is " << findMin(root, 1) << endl; 

	return 0; 
} 
```





