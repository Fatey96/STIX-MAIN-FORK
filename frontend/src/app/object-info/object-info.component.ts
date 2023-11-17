import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-object-info',
  templateUrl: './object-info.component.html',
  styleUrls: ['./object-info.component.css']
})
export class ObjectInfoComponent {
  @Input() propertyName: string = ''    // Display name of the property in the form
  @Input() stixProperty: string = ''    // Actual property name that conforms to the STIX specification
  @Input() isRequired: boolean = false  // Indicate if this property is a mandatory field in the form
  @Input() inputType: string = ''
  @Input() selectOptions: string[] = []
  @Input() checkboxOptions: string[] = []
  isCheckboxAreaExpanded = false
  selectedCheckboxOptions: string[] = []
  enteredListValue: string = ''   // Variable to store the current entered value
  listValues: string[] = []   // Array to store the list of entered values
  @Output() listValuesChanged = new EventEmitter<string[]>()

  // Handle input event and update list values
  updateListValues(): void {
    if (this.enteredListValue.trim() !== '') {
      this.listValues.push(this.enteredListValue.trim())
      this.enteredListValue = ''   // Clear the entered value
      this.listValuesChanged.emit(this.listValues)   // Emit updated list values
    }
  }

  // Remove an item from the list
  removeListValue(index: number): void {
    this.listValues.splice(index, 1)
    this.listValuesChanged.emit(this.listValues)  // Emit updated list values
  }

  // Allows for the opening/closing of the checkboxes dropdown
  toggleCheckboxArea() {
    this.isCheckboxAreaExpanded = !this.isCheckboxAreaExpanded
  }

  // Updates the _ selected text in the checkbox selects
  updateSelectedOptions(option: string) {
    if (this.selectedCheckboxOptions.includes(option)) {
      this.selectedCheckboxOptions = this.selectedCheckboxOptions.filter((item) => item !== option)
    } else {
      this.selectedCheckboxOptions.push(option)
    }
  }

  // Handle input event and update requirement status
  updateStatus(event: any): void {
    let value = parseFloat(event.target.value)
    let isLatitude = this.inputType === 'latitude'
    let isLongitude = this.inputType === 'longitude'

    if (!isNaN(value)) {
      if (this.inputType === 'latitude' || this.inputType === 'longitude') {
        let min = isLatitude ? -90 : -180
        let max = isLatitude ? 90 : 180

        if (value < min || value > max) {
          event.target.value = Math.min(max, Math.max(min, value)).toString()
        }
      }
    }
  }
}
