import sys

def main():
    k_line = sys.stdin.readline().strip()
    k = int(k_line)

    if k < 1:
        print("INVALID")
        return

    line = sys.stdin.readline().strip()
    numbers = list(map(float, line.split())) if line else []

    if len(numbers) < k:
        print()
        return

    window_sum = sum(numbers[:k])
    averages = [f"{window_sum / k:.2f}"]

    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        averages.append(f"{window_sum / k:.2f}")

    print(" ".join(averages))


if __name__ == "__main__":
    main()
