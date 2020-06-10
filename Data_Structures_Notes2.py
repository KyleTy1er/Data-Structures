



'''

Garbage Collection: python automatically performs this by checking to see if any piece of memory is unreferenced...
                    in the case of a linked list - when we remove the pointer to a certain point in the list, python's
                    runtime "garbage collector" will see this orphaned element in the list and get rid of it. This
                    only occurs in programming languages with a garbage collection.



Trees: Storing nested data that has both width and depth...
       Your File System is an example of a Tree Data Structure.

       You have the root - and everything under it are "children".
       kind of like a family tree...

       DOM tree - Document Object Model.



Binary Search trees: For every node in the tree, there can be at most TWO children.
                    An organizational rule is that every value to the left of the
                    parent node has to be less than the parent, and every value on the
                    right has to be greater than the parent.
                    What about equal values?
                    1. BST's can just disallow equal values...
                    2. If duplicates are allowed, just pick one side that handles duplicates.
                        - left side handles < values
                        - right side hands >= values
                    As we search for a value we will compare the value to the parent
                    node... this allows us to disregard all the values on one side.
                    And this is repeated as we move down the tree. If the value is
                    greater than the particular parent node we know to move right and
                    disregard left, or vica versa.

                    O(n) vs O(log2 n): when you 1/2 the input size for each comparison.

                    **** Logarithmic is the inverse of exponential ****

                    log2 1,000,000 = 20 in a BST of 1 million elements if you are
                    searching for one thing that will take you at most 20 comparisons.

                    [1,2,4,8,3,5,5] in the case of an array... if we are searching -
                    we have to iterate through each item of the list to find our value.
                    with a binary search tree we can cut down the number of operations
                    necessary to find a value on account of the organizational rule.
                    This is O(n) vs O(log2 n) runtime complexity classification.

                    Input size - what is the total number of things this data structure is storing.
                    what remains to search through?
                    input size depends on context however... for example if we have a sum function
                    that takes in an integer - the input size is just whatever the input is...


1. If there is no root, create the node
2. If there is a root compare the value against the roots value
    if it is less than put it on left side
    if it is greater than or equal to put it on right side
3.


'''