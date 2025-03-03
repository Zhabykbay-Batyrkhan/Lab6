def palindrome(s):
    string = ''.join(reversed(s))
    return string


s = input("Напиши слово для проверки палиндрома: ")

string = palindrome(s)
if string == s:
    print("Является палиндромом")
else:
    print("Не является палиндромом")