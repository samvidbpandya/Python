## Python Code to check Palindrome.....
def reverse(palindrome):
    return palindrome[::-1]
 
def isPalindrome(palindrome):
   
    rev = reverse(palindrome)
 
    
    if (palindrome == rev):
        return True
    return False
 
 
palindrome = input(str("Enter Word/Number"))
ans = isPalindrome(palindrome)
 
if ans == 1:
    print("Yes")
else:
    print("No")
