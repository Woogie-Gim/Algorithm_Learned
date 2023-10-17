# STL : map

### Map 이란?
- map은 각 노드가 key와 value 쌍으로 이루어진 트리
- 특히, 중복을 허용하지 않는다
- 따라서 map은 first, second가 있는 pair 객체로 저장되는데 first - key로 second - value로 저장
- C++의 map 내부 구현은 검색, 삽입, 삭제가 O(log n)인 레드블랙트리로 구성되어 있다.

### Map 기본 형태
```C++
map<key, value> mapl;
```

### Map 정렬
- map은 자료를 저장할 때 내부에서 자동으로 정렬된다.
- map은 key를 기준으로 정렬하며 오름차순으로 정렬한다.
- 만약 내림차순으로 정렬하고 싶은 경우
```C++
map<int, int, greater>mapl;
```
- 만약 다른 방법으로 int 데이터를 내림차순으로 정렬하고 싶을 경우 데이터에 -(마이너스)를 붙여 삽입하여 처리하면 내림차순으로 정렬

### 기본적인 메소드
- begin() : 첫 번째 원소의 iterator (반복자)를 반환한다. (즉 map의 원소를 반복자를 이용해서 접근할 수 있다.)
- end() : 마지막 원소 다음의 반복자를 반환
- clear() : 저장하고 있는 모든 원소를 삭제한다.
- insert() : 원소를 추가한다.
- find() : key와 관련된 원소의 반복자를 반환한다. (단 찾지 못한 경우 end() 반복자를 반환한다.)
- size() : 원소의 개수를 반환
- erase() : 해당 원소를 삭제한다.

```c++
// 함수의 원형

/* inser() */
pair insert( const value_type& _Val ); 
iterator insert( iterator _Where, const value_type& _Val );
template void insert( InputIterator _First, InputIterator _Last );

// 중복값을 허용하지 않기 때문에 key가 중복될 경우 insert 되지 않는다.

/* find() */
iterator find( const Key& _Key );
const_iterator find( const Key& _Key ) const;

/* erase() */
iterator erase( iterator _Where );
iterator erase( iterator _First, iterator _Last );
size_type erase( const key_type& _Key );
```

### 예제 코드
1. 정수형(int)을 key, value로 사용

```C++
#include <iostream>
#include <map>

using namespace std;

int main()
{
	map<int, int> ma;

	// 원소 추가
	ma.insert(make_pair(1, 3)); // key 값 : 1, value : 3
	ma.insert(make_pair(3, 13)); // key 값 : 3, value : 13

	// operator [] 를 사용하여 원소 추가
	ma[5] = 10;
	ma[4]++; // 특이하지만 이런 방법도 가능하다.key : 4인 원소가 없으므로 생성한뒤 기본값 : 0 에서 1을 더해준다.

	// make_pair 형식으로 저장 했으므로
	// key 값은 first로 접근 value 값은 second 로 접근
	for (auto iter = ma.begin(); iter != ma.end(); ++iter)
	{
		cout << "key : " << iter->first << " value : " << iter->second << "\n";
	}

	cout << "\n" << "\n";

	cout << "검색 하기!!" << '\n';
	cout << "key : 5 인 Value : ";
	cout << ma.find(5)->second << '\n' << '\n';

	// key : 3인 원소를 지워보자
	ma.erase(3);

	for (auto iter = ma.begin(); iter != ma.end(); ++iter)
	{
		cout << "key : " << iter->first << " value : " << iter->second << "\n";
	}
	cout << "\n";


	return 0;
}
```

- 결과

![Alt text](<images/map method.JPG>)

2) string을 key 또는 value로 사용

```c++
#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	map<int, string> ma;

	cout << "value를 string 으로" << "\n" << "\n";

	// insert
	ma.insert(make_pair(3, "red"));
	ma.insert(make_pair(1, "blue"));

	// operator [] 를 활용한 insert
	ma[5] = "black";

	for (auto iter = ma.begin(); iter != ma.end(); ++iter)
	{
		cout << "key : " << iter->first << " , value : " << iter->second << "\n";
	}
	cout << "\n" << "\n";

	cout << "String 을 key 값으로 사용" << "\n" << "\n";

	map<string, int> m;
	m.insert(make_pair("red", 3));
	m.insert(make_pair("blue", 1));

	// operator [] 를 활용한 insert
	m["black"] = 5;
	for (auto iter = m.begin(); iter != m.end(); ++iter)
	{
		cout << "key : " << iter->first << " , value : " << iter->second << "\n";
	}

	cout << "\n";
}
```

![Alt text](<images/map method.JPG>)

### upper_bound, lower_bound 메서드
- upper_bound 메서드의 경우 컨테이너의 오른쪽 원소 중 기준 원소보다 큰 값 중 가장 왼쪽에 있는 원소의 iterator 값을 리턴한다.
- lower_bound 메서드의 경우 오른쪽 원소 중 기준 원소와 같거나 큰 값 중 가장 왼쪽에 있는 원소의 iterator 값을 리턴한다.
- 차이점은 같은 값을 포함하느냐 마느냐 차이만 있다.

```c++
mymap['a'] = 20;
mymap['b'] = 40;
mymap['c'] = 60;
mymap['d'] = 80;
mymap['e'] = 100;

itlow = mymap.lower_bound('b');
itup = mymap.upper_bound('d');

// 위 코드의 경우 itlow는 b를 itup은 e를 가르키는 iterator가 된다.
```