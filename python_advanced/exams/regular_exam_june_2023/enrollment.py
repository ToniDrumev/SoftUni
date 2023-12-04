def gather_credits(credits_needed, *courses):
    all_courses = []
    credits_earned = 0
    courses_enrolled = []

    for course_info in courses:
        course_name = course_info[0]
        course_credits = course_info[1]

        all_courses.append([course_name, course_credits])

    for course in all_courses:
        if course[0] in courses_enrolled:
            continue

        if credits_earned >= credits_needed:
            break

        courses_enrolled.append(course[0])
        credits_earned += course[1]

    if credits_earned >= credits_needed:
        return f"Enrollment finished! Maximum credits: {credits_earned}.\n" \
               f"Courses: {', '.join(sorted(courses_enrolled))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - credits_earned} credits more."


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
