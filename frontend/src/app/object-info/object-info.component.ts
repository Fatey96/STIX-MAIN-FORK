import { Component, Input } from '@angular/core';

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
  isDropdownExpanded: boolean = false
  selectedCheckboxOptions: string[] = []
  inputValue: string = ''

  // Allows for the opening/closing of the checkboxes dropdown
  openDropdown() {
    this.isDropdownExpanded = !this.isDropdownExpanded
  }

  // Updates the selected options in the checkbox selects
  updateSelectedOptions(option: string) {
    if (this.selectedCheckboxOptions.includes(option)) {
      this.selectedCheckboxOptions = this.selectedCheckboxOptions.filter((item) => item !== option)
    } else {
      this.selectedCheckboxOptions.push(option)
    }
  }

  // Handle input event and update requirement status
  // TODO: Allow for the updating of requirement status for latitude, longitude, and precision
  updateNumber(event: any): void {
    let value = parseFloat(event.target.value)
    var min: number | undefined = 0
    var max: number | undefined = 0

    if (!isNaN(value)) {
      if (this.inputType === 'latitude') {
        min = -90
        max = 90
      }

      if (this.inputType === 'longitude') {
        min = -180
        max = 180
      }

      if (this.inputType === 'integer') {
        min = 1
        max = 999999999
      }

      if (value < min || value > max) {
        event.target.value = Math.min(max, Math.max(min, value)).toString()
      }
    }
  }

  updateText(event: any): void {
    let value = event.target.value

    if (this.inputType === 'product') {
      // Convert to lowercase and replace spaces with dashes
      value = value.toLowerCase().replace(/\s+/g, '-')
      event.target.value = value
    }
  }
}
