const express = require('express');
const cors = require('cors');
const app = express(); 

app.use(
    cors(),
    express.json(),
    express.urlencoded({extended: true})
)

//require mongoose config
require("./config/mongoose");

//require routes
require("./routes/store.routes")(app); 

app.listen(8000, () => console.log("Server listening on port 8000"))