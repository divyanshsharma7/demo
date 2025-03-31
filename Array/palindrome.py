def is_palindrome(s):
    s = s.lower()  # Convert to lowercase
    rev = s[::-1]  # Reverse the string using slicing
    return s == rev  # Check if the original and reversed strings are the same

# Example usage
s = "level"
result = is_palindrome(s)

if result:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
