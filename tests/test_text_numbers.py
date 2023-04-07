from text_numbers import word_to_number


def test_to_number():
    # Test the function using assert statements
    assert word_to_number("three hundred forty-two") == 342
    assert word_to_number("two hundred and sixty-five") == 265
    assert word_to_number("two hundred & sixty-five") == 265
    assert word_to_number("one million two hundred thousand") == 1200000
    assert (
        word_to_number(
            "nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine"
        )
        == 999999999
    )

    assert word_to_number("one point five") == 1.5
    assert word_to_number("three point one four") == 3.14
    assert word_to_number("zero point zero nine") == 0.09

    assert word_to_number("zero") == 0
    assert word_to_number("fifteen") == 15
    assert word_to_number("twenty-one") == 21
    assert word_to_number("one hundred") == 100
    assert word_to_number("one hundred and one") == 101
    assert word_to_number("two hundred and thirty-four") == 234
    assert word_to_number("five hundred & sixty-seven") == 567
    assert word_to_number("one thousand") == 1000
    assert word_to_number("one thousand and one") == 1001
    assert word_to_number("two thousand and forty-two") == 2042
    assert word_to_number("ten thousand") == 10000
    assert word_to_number("fifty-six thousand seven hundred and eighty-nine") == 56789
    assert word_to_number("one million") == 1000000
    assert (
        word_to_number(
            "two million three hundred and forty-five thousand six hundred and seventy-eight"
        )
        == 2345678
    )
    assert word_to_number("fifty million") == 50000000
    assert (
        word_to_number(
            "sixty-seven million eight hundred ninety thousand one hundred and twenty-three"
        )
        == 67890123
    )
    assert word_to_number("one billion") == 1000000000
    assert word_to_number("one billion and one") == 1000000001
    assert word_to_number("point five") == 0.5
    assert word_to_number("one point zero zero one") == 1.001
    assert word_to_number("fifty point zero two") == 50.02
    assert word_to_number("one hundred point one") == 100.1
