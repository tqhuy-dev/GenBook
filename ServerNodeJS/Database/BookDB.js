"use strict"

const BookDB = require('../Model/Book');

class BookData {
    getAllBooks(){
        return new Promise((resolve , reject) =>{
            var disableField = {
                // _id:false
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

    getAllBooksWithName(name){
        return new Promise((resolve , reject) =>{

            BookDB.find({name:name} , function(err, result) {
                console.log(name);
                if(err) {
                    reject(err);
                } else {
                    if(result.length > 0){
                        resolve(result);
                    } else {
                        reject('no data')
                    }
                }
            });
        });
    }
}

module.exports = BookData;