from loguru import logger
from pathlib import Path


def get_max_num(text: str):
    max_num = 0
    for index_letter, letter in enumerate(text):
        for index_next_letter, next_letter in enumerate(text):
            if index_next_letter <= index_letter:
                continue
            number = int(letter+next_letter)
            if number > max_num:
                max_num = number
    return max_num


def main(file: str):
    mod_path = Path(__file__).parent

    max_nums = []
    with open(f"{mod_path}/data/{file}", "r") as f:
        data = f.read().splitlines()

    for row in data:
        max_num = get_max_num(row)
        max_nums.append(max_num)
        logger.info(max_num)
    
    som = sum(max_nums)
    logger.info(f"Total sum: {som}")
    return som


if __name__ == "__main__":
    main(file="data_day3.txt")