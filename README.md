# FizzyNewt 2.0

## Objectives 

+ Create a standalone implementation of current FizzyNewt prototype (www.fizzynewt.com) that does not depend on Office 365.
+ Monetise at £1.99 per student. Capped at £10k per institution.
+ 5,000 student users after year 1
+ 20,000 users after year 3
+ 100,000 users after year 5

## Functionality Hit-List (Specification)

### Billing/Invoicing

+ Free for up to 100 students.
+ Otherwise free for 6 weeks trial.
+ Then functionality subject to received payment.
+ Annual invoice. 
+ Invoice according to code suffix (e.g. "LIFE") or institutional, capped at £10k pa.

### General

+ OAuth login system w/ email authentication.
+ Users identify institution when signingup. Institution list required. What if institution not in list?
+ Default user - Student
+ Staff do not NEED to register, i.e. can generate codes for a given institution and class.
+ Staff DO NEED to register if they wish to monitor their class attendance. Admin enabled.
+ GDPR?
+ Database backup (daily)

### Admin

+ Re-label class identifier (E.g. LF113 to LIFE113) for FN code. Apply to all registrations with code optional?
+ Auto/Manual email generation to warn of low attendance. Set threshold (e.g. < 50% attendance). Set frequency. 
+ Allow admin to nominate other staff (via email) to be admin.
+ Allow admin to nominate but restrict functionality.
+ 6 months validation of admin via email confirmation.
+ Update student record. Update name, email and ID.
+ Create student report by data (default 1 month)
+ Create student report by course.
+ Create student report by multiple courses (or via course suffix, e.g. "LIFE")
+ Global announcement popup - after every student submits code - specify start/finish.
+ Downloadable .csv reports
+ Add student attendance retroscpectively using student email, data, course identifier/FN code
+ Create weekly (or custom) repeat session code list.


### Student

+ Search and submit fizzy newt code for institution.
+ Notify absence for single class.
+ Notify of extended absense.
+ Submit class feedback (anonymously)
+ Remove themselves from course.
+ Create personal attendance report (filter by module).
+ Downloadable .csv reports.


## Staff

+ Generate FN class code for an institution. Class identifier, start time, expirty, permit feedback, additional message.
+ Additional message pops up when students submit their attendance via FN code
+ Review class feedback.
+ Create weekly (or custom) repeat session code list.