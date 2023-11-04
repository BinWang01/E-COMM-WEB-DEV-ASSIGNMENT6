from data.models import College, Department, Degree, Course, DegreeCourse
from django.shortcuts import render, get_object_or_404, redirect
from data.forms import (
    CollegeForm,
    DepartmentForm,
    DegreeForm,
    CourseForm,
    DegreeCourseForm,
)
from django.contrib import messages
import pandas as pd
from io import StringIO


# Create your views here.
def index(request):
    degreecourses = (
        DegreeCourse.objects.select_related("degree").select_related("course").all()
    )
    return render(request, "index.html", {"items": degreecourses})


def bulk_upload(request):
    return render(request, "bulk_upload.html")


def college_list(request):
    colleges = College.objects.all()
    return render(request, "college/college-list.html", {"colleges": colleges})


def college_edit(request, pk=None):
    if pk is not None:
        college = get_object_or_404(College, pk=pk)
    else:
        college = None

    if request.method == "POST":
        form = CollegeForm(request.POST, instance=college)
        if form.is_valid():
            updated_college = form.save()
            if college is None:
                messages.success(
                    request, 'College "{}" was created.'.format(updated_college)
                )
            else:
                messages.success(
                    request, 'College "{}" was updated.'.format(updated_college)
                )

            return redirect("college_list")
    else:
        form = CollegeForm(instance=college)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "College",
            "instance": college,
        },
    )


def college_import(request):
    csv = request.FILES["csv_file"]
    csv_data = pd.read_csv(StringIO(csv.read().decode("utf-8")))
    for record in csv_data.to_dict(orient="records"):
        if (
            College.objects.filter(college_name=record["college_name"]).exists()
            == False
        ):
            data_dict = {}
            data_dict["college_name"] = record["college_name"]
            data_dict["college_website"] = record["college_website"]
            data_dict["college_description"] = record["college_description"]
            form = CollegeForm(data_dict)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'College "{}" was created.'.format(record["college_name"])
                )
        else:
            messages.info(
                request,
                'College "{}" already exits. Row skipped.'.format(
                    record["college_name"]
                ),
            )
    return redirect("college_list")


def department_list(request):
    departments = Department.objects.select_related("college").all()
    return render(
        request, "department/department-list.html", {"departments": departments}
    )


def department_edit(request, pk=None):
    if pk is not None:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = None

    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            updated_department = form.save()
            if department is None:
                messages.success(
                    request, 'Department "{}" was created.'.format(updated_department)
                )
            else:
                messages.success(
                    request, 'Department "{}" was updated.'.format(updated_department)
                )

            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Department",
            "instance": department,
        },
    )


def department_import(request):
    csv = request.FILES["csv_file"]
    csv_data = pd.read_csv(StringIO(csv.read().decode("utf-8")))
    for record in csv_data.to_dict(orient="records"):
        if (
            Department.objects.filter(
                department_name=record["department_name"]
            ).exists()
            == False
        ):
            data_dict = {}
            data_dict["department_name"] = record["department_name"]
            data_dict["department_website"] = record["department_website"]
            data_dict["department_description"] = record["department_description"]
            data_dict["college"] = int(record["college_id"])
            form = DepartmentForm(data_dict)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Department "{}" was created.'.format(record["department_name"]),
                )
        else:
            messages.info(
                request,
                'Department "{}" already exits. Row skipped.'.format(
                    record["department_name"]
                ),
            )
    return redirect("department_list")


def degree_list(request):
    degrees = Degree.objects.select_related("department").all()
    return render(request, "degree/degree-list.html", {"degrees": degrees})


def degree_edit(request, pk=None):
    if pk is not None:
        degree = get_object_or_404(Degree, pk=pk)
    else:
        degree = None

    if request.method == "POST":
        form = DegreeForm(request.POST, instance=degree)
        if form.is_valid():
            updated_degree = form.save()
            if degree is None:
                messages.success(
                    request, 'Degree "{}" was created.'.format(updated_degree)
                )
            else:
                messages.success(
                    request, 'Degree "{}" was updated.'.format(updated_degree)
                )

            return redirect("degree_list")
    else:
        form = DegreeForm(instance=degree)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Degree",
            "instance": degree,
        },
    )


def degree_import(request):
    csv = request.FILES["csv_file"]
    csv_data = pd.read_csv(StringIO(csv.read().decode("utf-8")))
    for record in csv_data.to_dict(orient="records"):
        if Degree.objects.filter(degree_name=record["degree_name"]).exists() == False:
            data_dict = {}
            data_dict["degree_name"] = record["degree_name"]
            data_dict["degree_description"] = record["degree_description"]
            data_dict["degree_website"] = record["degree_website"]
            data_dict["online_degree"] = bool(record["online_degree"])
            data_dict["total_hours"] = int(record["total_hours"])
            data_dict["department"] = int(record["department_id"])
            form = DegreeForm(data_dict)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Degree "{}" was created.'.format(record["degree_name"])
                )
        else:
            messages.info(
                request,
                'Degree "{}" already exits. Row skipped.'.format(record["degree_name"]),
            )
    return redirect("degree_list")


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course/course-list.html", {"courses": courses})


def course_edit(request, pk=None):
    if pk is not None:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = None

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            updated_course = form.save()
            if course is None:
                messages.success(
                    request, 'Course "{}" was created.'.format(updated_course)
                )
            else:
                messages.success(
                    request, 'Course "{}" was updated.'.format(updated_course)
                )

            return redirect("course_list")
    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Course",
            "instance": course,
        },
    )


def course_import(request):
    csv = request.FILES["csv_file"]
    csv_data = pd.read_csv(StringIO(csv.read().decode("utf-8")))
    for record in csv_data.to_dict(orient="records"):
        if (
            Course.objects.filter(course_number=record["course_number"]).exists()
            == False
        ):
            data_dict = {}
            data_dict["course_number"] = record["course_number"]
            data_dict["course_name"] = record["course_name"]
            data_dict["course_description"] = record["course_description"]
            data_dict["total_hours"] = int(record["total_hours"])
            form = CourseForm(data_dict)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Course "{}: {}" was created.'.format(
                        record["course_number"], record["course_name"]
                    ),
                )
        else:
            messages.info(
                request,
                'Course "{}: {}" already exits. Row skipped.'.format(
                    record["course_number"], record["course_name"]
                ),
            )
    return redirect("course_list")


def degreecourse_list(request):
    degreecourses = (
        DegreeCourse.objects.select_related("degree").select_related("course").all()
    )
    return render(
        request, "degreecourse/degreecourse-list.html", {"degreecourses": degreecourses}
    )


def degreecourse_edit(request, pk=None):
    if pk is not None:
        degreecourse = get_object_or_404(DegreeCourse, pk=pk)
    else:
        degreecourse = None

    if request.method == "POST":
        form = DegreeCourseForm(request.POST, instance=degreecourse)
        if form.is_valid():
            updated_degreecourse = form.save()
            if degreecourse is None:
                messages.success(
                    request,
                    'Degree Course "{}" was created.'.format(updated_degreecourse),
                )
            else:
                messages.success(
                    request,
                    'Degree Course "{}" was updated.'.format(updated_degreecourse),
                )

            return redirect("degreecourse_list")
    else:
        form = DegreeCourseForm(instance=degreecourse)

    return render(
        request,
        "instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "DegreeCourse",
            "instance": degreecourse,
        },
    )


def degreecourse_import(request):
    csv = request.FILES["csv_file"]
    csv_data = pd.read_csv(StringIO(csv.read().decode("utf-8")))
    for record in csv_data.to_dict(orient="records"):
        if (
            DegreeCourse.objects.filter(fiscal_year=int(record["fiscal_year"]))
            .filter(degree_id=int(record["degree_id"]))
            .filter(course_id=int(record["course_id"]))
            .exists()
            == False
        ):
            data_dict = {}
            data_dict["fiscal_year"] = int(record["fiscal_year"])
            data_dict["degree"] = int(record["degree_id"])
            data_dict["course"] = int(record["course_id"])
            data_dict["is_optional"] = bool(record["is_optional"])
            data_dict["is_core"] = bool(record["is_core"])
            data_dict["is_degree"] = bool(record["is_degree"])
            data_dict["is_major"] = bool(record["is_major"])
            form = DegreeCourseForm(data_dict)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Degree Course: "fiscal year {}, degree id {}, course_id {}" was created.'.format(
                        record["fiscal_year"], record["degree_id"], record["course_id"]
                    ),
                )
        else:
            messages.info(
                request,
                'Degree Course "fiscal year {}, degree id {}, course_id {}" already exits. Row skipped.'.format(
                    record["fiscal_year"], record["degree_id"], record["course_id"]
                ),
            )
    return redirect("degreecourse_list")
