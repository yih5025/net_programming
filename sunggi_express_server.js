const express = require('express');
const app = express();
const port = 8010;
const bodyParser = require('body-parser');
let data_s = {
}
let a, b, c, d;
// JSON 파싱을 위한 미들웨어 등록
app.use(bodyParser.json());

// GET 요청 핸들러
app.get('/', function(req, res) {
  // GET 요청 처리 작업
  res.send("get 요청에 대한 응답입니다.");
});

// POST 요청 핸들러
app.post('/', function (req, res) {
  
  if (req.body["h_sound"] != null) {

    console.log('h_sound : ' + req.body["h_sound"]);
    console.log('h_alert : ' + req.body["h_alert"]);

    s_sound = req.body["h_sound"];
    s_alert = req.body["h_alert"];

    a = req.body["h_sound"];
    b = req.body["h_alert"];

    // 응답 전송
    res.send(req.body);
  } else {
    console.log("호실 데이터 수신을 실패했습니다.");
  }

  data_s = {
    "s_sound": a,
    "s_alert": b
  }

  if (req.body["s_sound"] != null) {

    console.log('h_sound : ' + req.body["s_sound"]);
    console.log('h_sound : ' + req.body["s_alert"]);

    console.log(data_s);
    // 응답 전송
    res.send(data_s);
  } else {
    console.log("사감 데이터 수신을 실패했습니다.");
  }
  
});

// 서버 시작
app.listen(port, () => {
  console.log(`웹 서버가 http://ip:${port} 에서 실행 중입니다.`);
});