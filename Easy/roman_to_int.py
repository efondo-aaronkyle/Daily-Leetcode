def roman_to_integer(roman_numeral):
    result = 0
    roman_to_int = {
        'I': 1, 
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for roman in range(len(roman_numeral)):
        if roman + 1 < len(roman_numeral) and roman_to_int[roman_numeral[roman]] < roman_to_int[roman_numeral[roman + 1]]:
            result -= roman_to_int[roman_numeral[roman]]
        else:
            result += roman_to_int[roman_numeral[roman]]
    
    return result

print(roman_to_integer("III"))
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))