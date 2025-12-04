from loguru import logger
from pathlib import Path
from typing import Generator
import re
import numpy as np

def find_repeating_sequences(text: str):
    search_text = ""
    all_matches = {}
    for letter in text:
        search_text += letter
        matches = [match.start() for match in re.finditer(search_text, text)]
        if len(matches) > 1:
            result = ""
            length_str = len(search_text)
            np_matches = np.array(matches) # converting `a` to numpy array
            diff_list = np.diff(np_matches)
            if np.all(diff_list == length_str):
                for index in matches:
                    result += text[index]
                if len(text) == len(matches) or text == len(matches) * search_text:
                    return True
    return False


def create_range(numbers: list[str]) -> Generator:
    return range(int(numbers[0]), int(numbers[1])+1)


def main(file: str):
    mod_path = Path(__file__).parent

    with open(f"{mod_path}/data/{file}", "r") as f:
        data = [interval.split('-') for interval in f.read().split(',')]    
    
    invalid_ids = []
    for sequence in data:
        sequence_gen = create_range(sequence)
        for num in sequence_gen:
            is_repeating = find_repeating_sequences(str(num))

            if is_repeating:
                invalid_ids.append(num)

    logger.debug(invalid_ids)
    som = sum(invalid_ids)
    logger.info(f"Sum of invalid ids: {som}")
    return som

if __name__ == "__main__":
    main(file="data_day2.txt")