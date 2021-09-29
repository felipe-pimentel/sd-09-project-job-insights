from jobs import read


def get_unique_job_types(path):
    general_list = read(path)

    job_list = [job['max_salary'] for job in general_list]
    unic_job_list = [element for element in job_list if element != '']
    elements_int = [int(sal) for sal in unic_job_list]

    return max(elements_int)


get_unique_job_types("jobs.csv")
