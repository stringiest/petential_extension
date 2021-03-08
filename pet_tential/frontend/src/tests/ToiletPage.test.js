import React from "react";
import { shallow } from "enzyme";
import ToiletPage from '../components/ToiletPage';

it("renders without crashing", () => {
    const wrapper = shallow(<ToiletPage />);
    const appComponent = wrapper.find("[data-test='component-toilet']")
    expect(appComponent.length).toBe(1);
});