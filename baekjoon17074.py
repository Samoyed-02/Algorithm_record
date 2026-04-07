# 남규는 정수 N개로 이루어진 배열 하나를 갖고 있다.
# 남규는 그 배열에 있는 수중 하나만 버린다.
# 남규는 숫자를 버렸을 때 그 배열이 정렬되어있기를 바란다.
# 남규가 갖고 있는 배열이 주어지면 수 하나를 버려 정렬된 배열을 남기는 방법의 수를 구해보자

num = int(input())
numbers = list(map(float,input().split()))

breaks = [i for i in range(num-1) if numbers[i] > numbers[i+1]]

if len(breaks) == 0:
    print(num)

elif len(breaks) ==1:
    count = 0
    k = breaks[0]
    for i in [k,k+1]:
        new = numbers[:]
        del new[i]
        if new == sorted(new):
            count += 1
    print(count)

else:
    print(0)
