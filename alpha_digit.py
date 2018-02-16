while True:
    print("Enter '<' to stop :")
    str1=input("Enter a string(isAlpha) : ");
    if str1=='<':
        break
    print(str1.isalpha())
    str1=input("Enter a string(isDigit) : ");
    if str1=='<':
        break
    print(str1.isdigit())
