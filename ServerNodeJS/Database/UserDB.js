"use strict"

const UserDB = require('../Model/User');

class UserData {
    checkAccount(req){
        return new Promise((resolve , reject) =>{
            var disableField = { 
                _id: false,
                password:false,
                private_key:false
            };
        
            UserDB.find({
                private_key: req.body.private_key
            } , disableField ).exec()
            .then( result => {
                if(result.length < 1){
                    reject(401);
                }
                else{
                    resolve(result[0]);
                }
            })
            .catch(err => {
                reject(err);
            })
        })
    }

    getAllUsers(){
        var disableField = {
            _id:false,
            password:false,
            private_key:false,
            books:false
        };

        return new Promise((resolve , reject) =>{
            UserDB.find({} , disableField)
            .exec()
            .then( result =>{
                if(result.length < 1){
                    reject(401);
                } else {
                    resolve(result);
                }
            })
            .catch(err =>{
                reject(err);
            })
        });
    }
}

module.exports = UserData;