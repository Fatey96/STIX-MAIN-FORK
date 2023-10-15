import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-object-info',
  templateUrl: './object-info.component.html',
  styleUrls: ['./object-info.component.css']
})
export class ObjectInfoComponent {
  @Input() stixProperty: string | undefined
  @Input() propertyName: string | undefined
  @Input() isRequired: boolean = false;
}
