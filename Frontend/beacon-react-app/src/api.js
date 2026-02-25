import axios from "axios";

// Local dev: http://localhost:8000
// Production: https://ma-thursday2pm-team1-2-1.onrender.com
export const api = axios.create({
  baseURL: "http://localhost:8000"
});

// For logout (optional)
/**
api.interceptors.request.use((cfg) => {
  const t = localStorage.getItem("accessToken");
  if (t) cfg.headers.Authorization = `Bearer ${t}`;
  return cfg;
});
*/

// Login only
api.interceptors.request.use((cfg) => {
  const url = (cfg.url || "").toString();

  // Paths that don't require auth
  const isAuthFree = url.includes("/instructor/login/")
    || url.includes("/api/token/")
    || url.includes("/student/login/");

  // Attach token if not auth-free
  if (!isAuthFree) {
    const t = localStorage.getItem("accessToken");
    if (t) cfg.headers.Authorization = `Bearer ${t}`;
  }

  return cfg;
});
