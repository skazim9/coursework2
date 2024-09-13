class Vacancy:
    """Класс для описания вакансии."""

    __slots__ = ('title', 'area', 'url', 'salary_from', 'salary_to', 'description')

    def __init__(self, title: str, area: str, url: str, salary_from: str, salary_to: str, description: str) -> None:
        self.title: str = title
        self.area: str = area
        self.url: str = url
        self.salary_from: str = salary_from if salary_from else "0"
        self.salary_to: str = salary_to if salary_to else "0"
        self.description: str = description

    def __str__(self) -> str:
        return f"{self.title}, {self.area}, Зарплата: от {self.salary_from} до {self.salary_to}, Ссылка: {self.url}"

    def __lt__(self, other: "Vacancy") -> bool:
        return int(self.salary_to) < int(other.salary_to)

    def validate(self) -> None:
        if not self.title or not self.url:
            raise ValueError("Название и ссылка на вакансию обязательны.")