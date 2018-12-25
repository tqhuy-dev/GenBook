const express = require('express');
const app = express();
const fs = require('fs');
// const userController = require('./controller/UserController');

app.get('/api/v1/data/genbook' , (req , res , next) =>{
    res.status(200).json({
        message:'api is working',
        status:'success'
    })
});
// app.use('/v1/api/user' , userController);
module.exports = app;