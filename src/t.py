def matches_salary_range(job, salary):
    try:
        if job["min_salary"] > job["max_salary"]:
            raise ValueError

        if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
            return True

    except (ValueError, KeyError, TypeError):
        raise ValueError
    return False

