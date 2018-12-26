const express = require('express');
const router = express.Router();
const UserDB = require('../Model/User')
const mongoose = require('mongoose');

router.post('/login' , (req , res , next) =>{
    UserDB.find({
        private_key:req.body.private_key
    })
    .exec()
    .then( result =>{
        if(result.length < 1){
            return res.status(400).json({
                error: 'auth fail'
            });
        }
        else {
            return res.status(200).json({
                message:'auth successfully'
            })
        }
    })
    .catch( err =>{
        res.status(500).json({
            error:err
        })
    })
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