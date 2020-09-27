const port = process.env.PORT || 3000;
const { exec } = require("child_process");
const express = require("express");
var bodyParser = require('body-parser')

const app = express();
app.use(bodyParser.json())

app.get('/api/getLP/:imgID', (req, res) => {
    var image = req.params.imgID;

    exec(`wget https://i.imgur.com/${image}.jpg`);

    exec(`alpr ${image}.jpg`, (err, stdout, stderr) => {
try{
        var output = stdout.split('\n')[1].match('[A-Z0-9]{3,6}')[0];
} catch (e) {
	exec(`rm ${image}.jpg`);
	res.json({"license_plate":"NO PLATE DETECTED"});
};
        
if(output){
	exec(`rm ${image}.jpg`);
        res.json({"license_plate":`${output}`});
};
    });

    //res.json(200);
});

app.listen(port,() => console.log("App started..."));
