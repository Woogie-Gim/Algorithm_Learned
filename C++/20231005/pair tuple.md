# pair / tuple

## pair

- utility 라이브러리에 해당하는 pair는 배열 안에 쌍으로 변수를 저장할 수 있으며 또한 다양한 type을 한번에 저장할 수 있다
- utility 라이브러리에 있지만 보통 vector나 queue를 통해서 사용한다

```c++
#include <iostream>
#include <queue>

q<pair<int, int>> q;

q.push({1, 1});

int y = q.front().first;
int x = q.front().second;
```

## tuple

- tuple은 tuple 라이브러리를 통해 접근할 수 있고 get 메서드를 통해서 변수에 접근할 수 있다. 3개의 변수를 한번에 저장할 수 있다.

```c++
#include<iostream>
#include<tuple>
#include<queue>
using namespace std;

int x, y, z;
queue<tuple<int, int, int>> q;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	x = 3;
	y = 5;
	z = 7;

	q.push(make_tuple(x, y, z));

	cout << get<0>(q.front()) << " ";
	cout << get<1>(q.front()) << " ";
	cout << get<2>(q.front()) << " ";
}
```