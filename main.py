from bytesSwap import swap16, swap32
from test import TestMain

x16 = [0x1234, 0x3424, 0x3425, 0x6242, 0x4246, 0x8245, 0x7362, 0x8262, 0x5156, 0x7152]
print("Little: " + str(["{:04x}".format(x) for x in x16]))
x16_big = [swap16(x) for x in x16]
print("Little_to_Big: " + str(["{:04x}".format(x) for x in x16_big]))
print("Little_to_Big_test: " + str(["{:04x}".format(TestMain.swap16_test(x)) for x in x16]))
TestMain.test_equal(x16_big, [TestMain.swap16_test(x) for x in x16])
x16_little = [swap16(x) for x in x16_big]
print("Big_to_Little: " + str(["{:04x}".format(x) for x in x16_little]))
print("Big_to_Little_test: " + str(["{:04x}".format(TestMain.swap16_test(x)) for x in x16_big]))
TestMain.test_equal(x16_little, [TestMain.swap16_test(x) for x in x16_big])
print("\n")

x32 = [0x12345678, 0x35257235, 0x52725263, 0x68346125, 0x69013474, 0x25821467, 0x25732345, 0x14353614, 0x62934501,
       0x27593204]
print("Little: " + str(["{:08x}".format(x) for x in x32]))
x32_big = [swap32(x) for x in x32]
print("Little_to_Big: " + str(["{:08x}".format(x) for x in x32_big]))
print("Little_to_Big_test: " + str(["{:08x}".format(TestMain.swap32_test(x)) for x in x32]))
TestMain.test_equal(x32_big, [TestMain.swap32_test(x) for x in x32])
x32_little = [swap32(x) for x in x32_big]
print("Big_to_Little: " + str(["{:08x}".format(x) for x in x32_little]))
print("Big_to_Little_test: " + str(["{:08x}".format(TestMain.swap32_test(x)) for x in x32_big]))
TestMain.test_equal(x32_little, [TestMain.swap32_test(x) for x in x32_big])
