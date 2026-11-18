#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <iomanip>

using namespace std;

vector<int> analyzeString(const string& text) {
    vector<int> stats(4, 0);
    stats[0] = text.length();
    bool inWord = false;
    for (char c : text) {
        if (isupper(c)) stats[2]++;
        else if (islower(c)) stats[3]++;
        if (isspace(c)) {
            inWord = false;
        } else if (!inWord) {
            inWord = true;
            stats[1]++;
        }
    }
    return stats;
}

void taskStrings() {
    cout << "--- Задача 1: Строки ---" << endl;
    vector<string> lines;
    string input;
    cout << "Вводите строки (введите 'and' для завершения):" << endl;
    while (true) {
        getline(cin, input);
        if (input == "and") break;
        lines.push_back(input);
    }

    sort(lines.begin(), lines.end());

    cout << "\nРезультат:" << endl;
    for (const string& line : lines) {
        vector<int> stats = analyzeString(line);
        cout << line << " [Длина: " << stats[0]
             << ", Слов: " << stats[1]
             << ", Заглавных: " << stats[2]
             << ", Строчных: " << stats[3] << "]" << endl;
    }
}

vector<double*> findPositiveZones(vector<vector<double>>& matrix) {
    vector<double*> result;
    int n = matrix.size();
    int m = matrix[0].size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bool inZone = false;
            if (i < n / 2 && j < m / 2) inZone = true;
            if (i >= n / 2 && j >= m / 2) inZone = true;
            if (inZone && matrix[i][j] > 0) {
                result.push_back(&matrix[i][j]);
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

    vector<vector<double>> matrix(n, vector<double>(m));
    cout << "Введите элементы матрицы:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    vector<double*> positives = findPositiveZones(matrix);

    cout << "\nПоложительные элементы в заштрихованной области:" << endl;
    for (double* p : positives) {
        cout << *p << " ";
    }
    cout << endl;
}

int main() {
    setlocale(LC_ALL, "Russian");
    taskStrings();
    taskMatrix();
    return 0;
}
