# Higher Lower Game

A Python implementation of the classic "Higher Lower" game where players compare follower counts of famous personalities and guess which has more.

---

## **How to Play**

1. **Objective**: Guess which account has more followers on social media.
2. **Setup**:
   - The program randomly selects two accounts.
   - Details about the accounts (name, description, and country) are displayed.
3. **Gameplay**:
   - Type `A` if you think the first account has more followers.
   - Type `B` if you think the second account has more followers.
   - If your guess is correct, your score increases, and the game continues.
   - If incorrect, the game ends, displaying your final score.

---

## **Features**

- **Randomized Account Selection**:
  - Ensures diverse and engaging gameplay.
  - Prevents repeated accounts in consecutive rounds.

- **Dynamic User Interaction**:
  - Displays account details with clear formatting.
  - Provides immediate feedback on guesses.

- **Scoring System**:
  - Tracks and displays scores after each correct guess.
  - Ends the game when an incorrect guess is made.

---

## **How to Run**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/higher-lower-game.git

2. Navigate to the project directory:
   ```bash
   cd higher-lower-game

3.	Run the game:
   ```bash
   python higher_lower_game.py
