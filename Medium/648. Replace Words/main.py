class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        new_sent = []
        cur_word = ""
        for c in sentence:
            if c is not " ":
                if cur_word in dictionary: # Found a root
                    continue
                cur_word += c
            else:
                new_sent.append(cur_word)
                new_sent.append(" ")
                cur_word = ""
        new_sent.append(cur_word)
        return "".join(new_sent)
