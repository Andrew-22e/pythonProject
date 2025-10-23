// delete _filename;
// delete _dirname;

window = top = self = global;
window.setInterval = function(res,res1){
    console.log("对象","window","方法","setInterval","参数",res,res1);
}
window.clearInterval = function(res){
    console.log("对象","window","方法","clearInterval","参数",res);
}
window.setTimeout = function(res){
    console.log("对象","window","方法","setTimeout","参数",res);
}
window.addEventListener = function(res,res1,res2){
    console.log("对象","window","方法","addEventListener","参数",res,res1,res2);
}
window.attachEvent = function(res,res1){
    console.log("对象","window","方法","attachEvent","参数",res,res1);
}
document = {
    visibilityState : "visible",
    body:null,
    all:[],
    createElement: function(res){
        console.log("对象","document","方法","createElement","参数",res);
        if(res == "div")
            return div
        if(res == "form")
            return "form"
        if(res == "input"){
            return "input"
        }
    },
    appendChild: function(res){
        console.log("对象","document","方法","appendChild","参数",res);
    },
    removeChild: function(res){
        console.log("对象","document","方法","removeChild","参数",res);
    },
    getElementsByTagName : function(res){
        console.log("对象","document","方法","getElementsByTagName","参数",res);
        if(res == "script")
            return [script,script]
        if(res == "meta")
            return [meta,meta]
        if(res == "base")
            return []
    },
    getElementById : function(res) { 
        console.log("对象","document","方法","getElementById","参数",res);
    },
    getAttribute : function(res) { 
        console.log("对象","div","方法","getAttribute","参数",res);
    }
};
div = {
    getElementsByTagName : function(res) { 
        console.log("对象","div","方法","getElementsByTagName","参数",res);
        if(res == 'i')
            return []
    }
}
head = {removeChild : function(res) { 
                console.log("对象","script","方法","removeChild","参数",res);
            }}
script = {
        getAttribute : function(res) { 
            console.log("对象","script","方法","getAttribute","参数",res);
            return "m"
        },
        parentElement : head
        // type:"text/javascript",
        // r:"m",
        // type:"text/javascript",
        // r:"m",
        // charset:"utf-8",
        // src:"/vdGfdDb5PQO5/JlwbhPfc3stb.6771a74.js"
}
content = "FeQqtMKiWIo7IXlxK7oYw_0ax_aMigwDYQTskANgY._vcJLs0H5WruNJQnrf.rQ6cDWN0hnhJ0TlUCsP3lSizPUJahRd2sZ27Sx1N3sB5l00BS5THhGFnX5.VrFszUshkYH7uXt4n3yPDLGe8VqSQMGBLptk3DAscAoh_axmWMXozfEztz0eoz.cv0cA4v1dbN1_yQ166vT0PV957V5f5rQYXef1qo8RqnlhINEvfMeypU9iTzWZ5J_fUm7LKpHT"
meta = 
    {
        http_equiv:"Content-Type",
        content:"text/html; charset=utf-8",
        content:content,
        r : "m",
         getAttribute : function(res) { 
            console.log("对象","script","方法","getAttribute","参数",res);
            return "m"
        },
        removeChild : function(res) { 
            console.log("对象","script","方法","removeChild","参数",res);
        },
        parentNode : head,
        
    //     id:"FbkwzLN5XOx0",
    //     getAttribute : function(res) { 
    //         console.log("对象","meta","方法","getAttribute","参数",res);
    //         if(res=="r"){
    //             return 'm';
    //         }
    //     },
        
    //     parentNode:{
    //     removeChild : function(res) { 
    //         console.log("对象","style","方法","removeChild","参数",res);
    //     }
    // }
    }

location = {
    "ancestorOrigins": {},
    "href": "https://www.ouyeel.com/steel/search?keySearch=SAPH440&pageIndex=0&pageSize=50",
    "origin": "https://www.ouyeel.com",
    "protocol": "https:",
    "host": "www.ouyeel.com",
    "hostname": "www.ouyeel.com",
    "port": "",
    "pathname": "/steel/search",
    "search": "?keySearch=SAPH440&pageIndex=0&pageSize=50",
    "hash": ""
}
navigator = {
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54",
    "appCodeName": "Mozilla",
    "appName": "Netscape",
    "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
}

function getEnvs(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
      get: function(target, property, receiver) {
        console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
        return target[property];
      },
      set: function(target, property, value, receiver) {
        console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
        return Reflect.set(...arguments);
      }
    }`;
        eval(`try {
            ${proxyObjs[i]};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        } catch (e) {
            ${proxyObjs[i]} = {};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        }`);
    }
}
proxyObjs = ['window', 'document', 'location', 'navigator', 'history', 'screen','script','meta','base']
getEnvs(proxyObjs);