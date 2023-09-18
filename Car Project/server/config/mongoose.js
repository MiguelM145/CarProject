const mongoose = require("mongoose");

mongoose.connect("mongodb://127.0.0.1/exam_db", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
    .then ( () => console.log("Connected to MongoDb"))
    .catch(err => console.log("There was an error connecting to MongoDB: ", err))