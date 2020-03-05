import requests
from .api import get_json_request

class myEducatorApiCalls:
    base_url = ""
    current_url = ""
    task = {}
    cred = {}
    def __init__(self):
        self.base_url = "https://go.myeducator.com/api/"
        cred = open(".credentials", 'r')
        for line in cred:
            self.cred[line.strip().split(',')[0]] = line.strip().split(',')[1]
        cred.close()
        self.task = self.cred

    def get_all_courses(self):
        self.current_url = self.base_url + "user_courses/"
        request = get_json_request(self.current_url, self.task)
        return request

    def get_course_by_id(self, course_id):
        self.task["courseid"] = course_id
        self.current_url = self.base_url + "course_activities/"
        request = get_json_request(self.current_url, self.task)
        self.task = self.cred
        return request

    def get_activity_by_id(self, activity_id):
        self.task["activityid"] = activity_id
        self.current_url = self.base_url + "activity_submissions/"
        request = get_json_request(self.current_url, self.task)
        self.task = self.cred
        return request

    def get_submission(self, submission_id):
        self.task["submissionid"] = submission_id
        self.current_url = self.base_url + "activity_submission_files/"
        request = requests.post(self.current_url, json=self.task)
        self.task = self.cred
        return request

    def get_user_by_id(self, user_id):
        self.task["userid"] = user_id
        self.current_url = self.base_url + "user_details/"
        request = requests.post(self.current_url, json=self.task)
        self.task = self.cred
        return request
