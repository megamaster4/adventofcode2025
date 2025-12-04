from loguru import logger
from pathlib import Path
from typing import Generator
import re


def find_repeating_sequences(text: str):
    search_text = ""
    all_matches = {}
    logger.info(text)
    for letter in text:
        search_text += letter
        logger.info(letter)
        logger.info(search_text)
        matches = [match.start() for match in re.finditer(search_text, text)]
        all_matches[search_text] = matches
    return all_matches


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
            is_repeating = find_repeating_sequences(str(num))
            logger.debug(num)
            logger.debug(is_repeating)

            if is_repeating:
                invalid_ids.append(num)
    
    logger.debug(invalid_ids)
    

if __name__ == "__main__":
    main()