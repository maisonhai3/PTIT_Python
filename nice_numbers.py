# from loguru import logger


def is_nice_number(number: str) -> bool:
    return all(number[i] == number[i+2] for i in range(len(number) - 2))


# @logger.catch
def main():
    n_test = int(input().strip())

    results = []
    for _ in range(n_test):
        input_number = input().strip()
        results.append("YES" if is_nice_number(input_number) else "NO")

    print("\n".join(results))


if __name__ == "__main__":
    main()
