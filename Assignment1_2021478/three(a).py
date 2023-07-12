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
    
    # Fill the matrix
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




''' Function for Printing the Matrix '''

def print_matrix(matrix):
    print('The Matrix is as followed')
    for row in matrix:
        for col in row:
            print(str(col).rjust(3), end=' ')
        print()




mat=local_alignment_matrix(sequence2,sequence1)

print_matrix(mat)
