from src.jobs import read


def get_unique_job_types(path):

    jobs = read(path)
    print(jobs)
    return []