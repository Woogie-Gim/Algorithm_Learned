# 0번 인덱스 기준 오름차순 / 0번 인덱스가 같으면 1번 인덱스 기준 오름 차순 정렬

```c++
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<vector<int>> v;

bool comp(vector<int> &v1, vector<int> &v2)
{
	if (v1[0] == v2[0]) return v1[1] < v2[1];
	else return v1[0] < v2[0];
}

int main()
{
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int x, y;
		cin >> x >> y;

		v.push_back({ x, y });
	}

	sort(v.begin(), v.end(), comp);

	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < 2; x++)
		{
			cout << v[y][x] << ' ';
		}
		cout << "\n";
	}

	return 0;
}
```