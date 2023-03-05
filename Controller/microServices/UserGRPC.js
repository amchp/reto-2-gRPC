import { createRequire } from "module";
const require = createRequire(import.meta.url);
const config = require("../config.json");
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

const PROTOS_PATH = config.PROTOSDIRECTORY;
const USER_PROTOS_PATH = `${PROTOS_PATH}user.proto`
import { promisify } from "util";

class UserService {
    constructor() {
        const packageDefinition = protoLoader.loadSync(
            USER_PROTOS_PATH,
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
        const userservice = protoDescriptor.UserService;

        this.stub = new userservice(`${config.IP_USER_SERVICE}:${config.PORT_USER_SERVICE}`, grpc.credentials.createInsecure());
    }

    async createUser(user) {
        let createUser = promisify(this.stub.createUser.bind(this.stub));
        return await createUser(user);
    }

    async getUserList() {
        let getUserList = promisify(this.stub.getUserList.bind(this.stub));
        return await getUserList({});
    }

    async getUser(ID) {
        let getUser = promisify(this.stub.getUser.bind(this.stub));
        return await getUser(ID);
    }

    async updateUser(user) {
        let updateUser = promisify(this.stub.updateUser.bind(this.stub));
        return await updateUser(user)
    }

    async deleteUser(ID) {
        let deleteUser = promisify(this.stub.deleteUser.bind(this.stub));
        return await deleteUser(ID);
    }

}
export default UserService;