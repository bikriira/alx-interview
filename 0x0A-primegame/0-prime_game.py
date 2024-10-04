def sieve_of_eratosthenes(n):
    """Generate prime numbers up to n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]


def isWinner(x, nums):
    # print("dieve len:", sieve_of_eratosthenes(nums[0]))
    wins = []
    for round in range(x):
        # print(len(sieve_of_eratosthenes(nums[round])))
        if len(sieve_of_eratosthenes(nums[round])) % 2 == 0:
            # print("Ben")
            wins.append("Ben")
        else:
            # print("Maria")
            wins.append("Maria")
        # primes = list(range(1, nums[round] + 1))

        # def rem_multiples(numbers, player):

        #     if len(numbers) == 1 and numbers[0] == 1:
        #         return not player
        #     for i in range(len(primes)):
        #             base_num = numbers[i]
        #             # Use a list comprehension to create a new list without multiples
        #             numbers = [num for num in numbers if num % base_num != 0]
        #             return rem_multiples(numbers, not player)
        #     # This line should be outside the for loop
        #     return rem_multiples(numbers, not player)

        # winner = rem_multiples(numbers, True)
        # wins.append(winner)

    # Convert boolean wins to player names
    # parsed_wins = ["Ben" if not x else "Maria" for x in wins]
    return max(wins, key=wins.count)
