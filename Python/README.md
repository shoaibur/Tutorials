# Python: Basics
1. Difference between *is* and *==* operators
  * *==* operator checks if the contents are equal, e.g., *x == y* checks if the content/value of *x* is equal to the content/value of *y*, while *is* operator if two objects share the same memory, e.g., *x is y* checks if object ids of *x* and *y* are same (in the memory).
  * If *x = []* and *y = []*, then *x == y* returns *True*, because both are empty list; however, *x is y* returns *False*, because *x* and *y* are allocated in two different locations in the memory, which can be verified using commands: *id(x)* and *id(y)*, which will return two distinct identifiers.
  * If *x = 7* and *y = 7*, then both *x == y* and *x is y* return True. When two objects have fixed content, they are allocated in the same memoroy areas. Here is an example that explains this phenomenon: If *x = [1,2,3]* and *y = x*, then value of *y* is also [1,2,3]. However, if we change an element of *x*, say *x[1] = 5*, then *x* will be [1,5,3], but what's about *y*? In fact, *y* is also [1,5,3], because *x* and *y* share same memory, so changing one will also impact other.

2. Difference between *x = x+1* and *x += 1*
  * Both return same value of x. However, *x += 1* is supposed to be executed in-place (given that x has an __ iadd __ method), while *x = x + 1* gets a new allocation for updated x. 





2. Check if each word in a string begins with a capital letter

3. Capitalize the first character of a string

4. Capitalize the first character of each word in a string


5. Uppercase or lowercase an entire string

6. Check if a string is all uppercase

7. Uppercase first and last character of a string

8. Check if a string is composed of all lower case characters

9. Check if the first character in a string is lowercase


10. Check if a string contains a specific substring

11. Check if a string begins with or ends with a specific character?

12. Check if all characters are whitespace characters

13. Check if a string contains only numbers

14. Check if a string contains only characters of the alphabet

15. Check if all characters in a string are alphanumeric


16. Check if all characters in a string conform to ASCII

17. Encode a given string as ASCII



18. Count the total number of characters in a string

19. Count the number of a specific character in a string


20. Split a string on a specific character

21. When would you use splitlines()?

22. Give an example of using the partition() function


23. Find the index of the first occurrence of a substring in a string

24. Search a specific part of a string for a substring

25. When would you use rfind()?


26. Reverse the string “hello world”

27. Give an example of string slicing

28. Convert an integer to a string

29. Return the minimum character in a string

30. Replace all instances of a substring in a string

31. Remove whitespace from the left, right or both sides of a string

32. Remove vowels from a string

33. Concatenate two strings

34. Join a list of strings into a single string, delimited by hyphens


35. What is an f-string and how do you use it?

36. Interpolate a variable into a string using format()

37. Does defining a string twice (associated with 2 different variable names) create one 

38. Give an example of using maketrans() and translate()

39. What is the effect of multiplying a string by 3?

40. What does it mean for strings to be immutable in Python?

41. Can an integer be added to a string in Python?

