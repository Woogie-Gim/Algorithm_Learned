# Priority_Queue (우선 순위 큐)

- Priority_Queue는 Queue의 한 종류로 이름 그대로 우선순위에 따라 정렬된 Queue
- 어떤 원소가 Push(삽입)된다면 주어진 우선순위에 맞춰서 Queue가 정렬되고, Pop(삭제)는 정렬된 Queue의 앞에서 이루어진다.
- 자료 구조 Heap으로 구현되었기 때문에, 특정 원소를 Push해 생기는 정렬 과정은 O(logN) 만에 이루어진다.

## C++ STL 우선순위큐 라이브러리 기본 명령어

```c++
#include <queue>
```
- queue와 동일한 library에서 지원해준다

### 선언
- priority_queue<자료형, Container, 비교함수>변수명
  - 선언한 자료현 변수들을 비교함수에 따라 정렬하는 Priority_Queue(우선순위큐)를 선언

- priority_queue<자료형> 변수명
  - 선언한 자료형 변수들을 내림차순에 따라 정렬하는 Priority_Queue(우선순위큐)를 선언

```c++
// ex)
#include <queue>

priority_queue<int, vector<int>, cmp>pq;

/* int형 변수들을 cmp 우선순위에 따라 정렬하는 pq라는 이름의 Priority_Queue(우선순위큐)를 선언 */
```

### 추가 및 삭제
- push(element): 우선순위큐에 원소를 삽입. (비교함수에 따라 내부적으로 정렬됨)
- pop() : 맨 앞에 있는 원소를 삭제

### 서칭
- top() : 맨 앞에 있는 원소를 반환

### 기타
- empty() : 우선순위큐가 비어있는 true 아니면 false를 반환
- size() : 우선순위큐의 크기를 반환

### 예시 1) 기본 - 내림 차순

```c++
#include <iostream>
#include <queue>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	priority_queue<int> pq;
	pq.push(5);
	pq.push(1);
	pq.push(7);

	for (int i = 0; i < 3; i++)
	{
		cout << pq.top() << " ";
		pq.pop();
	}

	return 0;
}
```
- 아스키코드 값이 큰 순서대로 정렬

#### 예시2) 기본 - 올림차순

```c++
#include <iostream>
#include <queue>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	priority_queue<int, vector<int>, greater<int>> pq;

	pq.push(5);
	pq.push(1);
	pq.push(7);

	for (int i = 0; i < 3; i++)
	{
		cout << pq.top() << ' ';
		pq.pop();
	}

	return 0;
}
```

- greater<int>

### 비교함수 선언
- 내가 원하는 우선순위를 지정하려면 연산자 오버로딩을 통해 원하는 우선순위대로 구현 가능

```c++
#include<iostream>
#include<queue>
using namespace std;
int arr[8] = { 4,7,8,1,5,3,6,9 };

// 구조체에 비교 연산자를 정의

struct cmp {
    bool operator()(int back, int front) {
        return front < back;
    }
};

int main()
{
    priority_queue<int, vector<int>, cmp>pq;


    for (int x = 0; x < 8; x++)
    {
        pq.push(arr[x]);
    }
    for (int x = 0; x < 8; x++)
    {
        cout << pq.top();
        pq.pop();
    }

    return 0;
}
```

```c++
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int arr[6] = { 2,6,3,1,7,4 };
struct cmp {
    bool operator()(int b,int f) {
        if (f % 2 == 0 && b % 2 == 1)return true;
        if (f % 2 == 1 && b % 2 == 0)return false;
        return b < f;
    }
};
int main()
{
    priority_queue<int, vector<int>, cmp>pq;
    for (int x = 0; x < 6; x++)pq.push(arr[x]);

    for (int x=0; x < 6; x++) {
        cout << pq.top() << " ";
        pq.pop();
    }

    return 0;
}
```

```c++
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int arr[5] = { 11,6,3,1,4 };
struct node {
    int a;
};

bool operator<(node b, node f) {
    if (f.a % 2 == 0 && b.a % 2 == 1)return true;
    if (f.a % 2 == 1 && b.a % 2 == 0)return false;
    return b.a < f.a;

}
int main()
{
    priority_queue<node>pq;
    node arr2[5];
    for (int x = 0; x < 5; x++) {
        arr2[x].a = arr[x];
        pq.push(arr2[x]);
    }

    while (!pq.empty())
    {
        cout << pq.top().a << " ";
        pq.pop();
    }
    return 0;
}
```

```c++
3  4  1  2  3
A  B  C A  Q

우선순위 조건..
1. 숫자 오름차순
2. 알파벳 오름차순..


#include<iostream>
#include<queue>
using namespace std;

struct node {
    int num;
    char ch;
};

node vect[5] = {
    {3,'A'},
    {4,'B'},
    {1,'C'},
    {2,'A'},
    {3,'Q'},
};

// 우선순위 조건
// 숫자 오름
// 문자 오름
priority_queue<node>q;

bool operator<(node t1, node t2)  // 외워주세요.. ㅜㅜ  // t2앞에꺼 t1뒤에꺼
{
    if (t2.num < t1.num)return true;
    if (t2.num > t1.num)return false;
    return t2.ch < t1.ch;
}
int main()
{

    for (int x = 0; x < 5; x++) {
        q.push(vect[x]);
    }
    
    for (int x = 0; x < 5; x++) {
        cout << q.top().num<<q.top().ch<<endl;
        q.pop();
    }
    
    return 0;
}
```

```c++
/* pair 자료형
  // second 오름
  // first 오름 
  {1,10},
  {23,3},
  {3,2},
  {2,3} */

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

struct node {
    int a, b;
};
node input[4] = {
    {1,10},
    {23,3},
    {3,2},
    {2,3}
};
struct cmp {
    bool operator()(pair<int,int>b,pair<int,int>f)
    {
        if (f.second < b.second)return true;
        if (f.second > b.second)return false;
        return f.first < b.first;
        
    }
};
int main()
{
    priority_queue<pair<int,int>, vector<pair<int, int>>, cmp>pq;
    pq.push({ 1,10 });
    pq.push({ 2,3 });
    pq.push({ 23,3 });
    pq.push({ 3,2 });
    
    
    for (int x = 0; x < 4; x++) {
        cout << pq.top().first << " " << pq.top().second << "\n";
        pq.pop();
    }
    return 0;
}
```

```c++
// 나이가 어림
// 이름은 알파벳순

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

struct node {
    string str;
    int age;
};

node arr[5] = {
    {"bob",20},{"jason",23},{"choi",20},{"tom",40},{"jenny",18}
};
struct cmp {
    bool operator()(node b, node f) // back front
    {
        if (f.age < b.age)return true;
        if (f.age > b.age)return false;
        return f.str < b.str;
    }
};

int main()
{
    priority_queue<node, vector<node>,cmp>pq;
    for (int x = 0; x < 5; x++)
    {
        pq.push(arr[x]);
    }
    for (int x = 0; x < 5; x++)
    {
        cout << pq.top().str << " " << pq.top().age << endl;
        pq.pop();
    }


    return 0;
}
```

```c++
// 배열안의 값이 작은 숫자가 적인
// 좌표값 뽑기

#include<iostream>
#include<string>
#include<queue>
using namespace std;

struct node {
    int y, x;
    int num;
};
int map[3][3] = {
    22,2,5,
    1,6,3,
    2,5,7
};
priority_queue<node>q;


bool operator<(node back, node front)
{
    return front.num < back.num;
}
int main()
{
    for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
            q.push({ y, x, map[y][x] });
        }
    }

    for (int x = 0; x < 9; x++) {
        cout << q.top().y << " " << q.top().x << endl;
        q.pop();
    }

    return 0;
}
```