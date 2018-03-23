import { Component, OnInit } from '@angular/core';
import { AlumnoService } from './alumno.service';
import { Observable } from 'rxjs/Rx';

@Component({
  selector: 'app-alumno', //element selector
  templateUrl: './alumno.component.html',
  styleUrls: ['./alumno.component.css']
})
export class AlumnoComponent implements OnInit {
  tituloRespuesta: string;
  alumno: string;
  identificacion: string;
  notas: INotas[];

  constructor(private _alumnoService: AlumnoService) {
  }

  ngOnInit() {
  }

  onUpdateAlumnoInfo(event: Event) {
    this.identificacion = (<HTMLInputElement>event.target).value; 
    this.getAlumno(this.identificacion);
  }

  getAlumno(identificacion) {
    this._alumnoService.getAlumno(identificacion).subscribe(
      data => { data = data[0];

        if (data.status == 'ok') {
          this.notas =  data.notas;
          this.alumno = data.alumno.nombres + ' ' + data.alumno.apellidos;
          console.log(this.notas);
          
        } else {
          
        }
        this.tituloRespuesta = data.response + ' - ID: ' + this.identificacion;
      },
      err => console.error(err),
      () => {
        console.log('Alumno cargado');
      }
    );
  }
}

interface INotas{
  profesor: string;
  materia: string;
  nota; string;
}
