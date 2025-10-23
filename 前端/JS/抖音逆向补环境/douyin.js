require('./env')
require('./source')

function main() {
    xhr_http = new XMLHttpRequest();
    console.log(xhr_http)
    a = window._abxx.apply(xhr_http,{"0":null})
    console.log(a);
    return a
}

url = "https://www.douyin.com/user/MS4wLjABAAAAe6ww-KW3nCqmIFuwcUz53hN0c73cKndHGTc13X7pGko?from_tab_name=main&vid=7545426675749358902"
console.log(main(url))