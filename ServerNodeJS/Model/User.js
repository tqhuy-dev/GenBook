const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    username : String,
    password: String,
    private_key:String,
    books:[]
});

module.exports = mongoose.model('UserDB' , userSchema , 'UserDB');