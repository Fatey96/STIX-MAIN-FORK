import { Component, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-object-btn',
  templateUrl: './object-btn.component.html',
  styleUrls: ['./object-btn.component.css']
})
export class ObjectBtnComponent {
  @Input() btnName: string | undefined
  @Input() btnClass: string | undefined
  @Output() btnClicked = new EventEmitter<{ objectClass: string | undefined, clicked: boolean }>();

  isClicked: boolean = false;

  objectSelect() {
    this.isClicked = !this.isClicked;
    this.btnClicked.emit({ objectClass: this.btnClass, clicked: this.isClicked });
  }
}
