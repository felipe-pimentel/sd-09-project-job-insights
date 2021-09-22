def filter_by_salary_range(jobs, salary):
    print(matches_salary_range(jobs, salary))
    if matches_salary_range(jobs, salary):
        filtered = [
            job
            for job in jobs if job["min_salary"] <= salary <= job["max_salary"]
        ]
    print("filtered ====", filtered)

    return filtered