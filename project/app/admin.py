from django.contrib import admin
from app.models import Users,SavedSearches,Notes,SavedSearchesChip,SavedSearchesChipValues,LimitAvailable,PlanDetails,SubscriptionDetails,PlanFeatures,Company,SavedList,SavedListToCompany,BusinessWatch,Officers,CompanyPhone,CompanyEmails

# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
	list_display=['u_id','u_uid','u_firstname','u_lastname','u_country_code','u_phone_no','u_company_name','u_company_no',
	'u_city','u_email','u_conutry','u_address','u_postal_code','u_email_option','u_password','u_status','u_role','u_current_subcription_id','create_at','update_at','u_last_login']


@admin.register(SavedSearches)
class SavedSearchesAdmin(admin.ModelAdmin):
	list_display = ['s_id','s_uid','s_fliter_name','s_search_type','users']

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
	list_display = ['n_id','n_uid','n_company_name','n_text','user']

@admin.register(SavedSearchesChip)
class SavedSearchesChipAdmin(admin.ModelAdmin):
	list_display = ['ss_cd_id','ss_cd_uid','ss_cd_chip_group','savedsearches']

@admin.register(SavedSearchesChipValues)
class SavedSearchesChipValuesAdmin(admin.ModelAdmin):
	list_display = ['ss_cv_id','ss_cv_uid','ss_cv_chip_value','savedsearcheschip']

@admin.register(LimitAvailable)
class LimitAvailableAdmin(admin.ModelAdmin):
	list_display = ['la_id','la_uid','la_limit_company_monitor_available','la_limit_director_monitor_available',
	'la_limit_company_reports_available','la_limit_director_reports_available','la_limit_credit_reports_available',
	'la_limitresults_downloads_exports_available','la_limit_chargeable_title_reports_available','la_limit_land_registry_records_available',
	'la_limit_corporate_land_records_available']				

@admin.register(PlanDetails)
class PlanDetailsAdmin(admin.ModelAdmin):
	list_display = ['p_id','p_uid','p_name','p_limit_company_monitor','p_limit_director_monitor','p_limit_company_reports',
	'p_limit_director_reports','p_limit_credit_reports','p_limit_results_download_exports','p_limit_chargeable_title_reports',
	'p_limit_land_registry_records','p_limit_corporate_land_records','p_level','p_amount','p_include_predecessor_features']


@admin.register(SubscriptionDetails)
class SubscriptionDetailsAdmin(admin.ModelAdmin):
	list_display = ['sub_id','sub_uid','sub_sr_no','sub_limit_details','sub_subscription_details','user','plandetails','limitavailable']	

@admin.register(PlanFeatures)
class PlanFeaturesAdmin(admin.ModelAdmin):
	list_display = ['pf_id','pf_uid','pf_feature_name','plandetails']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ['id','uuid','dbe_id','company_name','company_numver','regaddress_careof','regaddress_pobox',
	'regaddress_addressline1','regaddress_addressline2','regaddress_posttown','regaddress_county','regaddress_country',
	'regaddress_postcode','regaddress_postcode_trim','company_category','company_status','country_of_origin',
	'dissolution_date','incorporation_date','accounts_account_ref_day','accounts_account_ref_month','accounts_next_due_date',
	'accounts_last_made_update','accounts_account_category','returns_nextduedate','returns_lastmadeupdate','mortgages_nummortcharges',
	'mortgages_nummortoutstanding','mortgages_nummortpartsatisfied','mortgages_nummortsatisfied','siccode_sictext_1','siccode_1',
	'siccode_sictext_2','siccode_2','siccode_sictext_3','siccode_3','siccode_sictext_4','siccode_4','limitedpartnerships_numgenpartners',
	'limitedpartnerships_numlimpartners','uri','previousname_1_condate','_previousname_1_companyname','_previousname_2_condate',
	'_previousname_2_companyname','previousname_3_condate','_previousname_3_companyname','previousname_4_condate',
	'_previousname_4_companyname','previousname_5_condate','_previousname_5_companyname','previousname_6_condate','_previousname_6_companyname',
	'previousname_7_condate','_previousname_7_companyname','previousname_8_condate','_previousname_8_companyname','previousname_9_condate',
	'_previousname_9_companyname','previousname_10_condate','_previousname_10_companyname','confstmtnextduedate','confstmtlastmadeupdate']

@admin.register(SavedList)
class SavedListAdmin(admin.ModelAdmin):
	list_display = ['sl_id','sl_uid','sl_list_name','user'] 

@admin.register(SavedListToCompany)
class SavedListToCompanyAdmin(admin.ModelAdmin):
	list_display=['sltc_id','sltc_uid','savedlist','company']

@admin.register(BusinessWatch)
class BusinessWatchAdmin(admin.ModelAdmin):
	list_display = ['id','uuid','user','company']

@admin.register(Officers)
class OfficersAdmin(admin.ModelAdmin):
	list_display = ['id','uid','company','company_house_number','business_number','date_of_birth_year','date_of_birth_month',
	'name','full_name','first_name','middlename','lastname','title','title2','firstname','country_of_residence',
	'officer_role','postal_code','address_line1','premises','country','region','locality','occupation','resigned_on',
	'nationality','appointed_on']

@admin.register(CompanyPhone)
class CompanyPhoneAdmin(admin.ModelAdmin):
	list_display = ['id','uid','chn','business_name','phone','company_tps','company_ctps','postcode_trim','city','company']

@admin.register(CompanyEmails)
class CompanyEmailsAdmin(admin.ModelAdmin):
	list_display = ['id','uid','chn','email','business_name','postcode_trim','city','country','company']			
