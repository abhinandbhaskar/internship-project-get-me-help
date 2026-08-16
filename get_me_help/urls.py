"""get_me_help URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('main_page',views.main_page),
    path('home_page_adm',views.adminn_home_page),
    path('user_home_page',views.user_home_page),
    path('worker_home_page',views.worker_home_page),
    path('',views.login_page),
    path('loginn_post',views.loginn_post),
    path('main_registration',views.main_registration),
    path('user_reg',views.user_reg),
    path('user_reg_post',views.user_reg_post),
    path('view_user_profile',views.view_user_profile),
    path('edit_user_profile/<id>',views.edit_user_profile),
    path('edit_user_profile_post/<id>',views.edit_user_profile_post),
    path('view_workers_services',views.view_workers_services),
    path('view_wrk_request_sts',views.view_wrk_request_sts),
    path('payment_selection/<id>/<amnt>',views.payment_selection),
    path('make_payment/<eid>/<amnt>',views.make_payment),
    path('make_payment_post',views.make_payment_post),
    # path('make_payment_post/<id>',views.make_payment_post),
    path('user_work_request/<id>',views.user_work_request),
    path('add_bank_account',views.add_bank_account),
    path('add_bank_account_post',views.add_bank_account_post),
    # path('view_ubank_details',views.view_ubank_details),
    path('view_ubank_details',views.view_ubank_details),
    path('user_dlt_bank_dts/<id>',views.user_dlt_bank_dts),
    path('user_upt_bank_dts/<id>',views.user_upt_bank_dts),
    path('user_upt_bank_dts_post/<id>',views.user_upt_bank_dts_post),
    path('prevoius_works',views.prevoius_works),
    path('payment_status',views.payment_status),
    path('snd_feedback/<id>',views.snd_feedback),
    path('snd_feedback_post/<id>',views.snd_feedback_post),
    path('snd_complaint',views.snd_complaint),
    path('snd_complaint_post',views.snd_complaint_post),
    path('view_complaint_reply',views.view_complaint_reply),
    path('change_user_pass',views.change_user_pass),
    path('change_user_pass_post',views.change_user_pass_post),



    path('view_registered_workers',views.view_registered_workers),
    path('view_approved_workers',views.view_approved_workers),
    path('reject_worker/<id>',views.reject_worker),
    path('approve_worker/<id>',views.approve_worker),
    path('view_users',views.view_users),
    path('view_cmplt_snd_reply',views.view_cmplt_snd_reply),
    path('snd_replys/<id>',views.snd_replys),
    path('snd_reply_post/<id>',views.snd_reply_post),
    path('view_feedbacks',views.view_feedbacks),
    path('add_services',views.add_services),
    path('add_service_post',views.add_service_post),
    path('view_user_services',views.view_user_services),
    path('payment_report',views.payment_report),
    path('delete_services/<int:id>',views.delete_services),
    path('change_admin_pass',views.change_admin_pass),
    path('change_admin_pass_post',views.change_admin_pass_post),




    path('worker_reg',views.worker_reg),
    path('worker_reg_post',views.worker_reg_post),
    path('worker_profile',views.worker_profile),
    path('edit_wrkr_profile/<id>',views.edit_wrkr_profile),
    path('edit_wrkr_profile_post/<id>',views.edit_wrkr_profile_post),
    path('view_services',views.view_services),
    path('addworker_bnk_dtls',views.addworker_bnk_dtls),
    path('addworker_bnk_dtls_post',views.addworker_bnk_dtls_post),
    path('view_worker_baccnt',views.view_worker_baccnt),
    path('worker_dlt_bank_dts/<id>',views.worker_dlt_bank_dts),
    path('worker_upt_bank_dts/<id>',views.worker_upt_bank_dts),
    path('worker_upt_bank_dts_post/<id>',views.worker_upt_bank_dts_post),
    path('add_own_services/<id>',views.add_own_services),
    path('add_own_srv_post/<id>',views.add_own_srv_post),
    path('view_own_services',views.view_own_services),
    path('delete_own_services/<id>',views.delete_own_services),
    path('view_user_request',views.view_user_request),
    path('payments',views.payments),
    path('request_approve/<id>',views.request_approve),
    path('reject_request/<id>',views.reject_request),
    path('view_feedback',views.view_feedback),
    path('change_worker_pass',views.change_worker_pass),
    path('change_worker_pass_post',views.change_worker_pass_post),
]
