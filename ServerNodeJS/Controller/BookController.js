const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const BookData  = require('../Database/BookDB');

router.get('/' , (req , res , next) =>{
    var bookData = new BookData();
    var promise = bookData.getAllBooks();

    promise.then((data) =>{
        res.status(200).json(data);
    },(error) =>{
        res.status(401).json({
            status_code:error
        })
    });
});

module.exports = router;