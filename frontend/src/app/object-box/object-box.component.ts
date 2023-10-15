import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-object-box',
  templateUrl: './object-box.component.html',
  styleUrls: ['./object-box.component.css']
})
export class ObjectBoxComponent {
  @Input() stixType: string | undefined
  @Input() boxName: string | undefined
  @Input() formFields: any[] = []
  @Input() isSelected: boolean = false

  formCount: number[] = [0]

  addForm() {
    this.formCount.push(1)
  }
}
