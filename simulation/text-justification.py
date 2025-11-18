class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            last = i+1
            line_len = len(words[i])

            while last<len(words) and line_len + 1 + len(words[last]) <= maxWidth:
                line_len += len(words[last]) + 1
                last += 1
            
            line_words = words[i:last]
            gap = len(line_words)-1

            if gap == 0 or last == len(words):
                line =" ".join(line_words)
                pad = maxWidth - len(line)
                line += " "*pad
            else:
                total_sum = 0
                for k in range(len(line_words)):
                    total_sum+=len(line_words[k])
                each_pad = (maxWidth-total_sum)//gap
                more_pad = (maxWidth-total_sum)%gap
                line=""
                for m in range(gap):
                    if m<more_pad:
                        line+=line_words[m]+" "*(each_pad+1)
                    else:
                        line+=line_words[m]+" "*(each_pad)
                line+=line_words[-1]
            res.append(line)
            i = last
        return res