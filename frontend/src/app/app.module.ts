import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ObjectBtnComponent } from './object-btn/object-btn.component';
import { ObjectBoxComponent } from './object-box/object-box.component';

@NgModule({
  declarations: [
    AppComponent,
    ObjectBtnComponent,
    ObjectBoxComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
