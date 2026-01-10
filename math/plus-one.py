class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = ''.join(map(str, digits))
        num = int(new)
        return list(map(int, str(num+1)))