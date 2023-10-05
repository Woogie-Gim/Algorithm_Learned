# memeset

- memset 함수는 메모리의 값을 원하는 크기만큼 특정 값으로 세탕할 수 있는 함수
- memory + setting

배열 초기화 하기
```c++
#include <cstring>
memset(배열, 0, sizeof(배열))
```

- vector에선 사용할 수 없다