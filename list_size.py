import sys
data=[]

for k in range(20):
# provides getsizeof function
# NOTE: must fix choice of n # number of elements
# actual size in bytes
    a = len(data)
    b = sys.getsizeof(data)
    print( 'Length: {0:3d}; Size in bytes: {1:4d} '.format(a, b))
    data.append(None)
