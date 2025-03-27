import {
  ChangeDetectorRef,
  Component,
  ElementRef,
  Input,
  OnChanges,
  ViewChild,
} from "@angular/core";
import { AttributeHelperService } from "../attribute-helper.service";
import { AttributeDto, ElementDto } from "../types/json-response.dto";
import { ElementLookupService } from "../element-lookup.service";
import { CallBackHelperService } from "../callback-helper.service";

@Component({
  selector: "app-range-slider",
  styleUrls: ["./range-slider.component.scss"],
  templateUrl: "./range-slider.component.html",
})
export class RangeSliderComponent {
  @ViewChild("theSlider", { static: false }) theSlider!: ElementRef;
  @ViewChild("theMinRange", { static: false }) theMinRange!: ElementRef;
  @ViewChild("theMaxRange", { static: false }) theMaxRange!: ElementRef;

  @Input() element: ElementDto | null = null;
  @Input() parentLayout: string = "";

  min = 0;
  max = 100;
  minValue = 20;
  maxValue = 80;

  width = 0;
  left = 0;

  trackLeft = 20;
  trackWidth = 60;

  constructor(
    private cd: ChangeDetectorRef,
    private callbackService: CallBackHelperService,
    private attributeService: AttributeHelperService,
    private elementLookupService: ElementLookupService
  ) {}

  ngAfterViewInit(): void {
    if (this.element != null) {
      this.elementLookupService.addElementObject(
        this.element.id,
        this,
        this.element
      );

      this.setAttributes(this.element.attributes);

      this.callbackService.setCallbacks(
        this.theMinRange.nativeElement,
        this.element.when
      );
      this.callbackService.setCallbacks(
        this.theMaxRange.nativeElement,
        this.element.when
      );
      this.cd.detectChanges();
    }
  }

  setAttributes(attributes: AttributeDto[]) {
    let oldMin = this.min;
    let oldMax = this.max;

    this.min = parseInt(
      this.attributeService.findGetAttributeValue("min", attributes, "0")
    );
    this.max = parseInt(
      this.attributeService.findGetAttributeValue("max", attributes, "100")
    );

    // if (this.min !== oldMin || this.max !== oldMax) {
    //   this.setMinValue(this.min);
    //   this.setMaxValue(this.max);
    // }
    this.setMinValue(
      parseInt(
        this.attributeService.findGetAttributeValue(
          "min_value",
          attributes,
          "0"
        )
      )
    );
    this.setMaxValue(
      parseInt(
        this.attributeService.findGetAttributeValue(
          "max_value",
          attributes,
          "0"
        )
      )
    );

    this.updateTrack();

    let slider = this.theSlider.nativeElement;

    this.attributeService.setAttributesDirectly(slider, attributes);
    this.attributeService.addAttributes(slider, attributes);
    this.attributeService.textAttributes(slider, attributes);
    this.attributeService.addGeneralAttributes(slider, attributes);
    this.attributeService.addClasses(slider, attributes, [], []);

    if (this.element != null) {
      this.attributeService.setAbsoulteRelativePositions(
        this.parentLayout,
        slider,
        this.element
      );
    }

    this.cd.detectChanges();
  }

  updateValue(sliderType: "min" | "max", element: EventTarget | null) {
    if (element instanceof HTMLInputElement) {
      if (sliderType === "min") {
        this.setMinValue(parseInt(element.value, 10));
      } else {
        this.setMaxValue(parseInt(element.value, 10));
      }
    }

    this.updateTrack();
  }

  setMinValue(value: number) {
    this.minValue = value;

    if (this.minValue > this.maxValue) {
      this.minValue = this.maxValue;
    }
  }

  setMaxValue(value: number) {
    this.maxValue = value;

    if (this.maxValue < this.minValue) {
      this.maxValue = this.minValue;
    }
  }

  updateTrack() {
    const total = this.max - this.min;
    this.trackLeft = ((this.minValue - this.min) / total) * 100;
    this.trackWidth = ((this.maxValue - this.minValue) / total) * 100;
  }
}
