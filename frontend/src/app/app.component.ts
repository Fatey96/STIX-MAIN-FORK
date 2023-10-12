import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  selectedObjects: string[] = []

  objectClicked(buttonInfo: { objectClass: string | undefined, clicked: boolean }) {
    const { objectClass, clicked } = buttonInfo;  // Allows for object destructuring 

    if (!objectClass) return; // If objectClass is null or undefined, we don't process further

    const index = this.selectedObjects.indexOf(objectClass)

    if (clicked && index === -1) {  // If the button was clicked and its class is not already in the array, add it
      this.selectedObjects.push(objectClass)
    } 

    if (!clicked && index !== -1) { // If the button was unclicked and its class is in the array, remove it
      this.selectedObjects.splice(index, 1)
    }
  }
}
