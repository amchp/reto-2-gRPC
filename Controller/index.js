import userRouter from './routers/UserRouter.js';
import express from 'express';

const app = express();
const hostname = '127.0.0.1';
const port = 3000;


app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.use(express.json());
app.use("/user", userRouter);


app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});