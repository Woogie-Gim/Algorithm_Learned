# Sort 함수

- algorithm 라이브러리 사용

```c++
#include <algorithm>
```

- 기본형 : sort(시작, 끝, 조건)
- 특이 사항은 sort 내장함수 뿐만 아니라 C++ 에서의 STL에서 시작은 배열의 처음칸인데 끝이라는 곳은 끝의 다음 곳을 가르킨다.

```c++
// auto -> 변수 선언 시 초기화 선언 후 값 못 넣음
// 매개변수로 사용불가! 하지만 리턴값의 자료형으로 사용가능
// 구조체의 맴버변수로 사용 불가능!

#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int>vect = { 3,2,6,3,1,7 };

	// 이터레이터 (포인터)
	for (auto x = vect.begin(); x != vect.end(); x++) // 마지막 원소의 바로 뒤를 가르킨다!!
	{
		cout << *x;
	}

	return 0;
}
```

- 즉, 특이하게도 배열에 없는 칸, 배열의 마지막 칸 다음칸의 주소 값을 보낸다.
- sort 함수는 일차배열 또는 vector를 정렬할 때 쓰인다
- string 문자열 정렬할 때도 사용이 가능하다.

```c++
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int arr[5] = { 4, 1, 5, 2, 7 };
	sort(&arr[0], &arr[5]); // 시작점, 마지막 + 1 (오름차순)
	sort(arr, arr + 5, greater<int>()); // 시작점, 마지막 + 1 (내림차순)

	vector<int> vect = { 3, 6, 1, 2, 7, 4 };
	sort(vect.begin(), vect.end(), greater<int>());

	string str = "vsdrqzdxdca";
	sort(str.begin(), str.end());

	return 0;
}
```

- string "배열" sort

```c++
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	string arr[5] = { "INC", "JFK", "HND", "ATL", "PVG" };

	sort(arr, arr + 5, greater<string>());

	for (int x = 0; x < 5; x++)
	{
		cout << arr[x] << "\n";
	}

	return 0;
}
```

### Sort 정리

- char or string "배열"은 sort(aaq, aaq + 8);
- 배열 "아닌" string or vector는 begin / end 사용 sort(ar.begin(), ar.end());

### 다중 조건
- 단순한 오름차순 내림차순 조건이 아닌 다중 조건일 경우 compare 함수를 운영 해야한다.

### 예1) 1. 짝수 우선순위 2. 오름차순 순위

```c++
#include<iostream>
#include<algorithm>
using namespace std;
bool compare(int a, int b)
{
    if (a % 2 == 0 && b % 2 == 1)return true; // a우선순위가 높다
    if (a % 2 == 1 && b % 2 == 0)return false;
    return a < b;  // 둘다 홀수 또는 둘다 짝수일때는 
}
int main()
{
    /*우선순위 조건
        1. 짝수 우선
        2. 오름차순*/
    
    int arr[5] = { 4,1,5,2,7 };
    sort(arr, arr+5, compare);
    
    
    
    return 0;
}
```

### 예2) BTSGOOD / 1. H ~ O 우선 2. 오름차순 출력
```c++
#include<iostream>
#include<algorithm>
using namespace std;
bool compare(char a, char b)
{
    int aa=0, bb = 0;
    if (a >= 'h' && a <= 'o')aa = 1;
    if (b >= 'h' && b <= 'o')bb = 1;

    if (aa == 1 && bb == 0)return true;
    if (aa == 0 && bb == 1)return false;

    return a < b;
}
int main()
{
    /*1. H~O 우선
    2. 오름차순 출력
    */char arr[10] = "btsgood";
    
    sort(arr, arr + 7,compare);
    
    return 0;
}
```

### 예 3) 1. 숫자 내림 차순 2. 문자가 오름 차순

```c++
A B B A
1 2 1 9 

#include<iostream>
#include<algorithm>
using namespace std;
struct abc {
    char ch;
    int num;
};
bool compare(abc a, abc b)
{
    if (a.num > b.num)return true;
    if (a.num < b.num)return false;
    return a.ch < b.ch;
}
int main()
{


    abc arr[4] = {
        {'A',1},
        {'B',2},
        {'B',1},
        {'A',9},
    };

    sort(arr, arr + 4, compare);


    return 0;
}

```