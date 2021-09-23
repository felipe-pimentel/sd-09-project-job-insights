import pytest
from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    jobs = read("src/jobs.csv")
    with pytest.raises(ValueError, match="invalid sorting criteria: invalid"):
        sort_by(jobs, "invalid")
    pass
