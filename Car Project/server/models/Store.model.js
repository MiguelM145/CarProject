const mongoose = require("mongoose");

//change name of schema
const StoreSchema = new mongoose.Schema({
    storeName: {
        type: String,
        required: [true, "Name must contain 3 characters!"],

    },
    storeNumber: {
        type: Number,
        required: [true,  "Must be a unique number greater than 0"],
    },
    isOpen: {
        type: Boolean,
    }
}, {timestamps: true})

module.exports = mongoose.model("StoreFinder", StoreSchema);