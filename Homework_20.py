import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from tempfile import TemporaryDirectory


def save_json(path, data):
    """ჩაწერს მონაცემებს UTF-8 JSON ფაილში."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_json(path, default=None):
    """კითხულობს JSON ფაილს; არყოფნის ან არასწორი JSON-ისას აბრუნებს default-ს."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


@dataclass
class Movie:
    title: str
    year: int = 2000
    rating: float = 0.0
    genres: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not 0 <= self.rating <= 10:
            raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")


def best_movies(movies, min_rating):
    """აბრუნებს მინიმალურ რეიტინგზე მაღალი ან ტოლი შეფასების ფილმებს კლებადობით."""
    return sorted(
        (movie for movie in movies if movie.rating >= min_rating),
        key=lambda movie: movie.rating,
        reverse=True,
    )


def main():
    # სავარჯიშო 1: JSON ფაილის შენახვა და წაკითხვა
    with TemporaryDirectory() as temp_dir:
        folder = Path(temp_dir)
        json_path = folder / "movie_data.json"
        missing_path = folder / "missing.json"
        broken_path = folder / "broken.json"

        data = {"name": "ნინო", "scores": [90, 85], "pair": (1, 2)}
        save_json(json_path, data)
        loaded = load_json(json_path)
        print(loaded)
        print(type(loaded["pair"]))

        print(load_json(missing_path, default={}))

        broken_path.write_text('{"name": "ნინო",}', encoding="utf-8")
        print(load_json(broken_path, default="არასწორი ფაილი"))




    # სავარჯიშო 2: Movie dataclass
    first = Movie("მონანიება", 1984, 9.1, ["დრამა"])
    second = Movie("გზა", 2020, 7.5)
    third = Movie("მოგზაურობა", rating=8.2, genres=["თავგადასავალი"])
    movies = [first, second, third]

    print(first)
    print(first == Movie("მონანიება", 1984, 9.1, ["დრამა"]))

    second.genres.append("კომედია")
    print(second.genres, third.genres)

    for movie in best_movies(movies, 8):
        print(movie.title, movie.rating)

    json_text = json.dumps(asdict(first), ensure_ascii=False)
    print(json_text)

    try:
        Movie("ცუდი", 2000, 11)
    except ValueError as error:
        print("შეცდომა:", error)


if __name__ == "__main__":
    main()