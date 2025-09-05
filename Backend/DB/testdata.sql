-- Sprint 1 seed (idempotent). Re-runnable and transactional.
-- Order: users -> profiles -> courses -> drafts -> enrollments


-- ============ USERS (PostgreSQL upsert) ============
WITH src(email, password_hash, role) AS (
  VALUES
    ('alice@student.edu','hash_alice123','student'),
    ('bob@student.edu',  'hash_bob123',  'student'),
    ('carol@student.edu','hash_carol123','student'),
    ('jane@instructor.edu','hash_jane456','instructor'),
    ('mark@instructor.edu','hash_mark789','instructor')
)
INSERT INTO users AS u (email, password_hash, role)
SELECT s.email, s.password_hash, s.role
FROM src s
ON CONFLICT (email) DO UPDATE
SET password_hash = EXCLUDED.password_hash,
    role           = EXCLUDED.role;
