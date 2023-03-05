import config from './config.json' assert { type: "json" };
import userRouter from './routers/UserRouter.js';
import fileRouter from './routers/FileRouter.js'; 
import express from 'express';

const app = express();
const hostname = config.CONTROLLER_IP;
const port = config.CONTROLLER_PORT;


app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.use(express.json());
app.use("/user", userRouter);
app.use("/file", fileRouter);


app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});