import React from "react";
import { shallow } from "enzyme";
import Weather from '../components/Weather';

it("renders without crashing", () => {
    const wrapper = shallow(<Weather />);
    const appComponent = wrapper.find("[data-test='component-weather']")
    expect(appComponent.length).toBe(1);
});