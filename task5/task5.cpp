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

vector<int> residual(vector<int> &v, int k, int n){ // Определение остаточной по вектору
    vector<int> ans;
    long long tmp = v.size() / my_pow(2, n); // Размер коробочки для прохода по вектору и шаг прохода по вектору
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

string str_vector(vector<int> &v){ // Перевод из вектора в стоку
    string ans;
    for (int i = 0; i < v.size(); i++){
        ans = ans + (char)(v[i] + (int)'0');
    }
    return ans;
}

bool vec_equals(vector<int> v1, vector<int> v2){ // Проверяет равенство векторов
    if (v1.size() != v2.size()){
        return false;
    }
    for (int i = 0; i < v1.size(); i++){
        if (v1[i] != v2[i]){
            return false;
        }
    }
    return true;
}

string prov_sfp(vector<int> &v, char a){ // Проверяет и дает овет, какие переменные фиктивны или существенны
    string ans = "";
    int tmp = degree_two(v.size()); // Узнает кол-во переменных
    if (a == 's'){
        for (int i = 0; i < tmp; i++){
            if (!vec_equals(residual(v, 0, i+1), residual(v, 1, i+1))){
                ans = ans + (char)(i + 1 + (int)'0');
            }
        }
    } else if (a == 'f'){
        for (int i = 0; i < tmp; i++){
            if (vec_equals(residual(v, 0, i+1), residual(v, 1, i+1))){
                ans = ans + (char)(i + 1 + (int)'0');
            }
        }
    }
    if (ans.size() == 0){
        ans = "0";
    }
    return ans;
}

void help(){
    string ans = "\n\n\nЧтоб остановить игру, введите слово stop\n";
    ans += "Если нет фиктивных или существенных переменных, то пишите 0\n";
    ans += "Пример ввода данных: \n\n";
    ans += "Выберите существенные переменные для функции: 00101001\n\n";
    ans += "Попыток осталось: n\nВведите номер(а): 123\n\n";
    ans += "Если у вас остались вопросы, то их можно задать разработчику: ";
    ans += "https://vk.com/deltams4\n";
    ans += "Приятной игры ;)\n\n\n\n";
    cout << ans;
}

int main(){
    setlocale(LC_ALL, "Russian");

    cout << "Стандартно выбрано, что игра будет от трёх переменных.\nЕсли вы хотите изменить это, то введите число от 1 до 4 и нажмите Enter.\n\n";
    cout << "Чтоб начать игру нажмите Enter: ";
    string ts;

    getline(cin, ts);

    string tmp_ts = "";

    for (int i = 0; i < ts.size(); i++){
        if (ts[i] == ' '){
            continue;
        }
        tmp_ts = tmp_ts + ts[i];
    }

    ts = tmp_ts;

    vector<vector<int>> v;

    int complexity = 3;

    help();

    if (ts.size() == 1 && '1' <= ts[0] && ts[0] <= '4'){
        complexity = ts[0] - '0';
    }

    v = all_vectors(complexity);

    int proc = my_pow(2, my_pow(2, complexity));

    do{
        bool stop = false;
        int vec = rand() % proc;
        string s1 = "существенные переменные для ", s2 = "фиктивные переменные для ";
        string table_p;
        int varr = 1 + rand() % 2;
        if (varr == 1){
            cout << "Выберите "<< s1 << "функции: " << str_vector(v[vec]) << "\n";
            table_p = prov_sfp(v[vec], 's');
        } else {
            cout << "Выберите "<< s2 << "функции: " << str_vector(v[vec]) << "\n";
            table_p = prov_sfp(v[vec], 'f');
        }
        int t = 3; // КОЛ-ВО ПОПЫТОК
        do{
            if (t == 0){
                cout << "\nВы не смогли дать правильный ответ для этой функции :(\n";
                cout << "Правильный ответ: " << table_p << "\n\n";
                _sleep(1000);
                break;
            }
            cout << "\nПопыток осталось: " << t;
            cout << "\nВведите номер(а): ";
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
            if (plaer.size() != table_p.size()){
                cout << "Ответ неверный.\n";
                t--;
            } else {
                bool chek_pl_tb = false;
                for (int i = 0; i < plaer.size(); i++){
                    if (plaer[i] != table_p[i]){
                        chek_pl_tb = true;
                        break;
                    }
                }
                if (chek_pl_tb){
                    cout << "Ответ неверный.\n";
                    t--;
                    continue;
                }
                cout << "Это правильный вариант, молодец!\n\n";
                _sleep(500);
                break;
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
                    cout << "Я просил ввести 1 или 0...\n\n";
                    _sleep(2000);
                }
            }while(true);
        }
    } while(true);

    return 0;
}
