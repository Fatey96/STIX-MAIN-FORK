import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { MatIconModule } from '@angular/material/icon';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ObjectBtnComponent } from './object-btn/object-btn.component';
import { ObjectBoxComponent } from './object-box/object-box.component';
import { ObjectInfoComponent } from './object-info/object-info.component';
import { ObjectFormComponent } from './object-form/object-form.component';
import { RelationshipService } from './relationship.service';

@NgModule({
  declarations: [
    AppComponent,
    ObjectBtnComponent,
    ObjectBoxComponent,
    ObjectInfoComponent,
    ObjectFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    CommonModule,
    HttpClientModule,
    MatIconModule
  ],
  providers: [RelationshipService],
  bootstrap: [AppComponent]
})
export class AppModule { }
