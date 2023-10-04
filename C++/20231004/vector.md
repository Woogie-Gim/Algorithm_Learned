# vector
1.  사용이유
  vector를 써야하는 이유
  1-1. 쓸줄알아야한다. (가장 큰 이유)
        왜냐 ? 프로그래머스 스타트코드로 vector로 주기때문
  1-2. 남들이 짠 코드 이해를 위해
  1-3. 편의성
  인접리스트를 편하게 구현할 수 있다.
  queue hash 등을 쉽게 구현 가능

1. 값 하나씩 추가 
  리스트 addnode 처럼 값을 하나씩 더할 수 있다. push back()

  더했으면 뺄 수도 있다 pop back()

  ============================중간의 값을 더하거나 빼기
  vect.insert(vect.begin(),4) -> 맨 앞에 4 추가
  vect.erase(vect.begin()+2) -> 2번 원소 제거


3. 사이즈 구하기



4. 하드코딩해보기  Q 하드코딩 한 것을 거꾸로 출력 !!  ( 선언 후 나중에 하드코딩도 가능)
		// 정방향 역방향 reverse 알려주기
		reverse(vect.begin(),vect.end());

5.  5개 원소의 컨테이너에 v[8]=5;  하면 버그..


6.   처음 선언할때 vector<int>v(10); 하면 가능  (초기화 시에는 v(10,5))


7. 문제

4 7 5 5 1 9 7 하드코딩 후
4 또는 5또는 9가 등장 할때 마다 result 배열에 값 넣고 출력하기
출력 결과는 4 5 5 9 
 
#include<iostream>
#include<vector>
using namespace std;
vector<int>v = { 4,7,5,5,1,9,7 };

vector<int> get459()
{
	vector<int>result2;
	for (int x = 0; x < v.size(); x++) {
		if (v[x] == 4 || v[x] == 5 || v[x] == 9) {
			result2.push_back(v[x]);
		}
	}
	return result2;
}

int main()
{
	vector<int>result;
	for (int x = 0; x < v.size(); x++) {
		if (v[x] == 4 || v[x] == 5 || v[x] == 9) {
			result.push_back(v[x]);
		}
	}

	for (int x = 0; x < result.size(); x++)cout << result[x];
	
	vector<int>ret = get459();
	for (int x = 0; x < ret.size(); x++)cout << ret[x];

	return 0;
}


8. 문제
숫자 하나 입력받고 입력받은 숫자만큼 숫자를 입력받기  ( n번 푸쉬백 또는  (n) 하기)
그다음 입력받은 숫자들의 합출력

3
1 2 4

출력결과: 7



9. 문제

3
abcd
btskbs
pd           

숫자하나 입력받고 vector에 입력받은 숫자 개수 만큼 문자열 입력받기
입력받은 후 가장 긴 문자열 출력!


#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	int n;
	cin >> n;
	vector<string>v(n);

	int Maxlen = 0;
	int index = 0;
	for (int x = 0; x < n; x++)
	{
		cin >> v[x];
		if (Maxlen < v[x].size()) {
			Maxlen = v[x].size();
			index = x;
		}
	}
	cout << v[index];

	return 0;
}


10. 이차배열의 형태
vector<vector<string>>v;

예를들어 vector<vector<string>>v={{1,2,3},{4,5}};
[0] 123
[1] 45

출력해 보세요~

#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<vector<int>>v = { {1,2,3},{4,5} };
int main()
{
	for (int y = 0; y < v.size(); y++)
	{
		for (int x = 0; x < v[y].size(); x++)
		{
			cout << v[y][x];
		}
		cout << endl;
	}

	return 0;
}

==========================================
	vector<int>vect(2);	
	vector<vector<int>>v(2);
	v[0].push_back(3);
	v[1].push_back(5);
==========================================

vector<vector<int>>v(2);

v.push_back({});

vector<vector<int>>v(2,vector<int>(3));

=============================================
5
0 0 0 1 0
0 0 1 0 0
0 0 0 1 1
1 0 1 0 1
0 0 1 1 0

===========================================


// 지역선언 


#include<iostream>
#include<vector>
using namespace std;

int main()
{
	freopen("텍스트.txt", "r", stdin);

	int n; cin >> n;

	vector<vector<int>>map(n,vector<int>(n));
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < n; x++)
		{
			cin >> map[y][x];
		}
	}

	vector<vector<int>>map2(n);
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < n; x++)
		{
			int a;
			cin >> a;
			map2[y].push_back(a);
		}
	}

	vector<vector<int>>map3;
	for (int y = 0; y < n; y++)
	{
		map3.push_back({});
		for (int x = 0; x < n; x++) {
			int a; cin >> a;
			map3[y].push_back(a);
		}

	}


	return 0;
}

================================================
// 전역 선언

#include<iostream>
#include<vector>
using namespace std;
vector<vector<int>>map;
int main()
{
	freopen("텍스트.txt", "r", stdin);
	//method 1
	//int n; cin>>n;
	//for (int y = 0; y < n; y++) {
	//	map.push_back({});
	//	for (int x = 0; x < n; x++)
	//	{
	//		int a;  cin >> a;
	//		map[y].push_back(a);
	//	}		
	//}

	// method 2

	int n; cin >> n;
	map.assign(n, vector<int>(n));
	for (int y = 0; y < n; y++) {
		for (int x = 0; x < n; x++)
		{
			cin >> map[y][x];
				
		}
	}


	return 0;
}

====================================================


//conclusion

#include<iostream>
#include<vector>
using namespace std;
vector<vector<int>>map2;
int main()
{
	int n;
	cin >> n;
	vector<vector<int>>map(n, vector<int>(n)); //  지역선언

	map2.assign(n, vector<int>(n)); // 전역선언



	return 0;
}
