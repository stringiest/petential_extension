import React from "react";
import { shallow } from "enzyme";
import Pack from '../components/Pack';

global.fetch = jest.fn(() => 
        Promise.resolve({
            json: () => Promise.resolve({ pet_name: "houmous", is_host: true, id: "1"})
        }));

describe('Pack page', function() {
  it("renders without crashing", () => {
      const func = () => {};
      const hist = [];
  shallow(<Pack history={hist} leavePackCallback={func} match={{params: {packCode: "ABCDEF"}}}/>);
  });

//   it('shows pet details', () => {
//     let houmous = new Pack();
//     expect(houmous.props.petName).toEqual({petName: "houmous", isHost: True})
//   });
});


