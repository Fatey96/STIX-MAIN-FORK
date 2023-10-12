import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-object-box',
  templateUrl: './object-box.component.html',
  styleUrls: ['./object-box.component.css']
})
export class ObjectBoxComponent {
  @Input() boxClass: string | undefined
}
