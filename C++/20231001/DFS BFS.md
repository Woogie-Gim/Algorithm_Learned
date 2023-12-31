# DFS BFS

## 깊이 우선 탐색 (DFS)

- 깊이 우선 탐색은 그래프의 시작노드에서 출발하여 탐색할 한 쪽 분기를 정하여 최대 깊이 탐색을 마친 후 다른 쪽 분기로 이동하여 다시 탐색을 수행하는 알고리즘

- 특징 : 재귀 함수로 구현 / 스택 자료구조 이용 (FILO)
- 시간복잡도 (노드수 : V, 엣지 수 : E) : O(V + E)

- 깊이 우선 탐색은 실제 구현 시 재귀함수를 이용하므로 스택 오버플로에 유의

### 깊이 우선 탐색의 핵심 이론
- DFS는 한 번 방문한 노드를 다시 방문하면 안되므로 노드 방문 여부를 체크할 배열이 필요하며 그래프는 인접 리스트로 표현

1. DFS를 시작할 노드를 정한 후 사용할 자료구조 초기화
- DFS를 위해 필요한 초기 작업은 인접리스트로 그래프 표현
- 방문 배열 초기화
- 시작 노드 스택에 삽입

2. 스택에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 스택에 삽입
- 이제 pop을 수행하여 노드를 꺼냄
- 꺼낸 노드를 탐색 순서에 기입하고 인접리스틔 인접 노드를 스택에 삽입하여 방문 배열에 체크

3. 스택 자료구조에 값이 없을 때까지 반복하기
- 앞선 과정을 스택 자료구조에 값이 없을 때까지 반복
- 이때 이미 다녀간 노드는 방문 배열을 바탕으로 재삽입하지 않는 것이 핵심

## 너비 우선 탐색 (BFS)
- 너비우선탐색도 그래프를 완전 탐색하는 방법 중 하나
- 시작노드에서 출발해 시작노드를 기준으로 가까운 노드를 방문하면서 탐색하는 알고리즘

- 특징 : FIFO 탐색 / Queue 자료구조 이용
- 시간복잡도 (노드수 : V, 엣지 수 : E) : O(V + E)

- 너비 우선 탐색은 선입선출 방식으로 탐색하므로 큐를 이용해 구현
- 너비 우선 탐색은 탐색 시작 노드와 가까운 노드를 우선하여 탐색하므로 목표 노드에 도착하는 경로가 여러 개 일 때 최단 경로를 보장

### 너비 우선 탐색의 핵심 이론
1. BFS를 시작할 노드를 정한 후 사용할 자료구조 초기화하기
- BFS도 DFS와 마찬가지로 방문했던 노드는 다시 방문하지 않으므로 방문한 노드를 체크하기 위한 배열이 필요
- 그래프를 인접리스트로 표현하는 것 역시 DFS와 동일
- 하나 차이점이 있다면 탐색을 위해 스택이 아닌 큐를 사용

2. 큐에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 큐에 삽입
- 큐에서 노드를 꺼내면서 인접 노드를 큐에 삽입
- 방문 배열을 체크하여 이미 방문한 노드는 큐에 삽입하지 않는다
- 큐에서 꺼낸 노드는 탐색 순서에 기록

3. 큐 자료구조에 값이 없을 때까지 반복
- 큐에 노드가 없을 때까지 앞선 과정을 반복