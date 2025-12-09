class Rectangle:
    def __init__(self, height: int, width: int, color: str):
        self.height = height
        self.width = width
        self.color = self._standardize_color(color)

        self.chu_vi = self._tinh_chu_vi()
        self.dien_tich = self._tinh_dien_tich()

    def __str__(self) -> str:
        if self._validate():
            return f"{self.chu_vi} {self.dien_tich} {self.color}"
        else:
            return "INVALID"

    def _validate(self) -> bool:
        if self.height > 0 and self.width > 0:
            return True
        else:
            return False

    def _tinh_chu_vi(self) -> int:
        return (self.height + self.width) * 2

    def _tinh_dien_tich(self) -> int:
        return self.height * self.width

    def _standardize_color(self, color: str) -> str:
        return color.strip().capitalize()


def main():
    input_str = input().strip()

    w, h, c, *_ = input_str.split(" ")

    h = int(h)
    w = int(w)
    rectangle = Rectangle(h, w, c)
    print(rectangle)


if __name__ == "__main__":
    main()
