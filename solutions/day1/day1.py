from loguru import logger


def deter_direction(direction: str) -> int:
    if direction[0] == 'L':
        return -int(direction[1:])
    elif direction [0] == 'R':
        return int(direction[1:])
    else:
        raise ValueError


def main():
    with open("../data/data_day1.txt", "r") as f:
        data = f.read().splitlines()

    dial = list(range(0,100))
    start = dial[50]
    num_zero = 0

    for line in data:
        logger.info(f"Current Line: {line}")
        logger.info(f"Start position: {start}")
        direction = deter_direction(line)
        start = dial[(start+direction)%100]
        logger.info(f"End position: {start}")
        if start == 0:
            num_zero+=1

    logger.info(f"Number of zero: {num_zero}")

if __name__ == "__main__":
    main()