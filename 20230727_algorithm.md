# 0. 모듈러의 성질

+ 모듈러 연산이란? 나머지연산을 뜻한다. print(5%3) => 2 가 나오는거.

```python
print(5%3) # 2
print((5+8)% 3 ) # 1
print((5%3 + 8%3) %3) # 1
```

+ 해당 식을 통해서 (a+b)% c == (a%c + b%c) %c 를 도출할 수 있다.

```
- n = ac + d
- n// c  => a
- n%c => d

a = xc + y
b = wc + z
  = (x+w)c + y + z

(a + b) % c == (a%c + b%c) % c
(a * b) % c == (a%c * b%c) % c
(a - b) % c == (a%c - b%c + c) % c
            == (a%c - b%c + kc)%c (k는 임의의 양수 가능)
(a//b) % c ==> 수학적으로는 되지만, 코딩할 땐 안된다고 생각하자!
           ==> 더 정리하고자 한다면 페르마의 소정리를 공부해보자 a^p % p = a
```

+ 최대 연산
  + java , c : int=> 21억 , long, long long => 21억 * 21억 *2
  + python 역시 기본적으로 21억 * 21억 * 2 ( 그 이상은 느려진다. )



+ 1부터 1000000000 의 합의 % 1000000007

```python
total = 0
for i in range(1,100000001):
    total += i
    total %= 1000000007

print(total)
1000000007
```



# 1. 소수 판정

+ 자연수 하나를 입력 받아서 이 수가 소수면 YES, 소수가 아니면 No를 출력한다
+ 1을 조심해야한다.

```python
# 1. 완전 탐색으로 소수 판정 하는 방법
# n 제한이 일반적으로 10^12 정도로 나오게 되는데, 이럴 경우 완탐으로 돌면 시간초과에 걸리게 된다.

n = int(input()) # 자연수 하나를 입력 받는다.

cnt = 0 
for i in range(1,n+1):
    if n%i == 0:
        cnt +=1
        
if cnt == 2:
    print('YES')
else:
    print('NO')
   
```



```python
#2 1~ root n 까지의 약수가 정확히 하나인지 구한다.

# 이론
# 12의 약수
# 1 2 3 4 6 12
# (1,12) (2,6) (3,4) 의 순서쌍을 볼 수 있다.
# 왼쪽 <= sqrt(오른쪽) 이하임을 알 수 있다.

n = int(input()) # 자연수 하나를 입력 받는다.

cnt = 0 
for i in range(1,n+1):
    # 루트 이상일 경우 break로 더이상 계산하지 않는다. sqrt와 같은 실수연산은 되도록 안하도록 하자.
    if i * i > n:
        break
    if n%i == 0:
        cnt +=1
        
if cnt == 2:
    print('YES')
else:
    print('NO')
```





# 2. 약수구하기

```python
# 1. 완탐으로 하는 방법
n = int(input()) # 자연수 하나를 입력 받는다.
prime = []

for i in range(1,n+1):
    if n % i = 0:
        prime.append(i)

print(*prime)
```



```python
# 2. 순서쌍으로 하는방법 ( => 제곱수를 조심해야 한다. )
# 약수의 개수가 홀수 <=> 제곱수랑 필요충분조건이다(=동치다)
n = int(input()) # 자연수 하나를 입력 받는다.
prime = []

for i in range(1,n+1):
    if i*i > n:
        break
        
    if n % i = 0:
        prime.append(i)
        if i*i != n: # 밑에서 제기한 제곱수를 막기 위한 방법
        	prime.append(n//i)

prime(*prime)

# but 이럴 경우, 제곱 들이 문제가 된다.
# 4 일경우
# 1 2 2 4 이런식으로 나오게 된다.


```





# 3. 소인수 분해

```python
# 1. 완탐으로 하는 방법
n = int(input())
for i in range(2, n+1):
    while n % i == 0:
        print(i)
        n //= i

# 방식
# 12 인경우?
# 12 => 6 => 3 => 1 로 내려간다. 즉 나눠진 것들대로 출력하면된다.
```



```python
# n => a, b, c, d, e, f, g, h , i
# a*b*c*d*e*f*g*h*i => n

# 이떄 소인수가 sqrt n 보다 큰 경우는 많아봐야 1개이거나 없다.
n = int(input())

x = n # n 이 불변해야 i*i > n 이 성립하니까

for i in range(2,n+1):
    if i * i > n:
        break
        
    while x% i == 0:
        print(i)
        x //= i
if x != 1:
    print(x)

```





# 4. 유클리드 호제법

+ 목표 : 두 자연수 a, b 가 주어질 때 이 둘의 최대 공약수를 구한다. (log n)
+ a < b일 때 a와 b-a를 남기는 작업을 반복하면된다.

```python
# 최대 공약수를 구하는 방법(gcd)
a,b = map(int,input().split()) # a > b 라고 하자

while a&b != 0:
    a, b = b, a % b

print(b)
    
```



```python
# 최소 공배수를 구하는 방법(LCM) 
# 유클리드 호제법의 응용
a,b = map(int,input().split()) # a > b 라고 하자

A, B = a,b
while a&b != 0:
    a, b = b, a % b

print(A * B // b) # = > 구하고자하는 값 A,B 를 곱해준 뒤, 최대 공약수를 나누어주자.
    
```





# 5. 에라토스테네스의 체

![에라토스](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)



```python
# 목표: 1~n 까지의 자연수 중 소수를 모두 출력한다.
n = int(input())
isPrime = [True for i in range(n+1)]

#1. 완탐으로 하는 방법
isPrime[0] = False
isPrime[1] = False # 1은 소수가 아니니까!!
for i in range(2,n+1):
    if not isPrime[i]:
        continue
    
    for j in range(2*i,n+1,i):
        isPrime[j] = False

print(*[i for i in range(n+1) if isPrime[i]])
```



```python
# 목표: 1~n 까지의 자연수 중 소수를 모두 출력한다.
n = int(input())
isPrime = [True for i in range(n+1)]

#2. 가지치기 한 방법
isPrime[0] = False # 0 역시도 아니니까!
isPrime[1] = False # 1은 소수가 아니니까!!
for i in range(2,n+1):
    if not isPrime[i]:
        continue
    
    for j in range(i*i,n+1,i): # i 보다 작은 값은 이미 미리 봤으니까!
        isPrime[j] = False
        
print(*[i for i in range(n+1) if isPrime[i]])
```



```python
# 응용  :2 ~ n 까지의 자연수 각각의 가장 작은 소인수 출력

n = int(input())
prime = [-1 for i in range(n+1)]
for i in range(2,n+1):
    if prime[i] != -1:
        continue
    
    prime[i] = i
    for j in range(i*i, n+1, i):
        if prime[i] == -1:
            prime[i] = i

print(*prime[2:])

```





# 6. 빠른 거듭제곱



(n**m) % 1000000007 (n<=100, m<=1,000,000,000,000,00,000)



```python
# 파이썬의 경우
pow(n,m,1000000007)
```



```python
3**28을 구할 떄

ans = i
for i in range(3):
    ans *= 3
    ans %= 100000007

ans *= ans
ans *= 3
ans %= 100000007

ans *= ans
ans %= 100000007
# ??????
```



+ 재귀로 구하는 방법

```python
def pows(n,m):
    if m == 0:
        return 1
    
    ret = pows(n,m//2)
    ret *= ret
    ret %= 100000000007
    
    if m % 2 == 0:
        return ret
   	else:
        return (ret * n) % 100000000007
```



### Bonus 1. 1~n 까지의 k의 배수의 개수

```python
n = int(input())

print(n//k) # 완벽한 덩어리의 개수가 k의 배수가 된다.
```





### Bonus 2. 팩토리얼에 곱해진 소수의 개수

```python
# n!를 p로 몇번 나눌 수 있는지

# p 가 소수여야 가능한 방법
# 20!에 곱해진 2의 개수

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#   1   1   1   1    1     1     1     1     1     1
#       1       1          1           1           1
#               1                      1            
#                                      1

# 20// 2 + 20//4 + 20 // 8 + 20//16
# n// p + n//p^2 + n// p^3 + n// p^4.......

n, p = map(int,input().split())

cnt = 0
x = p
while x <= n:
    cnt += n//x
    x*= p

print(cnt)
```



```python
# 소수가 아닐 경우

# 20 에서 10인경우?
# 2 와 5 의 개수를 구한뒤, 최소개수를 답으로

# 20에서 20인경우?
# 2와 5의 개수를 구한 뒤, 2의 개수에 나누기 2를 한 뒤 최소개수를 답으로.
```
