// window = global;
// delete global;
// delete Buffer;

// // 定义 bdms 对象及其 init 方法
// window.bdms = {
//   init: function() {
//       // 实现初始化逻辑
//       return hr; // hr 需要先定义或替换为实际返回值
//   }
// };
// window.requestAnimationFrame = function() {}
// window.XMLHttpRequest = function() {}

// document =  {
//     all : function() {},
//     createElement : function() {},
//     createEvent : function() {},
// }

// function getEnvs(proxyObjs) {
//     for (let i = 0; i < proxyObjs.length; i++) {
//         const handler = `{
//       get: function(target, property, receiver) {
//         console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", 
//         property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
//         return target[property];
//       },
//       set: function(target, property, value, receiver) {
//         console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", 
//         property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
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
// }
// proxyObjs = ['window', 'document', 'location', 'navigator', 'history', 'screen','_abxx']
// getEnvs(proxyObjs);

window = global;
delete global;
delete Buffer;

// 定义 bdms 对象及其 init 方法
window.bdms = {
  init: function() {
      // 实现初始化逻辑
      return hr; // hr 需要先定义或替换为实际返回值
  }
};
window.requestAnimationFrame = function() {}
window.XMLHttpRequest = function() {}

document =  {
    all : function() {},
    createElement : function() {},
    createEvent : function() {},
}

// 定义_abxx函数，确保它是一个函数并具有apply方法
window._abxx = function() {
    // 这里应该实现_abxx的实际逻辑
    // 由于我们没有具体实现，暂时返回一个默认值
    return {};
};

// 确保_abxx具有apply方法（函数本身就具有apply方法）
// 如果_abxx在source.js中被重新定义，这将确保它是一个函数

function getEnvs(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
      get: function(target, property, receiver) {
        console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", 
        property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
        return target[property];
      },
      set: function(target, property, value, receiver) {
        console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", 
        property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
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
proxyObjs = ['window', 'document', 'location', 'navigator', 'history', 'screen', '_abxx']
getEnvs(proxyObjs);