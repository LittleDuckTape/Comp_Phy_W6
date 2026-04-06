# How To Run

## Using Terminal (Command Prompt / PowerShell)
1. Navigate to project folder (**cd [insert path to folder]**)
2. Run the program using **python main.py**

## Using Virtual Studio Code
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

You should get 10000 for all and (even + odd).

## Using check.py
Run **python check.py** in terminal or VSC

---

# Notes
- Buffer is implemented as stack (LIFO)
- Uses threading and condition variables for synchronization