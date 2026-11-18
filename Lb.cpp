#include <iostream>
#include <cstring>
#include <cctype>
#include <string>

using namespace std;

void analyzeString(const char* text, int* stats) {
    stats[0] = strlen(text);
    stats[1] = 0;
    stats[2] = 0;
    stats[3] = 0;

    bool inWord = false;
    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] >= 'A' && text[i] <= 'Z') stats[2]++;
        if (text[i] >= 'a' && text[i] <= 'z') stats[3]++;

        if (text[i] == ' ') {
            inWord = false;
        } else if (inWord == false) {
            inWord = true;
            stats[1]++;
        }
    }
}

void taskStrings() {
    cout << "--- Задача 1 ---" << endl;
    int capacity = 10;
    char** lines = new char*[capacity];
    int count = 0;

    cout << "Вводите строки (and для конца):" << endl;
    string input;
    while (true) {
        getline(cin, input);
        if (input == "and") break;

        if (count == capacity) {
            capacity = capacity * 2;
            char** newLines = new char*[capacity];
            for (int i = 0; i < count; i++) {
                newLines[i] = lines[i];
            }
            delete[] lines;
            lines = newLines;
        }

        lines[count] = new char[input.length() + 1];
        strcpy(lines[count], input.c_str());
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
        cout << lines[i] << " Длина:" << stats[0]
             << " Слов:" << stats[1]
             << " Заглавных:" << stats[2]
             << " Строчных:" << stats[3] << endl;
        delete[] lines[i];
    }
    delete[] lines;
}

void taskMatrix() {
    cout << "\n--- Задача 2 ---" << endl;
    int n, m;
    cout << "N и M: ";
    cin >> n >> m;

    double** matrix = new double*[n];
    for (int i = 0; i < n; i++) {
        matrix[i] = new double[m];
    }

    cout << "Элементы:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i < n / 2 && j < m / 2 && matrix[i][j] > 0) count++;
            if (i >= n / 2 && j >= m / 2 && matrix[i][j] > 0) count++;
        }
    }

    double** positives = nullptr;
    if (count > 0) {
        positives = new double*[count];
        int k = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i < n / 2 && j < m / 2 && matrix[i][j] > 0) {
                    positives[k] = &matrix[i][j];
                    k++;
                }
                if (i >= n / 2 && j >= m / 2 && matrix[i][j] > 0) {
                    positives[k] = &matrix[i][j];
                    k++;
                }
            }
        }
    }

    cout << "\nПоложительные в области:" << endl;
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
