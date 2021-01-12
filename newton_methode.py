def resol(A, b, n):
    #loop through all lines of A except the last one, 
    for line in range(n-1):
        piv = A[line][line]
        #print("first pivot\n", piv)
        #loop to find the maximum pivot's index .under the 'current line', in the same column
        for j in range(line+1, n):
            if A[j][line]>piv:
                piv = A[j][line] #change the pivot
                max_ind = j #save the index of max pivot
        if piv!=A[line][line]: #check if pivot have changed
            #permutation of line with line indexed by max_ind
            h1 = A[line]
            A[line]=A[max_ind]
            A[max_ind]=h1
            #permute b also
            h2 = b[line]
            b[line] = b[max_ind]
            b[max_ind] = h2
        #loop through lines under 'current line', and set them all to 0,
        #and update horizontal values (i-->)(done by second loop)
        for i in range(line+1, n):
            if A[i][line]!=0: 
                #if the element under 'current line' equals to 0 don't change it. 
		        #hance that we're substracting 0 from horizontal elements (i-->), so don't change those also.
                scalar = A[i][line]/piv 
                #scalar that will multiplies all horz (i-->) elements with thier associated elements from 'current line'
                for k in range(line+1, n):
                    A[i][k] = A[i][k] - scalar*A[line][k]
                b[i] = b[i] - scalar*b[line]
                A[i][line]=0

    #initialize the solution vector
    sol = [i for i in range(n)]
    sol[n-1] = b[n-1]/A[n-1][n-1]
    #loop in inverse order
    #e starts just before the last.
    for e in range(n-2, -1, -1):
        somm = 0
        #l starts at the last.
        for l in range(e+1, n):
            somm += sol[l]*A[e][l]
        sol[e] = (b[e]-somm)/A[e][e]
    return sol
#////////testing////////////////
# A = [[2,2,-1],[1,4,-1], [3,2,1]]
# b = [-5, -10, 2]
# n = 3
# x = resol(A, b, n)
# print(x)

def f(X, negative):
    #if "negative" is true return -f
    c1 = X[0]**2 + X[1]**2 + X[2]**2 - 3
    c2 = X[0]**2 + X[1]**2 - X[2] - 1
    c3 = X[0] + X[1] + X[2] - 3
    if negative: return [-c1, -c2, -c3]
    return [c1, c2, c3]

def dfc1(X):
    #derivitive of f(x,y,z) at c1
    c1 = 2*X[0]
    c2 = 2*X[1]
    c3 = 2*X[2]
    return [c1, c2, c3]
def dfc2(X):
    #derivitive of f(x,y,z) at c2
    c1 = 2*X[0]
    c2 = 2*X[1]
    c3 = -1
    return [c1, c2, c3]
def dfc3(X):
    #derivitive of f(x,y,z) at c3
    c1 = 1
    c2 = 1
    c3 = 1
    return [c1, c2, c3]

def jacob_f(X):
    #return a (3x3) matrix 
    J = [[], [], []]
    J[0] = dfc1(X)
    J[1] = dfc2(X)
    J[2] = dfc3(X)
    return J

def newton(Xi,erp):
    J_i = jacob_f(Xi)
    J_i_copy = J_i
    #J_i_copy = jacob_f(Xi)
    f_i = f(Xi,negative=True)
    f_i_copy = f_i
    #f_i_copy = f(Xi,negative=True)
    S_i = gauss.resol(J_i_copy, f_i_copy, 3)

    Xs = [i+j for (i,j) in zip(Xi, S_i)]
    error = [abs(e-l) for (e,l) in zip(Xi, Xs)]
    
    #while(error[0]>erp[0] and error[1]>erp[1] and error[2]>erp[2] ):
    norm_err = 0
    for i in range(3):
        norm_err = norm_err+error[i]**2
    while(norm_err>erp):
    #for i in range(100):
        #print(Xs)
        temp = Xs
        J_i = jacob_f(Xs)
        J_i_copy = J_i
        f_i = f(Xs, negative=True)
        f_i_copy = f_i
        S_i = gauss.resol(J_i_copy, f_i_copy, 3)
        Xs = [i+j for (i,j) in zip(Xs, S_i)]
        error = [abs(e-l) for (e,l) in zip(Xs, temp)]
        norm_err = 0
        for i in range(3):
            norm_err = norm_err+error[i]**2
        print(Xs)
#test 
# Xi = [1,0,1]
# newton(Xi, 0.0000001)
#->[1.0000000074505806, 0.9999999925494194, 1.0]