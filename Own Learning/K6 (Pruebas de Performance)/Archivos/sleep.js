import http from 'k6/http'
import {check , sleep} from 'k6'

export default function(){
    let url = "https://httpbin.test.k6.io/post";
    let response = http.post(url,"Hola Mundo");

    check(response,{
        'La Respuesta dice Hola Mundo':(r)=>r.body.includes("Hola Mundo")
    });
    sleep(10);
}