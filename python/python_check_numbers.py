# print("int+ 1134", '1134'.replace(" ", "").isdigit())
# print("int+ 1 000", "1 000".replace(" ", "").isdigit())
# print("int+  55  ", " 55  ".replace(" ", "").isdigit())
# print("int+  0 0  ", " 0 0   ".replace(" ", "").isdigit())
# print("int+  0 0g  ", " 0 0g  ".replace(" ", "").isdigit())
# print("int+  -0 0g  ", " -0 0g   ".replace(" ", "").isdigit())
# print("int+  -0. 0g  ", " -0. 0g   ".replace(" ", "").isdigit())
# print("int+  --0. 0g  ", " --0. 0g   ".replace(" ", "").isdigit())
# print("int+  --0.. 0g  ", " --0.. 0g   ".replace(" ", "").isdigit())
# print("int+  0 0gk  ", " 0 0gk    ".replace(" ", "").isdigit())
# print("int+  1.8  ", " 1.8    ".replace(" ", "").isdigit())


# print("int- -18 ", "-18".replace(" ", "").find("-") == 0 and "-18".count("-") == 1 and "-18".replace("-", "").replace(" ", "").isdigit())
# print("int-  - 18 ", " - 18".replace(" ", "").find("-") == 0 and " - 18".count("-") == 1 and " - 18".replace("-", "").replace(" ", "").isdigit())
# print("int-  -1 000", " -1 000".replace(" ", "").find("-") == 0 and " -1 000".count("-") == 1 and " -1 000".replace("-", "").replace(" ", "").isdigit())
# print("int-  1 000", " 1 000".replace(" ", "").find("-") == 0 and " 1 000".count("-") == 1 and " 1 000".replace("-", "").replace(" ", "").isdigit())
# print("int-  5", " 5".replace(" ", "").find("-") == 0 and " 5".count("-") == 1 and " 5".replace("-", "").replace(" ", "").isdigit())
# print("int-  -1.5", " -1.5".replace(" ", "").find("-") == 0 and " -1.5".count("-") == 1 and " -1.5".replace("-", "").replace(" ", "").isdigit())
# print("int-  -", " -".replace(" ", "").find("-") == 0 and " -".count("-") == 1 and " -".replace("-", "").replace(" ", "").isdigit())
# print("int-  -8g", " -8g".replace(" ", "").find("-") == 0 and " -8g".count("-") == 1 and " -8g".replace("-", "").replace(" ", "").isdigit())
# print("int-  5-3", " 5-3".replace(" ", "").find("-") == 0 and " 5-3".count("-") == 1 and " 5-3".replace("-", "").replace(" ", "").isdigit())
# print("int-  5-", " 5-".replace(" ", "").find("-") == 0 and " 5-".count("-") == 1 and " 5-".replace("-", "").replace(" ", "").isdigit())
# print("int-  --5", " --5".replace(" ", "").find("-") == 0 and " --5".count("-") == 1 and " --5".replace("-", "").replace(" ", "").isdigit())
# print("int-  -5-", " -5-".replace(" ", "").find("-") == 0 and " -5-".count("-") == 1 and " -5-".replace("-", "").replace(" ", "").isdigit())

# number = "  8   "
# print(f"int+- {number}", number.replace(" ", "").isdigit() or number.replace(" ", "").find("-") == 0 and number.count("-") == 1 and number.replace("-", "").replace(" ", "").isdigit())


# print("float+ 8.6", "8.6".replace(" ", "").replace(",", ".").count(".") == 1 and "8.6".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+  8. 6 ", " 8. 6 ".replace(" ", "").replace(",", ".").count(".") == 1 and " 8. 6 ".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ .6", ".6".replace(" ", "").replace(",", ".").count(".") == 1 and ".6".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ 8.", "8.".replace(" ", "").replace(",", ".").count(".") == 1 and "8.".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ 8,", "8,".replace(" ", "").replace(",", ".").count(".") == 1 and "8,".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ 8,.", "8,.".replace(" ", "").replace(",", ".").count(".") == 1 and "8,.".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ 8,,", "8,,".replace(" ", "").replace(",", ".").count(".") == 1 and "8,,".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ 8..", "8..".replace(" ", "").replace(",", ".").count(".") == 1 and "8..".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ ", "".replace(" ", "").replace(",", ".").count(".") == 1 and "".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+  ", " ".replace(" ", "").replace(",", ".").count(".") == 1 and " ".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ -777.8", "-777.8".replace(" ", "").replace(",", ".").count(".") == 1 and "-777.8".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ -777", "-777".replace(" ", "").replace(",", ".").count(".") == 1 and "-777".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ 55", "55".replace(" ", "").replace(",", ".").count(".") == 1 and "55".replace(",", ".").replace(".", "").replace(" ", "").isdigit())
# print("float+ 77g.9", "77g.9".replace(" ", "").replace(",", ".").count(".") == 1 and "77g.9".replace(",", ".").replace(".", "").replace(" ", "").isdigit())

# print("float- -77.9", "-77.9".replace(" ", "").replace(",", ".").count("-") == 1 and "-77.9".replace(" ", "").replace(",", ".").count(".") == 1 and "-77.9".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -.9", "-.9".replace(" ", "").replace(",", ".").count("-") == 1 and "-.9".replace(" ", "").replace(",", ".").count(".") == 1 and "-.9".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float-  -.9", " - . 9 ".replace(" ", "").replace(",", ".").count("-") == 1 and " - . 9 ".replace(" ", "").replace(",", ".").count(".") == 1 and " - . 9 ".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -9.", " -9.".replace(" ", "").replace(",", ".").count("-") == 1 and "-9.".replace(" ", "").replace(",", ".").count(".") == 1 and "-9.".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -9,", " -9,".replace(" ", "").replace(",", ".").count("-") == 1 and "-9,".replace(" ", "").replace(",", ".").count(".") == 1 and "-9,".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -9,", " -9,".replace(" ", "").replace(",", ".").count("-") == 1 and "-9,".replace(" ", "").replace(",", ".").count(".") == 1 and "-9,".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -77..9", "-77..9".replace(" ", "").replace(",", ".").count("-") == 1 and "-77..9".replace(" ", "").replace(",", ".").count(".") == 1 and "-77..9".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -77v.9", "-77v.9".replace(" ", "").replace(",", ".").count("-") == 1 and "-77v.9".replace(" ", "").replace(",", ".").count(".") == 1 and "-77v.9".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- 77.9", "77.9".replace(" ", "").replace(",", ".").count("-") == 1 and "77.9".replace(" ", "").replace(",", ".").count(".") == 1 and "77.9".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float-  ", " ".replace(" ", "").replace(",", ".").count("-") == 1 and " ".replace(" ", "").replace(",", ".").count(".") == 1 and " ".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- --88.9", "--88.9".replace(" ", "").replace(",", ".").count("-") == 1 and "--88.9".replace(" ", "").replace(",", ".").count(".") == 1 and "--88.9".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -88,,9", "-88,,9".replace(" ", "").replace(",", ".").count("-") == 1 and "-88,,9".replace(" ", "").replace(",", ".").count(".") == 1 and "-88,,9".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- ", "".replace(" ", "").replace(",", ".").count("-") == 1 and "".replace(" ", "").replace(",", ".").count(".") == 1 and "".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- 6", "6".replace(" ", "").replace(",", ".").count("-") == 1 and "6".replace(" ", "").replace(",", ".").count(".") == 1 and "6".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -6", "-6".replace(" ", "").replace(",", ".").count("-") == 1 and "-6".replace(" ", "").replace(",", ".").count(".") == 1 and "-6".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())
# print("float- -6", "-6".replace(" ", "").replace(",", ".").count("-") == 1 and "-6".replace(" ", "").replace(",", ".").count(".") == 1 and "-6".replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit())


# second_number = "9,0"
# print(f"float+- {second_number}", second_number.replace(" ", "").replace(",", ".").count("-") == 1 and second_number.replace(" ", "").replace(",", ".").count(".") == 1 and second_number.replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit() or second_number.replace(" ", "").replace(",", ".").count(".") == 1 and second_number.replace(",", ".").replace(".", "").replace(" ", "").isdigit())


number = "9.44"
int_positive = number.replace(" ", "").isdigit()
int_negative = number.replace(" ", "").find("-") == 0 and number.count("-") == 1 and number.replace("-", "").replace(" ", "").isdigit()
float_positive = number.replace(" ", "").replace(",", ".").count(".") == 1 and number.replace(",", ".").replace(".", "").replace(" ", "").isdigit()
float_negative = number.replace(",", ".").count("-") == 1 and number.replace(" ", "").replace(",", ".").count(".") == 1 and number.replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit()


