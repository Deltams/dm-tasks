#include <bits/stdc++.h>

using namespace std;

long long my_pow(long long a, long long p){ // Быстрое возведение в степень
    if (p == 0){
        return 1;
    }
    if (p % 2 == 0){
        return my_pow(a * a, p / 2);
    }
    return a * my_pow(a, p-1);
}

int degree_two(long long n){ // В какую степень 2 возведено число
    int t = 1, ans = 0;
    while (t != n){
        t *= 2;
        ans++;
    }
    return ans;
}

vector<int> cal_func_by_res(vector<int> v1, vector<int> v2, int n){ // Востановление функции по остаточным
    vector<int> ans;
    int tmp = v1.size()*2 / my_pow(2, n);
    for (int i = 0; i < v1.size(); i = i + tmp){
        for (int j = i; j < i + tmp; j++){
            ans.push_back(v1[j]);
        }
        for (int j = i; j < i + tmp; j++){
            ans.push_back(v2[j]);
        }
    }
    return ans;
}

int main(){
    setlocale(LC_ALL, "Russian");

    string s1, s2;
    int n;

    cout << "Введите нулевую остаточную: ";

    cin >> s1;

    cout << "Введите единичную остаточную: ";

    cin >> s2;

    cout << "Введите номер аргумента(1 - " << degree_two(s1.size()*2) <<"): ";

    cin >> n;

    vector<int> v1(s1.size()), v2(s2.size());

    for (int i = 0; i < s1.size(); i++){
        v1[i] = s1[i] - '0';
        v2[i] = s2[i] - '0';
    }

    for (auto to : cal_func_by_res(v1, v2, n)){
        cout << to << " ";
    }

    return 0;
}
