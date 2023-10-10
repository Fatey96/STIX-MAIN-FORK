import { Component, Input} from '@angular/core';

@Component({
  selector: 'app-object-btn',
  templateUrl: './object-btn.component.html',
  styleUrls: ['./object-btn.component.css']
})
export class ObjectBtnComponent {
  @Input() btnName: string | undefined
  @Input() btnClass: string | undefined

  isClicked: boolean = false;

  objectSelect(event: Event) {
    this.isClicked = !this.isClicked;
    alert(this.btnName)     // This will be removed later. It is here for testing purposes.
  }
}
