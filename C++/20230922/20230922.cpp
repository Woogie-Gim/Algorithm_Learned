/*연결 리스트*/

/*
원소를 저장할 때 그 다음 위치를 저장하는 방식의 리스트

연결 리스트의 성질
1. k번째 원소를 확인 / 변경하기 위해 O(k)가 필요함

3 -> 13 -> 72 -> 5
72를 찾기 위해선 3, 13을 거쳐야함

2. 임의의 위치에 원소를 추가 / 임의 위치의 원소 제거는 O(1)
3. 원소들이 메모리 상에 연속해있지 않아 Cache hit rate가 낮지만 할당이 다소 쉬움


연결 리스트 종류
1. 단일 연결 리스트 (Singly Linked List) : 각 원소가 자신의 다음 원소의 주소를 가지고 있는 리스트
2. 이중 연결 리스트 (Doubly Linked List) : 각 원소가 자신의 다음 이전 원소의 주소를 모두 가지고 있는 리스트
3. 원형 연결 리스트 (Circular Linked List) : 끝이 처음과 연결되어 있음

배열과 리스트는 모두 선형구조
								배열				리스트
k번째 원소의 접근					O(1)			 O(k)
임의 위치에 원소 추가/제거			O(N)			 O(1)
메모리 상의 배치					연속				 불연속
추가적으로 필요한 공간				 -				 O(N) -> 주소값을 가지고 있어야함
(Over head)

기능과 구현

임의의 위치에 있는 원소를 확인/변경, O(N)

임의의 위치에 원소를 추가, O(1)
임의의 위치에 원소를 제거, O(1)
=> 임의의 위치에 원소를 추가 / 제거를 많이 할 경우 연결리스트가 효율적

Node 구주체나 클래스를 만들어서 원소가 생성 될 때 동적할당 되는 구조

연결리스트 구조

struct NODE {
	struct NODE *prev, *next;
	int data;
};

코딩테스트의 경우는 STL list가 doubly linked list 이기 때문에 가져다 쓰면 됨

STL list

#include <bits/stdc++.h>
using namespace std;

int main(void) {
	list<int> L = { 1,2 }; // 1 2
	list<int>::iterator t = L.begin(); // t는 1을 가리키는 중
	L.push_front(10); // 10 1 2
	cout << *t << '\n'; // t가 가리키는 값 = 1을 출력
	L.push_back(5); // 10 1 2 5
	L.insert(t, 6); // t가 가리키는 곳 앞에 6을 삽입, 10 6 1 2 5
	t++; // t를 1칸 앞으로 전진, 현재 t가 가리키는 값은 2
	t = L.erase(t); // t가 가리키는 값을 제거, 그 다음 원소인 5의 위치를 반환
					// 10 6 1 5, t가 가리키는 값은 5
	cout << *t << '\n'; // 5
	for (auto i : L) cout << i << ' ';
	cout << '\n';
	for (list<int>::iterator it = L.begin(); it != L.end(); it++)
		cout << *it << ' ';
}
*/

// 정석 구현
#include<iostream>
using namespace std;
struct node {
	int a;
	node *next;
};

node *head, *last;

void addnode(int value){
	if (head == NULL)
	{
		head = new node();
		head->a = value;
		last = head;
	}
	else {
		last->next = new node();
		last = last->next;
		last->a = value;
	}
}
int main()
{

	addnode(3);
	addnode(5);
	addnode(2);
	addnode(7);
	addnode(87);
	addnode(1);

	return 0;
