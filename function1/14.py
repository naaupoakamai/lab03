from functions import volume_ball, polindrom, histogram, guess_the_num


radius = 5
print(f"Volume of a ball with radius {radius}: {volume_ball(radius)}")


word = "А роза упала на лапу Азора"
print(f"Is '{word}' a palindrome? {polindrom(word)}")


histogram([4, 9, 7])


guess_the_num()
