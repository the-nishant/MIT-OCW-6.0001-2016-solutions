# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if(len(sequence)==1):
        return [sequence]
    else:
        permutations = []
        letter = sequence[0]
        for word in get_permutations(sequence[1:]):
            permutations.append(letter+word)
            for i in range(len(word)):
                new_word = list(word)
                new_word.insert(i+1, letter)
                new_word = ''.join(new_word)
                if new_word not in permutations:
                    permutations.append(new_word)
        return permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    test1 = '1'
    print('Input:', test1)
    print('Expected Output:', ['1'])
    print('Actual Output:', get_permutations(test1))

    test2 = '121'
    print('Input:', test2)
    print('Expected Output:', ['121', '211', '112'])
    print('Actual Output:', get_permutations(test2))

    test3 = '123'
    print('Input:', test3)
    print('Expected Output:', ['123','213', '231', '132', '312', '321'])
    print('Actual Output:', get_permutations(test3))

