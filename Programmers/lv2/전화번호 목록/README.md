[전화번호 목록](https://programmers.co.kr/learn/courses/30/lessons/42577)
```python
def solution(phone_book):
    phone_book.sort()
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startswith(num1):
            return False
    return True
```
```bash
정확성 테스트
테스트 1 〉	통과 (0.03ms, 10.6MB)
테스트 2 〉	통과 (0.03ms, 10.7MB)
테스트 3 〉	통과 (0.05ms, 10.7MB)
테스트 4 〉	통과 (0.04ms, 10.6MB)
테스트 5 〉	통과 (0.03ms, 10.6MB)
테스트 6 〉	통과 (0.04ms, 10.7MB)
테스트 7 〉	통과 (0.04ms, 10.7MB)
테스트 8 〉	통과 (0.03ms, 10.8MB)
테스트 9 〉	통과 (0.04ms, 10.7MB)
테스트 10 〉	통과 (0.04ms, 10.8MB)
테스트 11 〉	통과 (0.04ms, 10.7MB)
효율성  테스트
테스트 1 〉	통과 (3.29ms, 15.3MB)
테스트 2 〉	통과 (3.31ms, 15.3MB)
```
문제의 의도에 맞게 hashmap으로 풀면
```python
def solution(phone_book):
    phone_book.sort()
    ans = dict(zip(map(hash, phone_book), [None]*len(phone_book)))

    for num in reversed(phone_book):
        for sli in list(map(len,phone_book)):
            if hash(num[:sli]) in ans and num[:sli] != num:
                return False
    return True
```
```bash
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.7MB)
테스트 2 〉	통과 (0.05ms, 10.6MB)
테스트 3 〉	통과 (0.05ms, 10.7MB)
테스트 4 〉	통과 (0.05ms, 10.6MB)
테스트 5 〉	통과 (0.07ms, 10.8MB)
테스트 6 〉	통과 (0.05ms, 10.6MB)
테스트 7 〉	통과 (0.04ms, 10.7MB)
테스트 8 〉	통과 (0.04ms, 10.6MB)
테스트 9 〉	통과 (0.04ms, 10.7MB)
테스트 10 〉	통과 (0.04ms, 10.7MB)
테스트 11 〉	통과 (0.05ms, 10.7MB)
효율성  테스트
테스트 1 〉	통과 (5.33ms, 15.4MB)
테스트 2 〉	통과 (5.24ms, 15.2MB)
```
hash() 비교
```python
def solution(phone_book):
    phone_book.sort()
    ans = dict(zip(phone_book, [None]*len(phone_book)))
    for num in reversed(phone_book):
        for sli in list(map(len,phone_book)):
            tmp = num[:sli]
            if tmp in ans and tmp != num:
                return False
    return True
```
```bash
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (0.04ms, 10.7MB)
테스트 4 〉	통과 (0.04ms, 10.8MB)
테스트 5 〉	통과 (0.04ms, 10.7MB)
테스트 6 〉	통과 (0.04ms, 10.7MB)
테스트 7 〉	통과 (0.04ms, 10.7MB)
테스트 8 〉	통과 (0.04ms, 10.7MB)
테스트 9 〉	통과 (0.04ms, 10.6MB)
테스트 10 〉	통과 (0.04ms, 10.7MB)
테스트 11 〉	통과 (0.05ms, 10.7MB)
효율성  테스트
테스트 1 〉	통과 (4.44ms, 15.3MB)
테스트 2 〉	통과 (4.37ms, 15.4MB)
```