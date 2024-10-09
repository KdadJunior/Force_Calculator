# def add_max(scores_D):
#     Dct={}
#     for x, y in scores_D.items():
#        Dct[x] = {"scores": y, "maxInt": max(y)}
#     return Dct
#
#
# def add_max(D):
#     D2 = {}
#     for k, v in D.items():
#         D2[k] = {}
#         D2[k]["scores"] = v
#         D2[k]["maxInt"] = max(v)
#     return D2
#
#
# a = add_max({"Nana": [20, 30, 40, 50]})
# print(a)

def match_words(Lst):
    count = 0
    for ch in Lst:
        if len(ch) >= 2 and ch[0] == ch[-1]:
            count += 1
    return count


example_words = ['abc', 'xyz', 'aba', '1221']
match_count = match_words(example_words)
print(match_count)