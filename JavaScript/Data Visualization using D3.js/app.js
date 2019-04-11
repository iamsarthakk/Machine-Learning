let express = require('express')
let app = express()

let path = require('path')

app.use(express.static(path.join(__dirname, 'public')))

app.get('/', function (req, res) {
   res.sendFile(__dirname + '/index.html');
})

let server = app.listen(process.env.PORT || 5000, function () {
   let host = server.address().address
   let port = server.address().port

   console.log("Example app listening at http://%s:%s", host, port)
})
