import UserService from "../microServices/userGRPC.js";

class UserController {
    constructor() {
        this.userService = new UserService();
    }

    async create(req, res) {
        const user = {
            name: req.body.name,
            age: req.body.age,
            password: req.body.password,
            email: req.body.email
        }
        const response = await this.userService.createUser(user);
        res.send(response);
    }

    async getList(req, res) {
        const users = await this.userService.getUserList({});
        res.send(users);
    }

    async get(req, res) {
        const user = await this.userService.getUser({ id: req.params.id })
        res.send(user);
    }

    async update(req, res) {
        const user = {
            id: req.params.id,
            name: req.body.name,
            age: req.body.age,
            password: req.body.password,
            email: req.body.email
        }
        const responce = await this.userService.updateUser(user);
        res.send(responce);
    }

    async delete(req, res) {
        const user = await this.userService.deleteUser({ id: req.params.id })
        res.send(user);
    }
}

export default UserController;