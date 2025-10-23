import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://mooc1.chaoxing.com",
    "Referer": "https://mooc1.chaoxing.com/mooc-ans/mooc2/work/dowork?courseId=255245710&classId=127533995&cpi=290670900&workId=45324144&answerId=54119663&standardEnc=449df629cd75428c34c9bcd473f1dbe9&enc=e634435d9df5a5ea56b5332a8771b909",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.2081 SLBChan/105 SLBVPV/64-bit",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "fid": "176854",
    "_uid": "258640759",
    "_d": "1757424891023",
    "UID": "258640759",
    "vc3": "IgK3hNLw6Zu%2Fc%2BJfY9leA%2Fek%2BGhuFYdV9tZk6ykEyQnTQ9NzgA5nCnUT4ApaTaqBjQS65FS6PuN%2B5eIJSMfOKzRjwHukeYDduXWu%2BIwHV1g8L0Zj2sHbGw667nhEHKAHOQnJcY2yQ5OvihPo6S22gdiVMGbMPYh5NohFX62ri3s%3Deaa77df86e22d6d9ee7fef6f2cb3eedd",
    "uf": "b2d2c93beefa90dc0421275b96a0102c4bd7f3d3eb16c096504f0757d4367bc0b5bfe39a28794b8ddb0e802b7e2f607ed5070f909e9f95aeea4a1670a3a8352fe9295d8c89b08ad0f44425e20f927c6b585575080c0461d5e5851b744f8aa02c9fb3947ed09a594c99e9c6a9f83dc32b587c6ae9f81f0d5576a4cdc6838eec8da5e4643deaa84096e2e63507b485f63970b5a05e402d2a6370184964ffe8c27cc9a0c65a3e71bd183172846cdc191586b1f899d50c1c3fa3aa2ebad65cd196bb",
    "cx_p_token": "0c6f085bd927908b3e4d0eebe3f0567e",
    "p_auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIyNTg2NDA3NTkiLCJsb2dpblRpbWUiOjE3NTc0MjQ4OTEwMjUsImV4cCI6MTc1ODAyOTY5MX0.qEsZbWH--a2AfwhKdYQPALpkJyd8ReyTTgZzHyxHPXw",
    "xxtenc": "86f1edc4a03a5e62dc47c889304904c0",
    "DSSTASH_LOG": "C_38-UN_0-US_258640759-T_1757424891025",
    "spaceFid": "176854",
    "spaceRoleId": "\"\"",
    "tl": "1",
    "k8s": "1757424897.283.15839.824821",
    "jrose": "464784BBEC737AF4C5EFC38439B6A6A8.mooc-1328041167-p5mz7",
    "route": "2fe558bdb0a1aea656e6ca70ad0cad20"
}
url = "https://mooc1.chaoxing.com/mooc-ans/work/addStudentWorkNewWeb"
params = {
    "_classId": "127533995",
    "courseid": "255245710",
    "token": "d907281a94a22efbdeededee90a3334d",
    "totalQuestionNum": "6151a9b7a2ba374e43de4a8ee13b605e",
    "pyFlag": "1",
    "ua": "pc",
    "formType": "post",
    "saveStatus": "1",
    "version": "1"
}
data = {
    "courseId": "255245710",
    "classId": "127533995",
    "knowledgeid": "0",
    "cpi": "290670900",
    "workRelationId": "45324144",
    "workAnswerId": "54119663",
    "jobid": "",
    "standardEnc": "449df629cd75428c34c9bcd473f1dbe9",
    "enc_work": "d907281a94a22efbdeededee90a3334d",
    "totalQuestionNum": "6151a9b7a2ba374e43de4a8ee13b605e",
    "pyFlag": "1",
    "answerwqbid": "214551337,214551338,",
    "mooc2": "1",
    "randomOptions": "false",
    "workTimesEnc": "",
    "answertype214551337": "4",
    "answer214551337": "<p>这是第一题<br/></p>",
    "answertype214551338": "4",
    "answer214551338": "<p>这是第二题<br/></p>"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)