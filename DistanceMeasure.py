from math import sqrt
from decimal import Decimal
my_decimal=3
def euclidean(x, y):
    distance = 0
    for a, b in zip(x, y):
        distance += (sum([(pow((a-b),2))]))
    return round(sqrt(distance),my_decimal)
print("Euclidean Distance between [1,3,4,1],[3,2,1,1]:",euclidean([1,3,4,1],[3,2,1,1]))
def manhattan(x, y):
    distance=0
    for a,b in zip(x,y):
        distance += sum([abs(a-b)])
    return round(distance,my_decimal)
print("Manhattan Distance between [1,3,4,1],[3,2,1,1]:",manhattan([1,3,4,1],[3,2,1,1]))

# Function distance between two points
# and calculate distance value to given
# root value(p is root value)
def p_root(value, root):
    root_value = 1 / float(root)
    return round (Decimal(value) **
             Decimal(root_value), my_decimal)
def minkowski_distance(x, y, p_value):
    # pass the p_root function to calculate
    # all the value of vector parallelly
    return (p_root(sum(pow(abs(a-b), p_value)
            for a, b in zip(x, y)), p_value))
 
for x in range(6):
    p=x+1
    print(f"Minkowski Distance between [1,3,4,1],[3,2,1,1] when p={p}",minkowski_distance([1,3,4,1],[3,2,1,1], p))

def cosine_similarity(x,y):
    numerator = 0
    sum_x = 0
    sum_y = 0
    for a,b in zip(x,y):
        numerator += sum([a * b])
        sum_x += sum([a**2])
        sum_y += sum([b**2])
    denominator = sqrt(sum_x) * sqrt(sum_y)
    return round(numerator / denominator, my_decimal)
print("Cosine Similarity between [1,3,4,1],[3,2,1,1]:", cosine_similarity([1,3,4,1],[3,2,1,1]))

def jaccard_similarity(x,y):
    intersection = len(set(x).intersection(set(y)))
    union = len(set(x).union(set(y)))
    return round(intersection / union, my_decimal)
print("\nJaccard Similarity between [0,1,2,5,6] and [0,2,3,4,5,7,9]:",jaccard_similarity([0,1,2,5,6], [0,2,3,4,5,7,9]))
print("Jaccard Distance between [0,1,2,5,6] and [0,2,3,4,5,7,9]:", 1-jaccard_similarity([0,1,2,5,6],[0,2,3,4,5,7,9]))
def chebyshev_distance(point1, point2):
     distance = 0.0
     dimension = len(point1)
     for i in range(dimension):
         distance = max(distance, abs(point1[i] - point2[i]))
     return round(distance, my_decimal)
print("\nChebyshev Distance between [1,3,4,1],[3,2,1,1]:",chebyshev_distance([1,3,4,1],[3,2,1,1]))


def canberra_distance(point1, point2):
     distance = 0.0
     for i in range(len(point1)):
         divider = abs(point1[i]) + abs(point2[i])
         if divider == 0.0:
             continue
  
         distance += abs(point1[i] - point2[i]) / divider
  
     return round(distance, my_decimal)
print("Canberra Distance between [1,3,4,1],[3,2,1,1]:",canberra_distance([1,3,4,1],[3,2,1,1]))

# Return the Hamming distance between string1 and string2.
# string1 and string2 should be the same length.
def hamming_distance(string1, string2): 
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance
example_dist = hamming_distance("GATTACA", "GACTATA")
print(f"Hamming Distance between 'GATTACA' and 'GACTATA': {example_dist}")
