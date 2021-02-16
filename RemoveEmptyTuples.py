def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples


# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))


# # Method 2
# # Python program to remove empty tuples from
# # a list of tuples function to remove empty
# # tuples using filter
# def Remove(tuples):
#     tuples = filter(None, tuples)
#     return tuples
#
#
# # Driver Code
# tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
#           ('krishna', 'akbar', '45'), ('', ''), ()]
# print(Remove(tuples)) 