from jobs import read


def get_unique_job_types(path):
    general_list = read(path)

    job_list = [job["job_type"] for job in general_list]
    unic_job_list = [type_ for type_ in set(job_list)]

    return unic_job_list


get_unique_job_types("jobs.csv")
