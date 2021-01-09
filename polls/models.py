from django.db import models

class STATES(models.Model):
	states = (
('1', 'Abuja'),
('2', 'Abia'),
('3', 'Anambra'),
('4', 'Akwa Ibom'),
('5', 'Adamawa'),
('6', 'Bauchi'),
('7', 'Bayelsa'),
('8', 'Benue'),
('9', 'Borno'),
('10', 'Cross River'),
('12', 'Ebonyi'),
('13', 'Edo'),
('14', 'Ekiti'),
('15', 'Enugu'),
('16', 'Gombe'),
('17', 'Imo'),
('18', 'Jigawa'),
('19', 'Kaduna'),
('20', 'Kano'),
('21', 'Katsina'),
('22', 'Kebbi'),
('23', 'Kogi'),
('24', 'Kwara'),
('25', 'Delta'),
('26', 'Nasarawa'),
('27', 'Niger'),
('28', 'Ogun'),
('29', 'Ondo'),
('30', 'Osun'),
('31', 'Oyo'),
('32', 'Plateau'),
('33', 'Rivers'),
('34', 'Sokoto'),
('35', 'Taraba'),
('36', 'Yobe'),
('37', 'Zamfara'),
('251', 'Lagos')
		)
	#state_id = models.CharField(max_length=5, blank=True)
	state_name = models.CharField(max_length=200, blank=True, choices=states)

	def __str__(self):
		return '{}'.format(self.state_name)

class LGA(models.Model):
	lga_id = models.CharField(max_length=200, blank=True, unique=True) 
	lga_name = models.CharField(max_length=200, blank=True, unique=True) 
	state_id = models.ForeignKey(STATES, related_name='lga_state_id', on_delete=models.CASCADE) 
	lga_description = models.TextField(blank=True)
	entered_by_user = models.CharField(max_length=200, blank=True)
	date_entered = models.DateTimeField(auto_now_add=True)
	user_ip_address = models.CharField(max_length=200, blank=True, unique=True) 

	def __str__(self):
		return '{}, {}'.format(self.lga_name, self.lga_id, self.lga_description)

class PARTY(models.Model):
	party_name = models.CharField(max_length=200, blank=True, unique=True)
	party_abbreviation = models.CharField(max_length=200, blank=True)


	def __str__(self):
		return '{}'.format(self.party_name)

class ANNOUNCED_PU_RESULTS(models.Model):
	polling_unit_uniqueid = models.CharField(max_length=200, blank=True)
	party = models.ForeignKey(PARTY, related_name='pu_results', on_delete=models.CASCADE, blank=True)
	party_score =models.CharField(max_length=200, blank=True)
	entered_by_user = models.CharField(max_length=200, blank=True)
	date_entered = models.DateTimeField(auto_now_add=True)
	user_ip_address = models.CharField(max_length=200, blank=True, unique=True)

	def __str__(self):
		return '{}, {}, {}'.format(self.polling_unit_uniqueid, self.party, self.party_score)

class WARD(models.Model):
	ward_id = models.CharField(max_length=200, blank=True)
	ward_name = models.CharField(max_length=200, blank=True)
	lga_id = models.ForeignKey(LGA, related_name='ward_lga_id', on_delete=models.CASCADE)
	entered_by_user = models.CharField(max_length=200, blank=True)
	date_entered = models.DateTimeField(auto_now_add=True)
	user_ip_address = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.ward_name

class POLLING_UNIT(models.Model):
	unique_id = models.ForeignKey(ANNOUNCED_PU_RESULTS, related_name='announced_polling_unit_uniqueid',
		on_delete=models.CASCADE, blank=True, default='pu')
	poll_unit_id = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
	ward_id = models.ForeignKey(WARD, related_name='pu_ward_id', on_delete=models.CASCADE)
	lga_id = models.ForeignKey(LGA, related_name='pu_lga_id', on_delete=models.CASCADE)
	state_id = models.ForeignKey(STATES, related_name='pu_state_id', on_delete=models.CASCADE)
	uniqueward_id = models.DecimalField(max_digits=12, decimal_places=2)
	polling_unit_number = models.CharField(max_length=200, blank=True)
	polling_unit_name = models.CharField(max_length=200, blank=True)
	polling_unit_description = models.TextField(blank=True)
	lat_poll = models.CharField(max_length=200, blank=True)
	long_poll = models.CharField(max_length=200, blank=True)
	entered_by_user = models.CharField(max_length=200, blank=True)
	date_entered = models.DateTimeField(auto_now_add=True)
	user_ip_address = models.CharField(max_length=200, blank=True, unique=True)

	def __str__(self):
		return '{},{}'.format(self.polling_unit_name, self.poll_unit_id)

class AGENT_NAME(models.Model):
	first_name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=True)
	phone = models.CharField(max_length=200, blank=True)
	email = models.EmailField()
	poll_unit_id = models.ForeignKey(POLLING_UNIT, related_name='polling_unit',
		on_delete=models.CASCADE)

	def __str__(self):
		return '{},{},{}'.format(self.first_name, self.last_name, self.poll_unit_id)

class ANNOUNCED_LGA_RESULTS(models.Model):
	lga_name = models.ForeignKey(LGA, related_name='announced_lga_name', on_delete=models.CASCADE)
	party = models.ForeignKey(PARTY, related_name='party', on_delete=models.CASCADE, blank=True)
	party_score = models.CharField(max_length=200, blank=True)
	entered_by_user = models.CharField(max_length=200, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	user_ip_address = models.CharField(max_length=200, blank=True, unique=True)

	def __str__(self):
		return '{}, {}'.format(self.lga_name, self.party, self.party_score)

class ANNOUNCED_STATE_RESULTS(models.Model):
	state_name = models.CharField(max_length=200, blank=True)
	party = models.ForeignKey(PARTY, related_name='state_results', on_delete=models.CASCADE,blank=True)
	party_score =models.CharField(max_length=200, blank=True)
	entered_by_user = models.CharField(max_length=200, blank=True)
	date_entered = models.DateTimeField(auto_now_add=True)
	user_ip_address = models.CharField(max_length=200, blank=True, unique=True)

	def __str__(self):
		return '{}, {}, {}'.format(self.state_name, self.party, self.party_score)


class ANNOUNCED_WARD_RESULTS(models.Model):
	ward_name = models.CharField(max_length=200, blank=True)
	party = models.ForeignKey(PARTY, related_name='ward_results', on_delete=models.CASCADE, blank=True)
	party_score =models.CharField(max_length=200, blank=True)
	entered_by_user = models.CharField(max_length=200, blank=True)
	date_entered = models.CharField(max_length=200, blank=True)
	user_ip_address = models.CharField(max_length=200, blank=True, unique=True)

	def __str__(self):
		return '{}, {}', {}.format(self.ward_name, self.party, self.party_score)

