"use strict"

const UserDB = require('../Model/User');

class UserData {
    checkAccount(req){
        return new Promise((resolve , reject) =>{
            UserDB.find({
                private_key: req.body.private_key
            }).exec()
            .then( result => {
                if(result.length < 1){
                    reject(401);
                }
                else{
                    resolve(result[0]["username"]);
                }
            })
            .catch(err => {
                reject(500);
            })
        })
    }
}

module.exports = UserData;