import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ObjectBoxComponent } from './object-box.component';

describe('ObjectBoxComponent', () => {
  let component: ObjectBoxComponent;
  let fixture: ComponentFixture<ObjectBoxComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ObjectBoxComponent]
    });
    fixture = TestBed.createComponent(ObjectBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
