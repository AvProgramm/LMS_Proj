from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfile, Course, Enrollment
from .serializer import CourseSerializer, EnrollmentSerializer

class StudentEnrolledCourses(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        try:
            student = StudentProfile.objects.get(pk=student_id)
        except StudentProfile.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

        enrolled_courses = Course.objects.filter(enrollment__student=student)
        serializer = CourseSerializer(enrolled_courses, many=True)
        return Response(serializer.data, status=200)


class StudentUnenrolledCourses(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        try:
            student = StudentProfile.objects.get(pk=student_id)
        except StudentProfile.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)

        unenrolled_courses = Course.objects.exclude(enrollment__student=student)
        serializer = CourseSerializer(unenrolled_courses, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, student_id):
        course_id = request.data.get("course_id")

        try:
            student = StudentProfile.objects.get(pk=student_id)
            course = Course.objects.get(pk=course_id)
        except StudentProfile.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=404)

        if Enrollment.objects.filter(student=student, course=course).exists():
            return Response({'error': 'Already enrolled'}, status=400)

        enrollment = Enrollment.objects.create(student=student, course=course)
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=201)
