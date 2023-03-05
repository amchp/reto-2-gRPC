import UserController from '../Controllers/UserController.js';
import express from 'express';

let userRouter = express.Router();

const userContrller = new UserController();

userRouter.get("/", (req, res) => {
    userContrller.getList(req, res);
});
userRouter.post("/", (req, res) => {userContrller.create(req, res)});
userRouter.get("/:id", (req, res) => { userContrller.get(req, res)});
userRouter.put("/:id", (req, res) => {userContrller.update(req, res)});
userRouter.delete("/:id", (req, res) => {userContrller.delete(req, res)});

export default userRouter;
