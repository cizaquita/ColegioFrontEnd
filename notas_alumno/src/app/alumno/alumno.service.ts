import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

const httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class AlumnoService{
 
    constructor(public http: HttpClient){
    }
 
    getAlumno(identificacion): Observable<any>{
        return this.http.get('http://ada.resistencia.la:9000/info_estudiante/?ident=' + identificacion);
    } 
 
}