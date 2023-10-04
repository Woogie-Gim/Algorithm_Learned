# string class
- char 변수와 다르게 문자열 끝에 '\0' 문자가 들어가지 않으며, 문자열의 길이를 동적으로 변경 가능 하다.
- 
## 스트링 헤더 파일
```c++
#include <iostream>
#include <string>
using namespace std;

int main()
{
  string a = "ABCD";
  cout << a;
  // ABCD
  return 0;
}
```

## 문자열 메서드
- string str; : 문자열 생성
- cin >> str; : 공백(space) 이전까지의 문자열을 입력받는다
- getline(cin, str) : \n 이전까지의 문자열, 즉 한 줄을 통째로 입력받는다
- getline(cin, str, 'a') : 'a' 문자 이전까지의 문자열을 입력받는다
- length() : 문자열 길이 출력
- find() : 특정 문자열이 어디에 있는지 검색하여, index를 알려준다
- substr() : 특정 index 부터 몇 글자수 문자열을 추출한다
- stoi() : 문자열을 수로 변환하는 메서드
- to_string() : 숫자 타입의 데이터를 스트링 타입으로 변환
- isdigit(c) : c문자가 숫자이면 true, 아니면 false를 반환
- isalpha(c) : c문자가 영어이면 true, 아니면 false를 반환
- toupper(c) : c문자를 대문자로 변환
- tolower(c) : c 문자를 소문자로 변환