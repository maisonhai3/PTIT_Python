import math


class PhanSo:
    tu_so = None
    mau_so = None

    def __init__(self, tu_so, mau_so):
        self.tu_so = int(tu_so)
        self.mau_so = int(mau_so)
        self._rut_gon()

    def _rut_gon(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def __repr__(self):
        return f"{self.tu_so}/{self.mau_so}"

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"


def main():
    str_input = input().strip()
    a, b, *_ = str_input.split(" ")

    phan_so = PhanSo(a, b)
    print(phan_so)


if __name__ == "__main__":
    main()
