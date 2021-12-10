from django.db import models

# Create your models here.

class Users(models.Model):
	u_id = models.IntegerField()
	u_uid = models.CharField(max_length=45)
	u_firstname = models.CharField(max_length=45)
	u_lastname = models.CharField(max_length=45)
	u_country_code = models.CharField(unique=True,max_length=45)
	u_phone_no = models.CharField(max_length=45)
	u_company_name = models.CharField(max_length=45)
	u_company_no = models.CharField(unique=True,max_length=45)
	u_city = models.CharField(max_length=45,unique=True)
	u_email = models.CharField(max_length=45,unique=True)
	u_conutry = models.CharField(max_length=45,unique=True)
	u_address = models.CharField(max_length=45)
	u_postal_code = models.CharField(unique=True,max_length=45)
	u_email_option = models.CharField(max_length=45)
	u_password = models.CharField(max_length=45)
	u_status = models.CharField(max_length=45)
	u_role = models.CharField(max_length=45)
	u_current_subcription_id = models.CharField(unique=True,max_length=45)
	create_at = models.DateTimeField(auto_now_add=True, blank=True)
	update_at = models.DateTimeField(auto_now_add=True,blank=True)
	u_last_login = models.CharField(max_length=45)


class SavedSearches(models.Model):
	users = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='users')
	s_id = models.IntegerField()
	s_uid = models.CharField(unique=True,max_length=45)
	s_fliter_name = models.CharField(max_length=45)
	s_search_type = models.CharField(max_length=45)


class Notes(models.Model):
	user = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='notes_user')
	n_id = models.IntegerField()
	n_uid = models.CharField(unique=True,max_length=45)
	n_company_name = models.CharField(max_length=45)
	n_text = models.CharField(max_length=45)

class SavedSearchesChip(models.Model):
	savedsearches=models.ForeignKey(SavedSearches,on_delete=models.CASCADE,related_name='savedsearches')
	ss_cd_id = models.IntegerField()
	ss_cd_uid = models.CharField(unique=True,max_length=45)
	ss_cd_chip_group = models.CharField(max_length=45)

class SavedSearchesChipValues(models.Model):
	savedsearcheschip = models.ForeignKey(SavedSearchesChip,on_delete=models.CASCADE,related_name='savedsearcheschip')
	ss_cv_id = models.IntegerField() #primary_key=True
	ss_cv_uid = models.CharField(unique=True,max_length=45)
	ss_cv_chip_value = models.CharField(unique=True,max_length=45)
	

class LimitAvailable(models.Model):
	la_id = models.IntegerField()
	la_uid = models.CharField(unique=True,max_length=45)
	la_limit_company_monitor_available = models.IntegerField()
	la_limit_director_monitor_available = models.IntegerField()
	la_limit_company_reports_available = models.IntegerField()
	la_limit_director_reports_available  = models.IntegerField()
	la_limit_credit_reports_available = models.IntegerField()
	la_limitresults_downloads_exports_available  = models.IntegerField()
	la_limit_chargeable_title_reports_available  = models.IntegerField()
	la_limit_land_registry_records_available  = models.IntegerField()
	la_limit_corporate_land_records_available  = models.IntegerField()

class PlanDetails(models.Model):
	p_id = models.IntegerField()
	p_uid = models.CharField(max_length=45,unique=True)
	p_name  = models.CharField(max_length=45)
	p_limit_company_monitor  = models.IntegerField()
	p_limit_director_monitor = models.IntegerField()
	p_limit_company_reports  = models.IntegerField()
	p_limit_director_reports = models.IntegerField()
	p_limit_credit_reports  = models.IntegerField()
	p_limit_results_download_exports = models.IntegerField()
	p_limit_chargeable_title_reports = models.IntegerField()
	p_limit_land_registry_records = models.IntegerField()
	p_limit_corporate_land_records = models.IntegerField()
	p_level  = models.IntegerField()
	p_amount = models.CharField(max_length=45)
	p_include_predecessor_features  = models.CharField(max_length=45) #This is widget is doughtfull

class SubscriptionDetails(models.Model):
	sub_id = models.IntegerField()
	sub_uid = models.CharField(max_length=45,unique=True)
	user = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='subscriptiondetails_user')
	plandetails = models.ForeignKey(PlanDetails,on_delete=models.CASCADE,related_name='subscriptiondetails_plandetails')
	sub_sr_no = models.CharField(max_length=45)
	sub_limit_details = models.CharField(max_length=45)
	sub_subscription_details = models.CharField(max_length=45)
	limitavailable = models.ForeignKey(LimitAvailable,on_delete=models.CASCADE,related_name='limitavailable')

class PlanFeatures(models.Model):
	pf_id  = models.IntegerField()
	pf_uid = models.CharField(max_length=45,unique=True)
	plandetails = models.ForeignKey(PlanDetails,on_delete=models.CASCADE,related_name='plandetails')
	pf_feature_name  = models.CharField(max_length=45)

class Company(models.Model):
	id = models.IntegerField(primary_key=True)
	uuid  = models.CharField(max_length=45,unique=True)
	dbe_id  = models.IntegerField()
	company_name = models.CharField(max_length=45)
	company_numver = models.CharField(max_length=45)
	regaddress_careof = models.CharField(max_length=45)
	regaddress_pobox = models.CharField(max_length=45)
	regaddress_addressline1 = models.CharField(max_length=45)
	regaddress_addressline2  = models.CharField(max_length=45)
	regaddress_posttown  = models.CharField(max_length=45)
	regaddress_county = models.CharField(max_length=45)
	regaddress_country  = models.CharField(max_length=45)
	regaddress_postcode = models.CharField(max_length=45)
	regaddress_postcode_trim  = models.CharField(max_length=45)
	company_category  = models.CharField(max_length=45)
	company_status = models.CharField(max_length=45)
	country_of_origin = models.CharField(max_length=45)
	dissolution_date  = models.CharField(max_length=45)
	incorporation_date = models.CharField(max_length=45)
	accounts_account_ref_day = models.CharField(max_length=45)
	accounts_account_ref_month = models.CharField(max_length=45)
	accounts_next_due_date = models.CharField(max_length=45)
	accounts_last_made_update = models.CharField(max_length=45)
	accounts_account_category = models.CharField(max_length=45)
	returns_nextduedate = models.CharField(max_length=45)
	returns_lastmadeupdate = models.CharField(max_length=45)
	mortgages_nummortcharges= models.CharField(max_length=45)
	mortgages_nummortoutstanding=models.CharField(max_length=45)
	mortgages_nummortpartsatisfied = models.CharField(max_length=45)
	mortgages_nummortsatisfied = models.CharField(max_length=45)
	siccode_sictext_1= models.CharField(max_length=45)
	siccode_1 = models.CharField(max_length=45)
	siccode_sictext_2= models.CharField(max_length=45)
	siccode_2 = models.CharField(max_length=45)
	siccode_sictext_3 = models.CharField(max_length=45)
	siccode_3  = models.CharField(max_length=45)
	siccode_sictext_4 = models.CharField(max_length=45)
	siccode_4  = models.CharField(max_length=45)
	limitedpartnerships_numgenpartners = models.CharField(max_length=45)
	limitedpartnerships_numlimpartners = models.CharField(max_length=45)
	uri = models.CharField(max_length=45)
	previousname_1_condate = models.CharField(max_length=45)
	_previousname_1_companyname = models.CharField(max_length=45)
	_previousname_2_condate  = models.CharField(max_length=45)
	_previousname_2_companyname = models.CharField(max_length=45)
	previousname_3_condate = models.CharField(max_length=45)
	_previousname_3_companyname= models.CharField(max_length=45)
	previousname_4_condate = models.CharField(max_length=45)
	_previousname_4_companyname = models.CharField(max_length=45)
	previousname_5_condate = models.CharField(max_length=45)
	_previousname_5_companyname = models.CharField(max_length=45)
	previousname_6_condate = models.CharField(max_length=45)
	_previousname_6_companyname = models.CharField(max_length=45)
	previousname_7_condate = models.CharField(max_length=45)
	_previousname_7_companyname = models.CharField(max_length=45)
	previousname_8_condate = models.CharField(max_length=45)
	_previousname_8_companyname = models.CharField(max_length=45)
	previousname_9_condate = models.CharField(max_length=45)
	_previousname_9_companyname = models.CharField(max_length=45)
	previousname_10_condate = models.CharField(max_length=45)
	_previousname_10_companyname = models.CharField(max_length=45)
	confstmtnextduedate = models.CharField(max_length=45)
	confstmtlastmadeupdate = models.CharField(max_length=45)



class SavedList(models.Model):
	sl_id = models.IntegerField()
	sl_uid = models.CharField(max_length=45)
	sl_list_name = models.CharField(max_length=45)
	user = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='savedlist_user')

class SavedListToCompany(models.Model):
	sltc_id = models.IntegerField()
	sltc_uid = models.CharField(max_length=45)
	savedlist = models.ForeignKey(SavedList,on_delete=models.CASCADE,related_name='savedlist')
	company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='savedlist_to_company_company')

class BusinessWatch(models.Model):
	id = models.IntegerField(primary_key=True)
	uuid = models.CharField(max_length=45)
	user = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='businesswatch_user')
	company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='business_watch_company')

class Officers(models.Model):
	id = models.IntegerField(primary_key=True)
	uid = models.CharField(max_length=45)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='officers_company')
	company_house_number = models.CharField(max_length=45)
	business_number=models.CharField(max_length=45)
	date_of_birth_year= models.CharField(max_length=45)
	date_of_birth_month = models.CharField(max_length=45)
	name = models.CharField(max_length=45)
	full_name = models.CharField(max_length=45)
	first_name = models.CharField(max_length=45)
	middlename = models.CharField(max_length=45)
	lastname = models.CharField(max_length=45)
	title  = models.CharField(max_length=45)
	title2 = models.CharField(max_length=45)
	firstname  = models.CharField(max_length=45)
	country_of_residence = models.CharField(max_length=45)
	officer_role = models.CharField(max_length=45)
	postal_code = models.CharField(max_length=45)
	address_line1 = models.CharField(max_length=45)
	premises = models.CharField(max_length=45)
	country = models.CharField(max_length=45)
	region = models.CharField(max_length=45)
	locality = models.CharField(max_length=45)
	occupation = models.CharField(max_length=45)
	resigned_on  = models.DateField()
	nationality = models.CharField(max_length=45)
	appointed_on = models.DateField()

class CompanyPhone(models.Model):
	id = models.IntegerField(primary_key=True)
	uid = models.CharField(max_length=45,unique=True)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='companyphone_company')
	chn = models.CharField(max_length=45)
	business_name = models.CharField(max_length=45)
	phone = models.CharField(max_length=45,unique=True)
	company_tps = models.CharField(max_length=45)
	company_ctps = models.CharField(max_length=45)
	postcode_trim = models.CharField(max_length=45)
	city  = models.CharField(max_length=45)

class CompanyEmails(models.Model):
	id = models.IntegerField(primary_key=True)	
	uid = models.CharField(max_length=45)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='company_Email_company')
	chn  = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	business_name = models.CharField(max_length=45)
	postcode_trim  = models.CharField(max_length=45)
	city = models.CharField(max_length=45)
	country = models.CharField(max_length=45)





















