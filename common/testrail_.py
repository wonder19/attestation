from datetime import datetime
from pprint import pprint

from pytest_testrail.testrail_api import APIClient
from testrail_api import TestRailAPI

#
api = TestRailAPI(
    "https://inopractice.testrail.io/",
    "fmn.tets@gmail.com",
    "pfTvOKLZCuDmU7vq1n46-ZazIhYJpU8o5BLkCdIPi",
)

# if use environment variables
# api = TestRailAPI()


#
# new_milestone = api.milestones.add_milestone(
#     project_id=1,
#     name="New milestone",
#     start_on=datetime.now()
# )
# pprint(new_milestone)
#
# my_test_run = api.runs.add_run(
#     project_id=1,
#     #suite_id=2,
#     name="My Api test run",
#     # include_all=True,
#     # milestone_id=new_milestone["id"]
# )
#
# result = api.results.add_result_for_case(
#     run_id=my_test_run["id"],
#     case_id=5,
#     status_id=1,
#     comment="Pass",
#     version="1"
# )
# attach = "screenshots/attach.jpg"
# api.attachments.add_attachment_to_result(result["id"], attach)
#
# api.runs.close_run(my_test_run["id"])
# api.milestones.update_milestone(new_milestone["id"], is_completed=True)

# client = APIClient("https://attestation.testrail.io/",
#                    "dorokhovamp@yandex.ru", "5A1bVIhPRm9QnxMacbPI-tXURX6iO1AnFPOJHkn.g")
# # client.user = "dorokhovamp@yandex.ru"
# # client.password = "5A1bVIhPRm9QnxMacbPI-tXURX6iO1AnFPOJHkn.g"
# case = client.send_get('get_case/1')
# pprint(case)
#
# client.send_get()
# new=api.projects.get_projects()[1]
# project_id=int(new['id'])
# print(new)
# print(new['id'])
#
# print(api.suites.add_suite(project_id=project_id, name='suit2'))
print(api.suites.get_suite(suite_id=3))
case_list = []
pprint(api.cases.get_cases(project_id=2, suite_id=3))
cases = api.cases.get_cases(project_id=2, suite_id=3)
for case in cases:
    case_list.append(int(case["id"]))
print(case_list)

new_run = api.runs.add_run(project_id=2, suite_id=3, case_ids=case_list)
print(new_run)

# api.runs.add_run(project_id=3,)
