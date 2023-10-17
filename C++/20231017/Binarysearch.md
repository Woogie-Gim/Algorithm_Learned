# BS : Binary Search

- 빠른 검색 / 탐색 방법
- Binary Search Tree : Binary Search를 통해 Tree 라는 구조에 저장하는 방식 자료

![Alt text](images/binarysearch.gif)

## 이진 탐색
- up down 게임 진행 방식과 같다
- 중앙값 부터 검색을 시작하는 것이 가장 유리 / 이진 검색도 같다

```
정수 n개 입력
target 변수가 정수 n개 안에 있는지 없는지 찾는다

4   7   9   11  13  15  19
start       mid         end

mid = (start + end) //2
mid < target
start = mid + 1

mid > target:
end = mid - 1

mid == target?

O(log n)의 속도로 탐색

데이터 값을 정렬 후에 진행을 해야한다.
```

### Binary Search 이진 탐색
- (단, 정렬이 되어 있는 상태의 data)
- 원하는 값을 찾을 때 for문 돌려서 O(n)의 속도가 아닌 O(logn)의 속도로 원하는 값을 탐색 할 수 있게 하는 알고리즘(탐색 기법)

- 정렬이 되어 있는 data 의 mid 값을 찾은 후 target과 비교 후
  - mid > target: end = mid - 1 로 줄이고

  - mid < target: start = mid + 1로 늘려가며 원하는 값을 찾아가는 방식
  

### 정렬 sort()
- sort() 함수는 C++의 algorithm 헤더에 포함되어 있다.

```C++
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
  int a[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
  sort(a, a + 10);

  vector<int> v[10] = {9, 3, 5, 4, 1, 10, 8, 6, 7, 2};
  sort(v.begin(), v.end());
}
```
- 기본적으로 오름차순으로 정렬을 수행한다.
- 배열의 시작점 주소와 마지막 주소 + 1을 적으면 된다.
- vector sort와 다르다는 점 유의

```C++
/* 변수 */ 
// start, end : 검사 범위의 시작점과 끝점의 인덱스를 가리키기 위한 변수
// mid : 검사 범위 내에서 실질적으로 검사하는 인덱스를 가리키는 변수로, 검사 범위의 중간에 있는 값

vector<int> nums;
int start = 0;
int end = nums.size() - 1;
int mid = (low + high) / 2;
```

### 이분 탐색 단계
- 리스트 혹은 배열은 무조건 정렬된 상태이어야 한다.
  1. 검사 범위에서 중간값 mid을 선택하여 찾고 있는 값이 맞는지 확인한다.
  2. 만약 찾는 값이 맞으면 해당 값 리턴한다.
  3. 만약 찾는 값이 중간 값보다 크면 검사 범위를 큰 쪽으로 다시 탐색한다.
    - mid > target 이면 high = mid - 1
  4. 반대로 찾는 값이 중간 값보다 작으면 검사 범위를 작은 쪽으로 다시 탐색한다.
    - mid < target 이면 low = mid + 1
  5. 앞의 과정을 원하는 값을 찾을 때까지 반복한다.
  6. 반복하다가 더 이상 찾지 못하고 검사할 곳도 없으면 (low > high) 돌아간다

### 이분 탐색 구현

```c++
/* 직접 구현 - 반복문 */
bool binary_search(vector<int> arr, int target)
{
  int start = 0;
  int end = arr.size() - 1;
  while (start <= end)
  {
    int mid = (start + end) / 2;
    if (target == arr[mid]) return true;
    if (target < arr[mid]) end = mid - 1;
    else if (target > arr[mid]) start = mid + 1;
  }
  return false;
}


/* 직접 구현 - 재귀 */
bool binary_search(vector<int> arr, int start, int end, int target)
{
  if (start > end) return false;
  int mid = (start + end) / 2;

  if (arr[mid] == target) return true;
  if (arr[mid] > target) return binary_search(arr, start, mid - 1, target);
  else return binary_search(arr, mid + 1, end, target);
}

/* STL 이용 */

// binary_search의 기본형
template <class ForwardIterator, class T>
  bool binary_search (ForwardIterator first, ForwardIterator last, const T& val)


#include<iostream>
#include<algorithm>
using namespace std;
 
//STL를 이용한 이진탐색을 이용하여 탐색
int main(void){
    int n= 100;
    int arr[n];
 
    for(int i=0; i<n; i++){
        arr[i] = i;
    }
 
    cout << "exist : " << binary_search(arr, arr+n, 70) << endl;
    
    return 0;
}
```

## 매개 변수 탐색
- 이진 탐색을 사용하여 조건을 만족하는 최대값을 구하는 방법
  - 최적화 문제를 "결정문제"로 풀 수있는 알고리즘

### 매개변수와 결정함수
- 매개 변수 탐색(Parametric search)에서는 매개변수와 결정함수를 정하는 것이 중요하다.

1. 매개변수 param
- 매개변수 탐색은 일반적으로 조건에 만족하는 최소/최대값을 찾는 문제이다. 이 때, 검사하는데 사용하는 매개변수를 param이라 한다.
- param은 검사범위 에서의 중간값 이다.
- 즉, param은 이진 탐색에서와 같이 mid = (start + end) / 2

2. 결정함수 fn(param)
- 결정함수는 param이 조건을 만족하면 true, 만족하지 않으면 false를 반환하는 함수이다. 반환 값에 따라 검사 범위를 변경한다.
- 매개변수의 범위는 연속이어야 하는데, 결정함수의 값이 전환되는 부분이 생긴다. 이때, true를 반환할 때의 매개변수가 문제의 정답이되는 최대 / 최소값이 된다.
- 결정함수의 결과에 따라 검사 범위를 변경해주어야 한다.

### 매개 변수 탐색 단계
- 조건을 만족하는 최대값을 탐색할 경우

1. 배열 가운데 위치한 x를 결정함수에 대입해 조건을 만족하는지 알아본다.
2. 조건을 만족한다면 검사 범위를 x보다 큰 쪽으로 설정한다. 조건을 만족하지 않는다면 검사범위를 x보다 작은 쪽으로 설정한다.
3. 1-2번 과정을 살펴볼 배열이 남아있지 않을 때까지 반복한다.
  