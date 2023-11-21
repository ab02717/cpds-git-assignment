def print_reversed(s):
    reversed = []
    for item in range(len(s)-1,-1,-1):
        reversed.append(s[item])
    print(''.join(reversed))

def print_twice(s):
    s+=s
    print(s)

def print_header(some_text):
    absa_ascii_art ="""

               ____   _____         
         /\   |  _ \ / ____|  /\    
        /  \  | |_) | (___   /  \   
       / /\ \ |  _ < \___ \ / /\ \  
      / ____ \| |_) |____) / ____ \ 
     /_/    \_\____/|_____/_/    \_\
     
    """
    print(f"\n {absa_ascii_art} \nNow printing the some text reversed and twice")
    print(f"Reversed: ") 
    print_reversed(f"{some_text}")
    print(f"Twice: ")
    print_twice(f"{some_text}")

if __name__ == "__main__":
    s = input("Input string to manipulate: ")
    #print_reversed(s)
    #print_twice(s)
    print_header(s)
