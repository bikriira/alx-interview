# 0x0A. Prime Game

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.4.3-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Game%20Theory-Advanced-orange.svg" alt="Game Theory">
  <img src="https://img.shields.io/badge/Algorithm-Prime%20Numbers-green.svg" alt="Algorithm">
</p>

## 🎮 Project Overview

The Prime Game is an exciting mathematical challenge where two players, Maria and Ben, engage in a battle of wits using prime numbers. Players take turns selecting prime numbers from a set of consecutive integers, with the player unable to make a move losing the game. 

``` from alx_interviev ```

> *"I thought the Prime Game was hard, but it was so easy that I generated all prime numbers using `def sieve_of_eratosthenes(n)` and if the length of returned prime numbers is odd, then player 2 wins (Ben); otherwise, Maria wins."*

## 🧠 Concepts Needed

To excel in this project, you'll need to understand:

- **Prime Numbers**: Efficient algorithms for identifying and working with primes
- **Sieve of Eratosthenes**: A classic algorithm for finding all prime numbers up to a given limit
- **Game Theory**: Fundamental principles of competitive games and optimal play strategies
- **Dynamic Programming**: Techniques for optimizing solutions by leveraging previous results
- **Python Programming**: Implementing game logic and algorithms using Python's powerful list manipulation capabilities

## 🛠️ Technical Requirements

- **Python Version**: 3.4.3
- **Code Editors**: `vi`, `vim`, `emacs`
- **Style Guide**: Strict adherence to PEP 8
- **Execution**: All files must be executable

## 📚 Tasks

### 0. Prime Game

Implement the Prime Game logic with the following prototype:

```python
def isWinner(x, nums)
```

Description: Determine the winner after x rounds, given an array of integers nums.


<details>
<summary><b>Example Gameplay (click to expand)</b></summary>
Round 1: n = 4

    Available Numbers: [1, 2, 3, 4]
    Maria picks 2 and removes 2, 4
    Remaining: [1, 3]
    Ben picks 3 and removes 3
    Remaining: [1]
    Result: Ben wins (no prime numbers left for Maria)

Round 2: n = 5

    Available Numbers: [1, 2, 3, 4, 5]
    Maria picks 2 and removes 2, 4
    Remaining: [1, 3, 5]
    Ben picks 3 and removes 3
    Remaining: [1, 5]
    Maria picks 5 and removes 5
    Remaining: [1]
    Result: Maria wins (no prime numbers left for Ben)

Round 3: n = 1

    Available Numbers: [1]
    Result: Ben wins (no prime numbers for Maria to choose)

Final Tally

    Maria Wins: 1 round
    Ben Wins: 2 rounds
    Overall Winner: Ben

</details>
🚀 Getting Started

    Clone this repository
    Implement the isWinner function in prime_game.py
    Test your implementation with various inputs
    Optimize your solution for efficiency


<p align="center">

Made with ❤️ by Bikri

</p>
