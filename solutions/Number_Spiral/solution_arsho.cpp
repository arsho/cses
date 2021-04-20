/*
Title     : Number Spiral
Category  : Introductory Problems
URL       : https://cses.fi/problemset/task/1071
Author    : arsho
Created   : 07 April 2021
*/


#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    long long cas, t, x, y, max_number, max_pos, min_pos;
    cin >> cas;
    for(t=0; t<cas; t++)
    {
        cin >> x >> y;
        if (x ==  1 && y == 1)
        {
            cout << 1 << endl;
            continue;
        }
        max_pos = max(x, y);
        min_pos = min(x, y);
        max_number = max_pos * max_pos;
        if (y >= x)
        {
            if (y % 2 == 1)
                cout << max_number - min(x, y) + 1 << endl;
            else
                cout << max_number - max_pos + 1 - (max_pos - min_pos) << endl;
        }
        else
        {
            if (x % 2 == 0)
                cout << max_number - min(x, y) + 1 << endl;
            else
                cout << max_number - max_pos + 1 - (max_pos - min_pos) << endl;
        }
    }
    return 0;
}
/*
Sample Input:
8
2 3
1 1
4 2
3 4
2 6
2 4
689913499 770079066
586095107 933655238
*/

/*
Sample Output:
8
1
15
12
27
11
593021767041187724
871712102163621276
*/

