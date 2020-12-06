var express = require('express');
var PythonShell = require('python-shell');
var app = express();
app.listen(3000, function () {
  console.log('Express server running on port 3000');
})
app.get('/hello', call_helloPython);
function call_helloPython(req, res) {
  // using spawn instead of exec, prefer a stream over a buffer
  // to avoid maxBuffer issue
  var spawn = require('child_process').spawn;
  var process = spawn('python', 
  ['hello.py',
    'angs' 
  ]);
  process.stdout.on('data', function (data) {
    res.send(data.toString());
  });
  
 /* var options = {
      args: ['value1', 'value2', 'value3']
  };
  PythonShell().run('./hello.py', options, function (err, data) {
    if (err) res.send(err);
    res.send(data.toString())
  });*/
}
