-- Switch default schema
SET search_path TO lms_schema;

-- Drop existing tables in correct dependency order
DROP TABLE IF EXISTS enrollment CASCADE;
DROP TABLE IF EXISTS course_draft CASCADE;
DROP TABLE IF EXISTS course CASCADE;
DROP TABLE IF EXISTS instructor_profile CASCADE;
DROP TABLE IF EXISTS student_profile CASCADE;
DROP TABLE IF EXISTS users CASCADE;
