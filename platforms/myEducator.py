import zipfile
import io
import os
from api.myEducator import myEducatorApiCalls
from api.api import clean_json_request

class MyEducator():
    def __init__(self, course = "", activity = ""):
        self.course = course
        self.activity = activity
        self.myApi = myEducatorApiCalls()
        self.get_course_id()
        self.get_activity_id()
        self.get_all_activity_files()

    def set_course(self, course = ""):
        self.course = course

    def get_course_id(self):
        request = self.myApi.get_all_courses()
        clean_req = clean_json_request(request, "title", "courseid")
        try:
            self.course_id = clean_req[self.course]
        except:
            print("course: \"" + self.course + "\" not found in class list")
    
    def get_activity_id(self):
        request = self.myApi.get_course_by_id(self.course_id)
        clean_req = clean_json_request(request, "title", "activityid")
        try:
            self.activity_id = clean_req[self.activity]
        except:
            print("class: \"" + self.course + "\" not found in class list")

    def get_all_activity_files(self):
        request = self.myApi.get_activity_by_id(self.activity_id)
        # first = True
        for key, value in clean_json_request(request, "userid", "submissionid").items():
            resp = self.myApi.get_submission(value)
            temp_file = zipfile.ZipFile(io.BytesIO(resp.content))
            for name in temp_file.infolist():
                name.filename = str(key) + "." + name.filename.split(".")[-1]
                temp_file.extract(name, "out/")
        self.rename_out_files()

    def rename_out_files(self):
        for temp_file in os.listdir("out"):
            user_details = self.myApi.get_user_by_id(temp_file.split(".")[0]).json()
            os.rename("out/" + temp_file, "out/" + user_details["last_name"] + "," + user_details["first_name"] + "." + temp_file.split(".")[-1])

