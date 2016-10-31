import numpy as np


# Matrix for transition probability of 26 characters
M = np.array([[0] * 26] * 26)


# input file from user
file_name = raw_input("Enter the file name")
file_object = open(filename,'r')

# taking input text from the file
input_text = file_object.read()

# removing the whitespaces
input_text.replace(" ","")

#splitting the replaced input text into individual characters
formed_list = list(input_text)


#Counting the frequency of transition from each alphabet to every other alphabet using transition matrix
for i in range(len(formed_list) - 1) :
	x,y = formed_list[i],formed_list[i+1]
	M[ord(x) - 97,ord(y)-97] += 1

counter = []

# calculating the sum of each row
for i in range(len(e)) :
	counter.append(e[i].sum())

# Matrix of probabilities
P = np.array([[0] * 26] * 26)

# entering the values of probabilitles in the matrix
for i in range(26):
	for j in range(26):
		if counter[i] != 0:
			P[i,j] = M[i,j] / counter[i]
		
		
		



