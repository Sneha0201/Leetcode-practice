class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 0:
            return ""
        n = len(encodedText)
        cols = n // rows
        result = []
        for start in range(cols):
            r = 0
            c = start
            while r < rows and c < cols:
                result.append(encodedText[r * cols + c])
                r += 1
                c += 1
        return "".join(result).rstrip()