import { Component, Input, ViewChildren, QueryList } from '@angular/core';
import { ObjectFormComponent } from '../object-form/object-form.component';

@Component({
  selector: 'app-object-box',
  templateUrl: './object-box.component.html',
  styleUrls: ['./object-box.component.css']
})
export class ObjectBoxComponent {
  @Input() stixType: string | undefined
  @Input() boxName: string | undefined
  @Input() formFields: any[] = []
  @Input() isSelected: boolean = false

  @ViewChildren(ObjectFormComponent) forms!: QueryList<ObjectFormComponent> // Query to get all child components of ObjectFormComponent within this component
  formCount: number[] = [0] // Form array initialized with one element to display one form by default

  addForm() { 
    const areAllFormsValid = this.forms.toArray().every(formComponent => formComponent.isValid()) // Checks if all forms are valid. 'every' returns true if all conditions are met
    if (areAllFormsValid) { // If all forms are valid, push new element (form) to formCount array
      this.formCount.push(1)
    } else {  // Not all forms are valid
      alert("Please complete all required fields before adding another form.")
    }
  }
}
