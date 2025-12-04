from solutions.day2 import day2, day2B

def test_main_part1():
    som = day2.main(file="example_day2.txt")
    assert som == 1227775554


def test_main_part2():
    som = day2B.main(file="example_day2.txt")
    assert som == 4174379265