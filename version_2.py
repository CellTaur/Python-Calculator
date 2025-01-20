# A fancier version of my program with some vulnerabilities present ;(

# Probably too complicated but that was my first thought, made in a minute :3
print(f"Result: {eval(f'{input("Number 1: ")}{input("Operation: ")}{input("Number 2: ")}', {'__builtins__': None}, {})}")
