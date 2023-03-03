import FileController from '../Controllers/FileController.js';
import express from 'express';

let fileRouter = express.Router();

const fileController = new FileController();

fileRouter.get("/", (req, res) => {fileController.getList(req, res);});
fileRouter.post("/", (req, res) => {fileController.create(req, res)});
fileRouter.get("/:name", (req, res) => { fileController.get(req, res)});
fileRouter.put("/:name", (req, res) => {fileController.update(req, res)});
fileRouter.delete("/:name", (req, res) => {fileController.delete(req, res)});

export default fileRouter;
