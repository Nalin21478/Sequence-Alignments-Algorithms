sequence1=str(input('Enter DNA Sequence 1 : ')) 
sequence2=str(input('Enter DNA Sequence 2 : ')) 
sequence1 = sequence1.upper() 
sequence2 = sequence2.upper()
print('Input the Scoring functions ')
match=int(input('Enter the Points for Match: '))
mis_match=int(input('Enter the Points for Mis-Match: '))
gap=int(input('Enter the Points for Gap: '))



'''Function for Creating and Filling the Matrix'''

def local_alignment_matrix(sequence1, sequence2):
    len1 = len(sequence1)
    len2 = len(sequence2)
    matrix = [[0 for j in range(len1 + 1)] for i in range(len2 + 1)]
    
   
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            diagonal = matrix[i - 1][j - 1]
            if sequence1[j - 1] != sequence2[i - 1]:
                diagonal += mis_match
            else:
                diagonal += match
            matrix[i][j] = max(0,
                matrix[i - 1][j] + gap,  
                matrix[i][j - 1] + gap,  
                diagonal)  
    
    return matrix






def matrix_traceback(i, j, align1, align2, seq1, seq2, matrix, opt_aligns):
    if matrix[i][j] == 0:
        opt_aligns.append((align1, align2))
        return
    
    if i > 0 and matrix[i][j] == matrix[i-1][j] + gap:
        matrix_traceback(i-1, j, '-' + align1, seq2[i-1] + align2, seq1, seq2, matrix, opt_aligns)
        
    if j > 0 and matrix[i][j] == matrix[i][j-1] + gap:
        matrix_traceback(i, j-1, seq1[j-1] + align1, '-' + align2, seq1, seq2, matrix, opt_aligns)
        
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
    
    max_score = 0
    max_i, max_j = 0, 0
    
  
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_i, max_j = i, j
    
    
    matrix_traceback(max_i, max_j, '', '', sequence1, sequence2, matrix, optimal_alignments)
    return optimal_alignments, max_score



mat = local_alignment_matrix(sequence2, sequence1)



optimal_alignments, optimal_score = get_score(sequence2, sequence1, mat)

print("Optimal score:", optimal_score)
print("The total optimal alignments are:",len(optimal_alignments))
for i, alignment in enumerate(optimal_alignments):
    
    print("Alignment", i+1, ":")
    print(alignment[0])
    print(alignment[1])
    print("\n")


