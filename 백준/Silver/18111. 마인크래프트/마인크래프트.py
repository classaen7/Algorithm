import sys


def main():
    input = sys.stdin.readline
    N, M, B = map(int, input().split())
    arr = [0] * 257
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in temp:
            arr[j] += 1
    result = []
    for i in range(257):
        time = 0
        b = 0
        for j in range(257):
            if arr[j] > 0:
                remainder = i - j
                if remainder > 0:
                    time += arr[j] * remainder
                    b -= arr[j] * remainder
                elif remainder < 0:
                    time += arr[j] * remainder * -2
                    b += arr[j] * remainder * -1
        if B + b >= 0:
            result.append(time)
        else:
            result.append(9999999999999999)

    ret = 9999999999999999
    height = 0
    for i in range(257):
        if result[i] <= ret:
            ret = result[i]
            height = i
    print("{0} {1}".format(ret, height))


if __name__ == "__main__":
    main()