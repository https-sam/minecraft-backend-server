
const express = require('express');
const app = express();
const fs = require('fs');
var exec = require('child_process').exec;
var cors = require('cors');
var schedule = require('node-schedule');

app.use(express.json());
app.use(cors());

app.post('/fetch-status', (req, res) => {
    exec('python3 /home/lol/scripts/getServerStatus.py && cat /home/lol/scripts/status.txt',
    function (error, stdout, stderr) {
        res.send({status :stdout.replace(/\s/g, '')});
        if (error !== null) {
             console.log('exec error: ' + error);
        }
    }); 
});


app.post('/fetch-props', async (req, res) => {
    exec('python3 /home/lol/scripts/getServerProp.py',
    function (error, stdout, stderr) {
        if(error) {
            throw err
        } // if json file suceesflly got updated..

        res.sendFile('/home/lol/server/minecraft-backend-server/curr_props.json');
    });
})

app.post('/fetch-ram-usage', (req, res) => {
    res.sendFile('/home/lol/server/minecraft-backend-server/ramUsage.txt');
});

app.post('/fetch-logs', (req, res) => {
    exec('python3 /home/lol/scripts/getLogs.py',
    function (error, stdout, stderr) {
        if(error) {
            throw err
        } // if json file suceesflly got updated..
        res.sendFile('/home/lol/server/minecraft-backend-server/logs.txt');
    });
    
});

app.post('/server-stop', (req, res) => {
    exec('sudo systemctl stop minecraft', err => {
        if(!err) {
            res.send('SUCCESS');
        }
        else console.log("Some error occured when restarting server");
    })
})

app.post('/server-restart', (req, res) => {
    exec('sudo systemctl restart minecraft', err => {
        if(!err) {
            res.send('SUCCESS');
        }
        else console.log("Some error occured when restarting server");
    })
})

app.post('/server-start', (req, res) => {
    exec('sudo systemctl start minecraft', err => {
        if(!err) {
            res.send('SUCCESS');
        }
        else console.log("Some error occured when starting server");
    })
})



app.listen(3005, '0.0.0.0', () => {
    console.info(`App Ruuning on 3005`);
})