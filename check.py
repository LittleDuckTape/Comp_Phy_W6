def count_lines(file):
    with open(file, "r") as f:
        return sum(1 for _ in f)
    
def check_even(file):
    with open(file, "r") as f:
        return all(int(x.strip()) % 2 == 0 for x in f)
    
def check_odd(file):
    with open(file, "r") as f:
        return all(int(x.strip()) % 2 == 1 for x in f)
    
all_count = count_lines("all.txt")
even_count = count_lines("even.txt")
odd_count = count_lines("odd.txt")

print("all:", all_count)
print("even:", even_count)
print("odd:", odd_count)
print("even + odd:", even_count + odd_count)

print("\neven correct:", check_even("even.txt"))
print("odd correct:", check_odd("odd.txt"))