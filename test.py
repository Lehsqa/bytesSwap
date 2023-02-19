class TestMain:
    @staticmethod
    def swap16_test(x):
        return int.from_bytes(x.to_bytes(2, byteorder='little'), byteorder='big', signed=False)

    @staticmethod
    def swap32_test(x):
        return int.from_bytes(x.to_bytes(4, byteorder='little'), byteorder='big', signed=False)

    @staticmethod
    def test_equal(x1, x2):
        print("Equal: " + str(x1 == x2))
