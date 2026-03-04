class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            line = []
            line_len = 0
            while i < len(words) and line_len + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1
            spaces = maxWidth - line_len
            if i == len(words) or len(line) == 1:
                line_str = " ".join(line)
                line_str += " " * (maxWidth - len(line_str))
            else:
                gaps = len(line) - 1
                space_each = spaces // gaps
                extra = spaces % gaps
                line_str = ""
                for j in range(gaps):
                    line_str += line[j]
                    line_str += " " * (space_each + (1 if j < extra else 0))
                line_str += line[-1]
            res.append(line_str)
        return res