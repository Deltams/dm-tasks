#include <bits/stdc++.h>

using namespace std;

long long my_pow(long long a, long long p){ // Áûñòðîå âîçâåäåíèå â ñòåïåíü
    if (p == 0){
        return 1;
    }
    if (p % 2 == 0){
        return my_pow(a * a, p / 2);
    }
    return a * my_pow(a, p-1);
}

vector<int> vec_pp(vector<int> v){ // Ïðèáàâëåíèå â êîíåö âåêòîðà 1
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

vector<vector<int>> all_vectors(long long n){ // Ôóíêöèÿ êîòîðàÿ ñîçäàåò âñå âåêòîðà îí n
    vector<vector<int>> v;
    long long tmp = my_pow(2, n);
    v.resize(my_pow(2, tmp));
    for (int i = 0; i < v.size(); i++){
        v[i].resize(tmp);
        if (i == 0){
            for (int j = 0; j < v[i].size(); j++){
                v[i][j] = 0;
            }
        } else {
            v[i] = vec_pp(v[i-1]);
        }
    }

    return v;
}

void print_result(vector<vector<int>> v){ // Âûâîä âñåõ âåêòîðîâ
    for (auto q : v){
        for (auto to : q){
            cout << to << " ";
        }
        cout << "\n";
    }
}

int main(){
    setlocale(LC_ALL, "Russian");

    long long n;

    cout << "Ââåäèòå ÷èñëî n: ";

    cin >> n;
    
    if (n < 0){
        cout << "Число аргументов не может быть отрицательным!";
        return 0;
    }

    print_result(all_vectors(n));

    return 0;
}
