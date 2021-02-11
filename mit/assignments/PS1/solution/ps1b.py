###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    if not egg_weights or target_weight < 0:
        # weight limit exceeded
        return None
    elif target_weight == 0:
        # use this egg
        return 1
    elif egg_weights[-1] > target_weight:
        # right branch: do not take egg
        return dp_make_weight(egg_weights[:-1], target_weight, memo)
    else:
        # left branch: take egg
        next_item = egg_weights[-1]
        # use all egg_weights
        left = dp_make_weight(egg_weights, target_weight - next_item)

        # right branch: egg to big
        right = dp_make_weight(egg_weights[:-1], target_weight)

        if left is None:
            return right
        elif right is None:
            return left
        elif left < right:
            return left+1
        else:
            return right+1

        

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # egg_weights = (1, 5, 10, 25)
    egg_weights = (1, 5)
    n = 6
    print(f"Egg weights = {egg_weights}")
    print(f"n = {n}")
    # print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
