import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import InstructorTopBar from "../../../components/InstructorTopBar/InstructorTopBar";
import s from "./InstructorStudentProgressDetail.module.css";
import Button from "../../../components/Button/Button";

export default function InstructorCourseProgressDetail() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [students, setStudents] = useState([]);
  const [sortHighToLow, setSortHighToLow] = useState(true);
  const [lessons, setLessons] = useState([]);
  const [activeTab, setActiveTab] = useState(null);

  const handleToggleLessons = () => {
    const willOpen = activeTab !== "lessons";
    setActiveTab(willOpen ? "lessons" : null);

    if (willOpen) {
      const mockLessons = [
        {
          lesson_id: "L1",
          title: "Intro",
          designer: "Alice",
          duration_weeks: 2,
          enrolled_count: 10,
          average_progress: 0.5,
        },
        {
          lesson_id: "L2",
          title: "Advanced",
          designer: "Bob",
          duration_weeks: 3,
          enrolled_count: 12,
          average_progress: 0.8,
        },
      ];
      setLessons(mockLessons);
    }
  };

  useEffect(() => {
    const fetchCourse = async () => {
      setLoading(true);
      try {
        const mockCourse = {
          course_id: courseId,
          course_title:
            courseId === "CS101"
              ? "Intro to Computer Science"
              : "Data Structures",
          course_credits: courseId === "CS101" ? 3 : 4,
          students_enrolled: courseId === "CS101" ? 25 : 30,
          average_progress: courseId === "CS101" ? 0.45 : 0.78,
          course_director: "Dr. Smith",
        };
        setCourse(mockCourse);

        const mockStudents = [
          {
            id: "S1",
            name: "Alice Tan",
            gmail: "alice.tan@gmail.com",
            lessons_completed: 4,
            total_lessons: 5,
            credits_earned: 12,
            progress: 0.8,
            enrolled_date: "2025-01-02",
            enrolledCourses: [],
          },
          {
            id: "S2",
            name: "Bob Lee",
            gmail: "bob.lee@gmail.com",
            lessons_completed: 3,
            total_lessons: 5,
            credits_earned: 9,
            progress: 0.6,
            enrolled_date: "2023-01-02",
            enrolledCourses: [],
          },
          {
            id: "S3",
            name: "Chloe Wong",
            gmail: "chloe.wong@gmail.com",
            lessons_completed: 2,
            total_lessons: 5,
            credits_earned: 6,
            progress: 0.4,
            enrolled_date: "2025-01-02",
            enrolledCourses: [],
          },
          {
            id: "S4",
            name: "Daniel Lim",
            gmail: "daniel.lim@gmail.com",
            lessons_completed: 5,
            total_lessons: 5,
            credits_earned: 15,
            progress: 1.0,
            enrolled_date: "2023-01-02",
            enrolledCourses: [],
          },
        ];
        setStudents(mockStudents);
      } catch (err) {
        console.error("Failed to fetch course details", err);
        alert("Failed to load course details.");
      } finally {
        setLoading(false);
      }
    };

    fetchCourse();
  }, [courseId]);

  if (loading) return <div>Loading course details…</div>;
  if (!course) return <div>No course found.</div>;

  const sortedStudents = [...students].sort((a, b) =>
    sortHighToLow ? b.progress - a.progress : a.progress - b.progress
  );

  const sortedLessons = [...lessons].sort((a, b) =>
    sortHighToLow ? b.duration_weeks - a.duration_weeks : a.duration_weeks - b.duration_weeks
  );

  const totalProgress =
    students.length > 0
      ? students.reduce((sum, student) => sum + (student.progress || 0), 0) /
        students.length
      : 0;

  return (
    <div className={s.wrap}>
      <InstructorTopBar />
      <header className={s.header}>
        <div className={s.left}>
          <h1 className={s.title}>STUDENT PROGRESS - COURSES</h1>
        </div>
      </header>

      <div className={s.container}>
        <div className={s.card}>
          <div className={s.cardTitle}>{course.course_title}</div>

          <div className={s.cardDesc1}>
            <span>Code: {course.course_id}</span>
            <span>Credits: {course.course_credits}</span>
            <span>Students: {course.students_enrolled}</span>
          </div>

          <div className={s.cardDesc2}>
            <span>Average Progress:</span>
            <div className={s.progressBar}>
              <div
                className={s.progressFill}
                style={{ width: `${totalProgress * 100}%` }}
              />
              <span className={s.progressText}>
                {Math.round(totalProgress * 100)}%
              </span>
            </div>
          </div>
        </div>

        <div className={s.buttonStack}>
          <Button
            className={s.enrollBtn}
            onClick={() => navigate("/instructor/student-progress")}
          >
            Back to Course Progress
          </Button>
          <Button
            variant="orange"
            className={s.enrollBtn}
            onClick={() => setSortHighToLow(!sortHighToLow)}
          >
            Sort {sortHighToLow ? "Low → High" : "High → Low"}
          </Button>
        </div>
      </div>

      <div className={s.wraprow}>
        <div className={s.row1}>
          <div
            className={`${s.panel1} ${
              activeTab === "students" ? s.tabActive : ""
            }`}
            onClick={() =>
              setActiveTab(activeTab === "students" ? null : "students")
            }
          >
            <h2 className={s.label}>Students</h2>
          </div>

          <div
            className={`${s.panel1} ${
              activeTab === "lessons" ? s.tabActive : ""
            }`}
            onClick={handleToggleLessons}
          >
            <h2 className={s.label}>Lessons</h2>
          </div>
        </div>
      </div>

      {activeTab === "students" && (
        <>
          {sortedStudents.map((student) => (
            <div
              key={student.id}
              className={s.card}
              style={{
                flexDirection: "row",
                justifyContent: "space-between",
                alignItems: "center",
                width: "75rem",
                margin: "1rem auto",
              }}
              onClick={() =>
                navigate(`/instructor/student-progress-detail/${student.id}`)
              }
            >
              <div className={s.studentInfoGroup}>
                <img
                  src="/profile_picture.png"
                  alt="Profile"
                  className={s.profileLogoTop}
                />
                <div className={s.studentInfoText}>
                  <span className={s.studentName}>
                    {student.id} - {student.name}
                  </span>
                  <span className={s.studentEmail}>{student.gmail}</span>
                  <span>
                    Lessons Completed: {student.lessons_completed}/
                    {student.total_lessons}
                  </span>
                  <span>
                    Credits Earned: {student.credits_earned}/
                    {course.course_credits * 10}
                  </span>
                </div>
              </div>

              <div className={s.progressColumn}>
                <div className={s.progressBar}>
                  <div
                    className={s.progressFill}
                    style={{ width: `${student.progress * 100}%` }}
                  />
                  <span className={s.progressText}>
                    {Math.round(student.progress * 100)}%
                  </span>
                </div>
                <span className={s.enrolledText}>
                  Enrolled: {student.enrolled_date}
                </span>
              </div>
            </div>
          ))}
        </>
      )}

      {activeTab === "lessons" && (
  <div className={s.lessonFile}>
    {sortedLessons.length > 0 ? (
      sortedLessons.map((lesson, idx) => (
        <div key={idx} className={s.lessonCard}>
          {/* Left section: Lesson info */}
          <div className={s.lessonInfo}>
            <span className={s.lessonTitle}>
              {lesson.lesson_id} - {lesson.title}
            </span>
            <span className={s.lessonSub}>
              Students Enrolled: {lesson.enrolled_count}
            </span>
          </div>

          {/* Right section: Progress info */}
          <div className={s.lessonProgress}>
            <span className={s.lessonAvg}>Average Progress</span>
            <div className={s.progressContainer}>
              <div className={s.progressBar}>
                <div
                  className={s.progressFillBlue}
                  style={{ width: `${lesson.average_progress * 100}%` }}
                />
              </div>
              <span className={s.progressTextOutside}>
                {Math.round(lesson.average_progress * 100)}%
              </span>
            </div>
          </div>
        </div>
      ))
    ) : (
      <span className={s.noLessons}>No Lessons</span>
          )}
        </div>
      )}
    </div>
  );
}
