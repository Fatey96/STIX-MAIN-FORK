import { Component, Input, ViewChildren, QueryList, Output, EventEmitter } from '@angular/core';
import { ObjectFormComponent } from '../object-form/object-form.component';

@Component({
  selector: 'app-object-box',
  templateUrl: './object-box.component.html',
  styleUrls: ['./object-box.component.css']
})
export class ObjectBoxComponent {
  @Input() stixType!: string   // Type of the STIX object this box represents
  @Input() boxName!: string    // Display name of the box
  @Input() formFields: any[] = []   // Fields to be displayed in the form within the box
  @Input() isSelected: boolean = false    // Flag to check if the box is currently selected  
  @Output() formAdded = new EventEmitter<void>()  // Event emitted when a new form is added
  @Output() formDeleted = new EventEmitter<void>()  // Event emitted when a form is deleted
  @Output() lastFormDeleted = new EventEmitter<string>()  // Event emitted when the last form inside the box is deleted
  @ViewChildren(ObjectFormComponent) forms!: QueryList<ObjectFormComponent> 

  // Contains details of each form within the box, initialized with one form to ensure there's always at least one form displayed by default
  formDetails: Array<{ id: number, fields: any[], formID: string }> = [
    { 
      id: Date.now(),
      fields: [],
      formID: this.generateUUID()
    }
  ]

  // Generates a random UUID (Universally Unique Identifier) - better way to do this later but this works for now
  generateUUID(): string {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16 | 0,
        v = c == 'x' ? r : (r & 0x3 | 0x8)
      return v.toString(16)
    })
  }

  // Method to add a new form to the box
  addForm() {
    // Check if all existing forms in the box are valid.
    const areAllFormsValid = this.forms.toArray().every(formComponent => formComponent.isValid())

    if (areAllFormsValid) {
      this.formDetails.push({ id: Date.now(), formID: this.generateUUID(), fields: [] })
      this.formAdded.emit()
    } else {
      alert("Please complete all required fields before adding another form.")
    }
  }
  
  // Method to delete a specific form based on its ID
  deleteForm(id: number) {
    const initialLength = this.formDetails.length;
    this.formDetails = this.formDetails.filter(form => form.id !== id)
    if (this.formDetails.length < initialLength) {
      this.formDeleted.emit()
      if (this.formDetails.length === 0) {
        this.lastFormDeleted.emit(this.stixType)
      }
    }
  }
  
  // Method to check if all the forms within the box are valid
  areAllFormsValid(): boolean {
    return this.forms.toArray().every(formComponent => formComponent.isValid())
  }  
}
