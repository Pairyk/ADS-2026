def main():
    str_one = input()
    str_two = input()

    if cleaner(str_one) == cleaner(str_two):
         print("Yes")
    else:
         print("No")
    
def cleaner(s):
    new_str = ''

    for i in range(0, len(s)):
            if s[i] == '#' and i != 0:
                new_str = new_str[0:len(new_str)-1]    
            elif s[i] == '#' and i == 0:
                continue
            else:
                new_str += s[i]
    
    return new_str

if __name__ == "__main__":
    main()
    