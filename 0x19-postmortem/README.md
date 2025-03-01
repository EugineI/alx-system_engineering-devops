Postmortem: Apache Server 500 Error Due to PHP Misconfiguration

Issue Summary
Duration: August 15, 2024, 14:30 - 15:45 EAT (1 hour 15 minutes)
Impact:
70% of users experienced a 500 Internal Server Error when accessing our website.
The homepage and API endpoints relying on PHP scripts were completely inaccessible.
Users reported issues via support tickets and social media.
Root Cause: A misconfigured PHP module update caused Apache to fail in serving PHP files.
Timeline
14:30 EAT - Issue detected via customer complaints and monitoring alerts showing increased 500 errors.
14:35 EAT - Engineering team starts investigation, checking Apache logs and running curl tests.
14:45 EAT - Initial assumption: A recent code deployment introduced a bug. Rollback initiated but issue persists.
15:00 EAT - strace used to debug Apache requests; ENOENT (file not found) error identified in logs.
15:10 EAT - Misleading assumption that file permissions were incorrect, leading to a failed fix attempt.
15:20 EAT - Issue escalated to DevOps team for deeper debugging.
15:30 EAT - php -m command reveals missing libphp.so module.
15:35 EAT - Engineers reinstall libapache2-mod-php and restart Apache.
15:45 EAT - Services restored; monitoring confirms normal operation.
Root Cause and Resolution
Root Cause:
A system update triggered an unintended removal of the libapache2-mod-php module, causing Apache to be unable to process PHP files. This led to a 500 Internal Server Error on all PHP-driven endpoints.
Resolution:
Identified the missing PHP module using php -m and confirmed its absence.
Reinstalled the module using:
bash
CopyEdit
apt-get install --reinstall libapache2-mod-php -y
Restarted Apache to apply changes:
Bash
Verified service recovery using curl and logs.
Corrective and Preventative Measures
Improvements Needed:
Enhance monitoring to detect missing dependencies earlier.
Improve post-update verification steps before rolling system updates to production.
Document and automate PHP module verification in CI/CD pipelines.

