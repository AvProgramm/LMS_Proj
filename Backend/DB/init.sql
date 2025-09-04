-- Switch default schema
SET search_path TO lms_schema;

-- Drop existing tables in correct dependency order
DROP TABLE IF EXISTS enrollment CASCADE;
DROP TABLE IF EXISTS course_draft CASCADE;
DROP TABLE IF EXISTS course CASCADE;
DROP TABLE IF EXISTS instructor_profile CASCADE;
DROP TABLE IF EXISTS student_profile CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- USERS
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);


-- STUDENT PROFILE
CREATE TABLE student_profile (
    student_profile_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    full_name VARCHAR(255) NOT NULL,
    student_no VARCHAR(50) UNIQUE NOT NULL,
    locked_at TIMESTAMP
);

-- INSTRUCTOR PROFILE
CREATE TABLE instructor_profile (
    instructor_profile_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    full_name VARCHAR(255) NOT NULL,
    staff_no VARCHAR(50) UNIQUE NOT NULL
);

