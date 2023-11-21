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
    print(f"Reversed: \n {some_text}:") 
    print_reversed(f"{some_text}")
    print(f"Twice: \n {some_text}:")
    print_twice(f"{some_text}")

if __name__ == "__main__":
    s = input()
    print_reversed(s)
    print_twice(s)
