
def create_cohort(course_name, course_code, cohort_year, cohort_semester):
    """With course name and code, plus cohort year and semester, creates cohort name and code

    Args:
        course_name (str): Course name of the cohor being created
        course_code (str): Course code of the cohor being created
        cohort_year (str): Year of the cohor being created
        cohort_semester (str): Semester of the cohor being created

    Returns:
        dict: a dict that associates name of the cohort and its code
    """
    
    name = f'{course_name} {cohort_year}{cohort_semester}'
    cohort_code = f'{course_code}{cohort_year}{cohort_semester}'
    
    return {'Nome': name, 'Código da Turma': cohort_code}