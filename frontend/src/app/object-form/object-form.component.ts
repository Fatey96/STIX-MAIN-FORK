import { Component, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-object-form',
  templateUrl: './object-form.component.html',
  styleUrls: ['./object-form.component.css']
})
export class ObjectFormComponent {
  @ViewChild('objectForm') form!: ElementRef<HTMLFormElement>;

  isValid() { // Uses native form validity checking mechanism
    return this.form.nativeElement.checkValidity();
  }
}
