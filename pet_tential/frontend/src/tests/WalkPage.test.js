import React from "react";
import { shallow } from "enzyme";
import WalkPage from '../components/WalkPage';

it("renders without crashing", () => {
    const wrapper = shallow(<WalkPage />);
    const appComponent = wrapper.find("[data-test='component-walk']")
    expect(appComponent.length).toBe(1);
});