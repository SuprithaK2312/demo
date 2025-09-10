def substring(str):
    unique=''
    substrings=[]
    lengths=[]
    for char in str:
        if char in unique:
            substrings.append(unique)
            unique=''
        if char not in unique:
            unique+=char
    print('Substrings: ',substrings)
    for i in substrings:
        lengths.append(len(i))
    res_length=max(lengths)

    for i in substrings:
        if res_length==len(i):
            longest_substring=i
    print('Longest substring:',longest_substring) 
    print('Length of the longest substring :',res_length)
    
str='abba'
substring(str)
        