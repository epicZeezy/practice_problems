def numJewelsInStones(jewels: str, stones: str) -> int:
        stones_dict = {}
        for char in stones:
            if char in stones_dict:
                stones_dict[char] += 1
            else:
                stones_dict[char] = 1
        total = 0
        for char in jewels:
            total += stones_dict.get(char, 0)
        return total
assert numJewelsInStones("aA", "aAAbbbb") == 3
assert numJewelsInStones("z", "ZZ") == 0