'''

curl -X POST -d "username=amr&password=amryu12345" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFtciIsInVzZXJfaWQiOjEsImVtYWlsIjoiYW1yYW53YXI5NDVAZ21haWwuY29tIiwiZXhwIjoxNTAwODA2MjY4fQ.xX9WJstlRR-7sus6CfcPskCeeM_90apfzjTyaB4QPsI

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFtciIsInVzZXJfaWQiOjEsImVtYWlsIjoiYW1yYW53YXI5NDVAZ21haWwuY29tIiwiZXhwIjoxNTAwODA1ODIwfQ.FgfQ1kB_DOsA2X62VZ06Yoo_2mFxIvris-VbIOChG3Q" http://127.0.0.1:8000/api/news/


curl -X PUT -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFtciIsInVzZXJfaWQiOjEsImVtYWlsIjoiYW1yYW53YXI5NDVAZ21haWwuY29tIiwiZXhwIjoxNTAwODA2MjY4fQ.xX9WJstlRR-7sus6CfcPskCeeM_90apfzjTyaB4QPsI" -H "Content-Type: application/json" -d '{"wait":true}' 'http://127.0.0.1:8000/api/news/edrgve/edit'

curl http://127.0.0.1:8000/api/comments/

'''
