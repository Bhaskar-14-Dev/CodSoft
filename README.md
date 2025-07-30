# Number 1 project

# Rule-Based Chatbot

This is a simple rule-based chatbot implemented in Python . The chatbot demonstrates basic natural language processing and conversation flow using if-else statements and pattern matching to respond to user inputs.

## Features

- Greets the user and says goodbye
- Answers questions about its name and identity
- Tells the current time and date
- Responds to weather-related queries (simulated)
- Recommends travel destinations
- Provides help instructions
- Handles unknown queries gracefully

## How to Run

1. **Install Python**  
   Make sure Python is installed on your computer. Download it from [python.org](https://www.python.org/downloads/) if needed.


2. **Open a Terminal/Command Prompt**  
   - Navigate to the folder where `chatbot.py` is located:
     ```bash
     cd path/to/project-folder
     ```

3. **Run the Chatbot**  
   ```bash
   python chatbot.py
   ```

   > **Note:**  
   > Please run this program in a terminal or command prompt. The VS Code "Run" button or Output panel will not work for interactive scripts that use `input()`.  
   > For best results, use the integrated terminal in VS Code (`Ctrl + \``).

## Example Interaction

```
TravelBot: Hi! I'm your travel assistant chatbot.
Type 'help' to see what I can do. Type 'bye' to exit.
=============================================
You: hello
TravelBot: Hello! How can I help you today? Good afternoon!
You: what is your name?
TravelBot: I'm TravelBot, your friendly travel assistant!
You: recommend me a place
TravelBot: I recommend visiting Paris for its rich culture, Bali for beautiful beaches, or New York for a vibrant city experience. Where would you like to go?
You: bye
TravelBot: Goodbye! Have a wonderful day.
```

## Project Structure

```
chatbot.py      # Main Python script for the chatbot
README.md       # Project documentation and instructions
```

## Author

Bhaskar-14-Dev  
Agniva Bhaskar

---

Feel free to fork this repository or use the code as a starting point for your own rule-based chatbot projects!





# Number 2 project

# Tic-Tac-Toe AI

This project implements an unbeatable AI agent that plays the classic game of Tic-Tac-Toe against a human player in the command line. The AI uses the Minimax algorithm to always make the best possible move, ensuring it never loses. This project is a great introduction to game theory and basic search algorithms.

## Features

- Play Tic-Tac-Toe against an AI that never loses
- Human plays as `X`, AI plays as `O`
- Input moves by entering positions 1-9 (as shown on the board)
- Clear display of the game board after every move
- Handles invalid or occupied moves gracefully
- No external libraries required

## How to Run

1. **Install Python**  
   Make sure you have Python installed. Download it from [python.org](https://www.python.org/downloads/) if you don't have it.


2. **Open a Terminal or Command Prompt**  
   Navigate to the project folder.

3. **Run the Game**
   ```bash
   python tic_tac_toe.ai.py
   ```
   (Use `python3` if your system requires it)

## Board Positions

When prompted for a move, use the following layout to choose your position:

```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

## Example Gameplay

```
Welcome to Tic-Tac-Toe!
You are 'X'. The AI is 'O'.

Board positions:
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9

Let's start!

  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Enter your move (1-9): 1

X |   |  
--+---+--
  |   |  
--+---+--
  |   |  

AI's turn...

X |   |  
--+---+--
  | O |  
--+---+--
  |   |  
```

The game continues until either the human or AI wins, or the game ends in a draw.

## Project Structure

```
tic_tac_toe.ai.py   # Main Python script for the game and AI
README.md           # Project documentation
```

## Concepts Demonstrated

- Minimax algorithm for optimal decision-making
- Game state evaluation
- Turn-based CLI game logic
- Basic user input validation

## Author

Bhaskar-14-Dev  
Agniva Bhaskar

---

*Feel free to use this code as a learning resource or as a base for your own projects!*




# number 3 project

# Recomendation_system 

This is a Python-based recommendation system that suggests **movies or books** to users based on their selected recomendation. The system is simple, interactive, and suitable for educational, internship, or demo projects.

## Features

- Presents a list of genres/emotions for the user to choose from.
- User selects a genre/emotion by number.
- User chooses whether they want recommendations for movies or books.
- Provides a list of recommended movies (with director and release year) or books (with author and published year) matching the selected genre.
- Clean, tabular output for easy readability.

## Sample Genres/Emotions

1. Action Sci-Fi  
2. Animation Comedy Family  
3. Thriller  
4. Animation Adventure Drama  
5. Crime Drama  
6. Action Sci-Fi Thriller  

## Example Usage

```plaintext
Select your emotion/genre of the day:
1. Action Sci-Fi
2. Animation Comedy Family
3. Thriller
4. Animation Adventure Drama
5. Crime Drama
6. Action Sci-Fi Thriller
Enter the number corresponding to your emotion/genre: 2
Would you like recommendations for movies or books? (Enter 'movies' or 'books'): books

Recommended BOOKS for 'Animation Comedy Family':
    Title         Author  Published Year
   Wonder   R.J. Palacio           2012
```

## How to Run

1. **Install Requirements**

   The only requirement is `pandas`. Install it using:
   ```
   pip install pandas
   ```

2. **Run the Script**

   Save the code as `emotion_based_recommendation_system.py` and run:
   ```
   python emotion_based_recommendation_system.py
   ```

## Project Structure

- `emotion_based_recommendation_system.py` &mdash; Main script for the recommendation system.
- `README.md` &mdash; Project documentation.

## Customization

- **Expand the Datasets:**  
  You can easily add more movies or books to the respective datasets in the script.
- **Add More Genres:**  
  Update the `emotions` list to include more genres or emotional categories.
- **Enhance Recommendation Logic:**  
  The current logic is content-based and uses genre matching. You can expand it to include collaborative filtering, user ratings, etc.

## Example Data Shown

**Movies:**  
- Title, Genre, Director, Release Year

**Books:**  
- Title, Genre, Author, Published Year

## License

This project is for educational and demonstration purposes.

---

**Happy recommending!**