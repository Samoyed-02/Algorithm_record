# 딜러와 플레이어는 각각 1~N까지의 정수가 적힌 카드 한장씩 받는다.
# 딜러는 아무것도 적혀있지 않은 더미 카드 한장을 추가로 받는다.
# 플레이어는 가진 점수가 0인 상태에서 게임을 시작한다.
# 플레이어 턴은 M회 수행한다.
# 턴 진행 순서
# 1. 플레이어가 달러의 패에서 원하는 카드 하나 가져온다,
# 2. 같은 쌍의 패는 제거, 적힌 값이 i 라면 A[i] 점을 얻는다. 
# 얻는 점수가 음수일 수 있고, 플레이어 점수도 음수 가능
# 3. 플레이어가 달러에게 자신의 패에서 원하는 카드 하나를 준다.
# 4. 달러의 패에 같은 값의 카드 쌍이 만들어 지면 제거, 플레이어 점수는 얻지 않는다.
# M 번째 턴에 끝내거나 더미 카드를 제외한 모든 카드 쌍이 사라진 순간 게임이 종료
# 턴이 수행되는 도중이라도 플레이어가 달러에게 카드를 줄 수 없다면 게임은 종료
# 종료되었을 때 플레이어가 얻을 수 있는 최대 점수를 구하는 프로그램을 작성해보아라
import itertools

N, M = input().split()
N, M = int(N), int(M)
K = 1
K = int(K)
chance = 0
chance = int(chance)
score = []

score = list(map(float, input().split()))
positive_scores = [ n for n in score if n >= 0]
positive_scores.sort(reverse=True)
prefix_sum = list(itertools.accumulate(positive_scores))
if K == N:
    chance += 1
else:
    while True:
        if K < N:
            K += 2
            if chance < M:
                chance += 1
            else:
                break
        elif K == N:
            if chance < M:
                chance += 1
                break
            else:
                break
        else :
            break
if len(positive_scores) == 0:
    print('0')
elif len(positive_scores) > chance:
   max_score = prefix_sum[chance-1]
   max_score = int(max_score)
   print(max_score)
else:
    result = sum(positive_scores)
    result = int(result)
    print(result)
        





