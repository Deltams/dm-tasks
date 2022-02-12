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

vector<int> vec_pp(vector<int> v){ // ����������� � ����� ������� 1
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

map<int, string> table_p;

vector<vector<int>> all_vectors(long long n){ // ������� ������� ������� ��� ������� �� n
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

string help(){
    string ans;
    ans = "1) ��������� ����\n2) ���������\n3) ������ �� X_2\n4) ���������� X_1\n";
    ans += "5) ������ �� X_1\n6) ���������� X_2\n7) �������� �� ������ 2(xor)\n";
    ans += "8) ����������\n9) ������� �����\n10) ���������������\n11) ��������� X_2\n";
    ans += "12) ���������� �� X_2 � X_1\n13) ��������� X_1\n14) ���������� �� X_1 � X_2\n";
    ans += "15) ����� �������\n16) ��������� �������\n���� ������ ������, ������� ����� stop\n";
    return ans;
}

string str_vector(vector<int> v){
    string ans;
    for (int i = 0; i < v.size(); i++){
        ans = ans + (char)(v[i] + (int)'0');
    }
    return ans;
}

int main(){
    setlocale(LC_ALL, "Russian");

    map<int, vector<int>> mp;
    vector<vector<int>> v = all_vectors(2);
    for (int i = 0; i < v.size(); i++){
        mp[i+1] = v[i];
    }
    table_p[1] = "��������� ����";
    table_p[2] = "���������";
    table_p[3] = "������ �� X_2";
    table_p[4] = "���������� X_1";
    table_p[5] = "������ �� X_1";
    table_p[6] = "���������� X_2";
    table_p[7] = "�������� �� ������ 2(xor)";
    table_p[8] = "����������";
    table_p[9] = "������� �����";
    table_p[10] = "���������������";
    table_p[11] = "��������� X_2";
    table_p[12] = "���������� �� X_2 � X_1";
    table_p[13] = "��������� X_1";
    table_p[14] = "���������� �� X_1 � X_2";
    table_p[15] = "����� �������";
    table_p[16] = "��������� �������";

    cout << "���� ������ ���� ������� Enter: ";
    string ts;

    getline(cin, ts);

    do{
        bool stop = false;
        int vec = 1 + rand() % 16;
        cout << "�������� ��� ��� �������: " << str_vector(mp[vec]) << "\n" << help();
        int t = 3; // ���-�� �������
        do{
            if (t == 0){
                cout << "\n�� �� ������ ���� ���������� ����� ��� ���� ������� :(\n";
                cout << "���������� �����: " << table_p[vec] << "\n\n";
                _sleep(1000);
                break;
            }
            cout << "\n������� ��������: " << t;
            cout << "\n������� �����: ";
            string plaer, tmp_plaer = "";
            getline(cin, plaer);
            for (int i = 0; i < plaer.size(); i++){
                if (plaer[i] == ' '){
                    continue;
                }
                tmp_plaer = tmp_plaer + plaer[i];
            }
            plaer = tmp_plaer;
            if ((plaer[0] == 's' || plaer[0] == 'S') &&
                (plaer[1] == 't' || plaer[1] == 'T') &&
                (plaer[2] == 'o' || plaer[2] == 'O') &&
                (plaer[3] == 'p' || plaer[3] == 'P')){
                stop = true;
                break;
            }
            cout << "\n";
            if (plaer.size() > 2){
                cout << "�� ����� ������ ��������, ��� �����!\n";
                t--;
            } else if (plaer.size() == 0) {
                cout << "�� ����� ������!\n";
                t--;
            } else if (plaer.size() == 1 && '0' <= plaer[0] <= '9'){
                if (vec == (int)(plaer[0] - '0')){
                    cout << "��� ���������� �������, �������!\n\n";
                    _sleep(500);
                    break;
                } else {
                    cout << "��� �������� �����\n";
                    t--;
                }
            } else if (plaer.size() == 2 && '0' <= plaer[0] <= '9' && '0' <= plaer[1] <= '9'){
                if (vec == (int)(plaer[0] - '0') * 10 + (int)(plaer[1] - '0')){
                    cout << "��� ���������� �������, �������!\n\n";
                    _sleep(500);
                    break;
                } else {
                    cout << "��� �������� �����\n";
                    t--;
                }
            } else {
                cout << "�� ������� ����� ������!\n";
                t--;
            }
        }while(true);
        if (stop){
            do{
                cout << "������� 1, ���� ������ ����������\n������� 0, ���� ������ ��������� ���� :(\n";

                string s;

                getline(cin, s);

                if (s.size() > 1){
                    cout << "�� ����� ������ ������ �������, ��� � ������ ������?\n";
                    _sleep(1000);
                    cout << "������ ��� ��� ���!\n\n";
                    continue;
                } else if (s.size() == 0){
                    cout << "�� ����� ������...\n";
                    _sleep(1000);
                    cout << "�����...\n";
                    _sleep(1000);
                    cout << "��� ��� ��� ���� �������.\n\n";
                } else if (s[0] == '1'){
                    break;
                } else if (s[0] == '0'){
                    cout << "�� ����� ������ ;)\n";
                    return 0;
                } else {
                    cout << "�� �����: " << s[0] << "\n������, ��� ��� ��� ���� �������.\n";
                    _sleep(1000);
                    cout << "� ������ ������ 1 ��� 0...\n";
                    _sleep(2000);
                    cout << "������, ��� ��� ��� ���� �������.\n\n";
                }
            }while(true);
        }
    } while(true);

    return 0;
}
