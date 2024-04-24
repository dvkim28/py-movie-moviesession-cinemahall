
import init_django_orm  # noqa: F401

from db.models import MovieSession
from datetime import datetime


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    new_session = MovieSession(show_time=movie_show_time)
    if cinema_hall_id and movie_id:
        new_session.movie_id = movie_id
        new_session.cinema_hall_id = cinema_hall_id
        new_session.save()
    return new_session


def get_movies_sessions(session_date: str | None = None) -> MovieSession:
    query = MovieSession.objects.all()
    if session_date:
        datetime.strptime(session_date, "%Y-%m-%d")
        query = MovieSession.objects.filter(
            show_time__date=session_date
        )
        return query
    return query


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    session = MovieSession.objects.get(id=movie_session_id)
    return session


def update_movie_session(session_id: int,
                         show_time: datetime | None = None,
                         movie_id: int | None = None,
                         cinema_hall_id: int | None = None,
                         ) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    query = MovieSession.objects.get(id=session_id)
    query.delete()
