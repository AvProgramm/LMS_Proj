import { useNavigate } from "react-router-dom";
import Button from "../../components/Button/Button";
import s from "./StudentMyCourses.module.css";

export default function StudentMyCourses() {
  const navigate = useNavigate();

  return (
    <div className={s.wrap}>
      <header className={s.header}>
        <h1 className={s.title}>MY COURSES</h1>
      </header>

      <section className={s.card}>
        <p className={s.emptyText}>
          No enrolled courses yet.<br />
          Go to enrollment to see all available courses to enrol.
        </p>

        <div className={s.ctaRow}>
          <Button
            variant="aqua"
            className={s.enrollBtn}
            onClick={() => navigate("/student/enrollment")}
          >
            <span>Enrollment</span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="22" height="22" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"
              className={s.arrow}
            >
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 8 16 12 12 16"></polyline>
              <line x1="8" y1="12" x2="16" y2="12"></line>
            </svg>
          </Button>
        </div>
      </section>
    </div>
  );
}
