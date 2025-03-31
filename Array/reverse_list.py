# 2️⃣ Reverse a List Without Using .reverse()
# 🔹 Problem: Given a list, reverse it without using Python’s .reverse() method.
# 📌 Example:

# Input: [1, 2, 3, 4, 5]  
# Output: [5, 4, 3, 2, 1]  
# 👉 Hint: Try using a loop or list slicing ([::-1]).


class A:
    def reverse_list(self, num):  # Add 'self' and pass 'num'
        for i in range(len(num) - 1, -1, -1):  # Corrected range
            print(num[i])  # Print elements in reverse order

num = [1, 2, 3, 4, 5]
obj = A()  # Create an object of class A
obj.reverse_list(num)  # Call the function and pass the list

print(f"Reverse order of the given list is: {num[::-1]}")  # Using slicing



