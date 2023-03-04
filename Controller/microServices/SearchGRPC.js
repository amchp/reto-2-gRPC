import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

const PROTOS_PATH = '/Users/alejandromcewen/Documents/Estudios/Semestre6/TopicosEspecialesEnTelematica/reto2/protos/';
const FILE_PROTOS_PATH = `${PROTOS_PATH}search.proto`
import { promisify } from "util";

class SearcherService {
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
        const fileservice = protoDescriptor.SearcherService;

        this.stub = new fileservice('localhost:50053', grpc.credentials.createInsecure());
    }

    async getFileListByUserId(user_id) {
        let getFileListByUserId = promisify(this.stub.getFileListByUserId.bind(this.stub));
        return await getFileListByUserId(user_id);
    }

    async getUsersByName(name) {
        let getUsersByName = promisify(this.stub.getUsersByName.bind(this.stub));
        return await getUsersByName(name);
    }
}
export default SearcherService;