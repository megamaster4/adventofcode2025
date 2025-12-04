from loguru import logger
from pathlib import Path
from typing import Generator


def is_repeating_string(s):
    res = (s + s).find(s, 1) != len(s)
    logger.debug(s.find_all(s))
    return res


def create_range(numbers: list[str]) -> Generator:
    logger.debug(numbers)
    return range(int(numbers[0]), int(numbers[1])+1)



def main():
    mod_path = Path(__file__).parent

    with open(f"{mod_path}/data/example_day2.txt", "r") as f:
        data = [interval.split('-') for interval in f.read().split(',')]    
    
    logger.debug(data)
    invalid_ids = []

    for sequence in data:
        sequence_gen = create_range(sequence)
        for num in sequence_gen:
            is_repeating = is_repeating_string(str(num))
            logger.debug(num)
            logger.debug(is_repeating)

            if is_repeating:
                invalid_ids.append(num)
    
    logger.debug(invalid_ids)
    

if __name__ == "__main__":
    main()