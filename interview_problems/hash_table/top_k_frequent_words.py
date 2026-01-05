from collections import Counter
import heapq
from dataclasses import dataclass,  field
from typing import List

@dataclass
class WordFreq:
    frequency: int
    word: str


    def __eq__(self, other):
        return other.frequency == self.frequency and other.word == self.word

    def __lt__(self, other):
        if self.frequency < other.frequency:
            return True
        if self.frequency == other.frequency and self.word < other.word:
            return True
        return False
    
    def __gt__(self, other):
        if self.frequency > other.frequency:
            return True
        if self.frequency > other.frequency and self.word > other.word:
            return True
        return False


def topKFrequent(words: List[str], k: int) -> List[str]:
    word_freq = Counter(words)
    word_freq_objects = [WordFreq(frequency=-value, word=key) for key, value in word_freq.items()]
    heapq.heapify(word_freq_objects)
    nsmallest = heapq.nsmallest(k, word_freq_objects)
    nsmallest_words = [item.word for item in nsmallest]
    return nsmallest_words

words = ["i","love","leetcode","i","love","coding"]
k = 2
assert topKFrequent(words, k) == ["i","love"]
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
assert topKFrequent(words, k) == ["the","is","sunny","day"]
