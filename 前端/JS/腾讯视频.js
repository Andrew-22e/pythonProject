// 腾讯视频密文逆向解析JS代码-加密（获取结果为：m3u8流媒体文件的地址）
const CryptoJS = require('crypto-js');
function decrypt(I1li1iIi, I1iiIIlI, iliIlI1) {
    let lIlIlIl1 = CryptoJS['AES']['decrypt'](I1li1iIi, CryptoJS['enc']['Utf8']['parse'](I1iiIIlI), {
        'iv': CryptoJS['enc']['Utf8']['parse'](iliIlI1),
        'mode': CryptoJS['mode']['CBC'],
        'padding': CryptoJS['pad']['Pkcs7']
    });
    return lIlIlIl1['toString'](CryptoJS['enc']['Utf8']);
}
//3个参数分别对应：密文、密钥、偏移量
mw = 'y4NSPqjXL+3vVY3/gxHm31EUeCrm49X0LZIzdMu3zl57FLyOVADHLF97iKNXZN9g1H4CVQkG8MlWGuUWOvx+7rKlEbNYtClbD2LjC9bXzKOn6JUQNd79FE36z3+fs9miGse6P0KkJsRKDrWlqVJy9J1a5u24MZNCKvqKkb9YQcrxMLqG2f3u6PDwBKWIl4GGWvI1v0MTg9t7N6lmKMaHkaD0Vc3lReVrN7QReO5xICXb30PFK7ZMcE8vpk57PpBO8qFVLqifzmNPdnn0OBq+CDgtTyKm34o5OeyN6RMcxgd9eDkJSGm5vlFIv+IAJHqivCdLbP9UEJSvA0sWO6xw178aPNNt7t6k5sejMbqXEbvg29RXiv0GygJDpqwWs9W6gwMsLrhJj1k/eTkgGoJfBMVsgYWsziWIWjVriuIwfSgTwO2CdU6LoksCPl+ORLfu'
key = '6ciN8WROaJOPfXLo'
iv = 'OrpprzTXLsjUrEGK'
console.log(decrypt(mw, key, iv))

// 腾讯视频密文逆向解析JS代码-MD5解密（获取结果为：key）
var sign = function(NowTime, url) {
    string = NowTime + url
    a = CryptoJS.MD5(string).toString()
    var b = CryptoJS.MD5(a);
    var c = CryptoJS.enc.Utf8.parse(b);
    var d = CryptoJS.enc.Utf8.parse('https://t.me/xmflv666');
    var e = CryptoJS.AES.encrypt(a, c, {
        iv: d,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return e.toString()
}
console.log(sign('1752590156', 'https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2F324olz7ilvo2j5f%2Fj00365ulv6q.html'))