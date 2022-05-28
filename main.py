# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from multiprocessing import Condition


def is_anagram(a, b):
   str1=a.replace(" ", "")
   str2=b.replace(" ", "")   
   if (sorted(str1) == sorted(str2)):
      return True
   else:
      return False
print(is_anagram('break', 'rear')) 