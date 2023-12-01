# Frontend Branch Breakdown

This is to provide a general description of how the frontend branch is set up. For more information, visit the respective file/function and comments there will explain. 

## Independent Files

### [app.component.css](src/app/app.component.css)
- These are styles to be used in app.component.html, and is where majority of the styling is done. Changes here can also apply to the styling of the components: object-box, object-btn, object-form, and object-info. 

### [app.component.html](src/app/app.component.html)
- This is the primary HTML file for the Angular application. This is a single-page application (SPA), so the content is divided into two divs: description-page and relationship-page.
    - The description-page div allows for the user to select the SDOs that they would like to include into their STIX bundle and input the information about each object. 
    - The relationship-page div allows for the user to view information about their created objects, set relationships between the objects, and generate the STIX bundle to either copy or download. 

### [app.component.ts](src/app/app.component.ts)
- This is the primary TypeScript file to be used in app.component.html. There are many functions here, and each function is explained with comments above and/or throughout it. Some of these functions include storing the created STIX objects, removing created STIX objects, creating relationships, removing relationships, and sending the data to the backend.

### [app.module.ts](src/app/app.module.ts)
- This file handles the imports and declarations to be used within the Angular application. This includes components, but also the FormsModule, HttpClientModule, MatIconModule, and more.

### [relationship.service.ts](src/app/relationship.service.ts)
- This file handles all of the relationship mapping between SDOs. The format is displayed below, with the common relationships defined at the top of the file. Additionally, this file includes a function to find all possible relationships between a source and a target to display.

    ```typescript
        "source": {
            ...this.commonRelationships,
            "relationship-type": ["target"],
        }
    ```

### [styles.css](src/styles.css)
- These are global styles. Custom colors are set up here to be used all throughout the project via `var(--color-name)`. To change a color globally, just input a different hex code for the variable.

### [index.html](src/index.html)
- Not much is here, as this is what allows everything else to display. However, the link for Material Icons is imported here.

## Components

Currently, there are four created components that are used throughout this application. Each one is explained below.

### [object-box](src/app/object-box)

The object-box component is used within the application as `<app-object-box></app-object-box>`. They are what displays the forms of the objects that the user can fill out.

There are four files to this component:
- [object-box.component.css](src/app/object-box/object-box.component.css)
    - This is the styling for the object boxes. It includes the div border, the headers, the Add Another Object button, and more.
- [object-box.component.html](src/app/object-box/object-box.component.html)
    - This is how the object boxes are set up. It starts with a header (the name of the object) as well as the type. Then it pulls in the form from object-form, followed by the input fields from object-info for the object, then a button to add another one of those objects. 
- object-box.component.spec.ts
    - This file has not been modified since its generation.
- [object-box.component.ts](src/app/object-box/object-box.component.ts)
    - This file handles generating a unique ID for the form so that each one can be identified separately. 
    - There are also functions that handle the addition/deletion of forms. 
    - It also checks to make sure that the forms within the box are valid via object-form.component.ts before proceeding in app.component.ts. 
    - Lastly, it handles updating a string array for the type "List of Type String."

Currently, it is used inside app.component.html as follows, with the object name, fields, and other relevant information in the ng-container above it:

```html
    <app-object-box [boxName]="box.name" [stixType]="box.type" *ngIf="isObjectSelected(box.type)"
        (lastFormDeleted)="onLastFormRemoved($event)" (formAdded)="updateTotalFormsCount(1)"
        (formDeleted)="updateTotalFormsCount(-1)" [formFields]="box.fields">
    </app-object-box>
```

### [object-btn](src/app/object-btn)

The object-btn component is used within the application as `<app-object-btn></app-object-btn>`. These are the buttons at the very top of the page that allow the user to select which objects they want.

There are four files to this component:
- [object-btn.component.css](src/app/object-btn/object-btn.component.css)
    - This is the styling for the object buttons. It includes button's normal state, as well as their hover and clicked state.
- [object-btn.component.html](src/app/object-btn/object-btn.component.html)
    - This one is very simple. It includes the button with its relevant classes.
- object-btn.component.spec.ts
    - This file has not been modified since its generation.
- [object-btn.component.ts](src/app/object-btn/object-btn.component.ts)
    - This file handles the clicking of the object. It sends the relevant information to app.component.ts for further work.

Currently, it is used inside app.component.html as follows:

```html
    <app-object-btn
        *ngFor="let object of [{name: '', class: ''},]" [btnName]="object.name" [btnClass]="object.class" (btnClicked)="onObjectButtonClicked($event)">
    </app-object-btn>
```

### [object-form](src/app/object-form)

The object-form component is used within the application as `<app-object-form></app-object-form>`. This handles gathering the form data for each form in each object.

There are four files to this component:
- [object-form.component.css](src/app/object-form/object-form.component.css)
    - This handles the appearance of the form. Only one selector is contained here.
- [object-form.component.html](src/app/object-form/object-form.component.html)
    - This is also pretty simple. It sets up the form for object-box and allows for the input fields to be available there.
- object-form.component.spec.ts
    - This file has not been modified since its generation.
- [object-form.component.ts](src/app/object-form/object-form.component.ts)
    - This handles two functions. It checks to ensure that each form is valid when called on by object-box.component.ts.
    - It also extracts the form data, with specific methods for specific input types, when the user clicks to proceed and will return that data to be stored in app.component.ts.

Currently, it is used inside object-box.component.html as follows:

```html
    <app-object-form [class]="stixType" [formTitle]="stixType + '-' + (i + 1)" [listValues]="listValues">
        <ng-container *ngFor="let field of formFields">
            <app-object-info></app-object-info>
        </ng-container>
    </app-object-form>
```

### [object-info](src/app/object-info)

The object-info component is used within the application as `<app-object-info></app-object-info>`. 

There are four files to this component:
- [object-info.component.css](src/app/object-info/object-info.component.css)
    - This handles how each input type appears with its label. 
- [object-info.component.html](src/app/object-info/object-info.component.html)
    - This has a variety of input types that can be applied to an object form, such as text, timestamp, integer, checkboxes, and more. They are labeled with a comment to differentiate them.
    - Each input has a few requirements to work, such as the class, type, id, name, whether it is required, etc. They all have a similar structure.
- object-info.component.spec.ts
    - This file has not been modified since its generation.
- [object-info.component.ts](src/app/object-info/object-info.component.ts)
    - There are functions that handle updating list values for the type String List. 
    - There is a function that opens the dropdown for the checkboxes option and the string list option.
    - There is a function that handles the updating of the checkbox options
    - Lastly, there are functions specific to the specialty fields that were created (latitude, longitude, product) to better apply the STIX 2.1 standards.

Currently, it is used inside object-box.component.html as follows:

```html
    <app-object-info 
        [inputType]="field.inputType" 
        [stixProperty]="field.stixProperty" 
        [propertyName]="field.propertyName" 
        [isRequired]="field.isRequired"
        [selectOptions]="field.selectOptions"
        [checkboxOptions]="field.checkboxOptions"
        (listValuesChanged)="updateListValues($event)"
    >
    </app-object-info>
```