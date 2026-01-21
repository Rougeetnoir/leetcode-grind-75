# s = ' A sentence with whitespace. \n'
# #Strip leading whitespace with lstrip(), trailing whitespace with rstrip(), both with strip().

# print('{}'.format(s.lstrip()))
# #A sentence with whitespace.  \n 
# print('{}'.format(s.rstrip()))
# # A sentence with whitespace.
# print('{}'.format(s.strip()))
# # A sentence with whitespace.

# # To strip characters other than whitespace, pass in the character(s) you want stripped.
# print('{}'.format(s.lstrip(' A')))

# s = "A man, a plan, a canal: Panama"
# res = ''.join(ch.lower() for ch in s if ch.isalnum())


# 我的思路：

# 我先要把string调整成lowercase, 且只有alphanumeric characters
# 我知道有左右两个指针，
# l=0, r=len(s)-1
# 我觉得应该分别对比s[l]和s[r]，如果两者一致
# l + 1, r - 1, 如果不一致，就return false
# 最后如果没有return false, 就return true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(ch.lower() for ch in s if ch.isalnum())
        #左右两个指针l r
        r = len(res) - 1
        for l in range(len(res)):
            if res[l] == res[r]:
                r -= 1
            else:
                return False
        return True
    
