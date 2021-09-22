import jobs

def get_unique_job_types(path):
    print(jobs.read(path))

    return []

if __name__ == "__main__":
    get_unique_job_types("src/jobs.csv")