def alternate(s):
    # Write your code here
    set_of_char = set([i for i in s])
    two_char = []
    length_of_s = 0
    for a in set_of_char:
        for b in set_of_char:
            if a != b:
                new = [a,b]
                if new not in two_char and new[::-1] not in two_char:
                    two_char.append(new)
    for i in two_char:
        length = [x for x in s if x==i[0] or x==i[1]]
        for j in range(len(length)):
            if j<(len(length)-1):
                if length[j] == length[j+1]:
                    break
            else :
                if length_of_s < len(length):
                    length_of_s = len(length)
    return length_of_s