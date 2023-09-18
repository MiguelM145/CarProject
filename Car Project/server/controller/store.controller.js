const StoreFinder = require("../models/Store.model");

module.exports = {
    findAll: (req, res) =>{
        StoreFinder.find()
            .then(allStores => res.json(allStores))
            .catch(err => res.json(err))
    },

    findOne: (req, res) => {
        StoreFinder.findById(req.params.id)
            .then(oneStore => res.json(oneStore))
            .catch(err => res.json(err))
    },

    create: (req, res) => {
        StoreFinder.create(req.body)
            .then(newStore => res.json(newStore))
            .catch(err => res.status(400).json(err))
    },

    update: (req, res) => {
        StoreFinder.findByIdAndUpdate(req.params.id, req.body, {new:true})
            .then(updatedStore => res.json(updatedStore))
            .catch(err => res.json(err))
    },

    delete: (req, res) => {
        StoreFinder.findByIdAndDelete(req.params.id)
            .then(deletedStore => res.json(deletedStore))
            .catch(err => res.status(400).json(err))
    }
}

