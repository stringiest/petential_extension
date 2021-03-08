import React from "react";
import { shallow, mount } from "enzyme";
import FoodPage from '../components/FoodPage';

// feature - go to page food and expect content to be 'Food Log'
// feature - fill in form and click Post, expect page to have content that they've just added
// unit -
// describe ('Test the FoodPage and actions', () => {
//   it('allows user to include meal type, date, comment and treats', () => {
//     let foodpage = new FoodPage();
//     expect(foodpage.state).toEqual({ mealType: "",
//     date: "",
//     comment: "",
//     treats: 0,
//     foodList: []})
//   });

// });

it("renders without crashing", () => {
    const wrapper = shallow(<FoodPage />);
    const appComponent = wrapper.find("[data-test='component-food']")
    expect(appComponent.length).toBe(1);
});
