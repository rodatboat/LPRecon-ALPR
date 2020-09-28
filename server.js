const port = process.env.PORT || 3000;
const { exec } = require("child_process");
const express = require("express");
var bodyParser = require('body-parser')

const app = express();
app.use(bodyParser.json())

app.get('/api/getLP/:imgID', (req, res) => {
    var image = req.params.imgID;

    exec(`wget https://i.imgur.com/${image}.jpg`);

    exec(`alpr -c us -j ${image}.jpg`, (err, stdout, stderr) => {
        try {
            console.log(stdout);
            var output = JSON.parse(stdout).results[0].plate;
        } catch (e) {
            exec(`rm ${image}.jpg`);
            res.json({ "license_plate": "NO PLATE DETECTED" });
        };

        if (output) {
            console.log(`Got license plate ${output}`)
            exec(`rm ${image}.jpg`);
            res.json({ "license_plate": `${output}` });
        };
    });

    //res.json(200);
});

app.get('/api/getCustomer/:LP', (req, res) => {
    var LP = req.params.LP;
    
    exec(`python3 fetch.py ${LP}`, (err, stdout, stderr) => {
        try {
            var output = stdout.split('\s');

        } catch (e) {
            res.json({ "user": "NOT FOUND." });
        };

        if (output) {

            console.log(`Got customer ${output}`);
            res.json({
                "name": `${output[0]}`
            });
        };
    });

    //res.json(200);
});

app.listen(port, () => console.log("App started..."));
