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
  @Input() listValues: string[] = []

  // Method to check if the form is valid using native browser validation
  isValid() {
    return this.form.nativeElement.checkValidity()
  }

  // Getter method that extracts form data from the HTML form and returns it
  getFormData(): { key: string, value: any }[] {
    const formElement = this.form.nativeElement  // Access the raw HTML form element
    const data: { key: string, value: any }[] = []  // Array to hold the extracted form data

    // Loop through all form controls (like input, select, textarea) in the form
    Array.from(formElement.elements).forEach((element: any) => {
      if (element.type === 'checkbox') {
        if (element.checked) {
          const existingData = data.find(item => item.key === element.id)   // Used to see if an option has been checked and added or not
          if (existingData) {
            existingData.value.push(element.value)
          } else {
            data.push({ key: element.id, value: [element.value] })
          }
        }
      } else if (element.type === 'text' && element.getAttribute('data-input-type') === 'stringlist') {
        const existingData = data.find(item => item.key === element.id);
        if (existingData) {
          existingData.value.push(...this.listValues)
        } else {
          data.push({ key: element.id, value: [...this.listValues] })
        }
      } else {
        if (element.value.trim() !== '') {
          data.push({ key: element.id, value: element.value })
        }
      }
    })

    return data  // Return the extracted form data
  }
}
