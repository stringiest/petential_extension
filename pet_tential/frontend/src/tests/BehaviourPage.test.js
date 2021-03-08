import React from "react";
import { shallow } from "enzyme";
import BehaviourPage from '../components/BehaviourPage';

it("renders without crashing", () => {
    const wrapper = shallow(<BehaviourPage />);
    const appComponent = wrapper.find("[data-test='component-behaviour']")
    expect(appComponent.length).toBe(1);
});