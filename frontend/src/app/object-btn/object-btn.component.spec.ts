import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ObjectBtnComponent } from './object-btn.component';

describe('ObjectBtnComponent', () => {
  let component: ObjectBtnComponent;
  let fixture: ComponentFixture<ObjectBtnComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ObjectBtnComponent]
    });
    fixture = TestBed.createComponent(ObjectBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
