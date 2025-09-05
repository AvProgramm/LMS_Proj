-- db/testdata.sql
-- Sprint 1 seed (idempotent). Re-runnable and transactional.
BEGIN;

SET search_path TO lms_schema;

-- Order: users -> profiles -> courses -> drafts -> enrollments
