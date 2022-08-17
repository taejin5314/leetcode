class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashMap = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
            
        seen = set()
        for word in words:
            newList = []
            for code in word:
                newList.append(hashMap[code])
            seen.add(''.join(newList))

        return len(seen)