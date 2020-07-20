def segment(counter,image,start):
      stack=[]
      stack.append(start)
      process=[]
      row,col=-1,-1
      while(len(stack)!=0):
        start=stack.pop(0)
        i,j=start[0],start[1]
        if(i>row):
          row=i
        if(j>col):
          col=j
        if(start not in process):
          process.append(start)
        
        if(i!=0 and image[i-1][j]>=1):
          image[i-1][j]=counter
          if([i-1,j] not in process and  [i-1,j] not in stack):
            stack.append([i-1,j])
        if(i!=15 and image[i+1][j]>=1):
          image[i+1][j]=counter
          if([i+1,j] not in process and [i+1,j] not in stack):
            stack.append([i+1,j])
        if(j!=0 and image[i][j-1]>=1):
          image[i][j-1]=counter
          if([i,j-1] not in process and [i,j-1] not in stack):
            stack.append([i,j-1])
        if(j!=15 and image[i][j+1]>=1):
          image[i][j+1]=counter
          if([i,j+1] not in process and [i,j+1] not in stack):
           stack.append([i,j+1])
        if(i!=0 and j!=0 and image[i-1][j-1]>=1):
          image[i-1][j-1]=counter
          if([i-1,j-1] not in process and [i-1,j-1] not in stack):
            stack.append([i-1,j-1])
        if(i!=0 and j!=15 and image[i-1][j+1]>=1):
          image[i-1][j+1]=counter
          if([i-1,j+1] not in process and [i-1,j+1] not in stack):
            stack.append([i-1,j+1])
        if(i!=15 and j!=0 and image[i+1][j-1]>=1):
          image[i+1][j-1]=counter
          if([i+1,j-1] not in process and [i+1,j-1] not in stack):
            stack.append([i+1,j-1])
        if(i!=15 and j!=15 and image[i+1][j+1]>=1):
          image[i+1][j+1]=counter
          if([i+1,j+1] not in process and [i+1,j+1] not in stack):
           stack.append([i+1,j+1])
        
      return row,col

from PIL import Image
import numpy as np
image=Image.open('/content/binaryimage1.png')
image=image.resize((16,16))

image=np.array(image)
print("actual image",image)
row,col=image.shape
first=0
counter=2
for i in range(0,row):
  for j in range(0,col):
      if(image[i][j]==1):
        row1,col1=segment(counter,image,[i,j])
        counter=counter+1
        i=row1+1
        j=col1+1
        break
print("total regions",max(image.flatten())-1)
print(image,"2 label for first region and 3 for second region")
'''
#OUTPUT
actual image [[ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  1  1  1  1  1  0  0  0]
 [ 0  0  0  0  0  0  0 39  1  1  1  1  1  0  0  0]
 [ 0  0  0  0  0  0  0  1  1  0  9  1  1  0  0  0]
 [ 0  0  0  0  0  0  0  1  1  1  1  1  1  0  0  0]
 [ 0  0  0  0  0  0  0  0  1  1  1  1  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  1  1  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 1  1  1  1  1  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  1  1  1  1  1  0  0  0  0  0  0  0  0  0  0]
 [ 0  1  0  1  1  1  0  0  0  0  0  0  0  0  0  0]
 [ 1  1  1  1  1  1  0  0  0  0  0  0  0  0  0  0]
 [ 1  1  1  1  1  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0 14  0  0  0  0  0  0  0  0  0  0  0  0  0]]
total regions 2
[[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 2 2 2 2 2 0 0 0]
 [0 0 0 0 0 0 0 2 2 2 2 2 2 0 0 0]
 [0 0 0 0 0 0 0 2 2 0 2 2 2 0 0 0]
 [0 0 0 0 0 0 0 2 2 2 2 2 2 0 0 0]
 [0 0 0 0 0 0 0 0 2 2 2 2 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 2 2 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0]
 [0 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0]
 [0 3 0 3 3 3 0 0 0 0 0 0 0 0 0 0]
 [3 3 3 3 3 3 0 0 0 0 0 0 0 0 0 0]
 [3 3 3 3 3 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0]] 2 label for first region and 3 for second region
'''
