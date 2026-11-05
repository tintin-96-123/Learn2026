# This is an infinite loop!
while True:
1 print("\nPlease tell me your name:")
f_name = input("First name: ")
l_name = input("Last name: ")
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")