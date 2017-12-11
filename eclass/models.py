from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# VIEWS FOR TEACHER

# Class
class eclass(models.Model):
	name = models.CharField(max_length=50, help_text="Add class")
	description = models.TextField(help_text="Add the description")

	def __str__(self):
		return str(self.name)


# course
class course(models.Model):
	title = models.CharField(max_length=100, help_text="Add course title")
	description = models.TextField(help_text="Add course description")
	picture = models.FileField(upload_to="courses")

	def __str__(self):
		return str(self.title)


#course for
class course_for(models.Model):
	course = models.ForeignKey(course, help_text="Add course", on_delete=models.CASCADE)
	eclass = models.ForeignKey(eclass, help_text="Add class", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.course) + " - " + str(self.eclass)


# Topic
class topic(models.Model):
	title = models.CharField(max_length=100, help_text="Add topic title")
	description = models.TextField(help_text="Add topic description")
	course = models.ForeignKey(course, help_text="Choose a course", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.title) + " - " + str(self.course)

# Chapter
class chapter(models.Model):
	title = models.CharField(max_length=100, help_text="Add topic title")
	description = models.TextField(help_text="Add topic description")
	topic = models.ForeignKey(topic, help_text="Choose a topic", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.title) + " - " + str(self.topic)

# Topic
class note(models.Model):
	title = models.CharField(max_length=100, help_text="Add topic title")
	description = models.TextField(help_text="Add topic description", blank=True, null=True,)
	document = models.FileField(upload_to='chapters', blank=True, null=True, help_text="Add a document file")
	doc_title = models.CharField(max_length=100, help_text="Add file title", null=True, blank=True, default="Add the file's title")
	Image = 'Image'
	Other = 'Other'
	f_types = {
	(Image, 'Image'),
	(Other, 'Other'),
	}
	file_type = models.CharField(max_length=200, choices=f_types, default="Image", blank=True, null=True,)
	file_description = models.TextField(help_text="Add file description", blank=True, null=True,)
	chapter = models.ForeignKey(chapter, help_text="Choose a chapter", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.title) + " - " + str(self.chapter)



# Student
class student(models.Model):
	first_name = models.CharField(max_length=100, help_text="Add First name")
	last_name = models.CharField(max_length=100, help_text="Add Last name")
	email = models.EmailField(help_text="Add Email")
	id_number = models.CharField(max_length=50, help_text="Add ID", unique=True)
	eclass = models.ForeignKey(eclass, help_text="Choose a class", on_delete=models.CASCADE)
	username = models.ForeignKey(User, help_text="Associated user", on_delete=models.CASCADE)

	Pending = 'Pending'
	created = 'created'
	statuses = {
	(Pending, 'Pending'),
	(created, 'created'),
	}

	status = models.CharField(max_length=20, choices=statuses, default="Pending")

	def __str__(self):
		return str(self.id_number) + " - " + str(self.first_name) + " - " + str(self.last_name)


# Assignment
class assignment(models.Model):
	title = models.CharField(max_length=50, help_text="Add title")
	description = models.TextField(help_text="Add topic description")

	Active = 'Active'
	Inactive = 'Inactive'
	Finished = 'Finished'
	statuses = {
	(Active, 'Active'),
	(Inactive, 'Inactive'),
	(Finished, 'Finished'),
	}

	status = models.CharField(max_length=20, choices=statuses, default="Inactive")

	def __str__(self):
		return str(self.title) + " - " + str(self.status)




#Assignment for
class assignment_for(models.Model):
	assignment = models.ForeignKey(assignment, help_text="Add assignment", on_delete=models.CASCADE)
	eclass = models.ForeignKey(eclass, help_text="Add class", on_delete=models.CASCADE)
	Active = 'Active'
	Inactive = 'Inactive'
	statuses = {
	(Active, 'Active'),
	(Inactive, 'Inactive'),
	}

	status = models.CharField(max_length=20, choices=statuses, default="Inactive")

	def __str__(self):
		return str(self.assignment) + " - " + str(self.eclass)


#Completed Assignments
class Completed_assignment(models.Model):
	assignment = models.ForeignKey(assignment, help_text="Add assignment", on_delete=models.CASCADE)
	student = models.ForeignKey(student, help_text="Add class", on_delete=models.CASCADE)
	time = models.DateField(default=datetime.today())
	score = models.CharField(max_length=5, help_text="Add scores")

	def __str__(self):
		return str(self.assignment) + " - " + str(self.student) + " - " + str(self.score)



#Question types
class qtype(models.Model):
	name = models.CharField(max_length=50, help_text="Enter name for the type")
	code = models.CharField(max_length=50, help_text="Enter code for the type")

	def __str__(self):
		return str(self.name)




# Questions
class question(models.Model):
	title = models.TextField(help_text="Enter question")
	q_type = models.ForeignKey(qtype, help_text="Choose question type", on_delete=models.CASCADE)
	document = models.FileField(upload_to='chapters', blank=True, null=True, help_text="Add a document file")
	answer = models.TextField(help_text="Add the correct answer")
	assignment = models.ForeignKey(assignment, help_text="Assignment", on_delete=models.CASCADE)
	# choices = models.ForeignKey(qchoice, help_text="Choose question type", on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return str(self.title) + " - " + str(self.answer)


# Question choices
class qchoice(models.Model):
	option = models.CharField(max_length=300, help_text="Enter option")
	q_type = models.ForeignKey(qtype, help_text="Choose question type", on_delete=models.CASCADE)
	question = models.ForeignKey(question, help_text="Choose question type", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.option) + " - " + str(self.question)



# current course for student
class current(models.Model):
	student = models.ForeignKey(student, on_delete=models.CASCADE, help_text="Choose a student")
	topic = models.ForeignKey(topic, on_delete=models.CASCADE, help_text="Choosea topic")
	chapter = models.ForeignKey(chapter, on_delete=models.CASCADE, help_text="Choose chapter", default=1)

	def __str__(self):
		return str(self.student) + " - " + str(self.topic)


# Invited students
class invited(models.Model):
	email = models.EmailField(help_text="Add Email")
	id_number = models.CharField(max_length=50, help_text="Add ID", unique=True)
	eclass = models.ForeignKey(eclass, help_text="Choose a class", on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id_number) + " - " + str(self.email)