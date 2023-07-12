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



''' Function for Printing the Matrix '''

def print_matrix(matrix):
    print('The Matrix is as followed')
    for row in matrix:
        for col in row:
            print(str(col).rjust(3), end=' ')
        print()




mat=global_alignment_matrix(sequence2,sequence1)

print_matrix(mat)
