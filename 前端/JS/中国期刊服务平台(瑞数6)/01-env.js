window = self = top = global
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
    createElement: function(res) { 
    console.log("对象","document","方法","createElement","参数",res);
    if(res == "div")
        return div
    },
    getElementsByTagName :function(res) { 
    console.log("对象","document","方法","getElementsByTagName","参数",res);
    if(res == "script")
        return script
    if(res == "base")
        return []
    if(res == "meta")
        return meta
    },
    getElementById :function(res) { 
    console.log("对象","document","方法","getElementById","参数",res);
    // if(res == "FbkwzLN5XOx0")
    //     return meta
    },
    attachEvent : function(res) { 
    console.log("对象","document","方法","attachEvent","参数",res);
    },
    addEventListener : function(res) { 
    console.log("对象","document","方法","addEventListener","参数",res);
}
}
script = {
    "0":{
        type:"text/javascript",
    r:"m",
    parentNode:{
        removeChild : function(res) { 
            console.log("对象","script","方法","removeChild","参数",res);
        }
    }
    },
    "1":{
        type:"text/javascript",
    r:"m",
    parentNode:{
        removeChild : function(res) { 
            console.log("对象","script","方法","removeChild","参数",res);
        }
    }
    }
}
content = "UOCokTbGhfwTraJSNByZgglkRnCqwX6eLiB_PqDNmygOaEulVfi91F.4OowjnIY0sr_MYet_hlCC574is5Yz8DWUlm99WMtvbYEq0WXOM2euFJzcrST_RqiNMZtTmMPYJ19GV_7wHjSftybVn6M68UtxnZmlL9r41H6Y.f.pv6b8ytGs1RyOS6Yf2bqsr5lLPED0gn7Bvng"
meta = [
    {
        http_equiv:"Content-Type",
        content:"text/html; charset=utf-8",
    },
    {
        id:"FbkwzLN5XOx0",
        getAttribute : function(res) { 
            console.log("对象","meta","方法","getAttribute","参数",res);
            if(res=="r"){
                return 'm';
            }
        },
        content:content,
        parentNode:{
        removeChild : function(res) { 
            console.log("对象","style","方法","removeChild","参数",res);
        }
    }
    }
]
div = {
    getElementsByTagName:function(res) { 
        console.log("对象","document","方法","getElementsByTagName","参数",res);
        if(res == "i") {
            return []
        }
    }
}
location = {
    "ancestorOrigins": {},
    "href": "https://qikan.cqvip.com/Qikan/Journal/JournalGuid?from=index",
    "origin": "https://qikan.cqvip.com",
    "protocol": "https:",
    "host": "qikan.cqvip.com",
    "hostname": "qikan.cqvip.com",
    "port": "",
    "pathname": "/Qikan/Journal/JournalGuid",
    "search": "?from=index",
    "hash": ""
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
proxyObjs = ['window', 'document', 'location', 'navigator', 'history', 'screen']
getEnvs(proxyObjs);