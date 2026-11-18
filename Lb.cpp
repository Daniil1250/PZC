#include <iostream>
#include <ctime>
#include <cstdlib>
#include <iomanip>

using namespace std;

int findMinIndex(double* arr, int len) {
    int minIndex = 0;
    for (int i = 1; i < len; i++) {
        if (arr[i] < arr[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}

void checkArrayTask() {
    const int N1 = 10;
    const int N2 = 12;

    double* A = new double[N1];
    double* B = new double[N2];

    for (int i = 0; i < N1; i++) {
        A[i] = (rand() % 100) / 3.0;
    }
    for (int i = 0; i < N2; i++) {
        B[i] = (rand() % 100) / 3.0;
    }

    cout << "Массив A: ";
    for (int i = 0; i < N1; i++) cout << A[i] << " ";
    cout << endl;

    cout << "Массив B: ";
    for (int i = 0; i < N2; i++) cout << B[i] << " ";
    cout << endl;

    int minIdxA = findMinIndex(A, N1);
    int minIdxB = findMinIndex(B, N2);

    cout << "\nИндекс минимума в A: " << minIdxA << endl;
    cout << "Индекс минимума в B: " << minIdxB << endl;

    int distToEndA = N1 - 1 - minIdxA;
    int distToEndB = N2 - 1 - minIdxB;

    if (distToEndA < distToEndB) {
        cout << "Минимум ближе к концу в массиве A" << endl;
    }
    else if (distToEndB < distToEndA) {
        cout << "Минимум ближе к концу в массиве B" << endl;
    }
    else {
        cout << "Минимумы находятся на одинаковом расстоянии от конца" << endl;
    }

    delete[] A;
    delete[] B;
}

void findMaxMinInMatrix(int** mat, int N, int M, int* maxTop, int* minBottom) {
    *maxTop = -999999;
    *minBottom = 999999;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (i < N / 2 && j < M / 2) {
                if (mat[i][j] > *maxTop) {
                    *maxTop = mat[i][j];
                }
            }
            if (i >= N / 2 && j >= M / 2) {
                if (mat[i][j] < *minBottom) {
                    *minBottom = mat[i][j];
                }
            }
        }
    }
}

void matrixTask() {
    const int N = 6;
    const int M = 8;

    int** mat = new int*[N];
    for (int i = 0; i < N; i++) {
        mat[i] = new int[M];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            mat[i][j] = rand() % 21 - 10;
        }
    }

    cout << "\nМатрица " << N << "x" << M << ":" << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << setw(4) << mat[i][j];
        }
        cout << endl;
    }

    int maxTop;
    int minBottom;
    
    findMaxMinInMatrix(mat, N, M, &maxTop, &minBottom);

    cout << "\nМаксимум в верхней заштрихованной области: " << maxTop << endl;
    cout << "Минимум в нижней заштрихованной области: " << minBottom << endl;

    for (int i = 0; i < N; i++) {
        delete[] mat[i];
    }
    delete[] mat;
}

int main() {
    setlocale(LC_ALL, "RU");
    srand(time(0));

    cout << "1. Задача с массивами" << endl;
    checkArrayTask();

    cout << "\n========================================" << endl;

    cout << "2. Задача с матрицей" << endl;
    matrixTask();

    return 0;
}
