#include <stdio.h>
#include <stdbool.h>

#define N 100

float *remontee(int n, float A[][n], float b[n], float sol[n])
{
    //float sol[n];
    sol[n - 1] = b[n - 1] / A[n - 1][n - 1];
    //printf("de remontee x3 = %f", sol[n-1]);
    int i;
    for (i = n - 2; i >= 0; i--)
    {
        float s = 0;
        int j;
        for (j = i + 1; j < n; j++)
        {
            s += sol[j] * A[i][j];
        }
        sol[i] = (b[i] - s) / A[i][i];
    }
    return sol;
}

void permuter(int k, int l, int n, float A[][n])
{
    float c;
    int i;
    for (i = 0; i < n; i++)
    {
        c = A[k][i];
        A[k][i] = A[l][i];
        A[l][i] = c;
    }
}
void printmatr(int n, int p, float matrice[n][p])
{
    printf("printing a (%d,%d) matrix: \n", n, p);
    int i, j;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < p; j++)
        {
            printf("%f|", matrice[i][j]);
        }
    }
    printf("\n");
}
void printvec(int n, float *vecteur)
{
    int i;
    printf("printing a vector: \n");
    for (i = 0; i < n; i++)
    {
        printf("%f|", vecteur[i]);
    }
    printf("\n");
}

float *gauss(int n, float A[][n], float b[n], float sol[n])
{
    int t = 0, i, j;
    for (t = 0; t < n - 1; t++)
    {
        //printmatr(n, n, A);
        //printvec(n, b);
        float pivot = A[t][t];
        //printf("pivot: %f\n", pivot);
        int li, max_ind;
        for (li = t + 1; li < n; li++)
        {
            if (A[li][t] > pivot)
            {
                pivot = A[li][t];
		max_ind = li;
            }
        }
        //printf("%d", li);
        //printf("pivot: %f\n", pivot);
        if (pivot != A[t][t])
        {
            permuter(t, max_ind, n, A);
        }
        for (i = t + 1; i < n; i++)
        {
            if (A[i][t] != 0)
            {
                float scalaire = A[i][t] / pivot;
                //for (j = 0; j < n; j++)
                for (j = 1; j < n; j++) //loop horizentallement
                {
                    A[i][j] = A[i][j] - scalaire * A[t][j];
                }
                b[i] = b[i] - scalaire * b[t];
                A[i][t] = 0;
            }
        }
    }
    printf("the traingular matrix is: \n");
    printmatr(n,n,A);
    printf("the associated vector is: \n");
    printvec(n, b);
    printf("calculating the solution...\n");
    return remontee(n, A, b, sol);
}

int main()
{
    int n = 3;
    float A[3][3] = {0, 1, 3, 1, 2, 0, 4, 5, 6};
    float b[3] = {9, 8, 10};
    printmatr(n, n, A);
    printvec(n, b);
    //float *solution;
    float sol[n];
    gauss(n, A, b, sol);
    printvec(n, sol);
    return 0;
}