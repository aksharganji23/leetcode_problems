class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res="".join(map(str,digits))
        res=int(res)+1
        digits_list = [int(digit) for digit in str(res)]
        return digits_list