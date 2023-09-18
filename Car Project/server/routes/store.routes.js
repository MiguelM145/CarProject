const storeFinderController = require("../controller/store.controller");

module.exports = app => {
    app.get("/api/stores" , storeFinderController.findAll);
    app.post("/api/stores", storeFinderController.create);
    app.get("/api/stores/:id", storeFinderController.findOne);
    app.put("/api/stores/:id", storeFinderController.update);
    app.delete("/api/stores/:id", storeFinderController.delete);
}