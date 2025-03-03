def count_upper_lower(s):
    
    upper_count = sum(map(str.isupper, s)) 
    lower_count = sum(map(str.islower, s))  
    return upper_count, lower_count


input_string = input()

upper_count, lower_count = count_upper_lower(input_string)

print(f"Прописные буквы: {upper_count}")
print(f"Строчные буквы: {lower_count}")
