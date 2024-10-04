#!/usr/bin/python3
"""
Prime Game Module

This module contains functions to simulate a game where two players, Maria and Ben,
take turns picking prime numbers from a set of consecutive integers. The game 
is played over multiple rounds, and the module includes functions for generating 
prime numbers and determining the winner.

Functions:
    sieve_of_eratosthenes(n): Generates prime numbers up to a given number `n`.
    isWinner(x, nums): Determines the winner of the Prime Game after `x` rounds.
"""


def sieve_of_eratosthenes(n):
    """
    Generate prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for generating primes.

    Returns:
        list: A list of prime numbers up to n.
    """
    if n <= 0:
        return [0]
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game for multiple rounds.

    The game involves two players, Maria and Ben, taking turns choosing
    prime numbers from a set of consecutive integers. The player who 
    cannot make a move loses the game.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers representing the maximum number 
                     for each round.

    Returns:
        str: The name of the player who won the most rounds 
             ('Maria' or 'Ben'), or None if it's a tie.
    """
    wins = []
    for round in range(x):
        # If the count of primes is even, Ben wins; otherwise, Maria wins
        if len(sieve_of_eratosthenes(nums[round])) % 2 == 0:
            wins.append("Ben")
        else:
            wins.append("Maria")

    # Return the player with the most wins
    return max(wins, key=wins.count) if wins else None
