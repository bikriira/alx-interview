#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

# Test Case 1: Basic test with mixed values
print("Winner: {}".format(isWinner(3, [20, 5, 1])))  # Expected Output: Ben

# Test Case 2: Single round with small n
print("Winner: {}".format(isWinner(1, [2])))  # Expected Output: Maria

# Test Case 3: Single round with no primes
print("Winner: {}".format(isWinner(1, [1])))  # Expected Output: Ben

# Test Case 4: Several rounds with different n values
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected Output: Ben

# Test Case 5: Larger n to test performance
print("Winner: {}".format(isWinner(2, [100, 200])))  # Expected Output: (depends on game logic, likely Maria or Ben)

# Test Case 6: All n equal to 1
print("Winner: {}".format(isWinner(4, [1, 1, 1, 1])))  # Expected Output: Ben

# Test Case 8: Very large n to test upper bound
print("Winner: {}".format(isWinner(1, [10000])))  # Expected Output: (depends on game logic, likely Maria or Ben)
