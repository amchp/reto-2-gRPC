import config from '../config.json' assert { type: "json" };
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

const PROTOS_PATH = config.PROTOSDIRECTORY;
const FILE_PROTOS_PATH = `${PROTOS_PATH}file.proto`
import { promisify } from "util";

class FileService {
    constructor() {
        const packageDefinition = protoLoader.loadSync(
            FILE_PROTOS_PATH,
            {
                keepCase: true,
                longs: String,
                enums: String,
                defaults: true,
                oneofs: true
            }
        );
        const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
        // The protoDescriptor object has the full package hierarchy
        const fileservice = protoDescriptor.FileService;

        this.stub = new fileservice('localhost:50052', grpc.credentials.createInsecure());
    }

    async createFile(file) {
        let createFile = promisify(this.stub.createFile.bind(this.stub));
        return await createFile(file);
    }

    async getFileList() {
        let getFileList = promisify(this.stub.getFileList.bind(this.stub));
        
        return await getFileList({});
    }

    async getFile(name) {
        let getFile = promisify(this.stub.getFile.bind(this.stub));
        return await getFile(name);
    }

    async updateFile(file) {
        let updateFile = promisify(this.stub.updateFile.bind(this.stub));
        return await updateFile(file)
    }

    async deleteFile(name) {
        let deleteFile = promisify(this.stub.deleteFile.bind(this.stub));
        return await deleteFile(name);
    }

}
export default FileService;