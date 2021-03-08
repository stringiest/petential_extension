import React from "react";
import { shallow } from "enzyme";
import CreatePackPage from '../components/CreatePackPage';

it("renders without crashing", () => {
    const wrapper = shallow(<CreatePackPage />);
    const appComponent = wrapper.find("[data-test='component-create-pack']")
    expect(appComponent.length).toBe(1);
});

it("renders button for create pack", () => {
    const wrapper = shallow(<CreatePackPage />);
    const button = wrapper.find("[data-test='create-button']")
    expect(button.length).toBe(1);
});

