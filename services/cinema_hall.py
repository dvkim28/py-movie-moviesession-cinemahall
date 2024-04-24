import init_django_orm  # noqa: F401

from db.models import CinemaHall


def get_cinema_halls() -> CinemaHall:
    query = CinemaHall.objects.all()
    return query


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> CinemaHall:
    new_hall = CinemaHall.objects.create(hall_name=hall_name,
                                         hall_rows=hall_rows,
                                         seats_in_row=hall_seats_in_row)
    return new_hall
