def ChkVowel(ch):
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print("It is Vowel")
    else:
        print("It is Consonant")

def main():
    char = input("Enter Character: ")
    
    ChkVowel(char)
    
if __name__ == "__main__":
    main()