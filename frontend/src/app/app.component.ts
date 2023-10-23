import { Component, ViewChildren, QueryList } from '@angular/core';
import { ObjectBtnComponent } from './object-btn/object-btn.component';
import { ObjectBoxComponent } from './object-box/object-box.component';
import { RelationshipService } from './relationship.service';

// Define the structure of the object buttons that represent STIX Domain Objects
interface ObjectButtonInfo {
  objectClass?: string
  objectName?: string
  clicked: boolean
}

// Define the structure of the details of a STIX object for relationship selection
interface StixObjectDetail {
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
  @ViewChildren(ObjectBtnComponent) buttons!: QueryList<ObjectBtnComponent>
  @ViewChildren(ObjectBoxComponent) objectBoxes!: QueryList<ObjectBoxComponent>
  selectedStixObjects: { stixType: string; name: string; id: string; }[] = []  // List of currently selected STIX objects
  totalFormsCount: number = 0  // Total number of forms across all object boxes
  isSelectingRelationships: boolean = false  // Flag to check if user is selecting relationships
  selectedStixObjectDetails: StixObjectDetail[] = [] // Details of the selected STIX objects for relationship selection
  selectedStixObjectDetailsVisible: { [key: string]: boolean } = {}  // Visibility state of each STIX object's details during relationship selection
  selectedRelationshipType: 'relationship' | 'sighting' | null = null  // Selected relationship type (relationship or sighting)
  selectedSightingReference: string | null = null  // Selected sighting reference
  selectedSourceReference: string | null = null  // Selected source of a relationship
  selectedTargetReference: string | null = null  // Selected target of a relationship
  availableRelationships: string[] = []  // Available relationships based on selected source and target
  selectedRelationship: string | null = null  // Currently selected relationship
  createdRelationships: Array<{ type: 'relationship' | 'sighting', sourceDetail: any, relationship?: string, targetDetail: any }> = []  // List of created relationships and sightings
  stixOutput: string = ''  // Stringified STIX output
  constructor(private relationshipService: RelationshipService) { }

  // Event handler for when a STIX object button is clicked from STIX Domain Objects (description-page, object-buttons-container)
  onObjectButtonClicked(ObjectButtonInfo: ObjectButtonInfo) {
    const { objectClass, objectName, clicked } = ObjectButtonInfo
    if (!objectClass || !objectName) return
    const index = this.selectedStixObjects.findIndex(obj => obj.stixType === objectClass)

    if (clicked) {
      if (index === -1) {
        this.selectedStixObjects.push({ stixType: objectClass, name: objectName, id: `${objectClass}--${this.generateUUID()}` })
        this.totalFormsCount++
      }
    } else {
      if (index !== -1) {
        this.selectedStixObjects.splice(index, 1)
        this.objectBoxes.toArray().forEach(box => {
          if (box.stixType === objectClass) {
            this.totalFormsCount -= box.formDetails.length
            box.formDetails = []
          }
        })
      }
    }
  }

  // Check if a particular STIX object is selected from STIX Domain Objects (description-page, object-buttons-container)
  isStixObjectSelected(stixType: string): boolean {
    return this.selectedStixObjects.some(obj => obj.stixType === stixType)
  }

  // Event handler for when the last form of a particular STIX type is removed
  // The corresponding object button is unclicked and the object is removed from the selectedStixObjects list
  onLastFormRemoved(stixType: string) {
    const index = this.selectedStixObjects.findIndex(obj => obj.stixType === stixType)
    if (index > -1) {
      this.selectedStixObjects.splice(index, 1)
      this.buttons.toArray().forEach(button => {
        if (button.btnClass === stixType) {
          button.isClicked = false
        }
      })
    }
  }

  // Updates the total forms count when a form is added or deleted
  updateTotalFormsCount(byAmount: number) {
    this.totalFormsCount += byAmount
  }

  // Check if all forms across all selected objects are complete before moving on to the relationships section
  areAllFormsComplete(): boolean {
    return this.objectBoxes.toArray().every(box => box.areAllFormsValid())
  }

  // When the user tries to move on to the relationship selection phase, it ensures that all forms are complete and stores the data
  onSelectRelationships() {
    if (!this.areAllFormsComplete()) {
      alert("Please complete all required fields before selecting relationships.")
    } else {
      this.isSelectingRelationships = true

      this.objectBoxes.toArray().forEach(box => {
        box.forms.toArray().forEach(form => {
          const formData = form.formData
          this.selectedStixObjectDetails.push({
            boxName: box.boxName,
            title: form.formTitle,
            stixType: box.stixType,
            id: this.generateUUID(),
            formData: formData
          })
        })
      })
    }
  }

  // Toggles the visibility of selected object details during the relationship phase
  toggleStixObjectDetailsVisibility(objectName: string) {
    this.selectedStixObjectDetailsVisible[objectName] = !this.selectedStixObjectDetailsVisible[objectName]
  }

  // Retrieves details for a given box name
  getDetailsForBoxName(boxName: string): StixObjectDetail[] {
    return this.selectedStixObjectDetails.filter(detail => detail.boxName === boxName)
  }

  // Handle the event when selecting a relationship
  selectRelationship() {
    this.selectedRelationshipType = 'relationship'
    this.updateAvailableRelationships()
  }

  // Handle the event when selecting a sighting
  selectSighting() {
    this.selectedRelationshipType = 'sighting'
  }

  // Updates the available relationships based on selected source and target
  updateAvailableRelationships() {
    // Fetch the details for the selected source and target
    const sourceDetails = this.selectedStixObjectDetails.find((detail: { title: string; }) => detail.title === this.selectedSourceReference)
    const targetDetails = this.selectedStixObjectDetails.find((detail: { title: string; }) => detail.title === this.selectedTargetReference)
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
  private isDuplicateRelationship(newRelationship: any): boolean {
    if (newRelationship.type === 'relationship') {
      return this.createdRelationships.some(existingRelationship =>
        existingRelationship.type === 'relationship' &&
        existingRelationship.sourceDetail.title === newRelationship.sourceDetail.title &&
        existingRelationship.relationship === newRelationship.relationship &&
        existingRelationship.targetDetail.title === newRelationship.targetDetail.title
      )
    } else if (newRelationship.type === 'sighting') {
      return this.createdRelationships.some(existingRelationship =>
        existingRelationship.type === 'sighting' &&
        existingRelationship.sourceDetail.title === newRelationship.sourceDetail.title
      )
    }
    return false
  }

  // Create a relationship
  createRelationship() {
    const sourceDetail = this.selectedStixObjectDetails.find(detail => detail.title === this.selectedSourceReference)
    const targetDetail = this.selectedStixObjectDetails.find(detail => detail.title === this.selectedTargetReference)

    if (!sourceDetail || !this.selectedRelationship || !targetDetail) {
      alert("Please fill out all fields before creating a relationship.")
      return
    }

    const newRelationship = {
      type: 'relationship' as const,
      sourceDetail: sourceDetail,
      relationship: this.selectedRelationship,
      targetDetail: targetDetail
    }

    if (!this.isDuplicateRelationship(newRelationship)) {
      this.createdRelationships.push(newRelationship)

      // Clear the select fields
      this.selectedSourceReference = null
      this.selectedTargetReference = null
      this.selectedRelationship = null
      this.availableRelationships = []
    } else {
      alert("This relationship already exists.")
    }
  }

  // Create a sighting
  createSighting() {
    const sightingDetail = this.selectedStixObjectDetails.find(detail => detail.title === this.selectedSightingReference)

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
      this.createdRelationships.push(newSighting)

      // Clear the select field
      this.selectedSightingReference = null
    } else {
      alert("This sighting already exists.")
    }
  }

  // Check if user can continue to the next phase by ensuring that every selected STIX object has been linked in a relationship or sighting
  canContinue(): boolean {
    for (let object of this.selectedStixObjects) {
      for (let detail of this.getDetailsForBoxName(object.name)) {
        const isInRelationship = this.createdRelationships.some(relationship =>
          (relationship.sourceDetail.title === detail.title || relationship.targetDetail.title === detail.title)
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
    for (const rel of this.createdRelationships) {
      linkedObjects.add(rel.sourceDetail.title)
      if (rel.type === 'relationship') {
        linkedObjects.add(rel.targetDetail.title)
      }
    }

    // Returns a list of titles that aren't linked to a relationship or sighting
    return this.selectedStixObjectDetails
      .map(detail => detail.title)
      .filter(title => !linkedObjects.has(title))
  }

  // Transforms relationship data to STIX format
  transformToSTIX(relationship: any): any {
    if (relationship.type === 'relationship') {
      return {
        id: 'relationship--' + this.generateUUID(),
        type: 'relationship',
        source_ref: relationship.sourceDetail.id,
        relationship_type: relationship.relationship,
        target_ref: relationship.targetDetail.id
        // Add other necessary STIX fields
      }
    } else if (relationship.type === 'sighting') {
      return {
        id: 'sighting--' + this.generateUUID(),
        type: 'sighting',
        sighting_of_ref: relationship.sourceDetail.id,
        // Add other necessary STIX fields
      }
    }
    return {}
  }

  // Transform STIX object details to STIX format
  transformToObject(detail: StixObjectDetail): any {
    const nameField = detail.formData.find(fd => fd.key === "Name");
    const finalName = nameField?.value || detail.title;
    return {
      type: detail.stixType,
      id: detail.id,
      name: finalName,
      ...Object.fromEntries(detail.formData.map(fd => [fd.key, fd.value]))
    };
  }

  // Generates a random UUID (Universally Unique Identifier) - better way to do this later but this works for now
  generateUUID(): string {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
      var r = Math.random() * 16 | 0,
        v = c == 'x' ? r : (r & 0x3 | 0x8)
      return v.toString(16)
    })
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
    const stixObjects = this.selectedStixObjectDetails.map(detail => this.transformToObject(detail))
    const stixRelationshipsAndSightings = this.createdRelationships.map(rel => this.transformToSTIX(rel))

    // Convert each STIX object and relationship/sighting to its string representation
    const stixStrings = [...stixObjects, ...stixRelationshipsAndSightings].map(obj => JSON.stringify(obj, null, 2))

    // Join them together, separating by commas and newlines
    this.stixOutput = stixStrings.join(',\n')

    // The below code would create a STIX bundle
    // // Create a STIX bundle containing all the formatted data.
    // const stixData = [...stixObjects, ...stixRelationshipsAndSightings]
    // const bundle = {
    //   type: "bundle",
    //   id: "bundle--" + this.generateUUID(),
    //   spec_version: "2.1",
    //   objects: stixData
    // }
    // // Stringify the bundle for JSON output
    // this.stixOutput = JSON.stringify(bundle, null, 2)
  }
}