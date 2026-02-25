// src/pages/EntryPage/EntryPage.jsx
import { useState } from "react";
import s from "./EntryPage.module.css";
import { useNavigate } from "react-router-dom";

export default function EntryPage() {
  const [hoveredRole, setHoveredRole] = useState(null);
  const navigate = useNavigate();

  const go = (r) => {
    const html = document.documentElement;
    html.setAttribute("data-role", r);
    localStorage.setItem("role", r);
    const next =
      r === "student"
        ? "/student/login"
        : r === "instructor"
          ? "/instructor/login"
          : "/admin/log-in";
    navigate(next);
  };

  const roles = [
    {
      id: "student",
      label: "Student",
      variant: "teal",
      icon: "🎓",
      desc: "Access courses, track progress, manage assignments",
    },
    {
      id: "instructor",
      label: "Instructor",
      variant: "orange",
      icon: "📚",
      desc: "Create courses, manage lessons, monitor students",
    },
    {
      id: "admin",
      label: "Admin",
      variant: "green",
      icon: "⚙️",
      desc: "Manage system, users, and institutional settings",
    },
  ];

  return (
    <div className={s.shell}>
      {/* Animated background orbs */}
      <div className={s.orbContainer}>
        <div className={`${s.orb} ${s.orb1}`} />
        <div className={`${s.orb} ${s.orb2}`} />
        <div className={`${s.orb} ${s.orb3}`} />
      </div>

      {/* LEFT PANEL — branding */}
      <section className={s.left}>
        <div className={s.logoWrap}>
          <div className={s.logoGlow} />
          <img src="/logo.svg" alt="Beacon Logo" className={s.logoImg} />
          <h1 className={s.brandName}>B E A C O N</h1>
          <p className={s.slogan}>"Brillare Luminoso"</p>
          <p className={s.tagline}>
            Your gateway to knowledge, progress, and excellence
          </p>
        </div>
      </section>

      {/* RIGHT PANEL — role selection */}
      <section className={s.right}>
        <div className={s.card}>
          <h2 className={s.title}>Welcome Back</h2>
          <p className={s.subtitle}>Choose your role to continue</p>

          <div className={s.roleGrid}>
            {roles.map((role, i) => (
              <button
                key={role.id}
                className={`${s.roleCard} ${hoveredRole === role.id ? s.roleCardActive : ""
                  }`}
                style={{ animationDelay: `${i * 100 + 200}ms` }}
                onMouseEnter={() => setHoveredRole(role.id)}
                onMouseLeave={() => setHoveredRole(null)}
                onClick={() => go(role.id)}
              >
                <span className={s.roleIcon}>{role.icon}</span>
                <span className={s.roleLabel}>{role.label}</span>
                <span className={s.roleDesc}>{role.desc}</span>
                <span className={s.roleArrow}>→</span>
              </button>
            ))}
          </div>
        </div>

        <p className={s.footer}>
          Beacon LMS &middot; Monash University &middot; 2026
        </p>
      </section>
    </div>
  );
}
