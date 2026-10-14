class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        scales = ["", "Thousand", "Million", "Billion"]

        def chunk_to_words(n: int) -> list[str]:   
            
            # 0 < n < 1000
            words = []
            if n >= 100:
                words += [below20[n // 100], "Hundred"]
                n %= 100
            if n >= 20:
                words.append(tens[n // 10])
                n %= 10
            if n:
                words.append(below20[n])
            return words

        result = []
        i = 0
        while num:
            chunk = num % 1000
            if chunk:  # skip empty chunks like the 000 in 1,000,000
                part = chunk_to_words(chunk)
                if scales[i]:
                    part.append(scales[i])
                result = part + result
            num //= 1000
            i += 1

        return " ".join(result)
