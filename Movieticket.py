class Movie:
    def __init__(self, title, schedule):
        self.title = title
        self.schedule = schedule
        self.seats = {time: [False] * 10 for time in schedule}

    def reserve_seat(self, time, seat_number):
        if time not in self.seats:
            print("해당 시간대에 영화가 상영되지 않습니다.")
            return
        if 0 <= seat_number < 10:
            if not self.seats[time][seat_number]:
                self.seats[time][seat_number] = True
                print(f"{self.title} 영화의 {time} 시간대 {seat_number}번 좌석이 예약되었습니다.")
            else:
                print("이미 예약된 좌석입니다.")
        else:
            print("유효한 좌석 번호를 입력하세요. (0-9)")


def get_available_seats(self, time):
    if time in self.seats:
        return sum(1 for seat in self.seats[time] if not seat)
    else:
        print("해당 시간대에 영화가 상영되지 않습니다.")
        return None


# 영화관 클래스 정의
class Theater:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, schedule):
        if title not in self.movies:

            self.movies[title] = Movie(title, schedule)
            print(f"{title} 영화가 추가되었습니다. 상영 시간: {schedule}")
        else:
            print("이미 추가된 영화입니다.")

    def reserve_movie_seat(self, title, time, seat_number):
        if title in self.movies:
            movie = self.movies[title]
            movie.reserve_seat(time, seat_number)
        else:
            print("해당 영화가 목록에 없습니다.")

    def get_movie_schedule(self, title):
        if title in self.movies:
            movie = self.movies[title]
            print(f"{title} 영화의 상영 시간표:")
            for time in movie.schedule:
                available_seats = movie.get_available_seats(time)
                print(f" - {time}: 예약 가능한 좌석 수 {available_seats}개")
        else:
            print("해당 영화가 목록에 없습니다.")


theater = Theater()

theater.add_movie("Inception", ["12:00", "15:00", "18:00"])
theater.add_movie("Interstellar", ["13:00", "16:00", "19:00"])

theater.reserve_movie_seat("Inception", "12:00", 3)
theater.reserve_movie_seat("Inception", "12:00", 3)  # 이미 예약된 좌석
theater.reserve_movie_seat("Inception", "15:00", 5)

theater.get_movie_schedule("Inception")
theater.get_movie_schedule("Interstellar")