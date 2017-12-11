from django.conf.urls import url
from . import views


urlpatterns = [

                # index
                url('^$', views.index, name="Home"),


                # Login page
                url('^login$', views.login, name="Login"),


                # authenticating the user
                url('^log_in$', views.log_in, name="Login"),


                # logout
                url('^logout$', views.logout, name="Login"),


                # Student dashboard
                url('^s/dashboard$', views.student_home, name="Home"),


                # Student courses
                url('^s/courses$', views.student_courses, name="courses"),

                # Topics in a course
                url(r's/course=(?P<course_id>\d+)$', views.student_course, name="course"),


                # Assignments for a class
                url('^s/assignments$', views.student_assignments, name="assignments"),


                # Take an assignment
                url(r's/assignment=(?P<assignment_id>\d+)$', views.student_assignment, name="assignment"),


                # Submitting assignment
                url(r's/submit-assignment=(?P<assignment_id>\d+)$', views.mark_assignment, name="Mark assignment"),


                #Notes for chapter
                url(r's/chapter=(?P<chapter_id>\d+)$', views.student_chapter, name="chapter"),






                # Admin urls


                # Dashboard
                url('^t/dashboard$', views.admin_home, name="Home"), 

                # All classes
                url('^t/classes$', views.admin_classes, name="Home"),

                # Class
                url(r't/class=(?P<class_id>\d+)', views.admin_class, name="Class"),


                # Adding a class
                url('^t/add-class$', views.admin_add_class, name="Add class"),

                url('^t/student$', views.admin_class, name="Home"),

                #All course
                url('^t/courses$', views.admin_courses, name="courses"),

                # Adding a course
                url('^t/add-course$', views.admin_add_course, name="courses"),


                #Topics for a course
                url(r't/topics=(?P<course_id>\d+)', views.admin_topics, name="topics"),

                #Adding a Topic
                url(r't/add-topic=(?P<course_id>\d+)$', views.admin_add_topic, name="courses"),

                #All chapters for a topic
                url(r't/chapters=(?P<topic_id>\d+)$', views.admin_chapters, name="chapters"),

                #Notes for chapter
                url(r't/chapter=(?P<chapter_id>\d+)$', views.admin_chapter, name="chapter"),

                #Adding a chapter
                url(r't/add-chapter=(?P<topic_id>\d+)$', views.admin_add_chapter, name="courses"),

                #Adding Notes
                url(r't/add-note=(?P<chapter_id>\d+)$', views.admin_add_note, name="courses"),

                #Student
                url(r't/individual=(?P<st_id>\w+)$', views.admin_student, name="student"),


                #All assignments
                url('^t/assignments$', views.admin_assignments, name="assignments"),

                #Assignment
                url(r't/assignment=(?P<assignment_id>\d+)$', views.admin_assignment, name="assignment"),


                # Adding assignment
                url('^t/add-assign$', views.admin_add_assign, name="Add assignment"),

                # Adding a question
                url(r't/add-question=(?P<assignment_id>\d+)$', views.admin_add_question, name="Add question"),


                # Link course to class
                url('^t/apply-course-to-class$', views.admin_apply_course, name="Link courses"),

                # Link assignment to class
                url('^t/apply-assignment-to-class$', views.admin_apply_assignment, name="Link assignments"),

                # Activate assignment
                url(r't/activate=(?P<assignment_id>\d+)$', views.admin_activate, name="Link assignments"),

                # Deactivate assignment
                url(r't/deactivate=(?P<assignment_id>\d+)$', views.admin_deactivate, name="Link assignments"),



                # Adding a student to a class
                url(r't/add-student-to-class=(?P<class_id>\d+)$', views.admin_invite_student, name="Invite student"),


                # If a student is already added
                url('^t/already-added$', views.admin_already_added, name="Student is already added"),

                # If a student is already invited
                url('^t/already-invited$', views.admin_already_invited, name="Student is already invited"),



                # Confirm the invitation
                url(r'confirm=(?P<st_id>\w+)$', views.confirm_membership, name="Confirming invitation"),


                # Confirming the invitation
                url(r'register=(?P<st_id>\w+)$', views.signup, name="Confirming invitation"),

                # Messaging a student
                url(r't/send-message-to=(?P<st_id>\w+)$', views.messageStudent, name="Send message"),


                # Messagin the whole class
                url(r't/send-message-to-class=(?P<class_id>\d+)$', views.messageClass, name="Message a class"),

                
               
               ]
