#include <bits/stdc++.h>

using namespace std;

long long my_pow(long long a, long long p){ // ������� ���������� � �������
    if (p == 0){
        return 1;
    }
    if (p % 2 == 0){
        return my_pow(a * a, p / 2);
    }
    return a * my_pow(a, p-1);
}

int degree_two(long long n){ // � ����� ������� 2 ��������� �����
    int t = 1, ans = 0;
    while (t != n){
        t *= 2;
        ans++;
    }
    return ans;
}

vector<int> residual(vector<int> &v, int k, int n){ // ����������� ���������� �� �������
    vector<int> ans;
    long long tmp = v.size() / my_pow(2, n); // ������ ��������� ��� ������� �� ������� � ��� ������� �� �������
    int i = 0;
    if (k == 1){
        i = tmp;
    }
    for ( ; i < v.size(); i = i + tmp*2){
        for (int j = i; j < i + tmp; j++){
            ans.push_back(v[j]);
        }
    }
    return ans;
}

int main(){
    setlocale(LC_ALL, "Russian");

    string s;
    int n, k;

    cout << "������� ������ �������: ";

    cin >> s;

    cout << "������� ����� ���������� ����������: ";

    cin >> k;

    cout << "������� ����� ���������(1 - " << degree_two(s.size()) <<"): ";

    cin >> n;

    vector<int> v(s.size());

    for (int i = 0; i < s.size(); i++){
        v[i] = s[i] - '0';
    }

    for (auto to : residual(v, k, n)){
        cout << to << " ";
    }

    return 0;
}
