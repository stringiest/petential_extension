import React from "react";
import { shallow } from "enzyme";
import JoinPackPage from '../components/JoinPackPage';

it("renders without crashing", () => {
    const wrapper = shallow(<JoinPackPage />);
    const appComponent = wrapper.find("[data-test='component-join-pack']")
    expect(appComponent.length).toBe(1);
});