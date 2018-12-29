const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const BookData  = require('../Database/BookDB');
var bookData = new BookData();

router.get('/' , (req , res , next) =>{

    var promise = bookData.getAllBooks();
    promise.then((data) =>{
        res.status(200).json(data);
    },(error) =>{
        res.status(401).json({
            status_code:error
        })
    });
});

router.get('/:nameBook' , (req , res , next) =>{

    var promise = bookData.getAllBooksWithName(req.params.nameBook);
    promise.then((data)=>{
        res.status(200).json(data);
    } , (error) =>{
        res.status(401).json({
            status:error
        });
    });
});

module.exports = router;