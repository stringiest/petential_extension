import React from "react";
import { shallow } from "enzyme";
import MedicalPage from '../components/MedicalPage';

it("renders without crashing", () => {
    const wrapper = shallow(<MedicalPage />);
    const appComponent = wrapper.find("[data-test='component-medical']")
    expect(appComponent.length).toBe(1);
});