const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    username : String,
    password: String,
    private_key:String,
    public_key:String,
    coin:Number,
    first_name:String,
    last_name:String,
    books:[]
});

module.exports = mongoose.model('UserDB' , userSchema , 'UserDB');