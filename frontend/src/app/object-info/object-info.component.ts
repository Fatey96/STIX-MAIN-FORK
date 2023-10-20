import { Component, Input, ElementRef, Renderer2, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-object-info',
  templateUrl: './object-info.component.html',
  styleUrls: ['./object-info.component.css']
})
export class ObjectInfoComponent implements AfterViewInit {
  @Input() propertyName: string = ''    // Display name of the property in the form
  @Input() stixProperty: string = ''    // Actual property name that conforms to the STIX specification
  @Input() isRequired: boolean = false  // Indicate if this property is a mandatory field in the form

  constructor(private el: ElementRef, private renderer: Renderer2) { }

  // Lifecycle hook that gets called after Angular initializes the component's views and child views
  ngAfterViewInit(): void {
    // Listen for changes on the 'input' element within this component
    this.renderer.listen(this.el.nativeElement.querySelector('input'), 'change', (event: any) => {
      // If the input type gets changed (for security reasons), reset the type attribute to 'text'
      if (event.target.type !== 'text') {
        this.renderer.setAttribute(event.target, 'type', 'text')
        alert('Modification of input type is not allowed!')
      }
    })
  }
}
