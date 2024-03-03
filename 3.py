def pal(text):
    if len(text) == 1 or len(text)==0:
    #if len(text) == 1 or text[0]==text[-1]:
    #if len(text) <= 1:
        print("Palindrome")
    else:
        if text[0] == text[-1]:
            pal(text[1:-1])
        else:
            print("Not a palindrome")

pal("madam")
pal("python")
pal("abba")