def solution(s):
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right + 1])
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)       # For odd-length palindromes
        expand_around_center(i, i + 1)  # For even-length palindromes

    return len(palindromes)


# Examples
#if _name_ == "_main_":
# Example 1
string1 = "ababa"
print("Input:", string1)
print("Expected Output: 5")
print("Your Output:", solution(string1))
print()

# Example 2
string2 = "abc"
print("Input:", string2)
print("Expected Output: 3")
print("Your Output:", solution(string2))
print()

# Example 3
string3 = "aaa"
print("Input:", string3)
print("Expected Output: 6")
print("Your Output:", solution(string3))