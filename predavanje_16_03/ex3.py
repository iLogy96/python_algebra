def lcs(pattern_1, pattern_2, len_1, len_2):
    if len_1 == 0 or len_2 == 0:
        return 0
    if pattern_1[len_1 - 1] == pattern_2[len_2 - 1]:
        return 1 + lcs(pattern_1, pattern_2, len_1 - 1, len_2 - 1)
    else :
        return max(lcs(pattern_1, pattern_2, len_1 - 1, len_2), lcs(pattern_1, pattern_2, len_1, len_2 - 1))
pattern_1 = "RGBGARGA"
pattern_2 = "BGRARG"
print("Lenght of LCS is: ", lcs(pattern_1, pattern_2, len(pattern_1), len(pattern_2)))