# CodingTest
코딩테스트 연습을 위한 레포지토리

## 커밋 메시지

- solve : 직접 해결한 문제
- solve, (need to review) : 직접 해결했지만 힌트를 참고하여 리뷰가 필요한 문제
- wrong : 틀렸던 문제, 해답지를 본 문제

## 필수 유형

### 1. 구현
- 무작정 문제를 풀지 않는다. 어떻게 문제를 풀어야 할지, 어떤 로직이 필요한지 고민한다.

### 2. 스택, 큐
- 스택은 리스트를 활용한다.
- 큐는 collections에서 deque를 활용한다

### 3. 힙
- import heapq 를 사용하여, heapq를 이용하자
- heapq.heapify(힙으로 바꿀 리스트)
- 아래 함수들을 이용해야 힙을 유지한 채 pop,push 가능
- heapq.heappop()
- heapq.heappush()
- 유의점! 힙큐는 최솟값을 보장하지만, 최댓값을 보장하지는 않는다
- -1 에 위치한게 최대라고 볼 수 없음

### 4. DFS,BFS
- DFS 는 스택 이용
- BFS 는 큐 이용

### 5. 이분탐색
- bisect를 활용하자

### 6. 완전탐색
- product(중복순열), combinations, permutations 등 활용
- bfs,dfs 도 활용 가능

### 7. 정렬
- 기준이 여러개면 arr.sort(key=lambda x: (x[0], x[1], x[2]))

### 기타
- from copy import deepcopy 로 완전 복사 가능
