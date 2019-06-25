import numpy as np

#bilinear interpolation
#https://en.wikipedia.org/wiki/Bilinear_interpolation


nx1 = 10 # nodes in x direction
ny1 = 14 # nodes in y direction
x = np.linspace(0, 0.5, nx1)
y = np.linspace(0.2, 0.9, ny1)
Q = np.zeros((nx1,ny1))

for i in range(len(x)):
    for j in range(len(y)):
        #Q[i,j] = 5*i + 2*j
        Q[i,j] = 1/(i+j+1) # Hilbert's matrix

nx2 = 13  # nodes in x direction for refined mesh
ny2 = 5  # nodes in y direction for refined mesh
xrefined = np.linspace(0, 0.5, nx2)
yrefined = np.linspace(0.2, 0.9, ny2)
Qrefined = np.zeros((nx2,ny2))

for i in range(len(xrefined)):
    for j in range(len(yrefined)):
        """
        Q11(x1,y1) Q21(x2,y1)
        Q12(x1,y2) Q22(x2,y2)
        """

        # find indices of Q
        for idx in range(0, len(x)) : 
            if x[idx] > xrefined[i]: 
                idx_x2 = idx
                break
        idx_x1 = idx_x2 - 1

        for idx in range(0, len(y)) : 
            if y[idx] > yrefined[j]: 
                idx_y2 = idx
                break
        idx_y1 = idx_y2 - 1
        
        x1 = x[idx_x1]
        x2 = x[idx_x2]
        y1 = y[idx_y1]
        y2 = y[idx_y2]

        # values of Q
        fQ11 = Q[idx_x1, idx_y1]  
        fQ12 = Q[idx_x1, idx_y2]  
        fQ21 = Q[idx_x2, idx_y1]  
        fQ22 = Q[idx_x2, idx_y2]        

        matrix1 = [x2-xrefined[i], xrefined[i]-x1]
        matrix2 = [[fQ11, fQ12], [fQ21, fQ22]]
        matrix3 = [y2-yrefined[j], yrefined[j]-y1]

        Qrefined[i,j] = 1/( (x2-x1)*(y2-y1) ) * np.dot(np.dot(matrix1,matrix2),matrix3)
print(Q)
print(Qrefined)
