/* BFS의 정석 문제 템플릿으로 활용 가능 */

#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>>maze;
int n, m;
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };
int visited[201][201];
int dist[201][201];

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> m;

	for (int y = 0; y < n; y++)
	{
		maze.push_back({});
		string str;
		cin >> str;
		for (int x = 0; x < m; x++)
		{
			maze[y].push_back(stoi(str.substr(x, 1)));
		}
	}
	
	queue<pair<int, int>> q;
	q.push({ 0, 0 });
	
	while(!q.empty())
	{
		int y = q.front().first;
		int x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int ny = y + dy[i];
			int nx = x + dx[i];

			if (ny < 0 || ny >(n - 1) || nx < 0 || nx >(m - 1)) continue;
			if (maze[ny][nx] == 1 && visited[ny][nx] == 0)
			{
				dist[ny][nx] = dist[y][x] + 1;
				q.push({ ny, nx });
				visited[ny][nx] = 1;
			}
		}
	}

	cout << dist[n - 1][m - 1] + 1;

	return 0;
}