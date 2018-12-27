"use strict"

const BookDB = require('../Model/Book');

class BookData {
    getAllBooks(){
        return new Promise((resolve , reject) =>{
            var disableField = {
                _id:false
            };

            BookDB.find({} , disableField)
            .exec()
            .then( result =>{
                if(result.length < 1){
                    reject(401);
                } else {
                    resolve(result);
                }
            })
            .catch(err =>{
                reject(500);
            })
        })
    }
}

module.exports = BookData;