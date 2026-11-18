#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;

void analyzeString(const char* text, int* stats) {
    stats[0] = strlen(text);
    stats[1] = 0;
    stats[2] = 0;
    stats[3] = 0;

    bool inWord = false;
    for (int i = 0; text[i] != '\0'; i++) {
        if (isupper(text[i])) stats[2]++;
        else if (islower(text[i])) stats[3]++;

        if (isspace(text[i])) {
            inWord = false;
        } else if (!inWord) {
            inWord = true;
            stats[1]++;
        }
    }
}

void taskStrings() {
    cout << "--- Задача 1: Строки ---" << endl;
    const int MAX_LINES = 100;
    const int MAX_LEN = 256;

    char** lines = new char*[MAX_LINES];
    int count = 0;

    cout << "Вводите строки (введите 'and' для завершения):" << endl;
    char buffer[MAX_LEN];
    while (count < MAX_LINES) {
        cin.getline(buffer, MAX_LEN);
        if (strcmp(buffer, "and") == 0) break;
        lines[count] = new char[strlen(buffer) + 1];
        strcpy(lines[count], buffer);
        count++;
    }

    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (strcmp(lines[j], lines[j + 1]) > 0) {
                char* temp = lines[j];
                lines[j] = lines[j + 1];
                lines[j + 1] = temp;
            }
        }
    }

    cout << "\nРезультат:" << endl;
    int stats[4];
    for (int i = 0; i < count; i++) {
        analyzeString(lines[i], stats);
        cout << lines[i] << " [Длина: " << stats[0]
             << ", Слов: " << stats[1]
             << ", Заглавных: " << stats[2]
             << ", Строчных: " << stats[3] << "]" << endl;
        delete[] lines[i];
    }
    delete[] lines;
}

double** findPositiveZones(double** matrix, int n, int m, int& resultCount) {
    resultCount = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bool inZone = (i < n / 2 && j < m / 2) || (i >= n / 2 && j >= m / 2);
            if (inZone && matrix[i][j] > 0) {
                resultCount++;
            }
        }
    }

    if (resultCount == 0) return nullptr;

    double** result = new double*[resultCount];
    int k = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bool inZone = (i < n / 2 && j < m / 2) || (i >= n / 2 && j >= m / 2);
            if (inZone && matrix[i][j] > 0) {
                result[k] = &matrix[i][j];
                k++;
            }
        }
    }
    return result;
}

void taskMatrix() {
    cout << "\n--- Задача 2: Матрица ---" << endl;
    int n, m;
    cout << "Введите N и M: ";
    cin >> n >> m;

    double** matrix = new double*[n];
    for (int i = 0; i < n; i++) {
        matrix[i] = new double[m];
    }

    cout << "Введите элементы матрицы:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    int count = 0;
    double** positives = findPositiveZones(matrix, n, m, count);

    cout << "\nПоложительные элементы в заштрихованной области:" << endl;
    for (int i = 0; i < count; i++) {
        cout << *positives[i] << " ";
    }
    cout << endl;

    if (positives != nullptr) delete[] positives;
    for (int i = 0; i < n; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
}

int main() {
    setlocale(LC_ALL, "Russian");
    taskStrings();
    taskMatrix();
    return 0;
}
