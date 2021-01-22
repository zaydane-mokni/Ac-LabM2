const path = require('path')
const express = require('express')

const app = express()
const port = process.env.PORT || 3000
const hostname = '127.0.0.1';

const basePath = path.join(__dirname, '../faceDetection')
app.use(express.static(basePath))

//start express server
app.listen(port, () => {
    console.log(`To start the server http://${hostname}:${port}`);
})
