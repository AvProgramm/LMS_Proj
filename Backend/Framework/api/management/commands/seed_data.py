"""
Django management command to seed the local database with test data.
Usage: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from api.models import (
    User, StudentProfile, InstructorProfile, AdminProfile,
    Course, Lesson, Enrollment, LessonEnrollment,
    LessonAssignment, LessonReading, LessonClassroom,
    Classroom, ClassroomEnrollment,
    StudentAssignmentProgress, StudentReadingProgress,
)
from django.utils import timezone


class Command(BaseCommand):
    help = "Seed the database with sample data for local development"

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # ── Users ──
        admin_user, _ = User.objects.get_or_create(
            email="admin@beacon.edu",
            defaults={"password_hash": "admin123", "role": "admin"},
        )
        inst_user1, _ = User.objects.get_or_create(
            email="jane@instructor.edu",
            defaults={"password_hash": "jane123", "role": "instructor"},
        )
        inst_user2, _ = User.objects.get_or_create(
            email="mark@instructor.edu",
            defaults={"password_hash": "mark123", "role": "instructor"},
        )
        stud_user1, _ = User.objects.get_or_create(
            email="alice@student.edu",
            defaults={"password_hash": "alice123", "role": "student"},
        )
        stud_user2, _ = User.objects.get_or_create(
            email="bob@student.edu",
            defaults={"password_hash": "bob123", "role": "student"},
        )
        stud_user3, _ = User.objects.get_or_create(
            email="carol@student.edu",
            defaults={"password_hash": "carol123", "role": "student"},
        )
        self.stdout.write(self.style.SUCCESS("  ✓ Users created"))

        # ── Profiles ──
        AdminProfile.objects.get_or_create(
            user=admin_user, defaults={"full_name": "System Admin"}
        )
        inst1, _ = InstructorProfile.objects.get_or_create(
            user=inst_user1,
            defaults={"full_name": "Jane Smith", "staff_no": "T3001", "title": "Dr."},
        )
        inst2, _ = InstructorProfile.objects.get_or_create(
            user=inst_user2,
            defaults={"full_name": "Mark Lee", "staff_no": "T3002", "title": "Prof."},
        )
        stud1, _ = StudentProfile.objects.get_or_create(
            user=stud_user1,
            defaults={
                "first_name": "Alice", "last_name": "Tan",
                "title": "Ms.", "student_no": "300001",
            },
        )
        stud2, _ = StudentProfile.objects.get_or_create(
            user=stud_user2,
            defaults={
                "first_name": "Bob", "last_name": "Gomez",
                "title": "Mr.", "student_no": "300002",
            },
        )
        stud3, _ = StudentProfile.objects.get_or_create(
            user=stud_user3,
            defaults={
                "first_name": "Carol", "last_name": "Ong",
                "title": "Ms.", "student_no": "300003",
            },
        )
        self.stdout.write(self.style.SUCCESS("  ✓ Profiles created"))

        # ── Courses ──
        course1, _ = Course.objects.get_or_create(
            course_id="PY1001",
            defaults={
                "title": "Introduction to Python",
                "status": "Active",
                "owner_instructor": inst1,
                "credits": 30,
                "director": "Jane Smith",
                "description": "Foundations of Python programming with problem solving, data structures, and small projects.",
            },
        )
        course2, _ = Course.objects.get_or_create(
            course_id="DB2001",
            defaults={
                "title": "Database Systems",
                "status": "Active",
                "owner_instructor": inst2,
                "credits": 30,
                "director": "Mark Lee",
                "description": "Relational modeling, SQL (DDL/DML), constraints, transactions, and query optimization.",
            },
        )
        course3, _ = Course.objects.get_or_create(
            course_id="WD3001",
            defaults={
                "title": "Web Development Fundamentals",
                "status": "Active",
                "owner_instructor": inst1,
                "credits": 24,
                "director": "Jane Smith",
                "description": "HTML, CSS, JavaScript, and modern web frameworks for building responsive applications.",
            },
        )
        self.stdout.write(self.style.SUCCESS("  ✓ Courses created"))

        # ── Lessons ──
        lessons_data = [
            # Course 1 — Python
            ("PY1001L1", course1, "Python Basics", "Variables, data types, and operators", "Understand Python syntax", 2, 5, inst1),
            ("PY1001L2", course1, "Control Flow", "If/else, loops, and comprehensions", "Master control structures", 2, 5, inst1),
            ("PY1001L3", course1, "Functions & Modules", "Defining functions, imports, and packages", "Write reusable code", 3, 8, inst1),
            ("PY1001L4", course1, "Data Structures", "Lists, dicts, sets, and tuples", "Use Python collections", 3, 7, inst1),
            ("PY1001L5", course1, "OOP in Python", "Classes, inheritance, and polymorphism", "Apply OOP principles", 4, 5, inst1),
            # Course 2 — Databases
            ("DB2001L1", course2, "Relational Model", "Tables, keys, and relationships", "Understand relational design", 2, 5, inst2),
            ("DB2001L2", course2, "SQL Basics", "SELECT, INSERT, UPDATE, DELETE", "Write basic SQL queries", 3, 10, inst2),
            ("DB2001L3", course2, "Advanced SQL", "JOINs, subqueries, and aggregations", "Write complex queries", 3, 8, inst2),
            ("DB2001L4", course2, "Normalization", "1NF through BCNF", "Normalize databases", 2, 7, inst2),
            # Course 3 — Web Dev
            ("WD3001L1", course3, "HTML & Semantic Markup", "HTML5 elements and structure", "Build semantic pages", 2, 6, inst1),
            ("WD3001L2", course3, "CSS & Layout", "Flexbox, Grid, and responsive design", "Style responsive layouts", 3, 8, inst1),
            ("WD3001L3", course3, "JavaScript Essentials", "DOM, events, and async programming", "Add interactivity", 4, 10, inst1),
        ]
        created_lessons = {}
        for lid, course, title, desc, obj, dur, cred, designer in lessons_data:
            lesson, _ = Lesson.objects.get_or_create(
                lesson_id=lid,
                defaults={
                    "course": course, "title": title, "description": desc,
                    "objectives": obj, "duration_weeks": dur, "credits": cred,
                    "status": "Active", "designer": designer, "created_by": designer,
                },
            )
            created_lessons[lid] = lesson
        self.stdout.write(self.style.SUCCESS("  ✓ Lessons created"))

        # ── Assignments & Readings ──
        assignments_data = [
            ("PY1001L1", "Hello World Script", "Write your first Python script"),
            ("PY1001L2", "Loop Practice", "Implement 5 loop patterns"),
            ("PY1001L3", "Calculator Module", "Build a calculator module"),
            ("PY1001L4", "Data Structures Quiz", "Complete the collections quiz"),
            ("PY1001L5", "OOP Project", "Build a class hierarchy"),
            ("DB2001L1", "ER Diagram", "Draw an ER diagram for a library system"),
            ("DB2001L2", "SQL Exercises", "Complete 10 SQL query exercises"),
            ("DB2001L3", "Complex Query Challenge", "Write 5 complex queries"),
            ("WD3001L1", "Semantic Page", "Build a semantic HTML page"),
            ("WD3001L2", "Responsive Layout", "Create a responsive portfolio"),
            ("WD3001L3", "Interactive App", "Build a to-do list app"),
        ]
        created_assignments = {}
        for lid, title, desc in assignments_data:
            asgn, _ = LessonAssignment.objects.get_or_create(
                lesson=created_lessons[lid], title=title,
                defaults={"description": desc},
            )
            created_assignments[(lid, title)] = asgn

        readings_data = [
            ("PY1001L1", "Python Official Tutorial", "https://docs.python.org/3/tutorial/"),
            ("PY1001L2", "Real Python: For Loops", "https://realpython.com/python-for-loop/"),
            ("PY1001L3", "Python Modules Guide", "https://docs.python.org/3/tutorial/modules.html"),
            ("DB2001L1", "Database Design Guide", "https://www.w3schools.com/sql/sql_intro.asp"),
            ("DB2001L2", "SQL Tutorial", "https://www.sqltutorial.org/"),
            ("WD3001L1", "MDN HTML Guide", "https://developer.mozilla.org/en-US/docs/Web/HTML"),
            ("WD3001L2", "CSS Tricks Flexbox", "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"),
            ("WD3001L3", "JavaScript.info", "https://javascript.info/"),
        ]
        created_readings = {}
        for lid, title, url in readings_data:
            rdg, _ = LessonReading.objects.get_or_create(
                lesson=created_lessons[lid], title=title,
                defaults={"url": url},
            )
            created_readings[(lid, title)] = rdg
        self.stdout.write(self.style.SUCCESS("  ✓ Assignments & Readings created"))

        # ── Classrooms ──
        cls1, _ = Classroom.objects.get_or_create(
            classroom_id="RM101A",
            defaults={"location": "Building A, Room 101", "capacity": 40, "is_online": False},
        )
        cls2, _ = Classroom.objects.get_or_create(
            classroom_id="RM202B",
            defaults={"location": "Building B, Room 202", "capacity": 30, "is_online": False},
        )
        cls_online, _ = Classroom.objects.get_or_create(
            classroom_id="ONL001",
            defaults={
                "location": "Online", "capacity": 100,
                "is_online": True, "zoom_link": "https://zoom.us/j/123456789",
            },
        )
        self.stdout.write(self.style.SUCCESS("  ✓ Classrooms created"))

        # ── Enrollments ──
        for student in [stud1, stud2, stud3]:
            Enrollment.objects.get_or_create(student=student, course=course1)
        for student in [stud1, stud2]:
            Enrollment.objects.get_or_create(student=student, course=course2)
        Enrollment.objects.get_or_create(student=stud3, course=course3)

        # Lesson enrollments
        for student in [stud1, stud2, stud3]:
            for lid in ["PY1001L1", "PY1001L2", "PY1001L3"]:
                LessonEnrollment.objects.get_or_create(
                    student=student, lesson=created_lessons[lid],
                )
        for student in [stud1, stud2]:
            for lid in ["DB2001L1", "DB2001L2"]:
                LessonEnrollment.objects.get_or_create(
                    student=student, lesson=created_lessons[lid],
                )
        self.stdout.write(self.style.SUCCESS("  ✓ Enrollments created"))

        # ── Link classrooms to lessons ──
        lc_data = [
            (created_lessons["PY1001L1"], cls1, "Monday", "09:00", "11:00", inst1),
            (created_lessons["PY1001L2"], cls2, "Wednesday", "14:00", "16:00", inst1),
            (created_lessons["DB2001L1"], cls1, "Tuesday", "10:00", "12:00", inst2),
            (created_lessons["WD3001L1"], cls_online, "Friday", "09:00", "11:00", inst1),
        ]
        from datetime import time as dtime
        for lesson, classroom, day, t_start, t_end, supervisor in lc_data:
            h1, m1 = map(int, t_start.split(":"))
            h2, m2 = map(int, t_end.split(":"))
            LessonClassroom.objects.get_or_create(
                lesson=lesson, classroom=classroom,
                defaults={
                    "day_of_week": day,
                    "time_start": dtime(h1, m1),
                    "time_end": dtime(h2, m2),
                    "supervisor": supervisor,
                },
            )
        self.stdout.write(self.style.SUCCESS("  ✓ Lesson-Classroom links created"))

        # ── Student progress ──
        # Alice has completed some assignments
        for key in [("PY1001L1", "Hello World Script"), ("PY1001L2", "Loop Practice")]:
            if key in created_assignments:
                StudentAssignmentProgress.objects.get_or_create(
                    student=stud1, assignment=created_assignments[key],
                    defaults={"is_completed": True},
                )
        for key in [("PY1001L1", "Python Official Tutorial")]:
            if key in created_readings:
                StudentReadingProgress.objects.get_or_create(
                    student=stud1, reading=created_readings[key],
                    defaults={"is_completed": True},
                )

        # Bob has completed one assignment
        for key in [("PY1001L1", "Hello World Script")]:
            if key in created_assignments:
                StudentAssignmentProgress.objects.get_or_create(
                    student=stud2, assignment=created_assignments[key],
                    defaults={"is_completed": True},
                )

        self.stdout.write(self.style.SUCCESS("  ✓ Student progress created"))
        self.stdout.write(self.style.SUCCESS("\n✅ Database seeded successfully!"))
        self.stdout.write("\n  Login credentials:")
        self.stdout.write("  ─────────────────────────────────────────")
        self.stdout.write("  Admin:      admin@beacon.edu / admin123")
        self.stdout.write("  Instructor: jane@instructor.edu / jane123")
        self.stdout.write("  Instructor: mark@instructor.edu / mark123")
        self.stdout.write("  Student:    alice@student.edu / alice123")
        self.stdout.write("  Student:    bob@student.edu / bob123")
        self.stdout.write("  Student:    carol@student.edu / carol123")
        self.stdout.write("  ─────────────────────────────────────────")
