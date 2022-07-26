@ECHO ON
call C:\ProgramData\Anaconda3\Scripts\activate.bat meddra_events_api
CD /D D:\python\PSM_API\PSM_P_E
 D:\python\PSM_API\PSM_P_E\manage.py runserver 10.0.0.132:7001
PAUSE
