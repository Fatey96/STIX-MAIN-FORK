import { Component, Input, Output, EventEmitter, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-object-form',
  templateUrl: './object-form.component.html',
  styleUrls: ['./object-form.component.css']
})
export class ObjectFormComponent {
  @Input() formTitle: string = ''    // Title of the form for reference during relationship selecting
  @Output() formDataChanged = new EventEmitter<any>()  // Output event to notify parent components whenever form data changes
  @ViewChild('objectForm') form!: ElementRef<HTMLFormElement>    // Reference to the actual HTML form element within the template

  // Method to check if the form is valid using native browser validation
  isValid() {
    return this.form.nativeElement.checkValidity()
  }

  // Getter method that extracts form data from the HTML form and returns it
  get formData() {
    const formElement = this.form.nativeElement  // Access the raw HTML form element
    const data: { key: string, value: any }[] = [];  // Array to hold the extracted form data

    // Loop through all form controls (like input, select, textarea) in the form
    Array.from(formElement.elements).forEach((element: any) => {
        if (element.name) {
            // Push each form control's name and value to the data array
            data.push({ key: element.name, value: element.value })
        }
    })
    return data  // Return the extracted form data
  }
}
