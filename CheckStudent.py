class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True


class AttendanceBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self,name, student_id):
        if student_id not in self.student_ids:
            student = Student(name, student_id)
            self.students.append(student)
            self.student_ids.add(student_id)

    def mark_student_attendance(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance()

    def get_attendance_summary(self):
        summary = {"출석": 0, "결석": 0}
        for student in self.students:
            if student.attendance:
                summary["출석"] += 1
            else:
                summary["결석"] += 1
        return summary

    def get_student_list(self):
        return [student.name for student in self.students if student.attendance]


# 출석부 테스트
attendance_book = AttendanceBook()
# 학생 추가
attendance_book.add_student("김철수", 101)
attendance_book.add_student("이영희", 102)
attendance_book.add_student("박민수", 103)
attendance_book.add_student("김철수", 101)
# 중복 학번
# 출석 체크
attendance_book.mark_student_attendance(101)
attendance_book.mark_student_attendance(103)
# 출석 요약 및 출석한 학생 목록 출력
print("출석 요약:", attendance_book.get_attendance_summary())
print("출석한 학생 목록:", attendance_book.get_student_list())