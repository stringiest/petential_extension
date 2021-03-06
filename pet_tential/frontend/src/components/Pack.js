import React, { Component } from "react";
import { Grid, Button, Typography, AppBar } from "@material-ui/core";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class Pack extends Component {
  constructor(props) {
    super(props);
    this.state = {
      petName: "",
      isHost: false,
      packId: ""
    };
    console.log("!!!!!")
    console.log(this.props);
    this.packCode = this.props.match.params.packCode;
    this.getPackDetails();
    this.leaveButtonPressed = this.leaveButtonPressed.bind(this);
  }

  getPackDetails() {
    fetch("/api/get-pack" + "?code=" + this.packCode)
      .then((response) => {
        if (!response.ok) {
          this.props.leavePackCallback();
          this.props.history.push("/");
        }
        return response.json();
      })
      .then((data) => {
        this.setState({
          petName: data.pet_name,
          isHost: data.is_host,
          packId: data.id
        });
      });
  }

  leaveButtonPressed() {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    };
    fetch("/api/leave-pack", requestOptions).then((_response) => {
      this.props.leavePackCallback();
      this.props.history.push("/");
    });
  }

render() {
    return (
      <div className="bg" data-test='component-pack'>
        <AppBar position="static" color="transparent" elevation={0}>
              <img src={require('./logo_without_words.png')} alt="logo" height={200} width={200}/>
        </AppBar>
          <br></br>
      <Grid container spacing={1} align="center">
    
        <Grid item xs={12} align="center">
            <Typography>
            <h1> Welcome to {this.state.petName.toString()}'s Pack Page </h1>
            <br />
            <br />
            <h4>Add members to your pack with this code: {this.packCode}</h4>  
            <br />
            <br />
            </Typography>
        </Grid>
        <Grid item xs={12} align="center">
            <Button style={{minWidth: '183px', minHeight: '30px'}} color="primary" variant="contained" to="/food" component={Link}>
                  Food
            </Button>
          </Grid>
          <Grid item xs={12} align="center">
            <Button style={{minWidth: '183px', minHeight: '30px'}} color="primary" variant="contained" to="/walk" component={Link}>
               Walk
            </Button>
          </Grid> 
          <Grid item xs={12} align="center">
                <Button style={{minWidth: '183px', minHeight: '30px'}} color="primary" variant="contained" to="/medical" component={Link}>
                  Medical
                </Button>
              </Grid>
              <Grid item xs={12} align="center">
                <Button style={{minWidth: '183px', minHeight: '30px'}} color="primary" variant="contained" to="/toilet" component={Link}>
                  Toilet Training
                </Button>
              </Grid>
              <Grid item xs={12} align="center">
                <Button color="primary" variant="contained" to="/behaviour" component={Link}>
                Behaviour Training
                </Button>
              </Grid>           
              <Grid item xs={12} align="center">
                <Button color="secondary" variant="contained" onClick={this.leaveButtonPressed}>
                Leave Pack
                </Button>
              </Grid>  
      </Grid>
      </div>
    );
  }
}