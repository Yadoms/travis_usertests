import pysftp

with pysftp.Connection('ftp.jano42.fr', username='janofnxr-usertests', password='Usertests2019') as sftp:
    with sftp.put('/report.html')
