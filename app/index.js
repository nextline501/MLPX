const express = require('express');
const app = express();
const db = require('./db');
const cors = require("cors");
const bodyParser = require("body-parser");

app.use(bodyParser.json());
app.use(cors());

app.get('/', (req, res) => {
  res.send("ok")
})

app.get('/api/aaplData', (req, res) => {
  res.send()
});

app.post('/api/pyy', (req, res) => {
  console.log(req.body)
})

app.get('/api/py', (req, res) => {

  let openPrice = 123;
  let highPrice = 125;
  let lowPrice = 122;
  let vol = 100000000;

  const { spawn } = require('child_process');
  const pyProg = spawn('python', ['./machineScript.py', openPrice, highPrice, lowPrice, vol]);

  pyProg.stdout.on('data', function(data) {
    console.log(data.toString());
    res.write(data);
    res.end()
  });
})


app.listen(5501, () => console.log('Application listening on port 5501!'))

module.exports = app
