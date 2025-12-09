class Rectangle:
    def __init__(self, height: int, width: int, color: str):
        self.height = height
        self.width = width
        self.color = self._standardize_color(color)

    def __str__(self) -> str:
        if self.is_valid():
            return f"{self.chu_vi} {self.dien_tich} {self.color}"
        else:
            return "INVALID"

    def is_valid(self) -> bool:
        """Check if the rectangle dimensions are valid."""
        return self.height > 0 and self.width > 0

    @property
    def chu_vi(self) -> int:
        """Calculate perimeter (chu vi) of the rectangle."""
        return (self.height + self.width) * 2

    @property
    def dien_tich(self) -> int:
        """Calculate area (dien tich) of the rectangle."""
        return self.height * self.width

    @staticmethod
    def _standardize_color(color: str) -> str:
        """Standardize color string by stripping whitespace and capitalizing."""
        return color.strip().capitalize()


def main() -> None:
    """Main function to handle rectangle input and output."""
    try:
        input_str = input().strip()

        # Parse input: width, height, color
        parts = input_str.split()
        if len(parts) < 3:
            print("INVALID")
            return

        w, h, c = parts[0], parts[1], parts[2]

        # Convert to integers and validate
        try:
            h = int(h)
            w = int(w)
        except ValueError:
            print("INVALID")
            return

        rectangle = Rectangle(h, w, c)
        print(rectangle)
    except EOFError:
        pass  # End of input
    except Exception as e:
        print("INVALID")


if __name__ == "__main__":
    main()
