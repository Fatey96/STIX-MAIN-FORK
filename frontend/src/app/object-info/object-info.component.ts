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
}
