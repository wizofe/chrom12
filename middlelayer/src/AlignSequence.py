def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval


def smatch(alpha, beta):
    if alpha == beta:
        return match_award
    elif alpha == '-' or beta == '-':
        return gap_penalty
    else:
        return m_penalty


def finalise(align1, align2):
    align1 = align1[::-1]  # reverse sequence 1
    align2 = align2[::-1]  # reverse sequence 2

    i, j = 0, 0

    symbol = ''
    found = 0
    score = 0
    id = 0
    for i in range(0, len(align1)):
        if align1[i] == align2[i]:
            symbol = symbol + align1[i]
            id = id + 1
            score += smatch(align1[i], align2[i])
        elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-':
            score += smatch(align1[i], align2[i])
            symbol += ' '
            found = 0
        elif align1[i] == '-' or align2[i] == '-':
            symbol += ' '
            score += gap_penalty

    id = float(id) / len(align1) * 100


def align_sequence(dna, protein, match_award=10, m_penalty=-5, gap_penalty=-5):
    m, n = len(dna), len(protein)
    score = zeros((m + 1, n + 1))  # DP table
    pointer = zeros((m + 1, n + 1))

    max_score = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score_diagonal = score[i - 1][j - 1] + smatch(dna[i - 1], protein[j - 1])
            score_up = score[i][j - 1] + gap_penalty
            score_left = score[i - 1][j] + gap_penalty
            score[i][j] = max(0, score_left, score_up, score_diagonal)
            if score[i][j] == 0:
                pointer[i][j] = 0
            if score[i][j] == score_left:
                pointer[i][j] = 1  # up
            if score[i][j] == score_up:
                pointer[i][j] = 2  # left
            if score[i][j] == score_diagonal:
                pointer[i][j] = 3  # diagonal
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j]

    align1, align2 = '', ''

    i, j = max_i, max_j

    while pointer[i][j] != 0:
        if pointer[i][j] == 3:
            align1 += dna[i - 1]
            align2 += protein[j - 1]
            i -= 1
            j -= 1
        elif pointer[i][j] == 2:
            align1 += '-'
            align2 += protein[j - 1]
            j -= 1
        elif pointer[i][j] == 1:
            align1 += dna[i - 1]
            align2 += '-'
            i -= 1

    finalise(align1, align2)