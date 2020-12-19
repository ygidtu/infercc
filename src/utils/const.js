import {createURL} from "./utils";

const urls = {
    static: createURL("/static"),
    docs: createURL("/docs"),
    task: createURL("/task"),
    file: createURL("/file"),
    support: createURL("/support"),
    create: createURL("/create"),
    data: createURL("/data")
};

export default urls;

