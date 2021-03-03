
import React from "react";
import Enzyme from 'enzyme';
import Adapter from '@wojtekmaj/enzyme-adapter-react-17';
import { shallow, mount } from "enzyme";
// import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import WelcomePage from '../components/WelcomePage';
// import toJson from "enzyme-to-json";

Enzyme.configure({ adapter: new Adapter() });

it("renders without error", () => {
  const wrapper = shallow(<WelcomePage />);
  const appComponent = wrapper.find("[data-test='component-welcome']")
  // const appComponent = findByTestAttr(wrapper, 'component-app');
  expect(appComponent.length).toBe(1);
  });

it("renders button for create pack", () => {
  const wrapper = shallow(<WelcomePage />);
  const button = wrapper.find("[data-test='create-button']")
  expect(button.length).toBe(1);
});
// it('renders welcome message', () => {
//   render(<WelcomePage />);  
//   expect(screen.getByText('Petential')).toBeInTheDocument();
// });
  // it("renders Page header", () => {
// const wrapper = shallow(<WelcomePage />);
// const welcome = <h3>Petential</h3>;
// expect(wrapper.contains(welcome)).toEqual(true);
// });
