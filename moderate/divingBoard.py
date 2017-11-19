def divingBoard(num_shorter, shorter_length, num_longer, longer_length, k):
    """
    :param shorter:
    :param longer:
    :return:
    """
    res = []
    if num_shorter == 0 and num_longer == 0 : return res
    if shorter_length == longer_length :
        return k*shorter_length if k <= num_longer + num_shorter else 0
    for i in range(0, min(num_shorter, k)+1):
        if num_longer >= (k-i):
            l = i*shorter_length + (k-i)*longer_length
            res.append(l)
    return res


if __name__ == "__main__":
    print divingBoard(3,1,4,2,3)