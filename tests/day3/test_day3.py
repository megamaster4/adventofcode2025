from solutions.day3 import day3, day3B

def test_main_part1():
    som = day3.main(file="example_day3.txt")
    assert som == 357


def test_main_part2():
    som = day3B.main(file="example_day3.txt")
    assert som == 3121910778619