import { AlumnoComponent } from './alumno/alumno.component';
import { AlumnoService } from './alumno/alumno.service';

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';


import { AppComponent } from './app.component';


@NgModule({
  declarations: [
    AppComponent,
    AlumnoComponent  
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    HttpClientModule
  ],
  providers:  [AlumnoService],
  bootstrap: [AppComponent]
})
export class AppModule { }
