const express = require('express')
const app = express()
app.use(express.static('.'))
app.listen(5000, () => {
    console.log('启动服务 http://localhost:5000')
})
