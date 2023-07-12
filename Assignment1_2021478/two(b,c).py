sequence1=str(input('Enter DNA Sequence 1 : ')) 
sequence2=str(input('Enter DNA Sequence 2 : ')) 
sequence1 = sequence1.upper() 
sequence2 = sequence2.upper()
print('Input the Scoring functions ')
match=int(input('Enter the Points for Match: '))
mis_match=int(input('Enter the Points for Mis-Match: '))
gap=int(input('Enter the Points for Gap: '))




'''Function for Creating and Filling the Matrix'''

def global_alignment_matrix(sequence1, sequence2):
    len1 = len(sequence1) + 1
    len2 = len(sequence2) + 1
    
    
    matrix = [[0] * len1 for _ in range(len2)]
    
    
    for i in range(1, len2):
        matrix[i][0] = matrix[i-1][0] + gap
    for j in range(1, len1):
        matrix[0][j] = matrix[0][j-1] + gap
    
    
    for i in range(1, len2):
        for j in range(1, len1):
            match_score = match if sequence1[j-1] == sequence2[i-1] else mis_match
            diagonal = matrix[i-1][j-1] + match_score
            up = matrix[i-1][j] + gap
            left = matrix[i][j-1] + gap
            matrix[i][j] = max(diagonal, up, left)
    
    return matrix










def matrix_traceback(i, j, align1, align2, seq1, seq2, matrix, opt_aligns):
    if i == 0 and j == 0:
        opt_aligns.append((align1, align2))
        return
    
    if i > 0 and matrix[i][j] == matrix[i-1][j] + gap:
        matrix_traceback(i-1, j, '-' + align1, seq2[i-1] + align2, seq1, seq2, matrix,  opt_aligns)
        
    if j > 0 and matrix[i][j] == matrix[i][j-1] + gap:
        matrix_traceback(i, j-1, seq1[j-1] + align1, '-' + align2, seq1, seq2, matrix,  opt_aligns)
        
    if i > 0 and j > 0:
        if seq1[j-1] == seq2[i-1]:
            diag_score = matrix[i-1][j-1] + match
        else:
            diag_score = matrix[i-1][j-1] + mis_match
        if matrix[i][j] == diag_score:
            matrix_traceback(i-1, j-1, seq1[j-1] + align1, seq2[i-1] + align2, seq1, seq2, matrix, opt_aligns)


def get_score(sequence1, sequence2, matrix):
    len1 = len(sequence1)
    len2 = len(sequence2)
    optimal_alignments = []
    
    matrix_traceback(len2, len1, '', '', sequence1, sequence2, matrix, optimal_alignments)
    optimal_score = matrix[len2][len1]
    return optimal_alignments, optimal_score

mat = global_alignment_matrix(sequence2, sequence1)



optimal_alignments, optimal_score = get_score(sequence2, sequence1, mat)

print("Optimal score:", optimal_score)
print("The total optimal alignments are:",len(optimal_alignments))
for i, alignment in enumerate(optimal_alignments):
    
    print("Alignment", i+1, ":")
    print(alignment[0])
    print(alignment[1])
    print("\n")

