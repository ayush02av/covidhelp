from django.db import models
import pytz
import datetime

UTC = pytz.utc
datetimeNow = datetime.datetime.now(UTC)+datetime.timedelta(hours=5.5)

class VerifiedLead(models.Model):
	Timestamp = models.DateTimeField(default=datetimeNow)
	Id = models.CharField(max_length=120, primary_key=True, default='id')
	Supplier = models.CharField(max_length=50, blank=True)
	Resource = models.CharField(max_length=50)
	Contact = models.CharField(max_length=20)
	Remarks = models.TextField(blank=True)

	def save(self, *args, **kwargs):
		self.Id = self.Supplier + self.Resource + self.Contact
		super().save(*args, **kwargs)

	def __str__(self):
		return self.Resource + ' @ ' + self.Contact + ' on ' + self.Timestamp.__str__()

class NonVerifiedLead(models.Model):
	Id = models.CharField(max_length=120, primary_key=True, default='id')
	Supplier = models.CharField(max_length=50, blank=True)
	Resource = models.CharField(max_length=50)
	Contact = models.CharField(max_length=20)
	Remarks = models.TextField(blank=True)

	def save(self, *args, **kwargs):
		self.Id = self.Supplier + self.Resource + self.Contact
		super().save(*args, **kwargs)

	def __str__(self):
		return self.Resource + ' @ ' + self.Contact

class Case(models.Model):
	date = models.DateTimeField(default=datetimeNow)

	total = models.CharField(max_length=20)
	active = models.CharField(max_length=20)
	death = models.CharField(max_length=20)
	recovered = models.CharField(max_length=20)

	def __str__(self):
		return 'total: ' + self.total + ', active: ' + self.active + ' on ' + self.date.__str__()

class BlogArticle(models.Model):
    date = models.DateTimeField(default=datetimeNow)

    Title = models.CharField(max_length=100)
    Content = models.TextField()

    def __str__(self):
        return self.Title + ' on ' + self.date.__str__()