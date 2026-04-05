# 나의 이름 A (나는 항상 모든 메세지를 읽는다.)
# 톡방에 있는 사람 수 N  (1 <= N <= 26)
# 총 메세지 개수 K ( 1 <= K <= 10,000)
# 정보를 알고 싶은 메세지의 번호 Q ( 1 <= Q <= K)
# 메세지를 읽지 않은 사람 수 >= 이전 메세지를 읽지 않은 사람의 수
import string

N, K, Q = input().split()
N, K, Q = int(N), int(K), int(Q)
upper_alphabet = list(string.ascii_uppercase)
person = upper_alphabet[1:N]
chat = [[None, None]] 
for _ in range(K):
    R, P = input().split()
    chat.append([R, P])

# Q 이후 송신자 제거
for i in range(Q, K + 1):
    target = chat[i][1]
    if target in person:
        person.remove(target)

# Q 이전에서 R값이 같은 송신자 제거
for i in range(Q - 1, 0, -1):
    if chat[i][0] == chat[Q][0]:
        if chat[i][1] in person:
            person.remove(chat[i][1])
    else:
        break

if chat[Q][0] == '0' or not person:
    print(-1)
else:
    print(*sorted(person))
