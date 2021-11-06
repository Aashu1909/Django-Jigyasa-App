from django.contrib import admin
from django.urls import path,include
from .import Admin_views,Staff_views,Student_views
from .import views

urlpatterns = [

     path('login_page/',views.ShowLoginPage,name="ShowLogin"),
     path('doLogin/',views.doLogin,name="doLogin"),
     path('logout_user/', views.logout_user,name="Logout_user"),
     path('accounts/', include('django.contrib.auth.urls'),name="Accounts"),
     # path('admin_login/',views.admin_login,name='AdminLogin'),
     # path('admin_login_page/',views.admin_login_page,name='adminLoginPage'),
     # path('admin_user_logout/',views.admin_user_logout,name='AdminLogout'),
     path('admin_user_details/',views.admin_user_details,name='AdminDetails'),
     path('admin_signup_page/',views.signup_admin_page,name='adminSignupPage'),
     path('admin_home_page/',Admin_views.home,name='AdminHome'),
     path('admin_edit_profile/',Admin_views.edit_profile,name='AdminEditProfile'),
     path('admin_edit_profile_save/',Admin_views.edit_profile_save,name='AdminEditProfileSave'),
     # Admin Faculty paths
     path('admin_add_faculty_page/',Admin_views.add_faculty, name='AdminAddFaculty'),
     path('admin_add_faculty_save_page/',Admin_views.add_faculty_save, name='AdminSaveFaculty'),
     path('admin_manage_faculty_page/', Admin_views.manage_faculty, name='AdminManageFaculty'),
     path('admin_edit_faculty_page/<str:staff_id>/', Admin_views.edit_faculty, name='AdminEditFaculty'),
     path('admin_edit_faculty_save_page', Admin_views.edit_faculty_save, name='AdminSaveEditFaculty'),
     # Admin course Path
     path('admin_add_course_page/',Admin_views.add_course, name='AdminAddCourse'),
     path('admin_add_course_save_page/',Admin_views.add_course_save, name='AdminSaveCourse'),
     path('admin_manage_course_page/',Admin_views.manage_course, name='AdminManageCourse'),
     path('admin_edit_course_page/<str:course_id>/',Admin_views.edit_course, name='AdminEditCourse'),
     path('admin_edit_course_save_page/', Admin_views.edit_course_save, name='AdminSaveEditCourse'),
     # admin Student Path
     path('admin_add_student_page/',Admin_views.add_student, name='AdminAddStudent'),
     path('admin_student_save_page/',Admin_views.add_student_save, name='AdminSaveStudent'),
     path('admin_manage_student_page/', Admin_views.manage_student, name='AdminManageStudent'),
     path('admin_edit_student_page/<str:student_id>', Admin_views.edit_student, name='AdminEditStudent'),
     path('admin_edit_student_save_page', Admin_views.edit_student_save, name='AdminSaveEditStudent'),
     # Admin Subject Path
     path('admin_add_subject_page/', Admin_views.add_subject, name='AdminAddSubject'),
     path('admin_add_subject_save_page/', Admin_views.add_subject_save, name='AdminSaveSubject'),
     path('admin_manage_subject_page/', Admin_views.manage_subject, name='AdminManageSubject'),
     path('admin_edit_subject_page/<str:subject_id>/', Admin_views.edit_subject, name='AdminEditSubject'),
     path('admin_edit_subject_save_page/', Admin_views.edit_subject_save, name='AdminSaveEditSubject'),
     # manage session year
     path('admin_manage_session_year_page/', Admin_views.manage_session, name='AdminManageSession'),
     path('admin_session_year_save_page/', Admin_views.manage_session_save, name='AdminManageSessionSave'),
     # Admin View Attendance.
     path('admin_view_attendance/', Admin_views.view_attendance, name='AdminViewAttendnace'),
     path('admin_get_attendance_dates/', Admin_views.get_attendance_date, name='AdminGetAttendnaceDate'),
     path('admin_fetch_student/', Admin_views.fetch_student_data, name='AdminFetchStudentData'),
     # Leave
     path('admin_view_staff_leave_page/', Admin_views.view_staff_leave_page, name='AdminViewStaffLeavePage'),
     path('admin_staff_leave_approve/<str:leave_id>/', Admin_views.staff_approve_leave, name='AdminStaffLeaveApproved'),
     path('admin_staff_leave_disapprove/<str:leave_id>/', Admin_views.staff_disapprove_leave, name='AdminStaffLeaveDisapproved'),
     path('admin_view_student_leave_page/', Admin_views.view_student_leave_page, name='AdminViewStudentLeavePage'),
     path('admin_student_leave_approve/<str:leave_id>/', Admin_views.student_approve_leave, name='AdminStudentLeaveApproved'),
     path('admin_student_leave_disapprove/<str:leave_id>/', Admin_views.student_disapprove_leave, name='AdminStudentLeaveDisapproved'),
     # Username And Email Availibility
     path('check_user_availabilty/', views.check_user_availability, name='CheckUserAvailabilty'),
     path('check_email_availabilty/', views.check_email_availability, name='CheckEmailAvailabilty'),
     # Feedbacks
     path('student_feedback_message/', Admin_views.student_feedback_message, name='AdminStudentFeedbackMessage'),
     path('student_feedback_message_replied/', Admin_views.student_feedback_message_replied, name='AdminStudentFeedbackMessageReplied'),
     path('staff_feedback_message/', Admin_views.staff_feedback_message, name='AdminStaffFeedbackMessage'),
     path('staff_feedback_message_replied/', Admin_views.staff_feedback_message_replied, name='AdminStaffFeedbackMessageReplied'),

         
     # path('faculty_login/',views.faculty_login, name='FacultyLogin'),
     # path('faculty_user_logout/',views.faculty_user_logout,name='FacultyLogout'),
     # path('faculty_login_page/',views.faculty_login_page, name='FacultyLoginPage'),
     path('faculty_signup_page/', views.signup_faculty_page, name='FacultySignupPage'),
     path('faculty_home_page/', Staff_views.faculty_home, name='FacultyHome'),
     path('get_students/', Staff_views.get_students, name="FacultyGetStudents"),
     path('faculty_take_attendance_page/', Staff_views.take_attendance, name='FacultyTakeAttendance'),
     path('faculty_save_attendance_data/', Staff_views.save_attendance, name="FacultySaveAttendance"),
     path('faculty_view_update_attendance_data/', Staff_views.update_attendance, name="FacultyViewUpdateAttendance"),
     path('faculty_get_attendance_dates/', Staff_views.get_attendance, name="FacultyGetAttendance"),
     path('faculty_fetch_student/', Staff_views.fetch_student, name="FacultyFetchStudent"),
     path('faculty_updated_attendance/', Staff_views.updated_attendance, name="FacultyUpdatedAttendance"),
     path('faculty_apply_leave/', Staff_views.apply_leave, name="FacultyApplyLeave"),
     path('faculty_apply_leave_save/', Staff_views.apply_leave_save, name="FacultyApplyLeaveSave"),
     path('faculty_schedule_meeting/', Staff_views.schedule_meeting, name="FacultyScheduleMeeting"),
     path('faculty_schedule_meeting_save/', Staff_views.schedule_meeting_save, name="FacultyScheduleMeetingSave"),
     path('faculty_feedback_menu/', Staff_views.feedback_menu, name="FacultyFeedbackMenu"),
     path('faculty_feedback_save/', Staff_views.feedback_save, name="FacultyFeedbackSave"),
     path('faculty_edit_profile/',Staff_views.edit_profile,name='StaffEditProfile'),
     path('faculty_edit_profile_save/',Staff_views.edit_profile_save,name='StaffEditProfileSave'),

     # path('student_login/',views.student_login,name='StudentLogin'),
     # path('student_user_logout/',views.student_user_logout,name='StudentLogout'),
     # path('student_login_page/',views.student_login_page, name='StudentLoginPage'),
     # path('student_signup_page/',views.signup_student_page, name='StudentSignupPage'),
     path('student_home_page/',Student_views.student_home, name='StudentHome'),
     path('student_view_attendance/',Student_views.view_attendance, name='StudentViewAttendance'),
     path('student_view_attendance_get/',Student_views.view_attendence_get, name='GetStudentAttendanceReport'),
     path('student_apply_leave/', Student_views.apply_leave, name="StudentApplyLeave"),
     path('student_apply_leave_save/', Student_views.apply_leave_save, name="StudentApplyLeaveSave"),
     path('student_feedback_menu/', Student_views.feedback_menu, name="StudentFeedbackMenu"),
     path('student_feedback_save/', Student_views.feedback_save, name="StudentFeedbackSave"),
     path('student_edit_profile/',Student_views.edit_profile,name='StudentEditProfile'),
     path('student_edit_profile_save/',Student_views.edit_profile_save,name='StudentEditProfileSave'),
     path('student_join_meeting/',Student_views.join_meeting,name='StudentJoinMeeting'),
          
]
