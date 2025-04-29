import http from 'k6/http';
import {sleep} from 'k6';

export let options = {
    vus: 10,
    duration: '5m',
    iterations: 40,
};
export default function(){
    http.get ('https://jsonplaceholder.typicode.com/post');
    sleep(10);
}