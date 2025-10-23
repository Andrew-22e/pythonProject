window = global;

delete global;
delete Buffer;

// window.chrome = {
//     "app": {
//         "isInstalled": false,
//         "InstallState": {
//             "DISABLED": "disabled",
//             "INSTALLED": "installed",
//             "NOT_INSTALLED": "not_installed"
//         },
//         "RunningState": {
//             "CANNOT_RUN": "cannot_run",
//             "READY_TO_RUN": "ready_to_run",
//             "RUNNING": "running"
//         }
//     }
// }
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    webdriver:false,
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0'
};
// 添加更多的浏览器环境模拟
document = {
    addEventListener : function(res,res1,res2){
        console.log("对象","window","方法","addEventListener","参数",res,res1,res2);
    },
    cookie:'api_uid=CiI96GjT6MGtRwCSV2cSAg==; jrpl=SxVWtyRoTh14OxzLVF9Z6fzDWOekbQhu; njrpl=SxVWtyRoTh14OxzLVF9Z6fzDWOekbQhu; dilx=AXtfyEciBYZ7peWiAOQT7; _nano_fp=Xpmyl0mal0gjX0PbXC_nc2C9LCRBFU0niYAdzK7K',
    referrer:'https://www.pinduoduo.com/home/3c/',
    getElementById : function(res){
        console.log("对象","window","方法","addEventListener","参数",res);
    }
};

screen = {
    availHeight: 816,
    availWidth: 1536,
};

history = {};
history.back = function() {};

location = {
    ancestorOrigins: {},
    href: "https://www.pinduoduo.com/home/baby/",
    origin: "https://www.pinduoduo.com",
    protocol: "https:",
    host: "www.pinduoduo.com",
    hostname: "www.pinduoduo.com",
    port: "",
    pathname: "/home/baby/",
    search: "",
    hash: ""
};

// function getEnvs(proxyObjs) {
//     for (let i = 0; i < proxyObjs.length; i++) {
//         const handler = `{
//       get: function(target, property, receiver) {
//         console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
//         return target[property];
//       },
//       set: function(target, property, value, receiver) {
//         console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
//         return Reflect.set(...arguments);
//       }
//     }`;
//         eval(`try {
//             ${proxyObjs[i]};
//             ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
//         } catch (e) {
//             ${proxyObjs[i]} = {};
//             ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
//         }`);
//     }
// };
// proxyObjs = ['window', 'document', 'location', 'navigator', 'history', 'screen']
// getEnvs(proxyObjs);