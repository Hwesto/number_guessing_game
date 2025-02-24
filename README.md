# 🎲 Number Guessing Game - Higher-Lower Casino Edition 🎰

A **command-line number guessing game** where you wager your funds and try to guess the house number between **1 and 100**.  
If you guess incorrectly, you **lose a quarter of your stake**. Guess correctly, and you **double your bet**!  

💵 **Bet wisely, track your high score, and test your luck!**

---

## 📦 Features

✅ Higher or lower guess feedback  
✅ Betting system with adjustable stakes  
✅ **Persistent high scores** saved across sessions  
✅ Clear user prompts with **input validation**  
✅ Dynamic advice based on guess proximity  
✅ Friendly CLI interface with visual banners  

---

## 🚀 Getting Started

### 🔧 Prerequisites

- **Python 3.7+** installed on your system  
- Git (optional for cloning)  

Check your Python version:

```bash
python --version
```

🛠️ Installation
Clone the repository (or download as ZIP):

```
bash
git clone https://github.com/your-username/number_guessing_game.git
cd number_guessing_game
```
Run the game:
```
bash
python main.py
```
💻 Usage
Launch the game:
```
bash
python main.py
```

Follow the prompts:

- Enter your bet amount (must be within your current balance).
- Guess a number between 1 and 100.
- Enter 0 at any guess to quit the round and retain your current stake.
- If your guess is wrong, you’ll receive advice (e.g., "guess higher, you're less than 40 away").
- If your guess is correct, you double your stake!
- High scores are saved automatically after each round.

🎮 Gameplay Example
```
plaintext

**********************************
*                                *
*    WELCOME TO HIGHER-LOWER!    *
*  Guess the number to WIN BIG   *
*                                *
**********************************

It's between 1 and 100, every time you guess wrong you lose a quarter of your stake, every time you win your bet doubles!

Current High Score: $200

Current Balance: $100
Would you like to play a round?

Y/N? Y

How much do you want to bet? $50

Number of Guesses Completed: 0
Take a guess... 45

You need to guess higher, you're less than 40 away!
You lost a quarter! Current Stake: $37.5

Number of Guesses Completed: 1
Take a guess... 67

🎉 You did it! You won $75.0
New high score: $175.0
```

🏆 Project Structure
```
plaintext

number_guessing_game/
├── main.py         # Main game logic
├── highscore.csv   # Stores persistent high score
├── README.md       # Project documentation
└── .gitignore      # (optional) Ignore unnecessary files
```

🌟 Features Overview

✅ Betting System
Start with $100.
Lose 25% of your stake on wrong guesses.
Win double your stake on a correct guess.

✅ High Score Persistence
High scores are saved in highscore.csv.
Scores persist between game sessions.

✅ Input Validation
Prevents invalid bets or guesses.
Accepts only numbers between 1 and 100 for guesses.

✅ User-Friendly Interface
Text-based banner and clear instructions.
Delays for improved pacing and suspense.

🌱 Future Improvements
 Add a leaderboard with multiple player names.
 Implement difficulty levels (e.g., wider guessing range).
 Introduce betting odds and multipliers.
 Save player stats across sessions.

📄 License
This project is unlicenced.



🙌 Author
Made with ❤️ by Hwesto
