export function fullURL(...urls) {
    return window.location.href.split("#")[0].replace(/(^\/|\/$)/g, "") + "/../" +
    createURL(...urls)
}

export function isEmpty(obj) {

    if (obj === null || obj === undefined) {
        return true
    }
  
    return JSON.stringify(obj) === JSON.stringify({});
  }


export function createURL(...urls) {
    let res = [];

    // let temp = "http://chenlulab.com:5001";
    let temp = ""
    if (temp !== "") {
        res.push(temp)
    }

    for (let i=0; i < urls.length; i++) {
        let temp = urls[i].toString();
        temp = temp.replace(/(^\/|\/$)/g, "");

        if (temp !== "") {
            res.push(temp)
        }
    }

    // return "/" + res.join("/")
    return res.join("/")
}


