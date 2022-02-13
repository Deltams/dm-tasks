#include <bits/stdc++.h>

using namespace std;

int degree_two(long long n){ // В какую степень 2 возведено число
    int t = 1, ans = 0;
    while (t != n){
        t *= 2;
        ans++;
    }
    return ans;
}

bool str_prov(string &s){ // Проверка на то, что вектор введен правильно
    int chek_size = 0;
    for (int i = 0; i < s.size(); i++){
        if ('0' <= s[i] && s[i] <= '1'){
            chek_size++;
        }
    }
    if (chek_size != s.size()){
        return false;
    }
    int ans = 1, tmp = s.size();
    while (ans <= tmp){
        if (ans == tmp){
            return true;
        }
        ans *= 2;
    }
    return false;
}

void string_standard(string &s){ // Приведение строки к стандарту
    string tmp = "";
    for (int i = 0; i < s.size(); i++){
        if (s[i] == ' '){
            continue;
        }
        tmp += s[i];
    }
    s = tmp;
}

vector<int> vec_pp(vector<int> v){ // Прибавление в конец вектора 1
    int tmp = 0;
    if (v[v.size()-1] == 1){
        tmp = 1;
        v[v.size()-1] = 0;
    } else {
        v[v.size()-1] = 1;
        return v;
    }
    for (int i = v.size()-2; i >= 0; i--){
        if (tmp == 0){
            break;
        } else if (v[i] == 1){
            v[i] = 0;
        } else {
            v[i] = 1;
            break;
        }
    }
    return v;
}

string sdnf(vector<int> v){ // Нахождение СДНФ - отрицание; * Конъюнкция; + дизъюнкция
    string ans = "";
    int chek = 0;
    for (int i = 0; i < v.size(); i++){
        if (v[i] == 0){
            chek++;
        }
    }
    if (chek == v.size()){
        return ans;
    }
    int tmp = degree_two(v.size());
    vector<vector<int>> G;
    G.resize(v.size());
    for (int i = 0; i < v.size(); i++){
        G[i].resize(tmp);
        if (i == 0){
            for (int j = 0; j < G[i].size(); j++){
                G[i][j] = 0;
            }
        } else {
            G[i] = vec_pp(G[i-1]);
        }
    }
    for (int i = 0; i < v.size(); i++){
        if (v[i] == 1){
            ans += "(";
            for (int j = 0; j < G[i].size(); j++){
                if (G[i][j] == 0){
                    ans += to_string(-j-1);
                } else {
                    ans += to_string(j+1);
                }
                if (j == G[i].size()-1){
                    continue;
                }
                ans += "*";
            }
            ans += ")+";
        }
    }
    ans.resize(ans.size()-1);
    return ans;
}

int main(){
    setlocale(LC_ALL, "Russian");

    string s;

    do{
        cout << "Введите вектор: ";

        getline(cin, s);

        string_standard(s);

        if (str_prov(s)){
            break;
        } else {
            cout << "\nВектор введен неверно!\nПример ввода: 01100110\n\n";
        }
    }while(true);

    vector<int> v(s.size());

    for (int i = 0; i < s.size(); i++){
        v[i] = s[i] - '0';
    }

    cout << "\nСДНФ: " << sdnf(v);

    return 0;
}
