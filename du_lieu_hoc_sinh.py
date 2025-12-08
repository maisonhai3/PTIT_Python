import json
from typing import List, Dict, Any


class ThiSinh:
    def __init__(self, name: str, math: float, physics: float, chemistry: float):
        self.name = name
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.diem_xet_tuyen = (math * 2) + (physics * 1.5) + chemistry

    def __repr__(self) -> str:
        return f"{self.name} {self.diem_xet_tuyen:.2f}"

    def __str__(self) -> str:
        return f"{self.name} {self.diem_xet_tuyen:.2f}"

    def __lt__(self, other: 'ThiSinh') -> bool:
        # if self.diem_xet_tuyen == other.diem_xet_tuyen:
        #     return self.name > other.name  # Sort names ascending on tie
        return self.diem_xet_tuyen < other.diem_xet_tuyen

    def __gt__(self, other: 'ThiSinh') -> bool:
        # if self.diem_xet_tuyen == other.diem_xet_tuyen:
        #     return self.name < other.name  # Sort alphabetically (ascending) on tie
        return self.diem_xet_tuyen > other.diem_xet_tuyen


def main() -> None:
    try:
        with open("data.json", "r") as file:
            data: List[Dict[str, Any]] = json.load(file)
    except FileNotFoundError:
        print("Error: data.json not found.")
        return

    danh_sach_xet_tuyen = [
        ThiSinh(
            thi_sinh_data["name"],
            thi_sinh_data["math"],
            thi_sinh_data["physics"],
            thi_sinh_data["chemistry"],
        )
        for thi_sinh_data in data
    ]

    sorted_data = sorted(danh_sach_xet_tuyen, reverse=True)

    for i in sorted_data:
        print(i)


if __name__ == "__main__":
    main()
