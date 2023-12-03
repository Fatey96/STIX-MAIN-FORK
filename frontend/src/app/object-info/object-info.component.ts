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
  @Input() radioOptions: string[] = []
  isCheckboxAreaExpanded = false
  selectedCheckboxOptions: string[] = []  

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
}
