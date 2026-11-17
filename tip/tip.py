def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_without_dollar_sign = d.strip().replace("$", "")
    return float(dollar_without_dollar_sign)


def percent_to_float(p):
    percent_without_percent_sign = p.strip().replace("%", "")
    percent_converted = float(percent_without_percent_sign) / 100.0
    return percent_converted

   # Example that converts user input to float.
   # x =input("x :")
   # print(float(x) * 2)

main()
