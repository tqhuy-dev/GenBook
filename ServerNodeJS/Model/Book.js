const mongoose = require('mongoose');

const bookSchema = mongoose.Schema({
    _id: mongoose.Schema.Types.ObjectId,
    name : String,
    owner: String,
    typebook:String,
    author:String,
    day:String,
});

module.exports = mongoose.model('BookDB' , bookSchema , 'BookDB');