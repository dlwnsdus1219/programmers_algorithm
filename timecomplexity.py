import random
findNumber = random.randrange(1, 101)

for i in range(1, 101):
    if i == findNumber:
        print(i)
        break

# 시간복잡도 활용 연습문제: 수 정렬하기
# 백준 온라인저지 2750번

# 예제 1: 연산 횟수 N
N = 10000
cnt = 1

for i in range(N):
    print("연산 횟수")
    cnt += 1

# # 예제 2: 연산 횟수 3N
# N = 10000
# cnt = 1

# for i in range(N):
#     print("연산 횟수" + str(cnt))
#     cnt += 1

# for i in range(N):
#     print("연산 횟수" + str(cnt))
#     cnt += 1

# for i in range(N):
#     print("연산 횟수" + str(cnt))
#     cnt += 1

## 코딩 테스트에서는 상수를 무시 --> 두 예제 코드 모두 시간 복잡도 O(n)으로 동일함!!

# 예제 3: 연산 횟수 N^2
N = 10000
cnt = 1

for i in range(N):
    for j in range(N):
         print("연산 횟수" + str(cnt))
         cnt += 1

# 이중 for문이 전체 코드의 시간 복잡도 기준이 된다!!