import cv2
import numpy as np


blackImage = np.zeros([600 , 600])

blackImage[200:400 , 200:400] = 255
print(blackImage)

# print(blackImage)

#      0  1  2  3  4  5
# 0  [[0. 0. 0. 0. 0. 0.]
# 1   [0. 0. 0. 0. 0. 0.]
# 2   [0. 0. 0. 0. 0. 0.]
# 3   [0. 0. 0. 0. 0. 0.]
# 4   [0. 0. 0. 0. 0. 0.]
# 5   [0. 0. 0. 0. 0. 0.]]

# [start_row : end_row, start_column : end_column]

# ● start_row: Starting index of the row from which we
# want to access the data.

# ● end_row: Index of the next row before which we
# want to access the data.

# ● start_column: Starting index of the column from
# which we want to access the data.

# ● end_column: Index of the next column before
# which we want to access the data.

# if u want all the cols --> " : " is enough

# 6th row --> row no 5 --> [5 : , : ]


# blackImage[5: , :] = 1

# print(blackImage[5: , :])

cv2.imshow("black", blackImage)


cv2.waitKey(0)








    