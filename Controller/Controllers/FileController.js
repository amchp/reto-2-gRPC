import FileService from "../microServices/FileGRPC.js";
import SearcherService from "../microServices/SearchGRPC.js";

class FileController {
    constructor() {
        this.fileService = new FileService();
        this.searchService = new SearcherService();
    }

    async create(req, res) {
        const file = {
            name: req.body.name,
            user_id: req.body.user_id,
            file_format: req.body.file_format,
            file: Buffer.from(req.body.file, 'utf8')
        };
        const response = await this.fileService.createFile(file);
        res.send(response);
    }

    async getList(req, res) {
        if (req.query.user_id) {
            const files = await this.searchService.getFileListByUserId({ user: req.query.user_id });
            res.send(files);
            return;
        }
        const files = await this.fileService.getFileList({});
        res.send(files);
    }

    async get(req, res) {
        const file = await this.fileService.getFile({ name: req.params.name })
        res.send(file);
    }

    async update(req, res) {
        const file = {
            name: req.body.name,
            user_id: req.body.user_id,
            file_format: req.body.file_format,
            file: Buffer.from(req.body.file, 'utf8')
        };
        const response = await this.fileService.updateFile(file);
        res.send(response);
    }

    async delete(req, res) {
        const file = await this.fileService.deleteFile({ name: req.params.name });
        res.send(file);
    }
}

export default FileController;