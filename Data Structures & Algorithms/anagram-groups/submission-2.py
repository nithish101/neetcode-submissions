class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_sets = []
        answer = []
        for word in strs:
            word_set = {}
            for c in word:
                if c in word_set:
                    word_set[c] += 1
                else:
                    word_set[c] = 1
            added = False
            for i, other in enumerate(word_sets):
                if word_set == other:
                    answer[i].append(word)
                    added = True
            if not added:
                word_sets.append(word_set)
                answer.append([word])

        return answer