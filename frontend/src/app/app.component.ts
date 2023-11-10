import { Component, ViewChildren, QueryList } from '@angular/core';
import { ObjectBtnComponent } from './object-btn/object-btn.component';
import { ObjectBoxComponent } from './object-box/object-box.component';
import { RelationshipService } from './relationship.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Define the structure of the object buttons that represent STIX Domain Objects
interface ObjectButtonInfo {  // function onObjectButtonClicked
  objectClass?: string
  objectName?: string
  clicked: boolean
}

// Define the structure of the details of a STIX object for relationship selection
interface StixObjectDetail {  // In createdStixObjects array, function getDetailsForBoxName, function transformObjectToStix
  boxName: string
  title: string
  stixType: string
  id: string
  formData: { key: string, value: string }[]
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private relationshipService: RelationshipService, private http: HttpClient) { }
  @ViewChildren(ObjectBtnComponent) buttons!: QueryList<ObjectBtnComponent>   // in function onLastFormRemoved
  @ViewChildren(ObjectBoxComponent) objectBoxes!: QueryList<ObjectBoxComponent>   // in functions onObjectButtonClicked, areAllFormsComplete, onSelectRelationshipsClick
  selectedObjects: { stixType: string; name: string; id: string; }[] = []   // in functions onObjectButtonClicked, isObjectSelected, onLastFormRemoved, canContinue
  createdStixObjects: StixObjectDetail[] = []  // in functions onSelectRelationshipsClick, onEditObjectsClick, getDetailsForBoxName, updateAvailableRelationships, createRelationship, createSighting, getUnlinkedObjects, onContinueClick
  displayCreatedObjects: { [key: string]: boolean } = {}   // in function toggleObjectDetailsVisibility
  totalForms: number = 0   // in functions onObjectButtonClicked, updateTotalFormsCount
  datasetAmount: number | null = null   // in functions onDatasetInput, onSelectRelationshipsClick, onContinueClick
  isSelectingRelationships: boolean = false   // in functions onSelectRelationshipsClick, onEditObjectsClick
  relationshipType: 'relationship' | 'sighting' | null = null   // in functions selectRelationship, selectSighting
  sightingReference: string | null = null   // in function createSighting
  sourceReference: string | null = null   // in functions onSourceReferenceChange, updateAvailableRelationships, createRelationship
  targetReference: string | null = null   // in functions onSourceReferenceChange, updateAvailableRelationships, createRelationship
  availableRelationships: string[] = []   // in functions updateAvailableRelationships, createRelationship
  chosenRelationship: string | null = null    // in function createRelationship
  relationshipsCreated: Array<{ type: 'relationship' | 'sighting', sourceDetail: any, relationship?: string, targetDetail: any }> = []    // in functions onEditObjectsClick, isDuplicateRelationship, createRelationship, createSighting, canContinue, getUnlinkedObjects, onContinueClick
  jsonOutput: string = ''   // in functions onEditObjectsClick, onContinueClick

  // Event handler for when a STIX object button is clicked from STIX Domain Objects (description-page, object-buttons-container)
  onObjectButtonClicked(ObjectButtonInfo: ObjectButtonInfo) {
    const { objectClass, objectName, clicked } = ObjectButtonInfo
    if (!objectClass || !objectName) return
    const index = this.selectedObjects.findIndex(obj => obj.stixType === objectClass)

    if (clicked) {
      this.selectedObjects.push({ stixType: objectClass, name: objectName, id: `${objectClass}--${this.generateUUID()}` })
      this.totalForms++
    } else {
      this.selectedObjects.splice(index, 1)
      this.objectBoxes.toArray().forEach(box => {
        if (box.stixType === objectClass) {
          this.totalForms -= box.formDetails.length
          box.formDetails = []
        }
      })
    }
  }

  // Check if a particular STIX object is selected from STIX Domain Objects (description-page, object-buttons-container)
  //* Necessary to display the object boxes when an object button is clicked
  isObjectSelected(stixType: string): boolean {
    return this.selectedObjects.some(obj => obj.stixType === stixType)
  }

  // Event handler for when the last form of a particular STIX type is removed
  // The corresponding object button is unclicked and the object is removed from the selectedObjects list
  onLastFormRemoved(stixType: string) {
    const index = this.selectedObjects.findIndex(obj => obj.stixType === stixType)
    this.selectedObjects.splice(index, 1)
    this.buttons.toArray().forEach(button => {
      if (button.btnClass === stixType) {
        button.isClicked = false
      }
    })
  }

  // Updates the total forms count when a form is added or deleted
  updateTotalFormsCount(byAmount: number) {
    this.totalForms += byAmount
  }

  onDatasetInput(event: any) {
    const inputValue = parseFloat(event.target.value)
    const clamp = (num: number, min: number, max: number) => Math.min(Math.max(num, min), max);
    const minval: number = 1
    const maxval: number = 100000

    this.datasetAmount = clamp(inputValue, minval, maxval)

    // Update the input value to match the datasetAmount
    event.target.value = this.datasetAmount
  }

  // Check if all forms across all selected objects are complete before moving on to the relationships section
  areAllFormsComplete(): boolean {
    return this.objectBoxes.toArray().every(box => box.areAllFormsValid())
  }

  // This prevents the user from being able to select the same object for both source and target for relationships
  onSourceReferenceChange() {
    // Check if the selected values are the same
    if (this.sourceReference === this.targetReference) {
      // If they are the same, clear the "Target Reference"
      this.targetReference = null
      this.updateAvailableRelationships()
    }
  }

  // When the user tries to move on to the relationship selection phase, it ensures that all forms are complete and stores the data
  onSelectRelationshipsClick() {
    if (!this.areAllFormsComplete()) {
      alert("Please complete all required fields before selecting relationships.")
      return
    }
    if (this.datasetAmount === null || isNaN(this.datasetAmount)) {
      alert("Please enter a valid dataset amount before proceeding.")
      return
    }

    this.isSelectingRelationships = true

    this.objectBoxes.toArray().forEach(box => {
      var count: number = 0
      box.forms.toArray().forEach(form => {
        const formData = form.getFormData()
        this.createdStixObjects.push({
          boxName: box.boxName,
          title: form.formTitle,
          stixType: box.stixType,
          id: box.formDetails[count].formID,
          formData: formData,
        })
        count += 1
      })
    })

    // Remove relationships with non-existent source_ref or target_ref
    this.relationshipsCreated = this.relationshipsCreated.filter(rel => {
      const sourceExists = this.createdStixObjects.find(obj => obj.id === rel.sourceDetail.id)
      const targetExists = this.createdStixObjects.find(obj => obj.id === rel.targetDetail.id)

      if (rel.type === "relationship") {
        if (sourceExists && targetExists) {   // Update sourceDetail and targetDetail with new data, keep relationship
          rel.sourceDetail = sourceExists
          rel.targetDetail = targetExists
          return true
        }
      } else if (rel.type === "sighting") {
        if (sourceExists) {   // Update sourceDetail with new data, keep sighting
          rel.sourceDetail = sourceExists
          return true
        }
      } else {
        return true   // Keep non-relationship/sighting objects
      }
      return false    // Remove relationships where id does not exist
    })
  }

  // When the user clicks the Edit Objects button to go back to the first page
  onEditObjectsClick() {
    this.isSelectingRelationships = false
    this.createdStixObjects = []
    this.jsonOutput = ""
  }

  // Toggles the visibility of selected object details during the relationship phase
  toggleObjectDetailsVisibility(objectName: string) {
    this.displayCreatedObjects[objectName] = !this.displayCreatedObjects[objectName]
  }

  // Retrieves details for a given box name
  getDetailsForBoxName(boxName: string): StixObjectDetail[] {
    return this.createdStixObjects.filter(detail => detail.boxName === boxName)
  }

  // Handle the event when selecting a relationship
  selectRelationship() {
    this.relationshipType = 'relationship'
    this.updateAvailableRelationships()
  }

  // Handle the event when selecting a sighting
  selectSighting() {
    this.relationshipType = 'sighting'
  }

  // Updates the available relationships based on selected source and target
  updateAvailableRelationships() {
    // Fetch the details for the selected source and target
    const sourceDetails = this.createdStixObjects.find((detail: { id: string; }) => detail.id === this.sourceReference)
    const targetDetails = this.createdStixObjects.find((detail: { id: string; }) => detail.id === this.targetReference)
    let sourceStixType: string | null = null
    let targetStixType: string | null = null

    if (sourceDetails && 'stixType' in sourceDetails) {
      sourceStixType = sourceDetails.stixType
    }

    if (targetDetails && 'stixType' in targetDetails) {
      targetStixType = targetDetails.stixType
    }

    if (sourceStixType && targetStixType) {
      this.availableRelationships = this.relationshipService.getPossibleRelationships(sourceStixType, targetStixType)
    } else {
      this.availableRelationships = []
    }
  }

  // Check for duplicate relationships
  isDuplicateRelationship(newRelationship: any): boolean {
    if (newRelationship.type === 'relationship') {
      return this.relationshipsCreated.some(existingRelationship =>
        existingRelationship.type === 'relationship' &&
        existingRelationship.sourceDetail.id === newRelationship.sourceDetail.id &&
        existingRelationship.relationship === newRelationship.relationship &&
        existingRelationship.targetDetail.id === newRelationship.targetDetail.id
      )
    } else if (newRelationship.type === 'sighting') {
      return this.relationshipsCreated.some(existingRelationship =>
        existingRelationship.type === 'sighting' &&
        existingRelationship.sourceDetail.id === newRelationship.sourceDetail.id
      )
    }
    return false
  }

  // Create a relationship
  createRelationship() {
    const sourceDetail = this.createdStixObjects.find(detail => detail.id === this.sourceReference)
    const targetDetail = this.createdStixObjects.find(detail => detail.id === this.targetReference)

    if (!sourceDetail || !this.chosenRelationship || !targetDetail) {
      alert("Please fill out all fields before creating a relationship.")
      return
    }

    const newRelationship = {
      type: 'relationship' as const,
      sourceDetail: sourceDetail,
      relationship: this.chosenRelationship,
      targetDetail: targetDetail
    }

    if (!this.isDuplicateRelationship(newRelationship)) {
      this.relationshipsCreated.push(newRelationship)

      // Clear the select fields
      this.sourceReference = null
      this.targetReference = null
      this.chosenRelationship = null
      this.availableRelationships = []
    } else {
      alert("This relationship already exists.")
    }
  }

  // Create a sighting
  createSighting() {
    const sightingDetail = this.createdStixObjects.find(detail => detail.id === this.sightingReference)

    if (!sightingDetail) {
      alert("Please fill out the sighting reference before creating a sighting.")
      return
    }

    const newSighting = {
      type: 'sighting' as const,
      sourceDetail: sightingDetail,
      targetDetail: {}
    }

    if (!this.isDuplicateRelationship(newSighting)) {
      this.relationshipsCreated.push(newSighting)

      // Clear the select field
      this.sightingReference = null
    } else {
      alert("This sighting already exists.")
    }
  }

  deleteRelationship(relationship: any) {
    const index = this.relationshipsCreated.findIndex(rel => rel === relationship)
    if (index !== -1) {
      this.relationshipsCreated.splice(index, 1)
      this.jsonOutput = ""
    }
  }

  // Check if user can continue to the next phase by ensuring that every selected STIX object has been linked in a relationship or sighting
  canContinue(): boolean {
    for (let object of this.selectedObjects) {
      for (let detail of this.getDetailsForBoxName(object.name)) {
        const isInRelationship = this.relationshipsCreated.some(relationship =>
          (relationship.sourceDetail.id === detail.id || relationship.targetDetail.id === detail.id)
        )

        if (!isInRelationship) {
          return false
        }
      }
    }
    return true
  }

  // Identify STIX objects that are not included in any relationship or sighting
  // Useful for informing the user of any unaddressed objects before they proceed - this part has not been implemented
  getUnlinkedObjects(): string[] {
    const linkedObjects = new Set<string>()

    // Populate with titles of objects that are present in the created relationships
    for (const rel of this.relationshipsCreated) {
      linkedObjects.add(rel.sourceDetail.title)
      if (rel.type === 'relationship') {
        linkedObjects.add(rel.targetDetail.title)
      }
    }

    // Returns a list of titles that aren't linked to a relationship or sighting
    return this.createdStixObjects
      .map(detail => detail.title)
      .filter(title => !linkedObjects.has(title))
  }

  // Transform STIX object details to STIX format
  transformObjectToStix(detail: StixObjectDetail): any {
    const nameField = detail.formData.find(fd => fd.key === "Name");
    const finalName = nameField?.value || detail.title;
    return {
      type: detail.stixType,
      id: detail.id,
      name: finalName,
      ...Object.fromEntries(detail.formData.map(fd => [fd.key, fd.value]))
    }
  }

  // Transforms relationship data to STIX format
  transformRelationshipToStix(relationship: any): any {
    if (relationship.type === 'relationship') {
      return {
        id: 'relationship--' + this.generateUUID(),
        type: 'relationship',
        source_ref: relationship.sourceDetail.id,
        relationship_type: relationship.relationship,
        target_ref: relationship.targetDetail.id
      }
    } else if (relationship.type === 'sighting') {
      return {
        id: 'sighting--' + this.generateUUID(),
        type: 'sighting',
        sighting_of_ref: relationship.sourceDetail.id,
      }
    }
    return {}
  }

  // Generates a random UUID (Universally Unique Identifier) - better way to do this later but this works for now
  generateUUID(): string {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16 | 0,
        v = c == 'x' ? r : (r & 0x3 | 0x8)
      return v.toString(16)
    })
  }

  private sendPostRequest(data: any): Observable<any> {
    return this.http.post<any>('http://localhost:8000/api/addStixData/', data, { observe: 'body', responseType: 'json' })
  }

  // Handles the continue button click event - ensures all STIX objects are in a relationship or sighting
  // If everything is in a relationship/sighting, compiles all STIX data into a single bundle and stringifies it into JSON format
  onContinueClick(): void {
    const unlinkedObjects = this.getUnlinkedObjects()

    // If there are unlinked objects, alert the user to address them first
    if (unlinkedObjects.length) {
      alert('Please ensure all selected STIX objects are in a relationship or sighting: ' + unlinkedObjects.join(', '))
      return
    }

    // Convert each STIX object detail and created relationship to the STIX format
    const stixObjects = this.createdStixObjects.map(detail => this.transformObjectToStix(detail))
    const stixRelationshipsAndSightings = this.relationshipsCreated.map(rel => this.transformRelationshipToStix(rel))

    //! Generate dataset #, objects, and relationships
    // Generate the objects array
    const objectsOutput = stixObjects.map(obj => ({
      type: obj.type,
      name: obj.name
    }))

    // Generate the relationships array using index references
    const relationshipsOutput = stixRelationshipsAndSightings.map(rel => {
      // If it's a sighting, it will only have a source
      if (rel.type === 'sighting') {
        return {
          source: stixObjects.findIndex(obj => obj.id === rel.sighting_of_ref),
          relationship: rel.type // This will set relationship as 'sighting'
        }
      }
      return {
        source: stixObjects.findIndex(obj => obj.id === rel.source_ref),
        target: stixObjects.findIndex(obj => obj.id === rel.target_ref),
        relationship: rel.relationship_type
      }
    })

    // Construct the final output structure
    const finalOutput = {
      dataset: this.datasetAmount,
      objects: objectsOutput,
      relationships: relationshipsOutput
    }

    this.jsonOutput = JSON.stringify(finalOutput, null, 2)

    this.sendPostRequest(this.jsonOutput).subscribe(
      response => {
        console.log(response.message)
      },
      error => {
        console.error("There was an error sending the request:", error)
      }
    )

    //! The below code would display the STIX objects and relationships without creating a bundle
    // // Convert each STIX object and relationship/sighting to its string representation
    // const stixStrings = [...stixObjects, ...stixRelationshipsAndSightings].map(obj => JSON.stringify(obj, null, 2))

    // // Join them together, separating by commas and newlines
    // this.jsonOutput = stixStrings.join(',\n')

    //! The below code would create a STIX bundle
    // // Create a STIX bundle containing all the formatted data.
    // const stixData = [...stixObjects, ...stixRelationshipsAndSightings]
    // const bundle = {
    //   type: "bundle",
    //   id: "bundle--" + this.generateUUID(),
    //   spec_version: "2.1",
    //   objects: stixData
    // }
    // // Stringify the bundle for JSON output
    // this.jsonOutput = JSON.stringify(bundle, null, 2)
  }
}