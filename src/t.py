def matches_salary_range(job, salary):
    try:
        if job["max_salary"] < salary < job[
          "min_salary"] or type(salary) != int:
            raise ValueError
        if job["max_salary"] >= salary >= job["min_salary"]:
            return True
    except (ArithmeticError, KeyError, TypeError, ValueError):
        raise ValueError
    return False


j = {'max_salary': 0, 'min_salary': 10}
s = 0
matches_salary_range(j, s)
