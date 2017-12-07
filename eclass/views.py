from django.shortcuts import render, redirect, get_object_or_404
from eclass.models import *
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

# Create your views here.

# Login
def login(request):
	return render(request, 'login.html')


# Logging in
def log_in(request):
    """ Validating a user """
    data = {}
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password=password)
        if user is not None:
            if not user.is_superuser:
                auth.login(request,user)
                return redirect('/s/dashboard')
                #return redirect(request.POST.get('next','/adminProducts'))
            else:
                auth.login(request,user)
                return redirect('/t/dashboard')
        else:
            return render(request, 'invalid-loginhtml')

# Logging out
def logout(request):
    auth.logout(request)
    return redirect('/login')



@login_required
def index(request):
	user = request.user
	if user.is_authenticated:
		if user.is_superuser:
			return redirect('/t/dashboard')
		else:
			return redirect('/s/dashboard')
	else:
		return redirect('/login')

# Student dashboard
@login_required
def student_home(request):
	user = request.user
	if not user.is_superuser:
		st =  student.objects.get(username=request.user)
		current_course = current.objects.get(student=st)
		crss = course_for.objects.filter(eclass=st.eclass)
		courses = []

		for crs in crss:
			courses.append(crs.course)

		# current course
		for current_topic in topic.objects.all():
			if current_topic == current_course.topic:
				for course_item in (course.objects.all()):
					if course_item == current_topic.course:
						course_final = current_topic.course
						break


		data = {}
		data['student'] = student.objects.get(username=request.user)
		data['current'] = current.objects.get(student=st)
		data['courses'] = courses
		data['course'] = course_final
		data['chapter'] = current_course.chapter
		return render(request, 'student-home.html', data)
	else:
		return redirect('/error')



# All course for a student
@login_required
def student_courses(request):
	user = request.user
	if not user.is_superuser:
		st =  student.objects.get(username=request.user)
		data = {}
		data['student'] = student.objects.get(username=request.user)
		data['courses'] = course.objects.all()
		data['course_for'] = course_for.objects.filter(eclass=st.eclass)
		return render(request, 'student-courses.html', data)
	else:
		return redirect('/error')



# Topics for a student
@login_required
def student_course(request, course_id):
	user = request.user
	if not user.is_superuser:
		instance = get_object_or_404(course, id=course_id)
		st =  student.objects.get(username=request.user)
		# cu = current.objects.get(student=student.objects.get(pk=st.id))
		setTopic = topic.objects.filter(course = course.objects.get(pk=course_id)).first()
		setChapter = chapter.objects.filter(topic = setTopic).first()

		current.objects.filter(student=st).update(topic = setTopic, chapter=setChapter)

		return redirect('/s/chapter=' + str(setChapter.id))

		# data = {}
		# data['student'] = student.objects.get(username=request.user)
		# data['topics'] = topic.objects.filter(course=course.objects.get(pk=course_id))
		# data['chapters'] = chapter.objects.all()
		# data['notes'] = note.objects.all()
		# data['course'] = course.objects.get(pk=course_id)
		# data['current'] = current.objects.get(student=student.objects.get(pk=st.id))
		# return render(request, 'student-course.html', data)
	else:
		return redirect('/error')


#Viewing notes in a chapter
@login_required
def student_chapter(request, chapter_id):
	user = request.user
	if not user.is_superuser:
		instance = get_object_or_404(chapter, id=chapter_id)
		st =  student.objects.get(username=request.user)
		chap = chapter.objects.get(pk=chapter_id)

		tops = topic.objects.all()

		for top in tops:
			if top == chap.topic:
				course = top.course
				break

		current.objects.filter(student=st).update(topic = chap.topic, chapter=chap)

		# cu = current.objects.get(student=student.objects.get(pk=st.id))
		data = {}
		data['student'] = student.objects.get(username=request.user)
		data['topics'] = topic.objects.filter(course=course)
		data['chapters'] = chapter.objects.all()
		data['notes'] = note.objects.all()
		data['course'] = course
		data['current'] = current.objects.get(student=student.objects.get(pk=st.id))
		data['user'] = user
		return render(request, 'student-course.html', data)
	else:
		return redirect('/error')


# All assignments for student
@login_required
def student_assignments(request):
	user = request.user
	if not user.is_superuser:
		st = student.objects.get(username=request.user)
		asss = assignment.objects.filter(status="Active")
		ass_count = assignment.objects.filter(status="Active").count()
		comps = Completed_assignment.objects.filter(student=student.objects.get(username=request.user))
		not_completed = []
		i=1

		
		# while i <= ass_count:
		# 	for ass in asss:
		# 		for comp in comps:
		# 			if ass == comp.assignment:
		# 				break
		# 			else:
		# 				if ass not in not_completed:
		# 					not_completed.append(ass)
		# 				# elif ass in not_completed:
		# 				# 	not_completed.remove(ass)
		# 	i+=1
		for ass in asss:
			not_completed.append(ass)

		for comp in comps:
			if comp.assignment in not_completed:
				not_completed.remove(comp.assignment)

		data = {}
		data['assfors'] = assignment_for.objects.filter(eclass=st.eclass)
		data['assignments'] = assignment.objects.filter(status="Active")
		data['completed'] = Completed_assignment.objects.filter(student=student.objects.get(username=request.user))
		data['incompleted'] = not_completed
		data['student'] = st
		return render(request, 'student-assignments.html', data)
	else:
		return redirect('/error')


# Taking an assignment
@login_required
def student_assignment(request, assignment_id):
	user = request.user
	if not user.is_superuser:
		instance = get_object_or_404(assignment, id=assignment_id)

		# Checking if the assignment is not done by the student
		theass = assignment.objects.get(id=assignment_id)
		dones = Completed_assignment.objects.filter(student = student.objects.get(username=request.user))
		for done in dones:
			if theass == done.assignment:
				return redirect('/error')
		data = {}
		data['assignment'] = assignment.objects.get(pk=assignment_id)
		data['questions'] = question.objects.filter(assignment=assignment.objects.get(pk=assignment_id))
		data['qcounter'] = question.objects.filter(assignment=assignment.objects.get(pk=assignment_id)).count()
		data['choices'] = qchoice.objects.all()
		data['types'] = qtype.objects.all()
		data['student'] = student.objects.get(username=request.user)
		return render(request, 'student-assignment.html', data)
	else:
		return redirect('/error')



# Marking an assignment
@login_required
def mark_assignment(request, assignment_id):
	user = request.user
	if not user.is_superuser:
		st = student.objects.get(username = request.user)
		if request.method == 'POST':
			count = int(request.POST.get('qcount'))
			temp = count
			j = 0
			corrects = 0
			subs = 0

			while temp > 0:
				j = j+1
				temp = temp/10
			k=1
			while j >= 0:
				k = k*10
				j = j-1

			answers = question.objects.all()
			i=0
			n = 0

			while i <= count:
				for answer in answers:
					name = str(answer.id)+str(i)
					if str(name) in request.POST:
						for quetype in qtype.objects.all():
							if answer.q_type == quetype:
								if quetype.code == "checkbox":
									answered = request.POST.getlist(str(name),'')
									for opt in answered:
										n = n+1
										if opt in answer.answer:
											subs = subs+1

									corrects = corrects + float(subs/n)

									
								else:
									answered = request.POST.get(str(name),'')
									if answered == answer.answer:
										corrects = corrects+1
				i=i+1


		score = (float(corrects) * 100)/float(count)

		Completed_assignment.objects.create(
			student = st,
			assignment = assignment.objects.get(pk=assignment_id),
			score = format(score, '.2f'),
			time = datetime.today(),)

		return redirect('/s/assignments')
	else:
		return redirect('/error')


# Admin Views
@login_required
def admin_home(request):
	user = request.user
	if user.is_superuser:
		return render(request, 'admin-home.html')
	else:
		return redirect('/error')



# All classes
@login_required
def admin_classes(request):
	user = request.user
	if user.is_superuser:
		data = {}
		data['classes'] = eclass.objects.all()
		return render(request, 'admin-classes.html', data)
	else:
		return redirect('/error')


# Adding a class
@login_required
def admin_add_class(request):
	user = request.user
	if user.is_superuser:
		if request.method == 'POST':
			name = request.POST['name']
			description = request.POST['description']

			eclass.objects.create(
				name = name,
				description = description
				)
			return redirect('/t/classes')
	else:
		return redirect('/error')


@login_required
def admin_class(request, class_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(eclass, id=class_id)
		data = {}
		data['class'] = eclass.objects.get(pk=class_id)
		data['students'] = student.objects.filter(eclass = eclass.objects.get(pk=class_id))
		return render(request, 'admin-class.html', data)
	else:
		return redirect('/error')

@login_required
def admin_student(request, st_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(User, id=st_id)
		cu = current.objects.get(student=student.objects.get(pk=st_id))
		cuTopic = cu.topic
		cuChap = cu.chapter
		tops = topic.objects.all()
		chaps = chapter.objects.all()

		#current topic
		for top in tops:
			if top == cu.topic:
				current_topic = top


		#current chapter
		for chap in chaps:
			if chap == cuChap:
				current_chapter = chap.title
				break

		data = {}
		data['student'] = student.objects.get(pk=st_id)
		data['dones'] = Completed_assignment.objects.filter(student=student.objects.get(pk=st_id))
		data['current_course'] = current_topic.course
		data['curent_topic'] = current_topic
		data['current'] = cu.topic
		data['current_chapter'] = current_chapter
		data['assignments'] = assignment.objects.all()
		data['user'] = user
		return render(request, 'admin-student.html', data)
	else:
		return redirect('/error')


# All assingments
@login_required
def admin_assignments(request):
	user = request.user
	if user.is_superuser:
		data = {}
		data['assignments'] = assignment.objects.all()
		data['eclasses'] = eclass.objects.all()
		data['user'] = user
		return render(request, 'admin-assignments.html', data)
	else:
		return redirect('/error')


#Assignment
@login_required
def admin_assignment(request, assignment_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(assignment, id=assignment_id)
		data = {}
		data['assignment'] = assignment.objects.get(pk=assignment_id)
		data['questions'] = question.objects.filter(assignment=assignment.objects.get(pk=assignment_id))
		data['classes'] = assignment_for.objects.filter(assignment=assignment.objects.get(pk=assignment_id))
		data['types'] = qtype.objects.all()
		data['choices'] = qchoice.objects.all()
		data['user'] = user
		return render(request, 'admin-assignment.html', data)
	else:
		return redirect('/error')



# Adding assignment
@login_required
def admin_add_assign(request):
	user = request.user
	if user.is_superuser:
		if request.method=="POST":
			title = request.POST['title']
			description = request.POST.get('description')
			assignment.objects.create(
				title = title,
				description = description,
				)
			return redirect('/t/assignments')
	else:
		return redirect('/error')


#Adding a question
@login_required
def admin_add_question(request, assignment_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(assignment, id=assignment_id)
		if request.method == "POST":
			title = request.POST['title']
			q_type = request.POST['q-type']
			answer = request.POST['correct']
			nchoices = request.POST.get('number-choices', '')

			if request.FILES:
				question.objects.create(
					title = title,
					q_type = qtype.objects.get(code=q_type),
					document = request.FILES['file'],
					answer = answer,
					assignment = assignment.objects.get(pk=assignment_id),)

			else:
				question.objects.create(
					title = title,
					q_type = qtype.objects.get(code=q_type),
					answer = answer,
					assignment = assignment.objects.get(pk=assignment_id),)

			if q_type == 'radio' or q_type == 'checkbox':
				i = 1
				while i <= int(nchoices):
					option = request.POST.get('option' + str(i), '')
					qchoice.objects.create(
						option = option,
						q_type = qtype.objects.get(code=q_type),
						question = question.objects.all().last(),
						)
					i = i+1

		return redirect('/t/assignment=' + assignment_id)
	else:
		return redirect('/error')


#All course
@login_required
def admin_courses(request):
	user = request.user
	if user.is_superuser:
		data = {}
		data['courses'] = course.objects.all()
		data['eclasses'] = eclass.objects.all()
		return render(request, 'admin-courses.html', data)
	else:
		return redirect('/error')

#Topics for a course
@login_required
def admin_topics(request, course_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(course, id=course_id)
		data = {}
		data['courses'] = course.objects.all()
		data['course'] = course.objects.get(pk=course_id)
		data['topics'] = topic.objects.filter(course=course_id)
		data['user'] = user
		return render(request, 'admin-topics.html', data)
	else:
		return redirect('/error')

# Adding a topic
@login_required

def admin_add_topic(request, course_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(course, id=course_id)
		if request.method == 'POST':
			courseTitle = request.POST['course']
			title = request.POST['title']
			description = request.POST['description']


			topic.objects.create(
				title = title,
				description = description,
				course = course.objects.get(title = courseTitle),
				)

			return redirect('/t/topics=' + str(course_id))
	else:
		return redirect('/error')



#All chapters for a topic
@login_required
def admin_chapters(request, topic_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(topic, id=topic_id)
		data = {}
		data['chapters'] = chapter.objects.filter(topic = topic.objects.get(pk=topic_id))
		data['topic'] = topic.objects.get(pk=topic_id)
		data['user'] = user
		return render(request, 'admin-chapters.html', data)
	else:
		return redirect('/error')



#Notes for a chapter
@login_required
def admin_chapter(request, chapter_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(chapter, id=chapter_id)
		data = {}
		data['chapter'] = chapter.objects.get(pk=chapter_id)
		data['notes'] = note.objects.filter(chapter = chapter.objects.get(pk=chapter_id))
		data['user'] = user
		return render(request, 'admin-chapter.html', data)
	else:
		return redirect('/error')


#Adding a chapter
@login_required
def admin_add_chapter(request, topic_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(topic, id=topic_id)
		if request.method == 'POST':
			title = request.POST['title']
			description = request.POST['description']


			chapter.objects.create(
				title = title,
				description = description,
				topic = topic.objects.get(pk = topic_id),
				)

			return redirect('/t/chapters=' + str(topic_id))
	else:
		return redirect('/error')



#Adding Notes
@login_required
def admin_add_note(request, chapter_id):
	user = request.user
	if user.is_superuser:
		instance = get_object_or_404(chapter, id=chapter_id)
		if request.method == 'POST':
			title = request.POST['title']
			description = request.POST.get('description', '')
			# document = request.FILES['file']
			doc_title = request.POST.get('file_title', '')
			file_type = request.POST.get('file_type', '')
			file_description = request.POST.get('file_description', '')

			if request.FILES:
				note.objects.create(
					title = title,
					description = description,
					document = request.FILES['file'],
					doc_title = doc_title,
					file_type = file_type,
					file_description = file_description,
					chapter = chapter.objects.get(pk = chapter_id),
					)

			else:
				note.objects.create(
					title = title,
					description = description,
					chapter = chapter.objects.get(pk = chapter_id),
					)

			return redirect('/t/chapter=' + str(chapter_id))
	else:
		return redirect('/error')




# Applying course to class
@login_required
def admin_apply_course(request):
	user = request.user
	if user.is_superuser:
		if request.method == "POST":
			cs = request.POST['course']
			ec = request.POST['eclass']
			css = course.objects.get(pk=int(cs))
			ecl = eclass.objects.get(pk=int(ec))
			cfors = course_for.objects.filter(course = course.objects.get(pk=int(cs)))
			cforscount = course_for.objects.filter(course = course.objects.get(pk=int(cs))).count()
			classes = []
			check = 0

			#Assign a course to a class
			if cforscount == 0:
				course_for.objects.create(
					course=course.objects.get(pk=int(cs)),
					eclass=eclass.objects.get(pk=int(ec)),
					)					
				return redirect('/t/courses')

			else:
				for cfor in cfors:
					classes.append(cfor.eclass)

				if ecl in classes:
					return redirect('/t/courses')

				else:
					course_for.objects.create(
						course=course.objects.get(pk=int(cs)),
						eclass=eclass.objects.get(pk=int(ec)),
						)
			return redirect('/t/courses')						
	else:
		return redirect('/error')

# Applying assignment to class
@login_required
def admin_apply_assignment(request):
	user = request.user
	if user.is_superuser:
		if request.method == "POST":
			cs = request.POST['assignment']
			ec = request.POST['eclass']
			css = assignment.objects.get(pk=int(cs))
			ecl = eclass.objects.get(pk=int(ec))
			cfors = assignment_for.objects.filter(assignment = assignment.objects.get(pk=int(cs)))
			cforscount = assignment_for.objects.filter(assignment = assignment.objects.get(pk=int(cs))).count()
			classes = []
			check = 0

			#Auto activate the assignment
			if str(css.status) != "Active":
				assignment.objects.filter(pk=int(cs)).update(status="Active")

			#Assign the assignment to class
			if cforscount == 0:
				assignment_for.objects.create(
					assignment=assignment.objects.get(pk=int(cs)),
					eclass=eclass.objects.get(pk=int(ec)),
					)					
				return redirect('/t/assignments')

			else:
				for cfor in cfors:
					classes.append(cfor.eclass)

				if ecl in classes:
					return redirect('/t/assignments')

				else:
					assignment_for.objects.create(
						assignment=assignment.objects.get(pk=int(cs)),
						eclass=eclass.objects.get(pk=int(ec)),
						)
			return redirect('/t/assignments')						
	else:
		return redirect('/error')


#Adding a course
@login_required
def admin_add_course(request):
	user = request.user
	if user.is_superuser:
		if request.method == "POST":
			title = request.POST['title']
			description = request.POST.get('description')
			course.objects.create(
				title=title,
				description=description,
				picture=request.FILES['thumbnail'])
			return redirect('/t/courses')
	else:
		return redirect('/error')


# Inviting a student to a class
@login_required
def admin_invite_student(request, class_id):
	user = request.user
	if user.is_superuser:
		if request.method == 'POST':
			first_name = request.POST['fname']
			last_name = request.POST['lname']
			id_number = request.POST['id']
			email = request.POST['email']
			crs = course_for.objects.filter(eclass=eclass.objects.get(pk=class_id))
			crscount = course_for.objects.filter(eclass=eclass.objects.get(pk=class_id)).count()

			if crscount == 0:
				return render(request, 'no-content-for-class.html')
			else:
				topss = topic.objects.filter(course=crs.last().course)
				topssCounter = topic.objects.filter(course=crs.last().course).count()
				if topssCounter == 0:
					return render(request, 'no-content-for-class.html')
				else:
					chappss = chapter.objects.filter(topic=topss.last())
					chappssCounter = chapter.objects.filter(topic=topss.last()).count()
					if chappssCounter == 0:
						return render(request, 'no-content-for-class.html')
					else:
						all_id = []
						all_inv = []
						sts = student.objects.all()
						invs = invited.objects.all()

						# Checking if the student is already invited
						for inv in invs:
							all_inv.append(inv.id_number)

						if id_number in all_inv:
							return redirect('/t/already-invited')

						# Checking if the student is already added
						for st in sts:
							all_id.append(st.id_number)

						if id_number in all_id:
							return redirect('/t/already-added')
						else:
							invited.objects.create(
								email=email,
								id_number=id_number,
								eclass=eclass.objects.get(id=class_id))
							return redirect('/t/class='+ str(class_id))
	else:
		return redirect('/error')


# If the student is already added
@login_required
def admin_already_added(request):
	user = request.user
	if user.is_superuser:
		return render(request, 'already-added.html')

	else:
		return redirect('/error')



# If the student is already added
@login_required
def admin_already_invited(request):
	user = request.user
	if user.is_superuser:
		return render(request, 'already-invited.html')

	else:
		return redirect('/error')


# Confrim membership
def confirm_membership(request, st_id):
	instance = get_object_or_404(invited, id_number=st_id)
	data ={}
	data['student'] = invited.objects.get(id_number=st_id)
	return render(request, 'sign-up.html', data)


# Signing up
def signup(request, st_id):
	instance = get_object_or_404(invited, id_number=st_id)
	inv = invited.objects.get(id_number=st_id)
	crs = course.objects.all()
	cfor = course_for.objects.filter(eclass=inv.eclass).last()
	top = topic.objects.filter(course=cfor.course).last()
	chap = chapter.objects.filter(topic=top).last()

	# eclasses = eclass.objects.all()

	# getting class
	# for ec in eclasses:
	# 	if ec == inv.eclass:
	# 		ecl = ec

	email = inv.email
	if request.method == "POST":
		username = request.POST['username']
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		password = request.POST['password']

		User.objects.create_user(
			username=username,
			password=password,
			first_name=first_name,
			last_name=last_name,
			email=email,)
		student.objects.create(
			first_name=first_name,
			last_name=last_name,
			eclass=inv.eclass,
			username=User.objects.get(username=username),
			email=inv.email,
			id_number=inv.id_number)
		current.objects.create(
			student=student.objects.get(username=User.objects.get(username=username)),
			topic=top,
			chapter=chapter.objects.filter(topic=top).last(),)
		invited.objects.get(id_number=st_id).delete()
		return redirect('/login')
