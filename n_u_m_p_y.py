#  __________________-----------------num py module: --------------:

# NumPy is a Python library used for working with arrays.

# It also has functions for working in domain of linear algebra, fourier transform, and matrices.

# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

# NumPy stands for Numerical Python.

# why use python: 

# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.



import numpy as np  # we can set alias name : 
# 
# # # numpy array list :

# dnarray = np.array([1,2,3,4,5,6])# numpy list :

# print("\nthis is numpy list array : ",end=" ")
# print(dnarray , "\n ")

# arr  = np.array([1,2,3,4,3,3])
# print(type(arr)) # this is to check the type of array 
# print(arr.dtype) # this is the data type of array 
# print(arr)# this is arr np.array list 
# print(len(arr))

# # to check numpy version : 

# print("num py version :", np.__version__ , "\n") # for finding out the version of your numpy 
# print("numpy version is  :", np.__version__)


# #normal array list : 
# array = [1,2,34,5]# a normal list : 
# print("this is a normal list see the diffrence : \n ")
# print(array , "\n ")

# ---------------creating arrays (): ----------:

# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

# arr = np.array([1,21,3,4,5,6,7])

# print("\n",arr, "\n")
# print(type(arr))

# To create an ndarray, we can pass a list, tuple or any array-like object into
 
# the array() method, and it will be converted into an ndarray:

# ar = np.array((1,21,3,4,5,6,7)) # tupple form array also will be converted in to ndarray form 
# arr = np.array({"harry":"marry", "darry":"larry"})
# print(arr)
# print("\n",arr, "\n")

#A dimension in arrays is one level of array depth (nested arrays).

# nested array: are arrays that have arrays as their elements.

# 0-D arrays : ----------------- 

# d0 = np.array(42)

# print(d0)

# 1-d Arrays : -------------

# A dimension in arrays is one level of array depth (nested arrays).

# nested array: are arrays that have arrays as their elements.

# d1 = np.array([1,2,3,4,5])

# print(d1)

# # 2-d Arrays : -------------

# d2 = np.array([[1,2,3],[4,5,6]])

# print(d2)

# 3-d Arrays : -------------

# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

# These are often used to represent a 3rd order tensor.

# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(d.shape)

# Check Number of Dimensions?

# NumPy Arrays provides the ndim attribute that returns an integer that 

# tells us how many dimensions the array have.
# d0 = np.array(42)
# d1 = np.array([1,2,3,4,5])
# d2 = np.array([[1,2,3],[4,5,6]])
# d3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

# print(d0, "dimesions number:" , d0.ndim) # to check the number of dimensions : 
# print(d1, "dimesions number:" , d1.ndim)
# print(d2, "dimesions number:" , d2.ndim)
# print(d3, "dimesions number:" , d3.ndim)

# to change the dimensions of ones arrays : --------

# When the array is created, you can define the number of dimensions by using the ndmin argument.

# arr = np.array([1, 2, 3, 4], ndmin=2) 
# print(arr)

# ab = np.array([1,2,3,5], ndmin=5)
# print(ab , "number of dimension " , ab.ndim)

# ----------------------NumPy Array Indexing------------:

# Access Array Elements

# Array indexing is the same as accessing an array element.

# You can access an array element by referring to its index number.

# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

# array indexing : 
# var = np.array([2,3,45,3,4])

# print(var[2])

# get more than one index : 

# var2 = np.array([2,3,45,3,4])

# print(var2[2], var2[4])

# Get third and fourth elements from the following array and add them.

# var3 = np.array([2,3,45,3,4])

# print(var3[2] + var3[4]) 
    
# To access elements from 2-D arrays we can use comma separated 

# integers representing the dimension and the index of the element.

# Think of 2-D arrays like a table with rows and columns, where the
#  dimension represents the row and the index represents the column.

# var24 = np.array([[2,3,56,354,34],[2,34,5,34,24]])

# print("first row second column is  : ",var24[0,1])

# Access the element on the 2nd row, 5th column:

# var24 = np.array([[2,3,56,354,34],[2,34,5,34,24]])

# print("second row 5th  column is  : ",var24[1,4])

# -----------------Access 3-D Arrays------:

# To access elements from 3-D arrays we can use comma separated integers
#  representing the dimensions and the index of the element.

# var23 = np.array([[[2,3,77,354,34],[2,34,78,34,24]],[[2,3,56,4334,34],[2,34,5,45,56]]])

# print("the value should be 78 : ",var23[0,1,2])

# Negative Indexing: -----------
# Use negative indexing to access an array from the end.

# operation on first row : 
# var21 = np.array([[2,3,56,354,34],[2,34,5,34,24]])
# print(var21[1,-1]) # second row last column because negative sign 

# operation on second row : 
# var20 = np.array([[2,3,56,354,34],[2,34,5,34,24]])
#  print(var20[0,-1]) first row last column because negative sign 


# --------------------------NumPy Array Slicing-----------:

# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

# If we don't pass start its considered 0

# If we don't pass end its considered length of array in that dimension

# If we don't pass step its considered 1

# arr = np.array([1,2,3,4,5,6])

# print("sliciing from 1 to 5  :",arr[1:5]) # The result includes the start index, but excludes the end index

# #Slice elements from index 4 to the end of the array:
# arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11])
# print("slicing from 4 to end : ",arr2[4:])# If we don't pass end its considered length of array in that dimension

# arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11])
# print(" slicing form 0 to 4  :", arr3[:4]) # Slice elements from the beginning to index 4 (not included):

# Negative Slicing--------
# Use the minus operator to refer to an index from the end:


# End Index: The -end_index specifies the starting point for the slice, counting from the 
# end of the array. It refers to the element that will be included in the slice. -1 represents
#  the last element, -2 represents the second-to-last element, and so on.

# Start Index: The -start_index specifies the ending point for the slice, 
# counting from the end of the array. It refers to the element that will not
#  be included in the slice. -1 represents the last element, -2 represents the second-to-last element, and so on.

# Slicing Direction: The slice goes from the element specified by -end_index 
# to the element just before -start_index. The result includes the element at -end_index and
#  excludes the element at -start_index.

# ab = np.array([1,2,4,3,5,3,9])
# print(ab[-6:-2])

# --------Step--------():

# In slicing, the step is an optional parameter that controls the increment between elements in the slice.
#  It allows you to skip elements when slicing an array or sequence.
#  The step is specified using the colon : as part of the slicing syntax. Here's the general syntax:


# start:stop:step
# start: The index at which the slice begins.
# stop: The index at which the slice ends (not inclusive).
# step: The step or increment to skip elements.
# By default, if you omit the step in slicing, it is assumed to be 1, which means that you include every element 
# from the start to the end. However, you can use the step to skip elements by specifying a value other than 1.

#Return every other element from index 1 to index 5:
# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])

# #Return every other element from the entire array:
# arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr2[::2])

# examples of simple slicing :------
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Slicing with a step of 2, which selects every other element
# result1 = my_list[0:10:2]
# print("slicing with a step of 2 :",result1)

# # Result: [0, 2, 4, 6, 8]

# # Slicing with a negative step, which reverses the order
# result2 = my_list[::-1]
# print("this method reverse the order :",result2)

# # Result: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# # Slicing with a step of 3 starting from index 2
# result3 = my_list[2::3]
# print("slicing with a step of 3: ",result3)
# # Result: [2, 5, 8]

# result4 = my_list[::2]
# print("this is result 4 ", result4)



# Slicing 2-D Arrays---------

# , is used to separate the row and column selections.

# variable1 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("From the second element, slice elements from index 1 to index 4 (not included):",variable1[1, 1:4])
# #Remember that second element has index 1.

# variable2 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("to call all index : ", variable2[0:2])


# variable3 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("From the first  element, slice elements from index 1 to index 4 (not included): ", variable3[0, 1:4])


# variable4 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("slicing index 4 , column 3rd from both the indexes :",variable4[0:2, 4])
# #, is used to separate the row and column selections.

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

# variable5 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print(variable5[0:2, 1:4])

# # ---------------------------NumPy Data Types----------------------------:

# -----Data Types in Python---:
# By default Python have these data types:

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j


#-------- Data Types in NumPy----------

# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for
#  unsigned integers etc.

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# Checking the Data Type of an Array-----
# The NumPy array object has a property called dtype that returns the data type of the array:

# Get the data type of an array object:

# arr = np.array([1, 2, 3, 4])
# print(arr.dtype)
# print(arr.dtype)

# #Get the data type of an array containing strings:

# arr2 = np.array(["harry", "marry", "darry "])
# print(arr2.dtype)

# aar3 = np.array(["harry", "darry", "marry ", "harry "])
# print(aar3.dtype)
# print(aar3)

# -------Creating Arrays With a Defined Data Type-------

# We use the array() function to create arrays, this function can take an optional argument: 

# dtype that allows us to define the expected data type of the array elements:

# var = np.array([2,3,4,5,34,34,34], dtype="S")# converted into string data type 
# print(var.dtype)
# print("a string :  ", var)

# var2 = np.array([2,3,4,5,34,34,34], dtype="U")# converted into string data type 
# print(var2.dtype)
# print("a unicode string : ",var2)

# # For i, u, f, S and U we can define size as well.

# var3 = np.array([2,3,4,5,34,34,34], dtype="i4")# converted into string data type 
# print(var3.dtype)
# print("an array with  data types 4 bites integer  : ",var3)


# What if a Value Can Not Be Converted?

# If a type is given in which elements can't be casted then NumPy will raise a ValueError.

# In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

# Example: 
# A non integer string like 'a' can not be converted to integer (will raise an error):

# Converting Data Type on Existing Arrays------------

# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the 
# data type directly like float for float and int for integer: 

# float data into integer : 
# arr = np.array([1.3 ,3.2 ,4.3 ,5.3])

# arrnew = arr.astype("i")
# print("\n float value  are converted into integer as a new copy of arr as arrnew :  ",arrnew,"\n")
# print("\n value data type and its bytes : ", arrnew.dtype,"\n")

# unicode string into sring : 
# arr2 = np.array(["harry ", "barry ", "marry ", "karry ", "marry "])

# arrnew2 = arr2.astype("S")
# print("\nstring value converted into unicode string by making a copy of arr2 as arrnew2  :  ",arrnew2,"\n")
# print("\n value data type and its bytes : ", arrnew2.dtype,"\n")


#float into integer : 
# # arr3 = np.array([1.3 ,3.2 ,4.3 ,5.3])

# # arrnew3 = arr3.astype(int)
# # print(arrnew3)
# # print(arrnew3.dtype)

# integer into boolean : 
# arrnew4 = np.array([13 ,32 ,43 ,53,0])

# arrnew4 = arrnew4.astype(bool)
# print("integer converted into boolean data type by making copy of it : ",arrnew4,"\n")
# print("data type is : ",arrnew4.dtype,"\n")


#-------------------------------NumPy Array Copy vs View-------------------:

# The Difference Between Copy and View

# The main difference between a copy and a view of an array is that the copy 
# is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array
# , and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array
# , and any changes made to the original array will affect the view.

# Make a copy, change the original array, and display both arrays:

# s = np.array([1,2,3,4,4,5,3,3,4])
# x = s.copy()
# s[1] = 42

# print("orignal array data : ",s)
# print("copy data that is not changed : ",x)

# # make a copy and now change the copy value, and dispaly both arrays : 
# y = np.array([1,2,3,4,4,5,3,988,4])
# i = y.copy()
# i[1] = 32

# print("orignal  data that is not changed :",y)
# print("copy data : ",i)

# # Make a view, change the original array, and display both arrays:
# arr = np.array([1, 2, 3, 4, 5])
# d = arr.view()
# arr[0] = 42

# print("orignal value ",arr)
# print("we changed orignal value so view will be changed to : ",d)

# # Make a view, change the view, and display both arrays
# arr2 = np.array([1, 2, 3, 5, 5])
# f = arr2.view()
# f[4] = 445

# print("orignal value will be changed because we changed the view  ",arr2)
# print(" veiw data : ",f)


# Check if Array Owns its Data:

# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute (base) that returns (None) if the array owns the data.

# Otherwise, the (base)  attribute refers to the original object.

# Print the value of the base attribute to check if an array owns it's data or not:

# s = np.array([1,2,3,4,4,5,3,3,4])

# rt = s.copy()
# tr = s.view()

# print("its returning none thats means copy owns the data : ",rt.base)
# print("it does not own data : ",tr.base)


# ----------------------NumPy Array Shape-----------------------:

# numpy.shape(array)

# Shape of an Array:
# The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index 
# having the number of corresponding elements.

# s = np.array([[2,3,4,5],[2,4,5,3]])
# print("the shape of \'s\': ",s.shape)
# print("s has 2 dimensions : ",s)
# #The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has
# #  2 elements and the second has 4.

# arr = np.array([1,2,4,5] ,ndmin=5) 
# print('shape : ',arr)
# print( "number of shape is : ", arr.shape)


# # # ---------------------#---#NumPy Array Reshaping-------------
# Syntax and parameters
# Here is the syntax of the function:

# numpy.reshape(array, shape, order = 'C')
# array: Input array.
# shape: Integers or tuples of integers.
# order: C-contiguous, F-contiguous, A-contiguous; this is an optional parameter.‘C’ order means that 
# operating row-rise on the array will be slightly quicker. ‘F’ order means that column-wise operations will
#  be faster. ‘A’ means to read / write the elements in Fortran-like index order.
# Return value: An array which is reshaped without any change to its d

# Reshaping means changing the shape of an array.

# The shape of an array is the number of elements in each dimension.

# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# Reshape From 1-D to 2-D:

# Convert the following 1-D array with 12 elements into a 2-D array.

# The outermost dimension will have 4 arrays, each with 3 elements:

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# arrnew = arr.reshape(4,3)
# print("this is arrnew shape",arrnew.shape)
# print("this is arrnew",arrnew)

# Reshape From 1-D to 3-D:------

# convert the following 1-D array with 12 elements into a 3-D array.

# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
# arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# arrnew2 = arr2.reshape(2,3,2)
# print("this is arrnew2 :",arrnew2.shape)
# print("this is arrnew2 shape:`",arrnew2)

# how to revert from 2D to array to 1D array:

# arrr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

# newarre = arrr.reshape(-1)
# print(newarre.shape)
# print(newarre)

# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.

# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a
#  3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

# Example
# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(3, 3)

# print(newarr)


# Returns Copy or View?:
# Check if the returned array is a copy or a view:
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print("if is shows the orignal value then its view : ",arr.reshape(2,4).base)


# Unknown Dimension:

# You are allowed to have one "unknown" dimension.

# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

# Pass -1 as the value, and NumPy will calculate this number for you.

# Example
# Convert 1D array with 8 elements to 3D array with 2x2 elements:

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(2, 2, -1)

# print(newarr)


# Flattening the array::

# Flattening array means converting a multidimensional array into a 1D array.

# We can use reshape(-1) to do this.

# Convert the array into a 1D array:

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arrn = arr.reshape(-1)
# print(arrn)
# print(arrn.shape)

# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for
#  rearranging the elements rot90, flip, fliplr, flipud etc. These fall
#  under Intermediate to Advanced section of numpy.

# ---------------NumPy Array Iterating-------------------:

# Iterating Arrays:

# Iterating means going through elements one by one.

# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

# If we iterate on a 1-D array it will go through each element one by one.

# Iterate on the elements of the following 1-D array:

# ir = np.array([1,3,4]) # iterating on element 1-D array 
# # print(ir)

# for i in ir: 
#     print('this is 1-D array in for loop ',i) # this is how u can iterate on element above 1-D array 

# # Iterating 2-D Arrays:

# In a 2-D array it will go through all the rows.

# Iterate on the elements of the following 2-D array:
# irs = np.array([[1,2,4],[3,2,5]]) # iterating on element 2-D array 
# for x in irs:
#     print('this is 2-D array in for loop ', x )

# If we iterate on a n-D array it will go through n-1th dimension one by one.

# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# Example
# Iterate on each scalar element of the 2-D array:

# var  = np.array([[1,2,3], [4,5,6]]) 

# for i in var : 
#     for y in i: 
#         print(y)
# #(result : 1,2,3,4,5,6 with break lines : )

# Iterating 3-D Arrays:

# In a 3-D array it will go through all the 2-D arrays.

# Iterate on the elements of the following 3-D array:
# var1  = np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,9]]])

# for v in var1: 
#     print(v) 

# To return the actual values, the scalars, we have to iterate the arrays in each dimension.
# Iterate down to the scalars:

# var1  = np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,9]]])

# for item in var1:
#     for key in item:
#         for value in key:
#             print(value)

# # Iterating Arrays Using nditer():

# # The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
# It solves some basic issues which we face in iteration, lets go through it with examples.

# Iterating on Each Scalar Element
# In basic for loops, iterating through each scalar of an array we need to use n for loops which 
# can be difficult to write for arrays with very high dimensionality.

# terate through the following 3-D array:
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
    # print(x)

# Iterating Array With Different Data Types:-----
# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# NumPy does not change the data type of the
# element in-place (where the element is in array) so it needs some other space to perform this action, 
# that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

# Iterate through the array as a string:-----

# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=["buffered"], op_dtypes="S"):
#     print( "this converted into data types string and nditer full rows and flags buffered  :",x )

# iterate through the array as a string in 2 d arrays : 
# arr = np.array([[1,2,3],[3,4,5]])
# for x in np.nditer(arr, flags=["buffered"], op_dtypes="S"):
#     print(x)

# Iterating With Different Step Size:---
# We can use filtering and followed by iteration.

# Example
# Iterate through every scalar element of the 2D array skipping 1 element:
# a = np.array([[1,2,3],[1,4,5]])

# for i in np.nditer(a[:, ::2]):
#     print(i)


# Enumerated Iteration Using ndenumerate():--------

# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be
#  used for those usecases.

# Enumerate on following 1D arrays elements::

# b = np.array([2,3,34,5])
 
# for idx , x in np.ndenumerate(b):
#     print(idx, x )


# # Enumerate on following 2D arrays elements::
# t = np.array([[2,3,34,5], [2,4,3,3]])
# for idx , i in np.ndenumerate(t):
#     print('rows and columns of array  :',idx,"arrays numbers  :", i )

# # test try ////----------:
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for idx , p in np.ndenumerate(arr):
#     print(idx, p)

#----------------------NumPy Joining Array---------------------------

# Joining NumPy Arrays:

# Joining means putting contents of two or more arrays in a single array.

# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

# We pass a sequence of arrays that we want to join to the "concatenate()" function, along with the axis. 
# If axis is not explicitly passed, it is taken as 0.

# Join two arrays:

# a = np.array([0,34,5,7])

# b = np.array([2,34,5,6])

# #joining two arrays oppositely : 

# ba = np.concatenate((b,a))
# print("this is b  into a :  ",ba)

# ab = np.concatenate((a,b))
# print("this is a into b :", ab)
# # result: a merge with b 

# Join two 2-D arrays along rows (axis=1):

# The axis parameter determines how arrays are combined, whether it's 
# along rows (axis 0) or along columns (axis 1) for two-dimensional arrays.

# arr = np.array([[1,3,4], [6,7,9]])

# arr2 = np.array([[13,34,56], [64,71,92]])

# combine = np.concatenate((arr,arr2), axis=1)# axis 1 = columns , axis 0 = rows 
# print(combine)


# Joining Arrays Using Stack Functions:
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other,
#  ie. stacking.

# We pass a sequence of arrays that we want to join to the stack() method along with the axis.
#  If axis is not explicitly passed it is taken as 0.

# Example

# In summary, the main difference is that np.concatenate combines arrays along an existing axis without introducing 
# a new dimension, while np.stack combines arrays along a new axis and can introduce a new dimension in the result.
# The choice between them depends on your specific use case and whether you want to create a new axis for stacking
# or simply concatenate arrays along an existing axis.

# arr = np.array([1,3,4])

# arr2 = np.array([13,71,92])

# combine = np.stack((arr,arr2), axis=1)# axis 1 = columns , axis 0 = rows 
# print(combine)

# Stacking Along Rows: 

# NumPy provides a helper function: hstack() to stack along rows.

# ar = np.array([1,39,4])

# ar2 = np.array([13,71,98])

# combiner = np.hstack((ar,ar2)) # hstack for stacking alog rows : 
# print(combiner)

# Stacking Along Columns:

# NumPy provides a helper function: vstack()  to stack along columns.

# ar = np.array([1,39,4])

# ar2 = np.array([13,71,98])

# combiner = np.vstack((ar,ar2)) # vstack for stacking along columns 
# print(combiner)

# # Stacking Along Height (depth):

# # NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

# a = np.array([1,39,4])

# a2 = np.array([13,71,98])

# combin = np.dstack((a,a2))# dstack for stacking along height (depth)
# print(combin)


# --------------------------NumPy Splitting Array-------------:

# Splitting NumPy Arrays:

# Splitting is reverse operation of Joining.

# Joining merges multiple arrays into one and Splitting breaks one array into multiple.

# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# Split the array in 3 parts:
# ray = np.array([2,3,4,5,4,4])

# spli = np.array_split(ray,3)
# print(spli)


# split the array in 5 parts : 
# pn = np.array([2,3,4,5,4,3,5,3,4])

# array = np.array_split(pn, 5 )

# print(array)


# Split Into Arrays: 

# The return value of the array_split() method is an array containing each of the split as an array.

# If you split an array into 3 arrays, you can access them from the result just like any array element:

# pn = np.array([1,4,5,43,3])

# newp = np.array_split(pn , 3)

# print(newp[1])
# print(newp[2])
# print(newp[0])

# # self code testing for enumerate fucntions : 
# for index ,value in enumerate(newp):

    
#     print(f"index :  {index}  and the value : {value} ")


# Splitting 2-D Arrays: 

# Use the same syntax when splitting 2-D arrays.

# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

# Example

# Split the 2-D array into three 2-D arrays.

# var1 = np.array([[3,4,5],[3,4,3],[3,46,2],[53,42,434],[2,4,1],[2,76,2]])

# newvar1 = np.array_split(var1 , 3 )

# print(newvar1)

# The example above returns three 2-D arrays.

# In addition, you can specify which axis you want to do the split around.

#


# The reason you're getting 6 splits instead of 3 is because the np.array_split function divides the array into 
# nearly equal-sized chunks along the specified axis. In your case, you have a 2D array var1, and you're trying 
# to split it into 3 equal-sized chunks. However, the array dimensions are such that the split is not perfectly even.

# Here's a breakdown of the splits:

# The first split occurs along the rows, resulting in two chunks:

# Chunk 1: [[3, 4, 5], [3, 4, 3], [3, 46, 2]]
# Chunk 2: [[53, 42, 434], [2, 4, 1], [2, 76, 2]]
# The second split occurs along the rows as well, but it starts from where the first split ended:

# Chunk 3: [[3, 4, 5], [3, 4, 3], [3, 46, 2]]
# Chunk 4: [[53, 42, 434], [2, 4, 1], [2, 76, 2]]
# The third split occurs along the rows again, starting from where the second split ended:

# Chunk 5: [[3, 4, 5], [3, 4, 3], [3, 46, 2]]
# Chunk 6: [[53, 42, 434], [2, 4, 1], [2, 76, 2]]
# As you can see, the np.array_split function divides the array into equal-sized rows, and since your original
#  array has 6 rows, you get 6 chunks. If you intended to split it into 3 equal-sized chunks, you would need to
#  reshape your array or pad it with additional rows to make the split even.

# Split the 2-D array into three 2-D arrays:

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)

# print(newarr)

# he example above returns three 2-D arrays.

# Let's look at another example, this time each element in the 2-D arrays contains 3 elements.
# -----------

#  The example below also returns three 2-D arrays, but they are split along the row (axis=1).


# var12 = np.array([[3,4,5],[3,4,3],[3,46,2],[53,42,434],[2,4,1],[2,76,2]])

# newvar12 = np.array_split(var12 , 3 , axis=1 ) # axis 1 = columns : 

# print(newvar12)

# # for finding in which index the array are in : 
# for index , value in enumerate(newvar12):
#     print(f"index : {index} and value : {value}")


# An alternate solution is using hsplit() opposite of hstack():

# Use the hsplit() method to split the 2-D array into three 2-D arrays along rows:

# var123 = np.array([[3,4,5],[3,4,3],[3,46,2],[53,42,434],[2,4,1],[2,76,2]])

# newvar123 = np.vsplit(var123, 3) # for rows vsplit , for columns hsplit, for dept dsplit : 

# print(newvar123)


# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().



# ------------------------------NumPy Searching Arrays------------------:

# Searching Arrays

# You can search an array for a certain value, and return the indexes that get a match.

# To search an array, use the where() method.

# Example:
# Find the indexes where the value is 4:

# pn = np.array([1,3,4,5,5,6,4,4])

# new = np.where(pn == 4 ) # will show that in which indexes is 4 in arrays;

# print("this is where 4 is in arrays indexes : ",new)


# Find the indexes where the values are even:

# sn = np.array([1,4,32,5,6,77,4,33,67,65,78])

# snnew = np.where(sn % 2 == 0 )

# print("index in arrays where conataining values  are even numbers : ",snnew)

# Find the indexes where the values are odd:

# sn1 = np.array([1,4,32,5,6,77,4,33,67,65,78])

# snn1ew = np.where(sn1 % 2 != 0 )

# print(f"index in arrays where conataining values  are odd  numbers : {snn1ew}")


# Search Sorted

# There is a method called searchsorted() which performs a binary search in the array, and returns the index where 
# the specified value would be inserted to maintain the search order.

# The searchsorted() method is assumed to be used on sorted arrays.

# Example
# Find the indexes where the value 7 should be inserted:

# arr = np.array([6, 7, 8, 9])

# x = np.searchsorted(arr, 7)

# print(x)


# Example explained: The number 7 should be inserted on index 1 to remain the sort order.

# The method starts the search from the left and returns the first index where the number 7 is no longer larger
#  than the next value.

# Search From the Right Side
# By default the left most index is returned, but we can give side='right' to return the right most index instead


# pn = np.array([6,7,8,9])

# newpn = np.searchsorted(pn , 7 , side="right")

# print("search sorted from the right side : ",newpn)


# Multiple Values------
# To search for more than one value, use an array with the specified values.

# Example
# Find the indexes where the values 2, 4, and 6 should be inserted:
# print("loading plz wait----------")
# sorrt = np.array([1,3,5,7])

# newsorrt = np.searchsorted(sorrt,[2,4,6])

# print(newsorrt)

# print("end ----------")

# The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would
#  be inserted in the original array to maintain the order.


# ---------------------------------NumPy Sorting Arrays------------------:

# Sorting Arrays
# Sorting means putting elements in an ordered sequence.

# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, 
# ascending or descending.

# The NumPy ndarray object has a function called "sort()" , that will sort a specified array.

# example : 
# sort array : 

# sn = np.array([5,6,3,1,2,4])

# print("Result : ",np.sort(sn)) ## note : This method returns a copy of the array, leaving the original array unchanged.

# # You can also sort arrays of strings, or any other data type:
# # Example
# # Sort the array alphabetically:
# s = np.array(["red ", "yellow", "green", "blue "])

# print(np.sort(s))

# # another example : 

# ab = np.array(["harry", "marry ", "carry ", "parrot ", "midhal ", "sunel " ,  "kamran ", "dehli "])
# print(np.sort(ab))

# Example
# Sort a boolean array:

# ca = np.array([True,False,True])

# print(np.sort(ca))

# Sorting a 2-D Array

# If you use the sort() method on a 2-D array, both arrays will be sorted:

# Example
# Sort a 2-D array:

# pa = np.array([[2,5,4,6],[1,7,9,3]])

# print("result : ",np.sort(pa))


# ----------------------------------NumPy Filter Array---------------------:

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.

# note : A boolean index list is a list of booleans corresponding to indexes in the array.

# If the value at an index is True that element is contained in the filtered array, if the value at that index
#  is False that element is excluded from the filtered array.

# ExampleGet your own Python Server

# Create an array from the elements on index 0 and 2:

# sn = np.array([41,43,534,534])

# x = [True,False,True,False]

# new = sn[x]

# print(new)

# The example above will return [41 534 ], why?

# Because the new array contains only the values where the filter
#  array had the value True, in this case, index 0 and 2.


# Creating the Filter Array:---
# In the example above we hard-coded the True and False values, but the 
# common use is to create a filter array based on conditions.


# a program that filters value that are greater than 20 in arrays:
# arr = np.array([10,15,24,56,87,12,14,19,78,45])# array object 

# filter_arr = []
# # empty list to store boolean values 

# # for loop iterator to append on boolean values on empty list  :
# for element in arr:
#     if element > 20 : 
#         filter_arr.append(True)

#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]
# # filtered newarr : 

# print("\nthis is the boolean index using dynamic code : ",filter_arr)
# print("\nthis is filtered array for numbers greater than 20  : ",newarr,"\n")




# Example:
# Create a filter array that will return only even elements from the original array:

# arr = np.array([10,15,24,56,87,12,14,19,78,45])# array object 

# filter_arr = []
# # empty list to store boolean values 

# # for loop iterator to append on boolean values on empty list  :
# for element in arr:
#     if element % 2 == 0  : 
#         filter_arr.append(True)

#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]
# # filtered newarr : 

# print("\nthis is the boolean index using dynamic code : ",filter_arr)
# print("\nthis is filtered array of even numbers   : ",newarr,"\n")


# Creating Filter Directly From Array

# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

# We can directly substitute the array instead of the iterable variable
# in our condition and it will work just as we expect it to.

# Create a filter array that will return only values higher than 42:

# ic = np.array([1,24,23,5,3,533,5])

# fitler_ic = ic > 20 

# new = ic[fitler_ic]

# print(fitler_ic)
# print(new)

# Example
# Create a filter array that will return only even elements from the original array:

# ids = np.array([1,24,23,5,3,533,5])

# fitler_ids = ids % 2 == 0 

# news = ids[fitler_ids]

# print(fitler_ids)
# print(news)



