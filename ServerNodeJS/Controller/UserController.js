const express = require('express');
const router = express.Router();
const UserDB = require('../Model/User')
const UserData = require('../Database/UserDB');
const mongoose = require('mongoose');

router.get('/' , (req , res , next) =>{
    UserDB.find({}).exec()
    .then( docs =>{
        res.status(200).json(docs)
    })
});

router.post('/login' , (req , res , next) =>{
    var userData = new UserData();
    var promise = userData.checkAccount(req);
    promise.then((data) => {
        res.status(200).json({
            data: data
        });
    } , (err) =>{
        res.status(401).json({
            status_code:err
        })
    });
});

router.post('/' , (req, res , next) =>{
    const newUser = new UserDB({
        _id : mongoose.Types.ObjectId(),
        username : req.body.username,
        password : req.body.password,
        private_key : req.body.private_key,
        books : req.body.books
    });
    newUser.save().then( result =>{
        res.status(200).json({
            message: 'create account sucessfully'
        })
    })
})

module.exports = router;