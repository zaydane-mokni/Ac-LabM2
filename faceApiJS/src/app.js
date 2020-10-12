const path = require('path')
const express = require('express')

const app = express()
const port = process.env.PORT || 3000

const basePath = path.join(__dirname, '../faceDetection')

app.use(express.static(basePath))

//start express server
app.listen(port, () => {
    console.log('Server started')
})
