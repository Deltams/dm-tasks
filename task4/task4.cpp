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

map<int, string> table_p;

vector<vector<int>> all_vectors(long long n){ // Функция которая создает все вектора он n
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
    ans = "1) Константа нуля\n2) Конъюкция\n3) Запрет по X_2\n4) Переменная X_1\n";
    ans += "5) Запрет по X_1\n6) Переменная X_2\n7) Сложение по модулю 2(xor)\n";
    ans += "8) Дизъюнкция\n9) Стрелка Пирса\n10) Эквивалентность\n11) Отрицание X_2\n";
    ans += "12) Импликация от X_2 к X_1\n13) Отрицание X_1\n14) Импликация от X_1 к X_2\n";
    ans += "15) Штрих Шеффера\n16) Константа единицы\nЕсли устали играть, введите слово stop\n";
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
    table_p[1] = "Константа нуля";
    table_p[2] = "Конъюкция";
    table_p[3] = "Запрет по X_2";
    table_p[4] = "Переменная X_1";
    table_p[5] = "Запрет по X_1";
    table_p[6] = "Переменная X_2";
    table_p[7] = "Сложение по модулю 2(xor)";
    table_p[8] = "Дизъюнкция";
    table_p[9] = "Стрелка Пирса";
    table_p[10] = "Эквивалентность";
    table_p[11] = "Отрицание X_2";
    table_p[12] = "Импликация от X_2 к X_1";
    table_p[13] = "Отрицание X_1";
    table_p[14] = "Импликация от X_1 к X_2";
    table_p[15] = "Штрих Шеффера";
    table_p[16] = "Константа единицы";

    cout << "Чтоб начать игру нажмите Enter: ";
    string ts;

    getline(cin, ts);

    do{
        bool stop = false;
        int vec = 1 + rand() % 16;
        cout << "Выберите имя для функции: " << str_vector(mp[vec]) << "\n" << help();
        int t = 3; // КОЛ-ВО ПОПЫТОК
        do{
            if (t == 0){
                cout << "\nВы не смогли дать правильный ответ для этой функции :(\n";
                cout << "Правильный ответ: " << table_p[vec] << "\n\n";
                _sleep(1000);
                break;
            }
            cout << "\nПопыток осталось: " << t;
            cout << "\nВведите номер: ";
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
                cout << "Вы ввели больше символов, чем нужно!\n";
                t--;
            } else if (plaer.size() == 0) {
                cout << "Вы ввели НИЧЕГО!\n";
                t--;
            } else if (plaer.size() == 1 && '0' <= plaer[0] <= '9'){
                if (vec == (int)(plaer[0] - '0')){
                    cout << "Это правильный вариант, молодец!\n\n";
                    _sleep(500);
                    break;
                } else {
                    cout << "Это неверный ответ\n";
                    t--;
                }
            } else if (plaer.size() == 2 && '0' <= plaer[0] <= '9' && '0' <= plaer[1] <= '9'){
                if (vec == (int)(plaer[0] - '0') * 10 + (int)(plaer[1] - '0')){
                    cout << "Это правильный вариант, молодец!\n\n";
                    _sleep(500);
                    break;
                } else {
                    cout << "Это неверный ответ\n";
                    t--;
                }
            } else {
                cout << "Вы неверно ввели данные!\n";
                t--;
            }
        }while(true);
        if (stop){
            do{
                cout << "Введите 1, если хотите продолжить\nВведите 0, если хотите закончить игру :(\n";

                string s;

                getline(cin, s);

                if (s.size() > 1){
                    cout << "Вы ввели больше одного символа, что я должен делать?\n";
                    _sleep(1000);
                    cout << "Спрошу вас еще раз!\n\n";
                    continue;
                } else if (s.size() == 0){
                    cout << "Вы ввели НИЧЕГО...\n";
                    _sleep(1000);
                    cout << "Ладно...\n";
                    _sleep(1000);
                    cout << "Дам вам еще одну попытку.\n\n";
                } else if (s[0] == '1'){
                    break;
                } else if (s[0] == '0'){
                    cout << "До новых встреч ;)\n";
                    return 0;
                } else {
                    cout << "Вы ввели: " << s[0] << "\nХорошо, вот вам еще одна попытка.\n";
                    _sleep(1000);
                    cout << "Я просил ввести 1 или 0...\n";
                    _sleep(2000);
                    cout << "Хорошо, вот вам еще одна попытка.\n\n";
                }
            }while(true);
        }
    } while(true);

    return 0;
}
