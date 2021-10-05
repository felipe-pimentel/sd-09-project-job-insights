from src.sorting import sort_by


def test_sort_by_criteria():
    criterias_list = [
        {
            "max_salary": "2000",
            "min_salary": "1000",
            "date_posted": "2020-05-10",
        },
        {
            "max_salary": "3000",
            "min_salary": "2000",
            "date_posted": "2020-06-10",
        },
        {
            "max_salary": "4000",
            "min_salary": "3000",
            "date_posted": "2020-07-10",
        },
        {
            "max_salary": "5000",
            "min_salary": "4000",
            "date_posted": "2020-08-10",
        },
        {
            "max_salary": "6000",
            "min_salary": "5000",
            "date_posted": "2020-09-10",
        },
        {
            "max_salary": "7000",
            "min_salary": "6000",
            "date_posted": "2020-10-10",
        },
        {
            "max_salary": "",
            "min_salary": "",
            "date_posted": "",
        },
    ]

    criteria = "min_salary"
    sort_by(criterias_list, criteria)
    assert criterias_list[0]["min_salary"] == "1000"
    assert criterias_list[1]["min_salary"] == "2000"
    assert criterias_list[2]["min_salary"] == "3000"
    assert criterias_list[3]["min_salary"] == "4000"
    assert criterias_list[4]["min_salary"] == "5000"
    assert criterias_list[5]["min_salary"] == "6000"
    assert criterias_list[6]["min_salary"] == ""

    criteria = "max_salary"
    sort_by(criterias_list, criteria)
    assert criterias_list[0]["max_salary"] == "7000"
    assert criterias_list[1]["max_salary"] == "6000"
    assert criterias_list[2]["max_salary"] == "5000"
    assert criterias_list[3]["max_salary"] == "4000"
    assert criterias_list[4]["max_salary"] == "3000"
    assert criterias_list[5]["max_salary"] == "2000"
    assert criterias_list[6]["max_salary"] == ""

    criteria = "date_posted"
    sort_by(criterias_list, criteria)
    assert criterias_list[0]["date_posted"] == "2020-10-10"
    assert criterias_list[1]["date_posted"] == "2020-09-10"
    assert criterias_list[2]["date_posted"] == "2020-08-10"
    assert criterias_list[3]["date_posted"] == "2020-07-10"
    assert criterias_list[4]["date_posted"] == "2020-06-10"
    assert criterias_list[5]["date_posted"] == "2020-05-10"
    assert criterias_list[6]["date_posted"] == ""
