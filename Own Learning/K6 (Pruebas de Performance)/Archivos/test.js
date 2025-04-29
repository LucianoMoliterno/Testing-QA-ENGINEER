import http from 'k6/http'
import {check} from 'k6'

export default function(){
    let url = "https://httpbin.test.k6.io/post";
    let response = http.post(url,"hola mundo");
    check(response,{
        'Respuesta de la Solicitud':(r)=>r.body.includes("hola mundo"),
        'Estatus de la Respuesta':(r)=>r.status === 200,
        'Tiempo de Solicitud < 500ms':(r)=>r.timings.duration < 500
    })
}