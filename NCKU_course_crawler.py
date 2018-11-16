from requests_html import HTMLSession
import json
import pandas as pd

session = HTMLSession()
major_need_crawl = ['B1', 'B2', 'B3', 'B5', 'C1', 'C2', 'C3', 'C4', 'F8', 'E1', 'E3', 'E4', 'E5', 'E6', 'E8', 'E9', 'F0', 'F1', 'F2', 'F4', 'F5', 'F6', 'F9', 'H1', 'H2', 'H3', 'H4', 'H5', 'I2', 'I3', 'I5', 'I6', 'I7', 'I8', 'D2', 'D4', 'D5', 'D8', 'E2', 'F7', 'E7', 'F2', 'F3', 'C5', 'C6']
all_major = {}
major = []
course = []

crawling_semes = input("input 1 or 2 semester :")
k = input("input major number :")
if crawling_semes == '2':
    r = session.get('http://course-query.acad.ncku.edu.tw/qry/qry002.php?syear=0106&sem=2&college_no=&dept_no={}'.format(k))
elif crawling_semes == '1':
    r = session.get('http://course-query.acad.ncku.edu.tw/qry/qry001.php?dept_no={}'.format(k))
else :
    print('please enter 1 or 2 !')
r.encoding = 'utf-8'
res = r.html.find('thead tr th')    

for i in range(1,5):
    resp = r.html.find('.course_y{} td'.format(i))
    for j in range(len(resp)):
        if (j+1) % len(res)==0 and j!=0:
        
            course.append(str(resp[j].text))
            major.append(course.copy())
            course.clear()
        else:
            course.append(str(resp[j].text))
    
all_major[k] = pd.DataFrame(major,columns = ["major_name", "major_number","number", "course_number", "class_number", "class", "grade", "sort", "group", "en_class", "class_name", "class_type", "credit","teacher_name", "select_people", "remain_number", "time","classroom", "note", "select_condition", "teacher_from_companies","class_number", "diff_num","Moocs"])

print(all_major['{}'.format(k)])

