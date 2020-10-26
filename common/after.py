from datetime import datetime
from pprint import pprint

from testrail_api import TestRailAPI

#
from common.constants import TestRail

api = TestRailAPI(
    "https://inopractice.testrail.io/",
    "fmn.tets@gmail.com",
    "pfTvOKLZCuDmU7vq1n46-ZazIhYJpU8o5BLkCdIPi",
)



def new_project_for_multisuite_run() -> dict:
    """
    Func for new project creation
    :return:
    """
    name = 'New Multisuite ' + str(datetime.utcnow())
    new_project = api.projects.add_project(name=name)
    print('New project: ')
    pprint(new_project)

    return new_project


def new_config_file(new_project):
    testrail_config = open("../testrail.cfg", "w")
    testrail_config.write(str(new_project.get('id')))


def new_single_suite(new_project: dict) -> dict:
    """
    Finc for single suite creation
    :param new_project:
    :return:
    """
    new_project_id = int(new_project.get("id"))
    new_suite = api.suites.add_suite(project_id=new_project_id, name='New Commonsuit')
    print('New suit: ')
    pprint(new_suite)
    return new_suite


def get_suite_list_from_old_project() -> list:
    suite_list_id = []
    suites_list = api.suites.get_suites(project_id=2)
    pprint(suites_list)
    for suite_iteme in suites_list:
        suite_list_id.append(suite_iteme['id'])
    print('Suite id list: ', suite_list_id)
    return suite_list_id

def get_suites_from_old_project() -> list:
    suite_list=[]
    suites_list = api.suites.get_suites(project_id=2)
    pprint(suites_list)
    for suite_iteme in suites_list:
        suite_list.append(suite_iteme)
    print('Suites list: ', suite_list)
    return suite_list


def get_section_list_from_old_project(suite_list_id:list) -> list:
    section_list_id = []
    for item in suite_list_id:
        sections = api.sections.get_sections(project_id=2, suite_id=int(item))
        for i in range(len(sections)):
            section_list_id.append(sections[i].get('id'))
    print("Sections id list: ", section_list_id)
    return section_list_id


def get_sections_from_old_project(suite_list_id:list) -> list:
    section_list=[]
    for item in suite_list_id:
        sections = api.sections.get_sections(project_id=2, suite_id=int(item))
        for i in range(len(sections)):
            section_list.append(sections[i])
    print("Sections list: ", section_list)
    return section_list


def add_section_in_single_suite(section_list_id, new_project_id, new_suite):
    section_tuple_list=[]
    # section_tuple=()
    for section_id in section_list_id:
        new_section_name = api.sections.get_section(section_id=section_id).get('name')
        new_section = api.sections.add_section(project_id=int(new_project_id.get('id')), suite_id=int(new_suite.get('id')),
                                               name=new_section_name)
        section_tuple=(section_id, new_section.get('id'))
        section_tuple_list.append(section_tuple)
    print('Section tuple list', section_tuple_list)
    return section_tuple_list


def add_cases_in_new_sections(section_list_id, new_project_id, section_tuple_list, new_suite):
    for section_id in section_list_id:
        for tuple in section_tuple_list:
            suite_id = api.sections.get_section(section_id=int(section_id)).get('suite_id')
            case_section_list = api.cases.get_cases(project_id=2, suite_id=int(suite_id), section_id=int(section_id))
            if int(section_id)==int(tuple[0]):
                for item in case_section_list:
                    item_id = item.get('id')
                    api.cases.update_case(case_id=item_id, section_id=int(tuple[1]))
            else:
                continue
            print("New section cases: ")
            pprint(api.cases.get_cases(project_id=2, suite_id=int(section_id),
                                       section_id=int(tuple[1])))
    new_sections = api.sections.get_sections(project_id=int(new_project_id.get('id')),
                                             suite_id=int(new_suite.get('id')))
    print('New sections list: ')
    pprint(new_sections)
    print('Adding finish with success')


def create_info_for_return(suite_list_id: list) -> list:
    list_for_return = []
    for suite_id in suite_list_id:
        cases = api.cases.get_cases(project_id=2, suite_id=suite_id)
        print("Cases from suite")
        pprint(cases)
        for diction in cases:
            tuple = (diction.get('id'), diction.get('section_id'))
            list_for_return.append(tuple)
    print("List of id&suite tuple", list_for_return)
    return list_for_return


# def return_case_to_old_project(list_for_return, new_project, new_suite):
#     new_cases=api.cases.get_cases(project_id=new_project.get('id'), suite_id=new_suite.get('id'))
#     for new_dict in new_cases:
#         for old_tuple in list_for_return:
#             if new_dict.get('id')==old_tuple[0]:
#                 api.cases.update_case(case_id=new_dict.get('id'), suite_id=old_tuple[1])
#     print('Return section: ')

def return_case_to_old_project(old_suit, section_list):
    for old_suite in old_suit:
        for section in section_list:
            if section.get('suite_id')==old_suite.get('id'):
                new_cases=api.cases.get_cases(project_id=2, suite_id=old_suite.get('id'))
                for new_dict in new_cases:
                    for old_tuple in TestRail.TUPLE_FOR_RETURN:
                        if new_dict.get('id')==old_tuple[0]:
                            api.cases.update_case(case_id=new_dict.get('id'), section_id=old_tuple[1])

    print('Success returning')

def check_multisuite_project():
    project_name_list=[]
    project_list=api.projects.get_projects()
    for project in project_list:
        project_name_list.append(project.get('name'))
    if 'practice' in project_name_list:
        return True
    else:
        return False


# check_multisuite_projct()
# new_project = new_project_for_multisuite_run()
# # new_config_file(new_project)
# new_suite=new_single_suite(new_project)
new_project = api.projects.get_project(project_id=32)
new_suite=api.suites.get_suite(suite_id=29)
old_suit_id_list=get_suite_list_from_old_project()
old_section_id_list=get_section_list_from_old_project(old_suit_id_list)
old_suit_list=get_suites_from_old_project()
old_section_list=get_sections_from_old_project(old_suit_id_list)
#
tuple_for_return=create_info_for_return(old_suit_id_list)
# section_list_tuple=add_section_in_single_suite(old_section_id_list, new_project, new_suite)
# add_cases_in_new_sections(old_section_id_list, new_project, section_list_tuple, new_suite)

return_case_to_old_project(old_suit_list, old_section_list)