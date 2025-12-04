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

    start = 50
    num_dial_clicks = 0

    for line in data:
        end = start
        logger.info(f"Current Line: {line}")
        logger.info(f"Start position: {start}")
        direction = deter_direction(line)
        
        index = start+direction

        logger.info(f"Dial position index: {index}")

        num_dial_clicks+=int(abs(direction)/100)
        logger.info(f"Full rotations: {num_dial_clicks}")

        start = (start + direction) % 100
        logger.info(f"End position: {start}")
        if end != 0 and start != 0:
            if (direction < 0 and start > end) or (direction > 0 and start < end):
                num_dial_clicks += 1
        if start == 0:
            num_dial_clicks += 1


    logger.info(f"Answer: {num_dial_clicks}")

if __name__ == "__main__":
    main()