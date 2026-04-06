# How To Run

## Using Terminal (Windows / Linux / macOS)
1. Navigate to project folder (**cd [insert path to folder]**)
2. Run the program **python main.py**

## Using Visual Studio Code
1. Open the folder in VS Code
2. Open 'main.py'
3. Click **Run** (▶) or press Ctrl + F5

---

# Output
After running the program, it should output 3 files:
- 'all.txt' -> all numbers
- 'even.txt' -> even numbers only
- 'odd.txt' -> odd numbers only

---

# How To Check Output

## Count Lines
Type into terminal:
- (Get-Content all.txt).Count
- (Get-Content even.txt).Count
- (Get-Content odd.txt).Count

You should get:
- all.txt = 10000
- even.txt + odd.txt = 10000

## Using check.py
Type **python check.py** in terminal or open **check.py** in VSC and press run (▶)

---

# How To Check Running Time

## On Linux/macOS
- Run **time python main.py**

## On Windows (Command Prompt / PowerShell)
- Run **Measure-Command { python main.py }**

---

# Notes
- Buffer is implemented as stack (LIFO)
- Uses threading and condition variables for synchronization