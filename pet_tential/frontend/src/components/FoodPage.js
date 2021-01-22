import React, { Component } from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,
  } from "react-router-dom";
  import Button from "@material-ui/core/Button";
  import Grid from "@material-ui/core/Grid";
  import Typography from "@material-ui/core/Typography";
  import TextField from "@material-ui/core/TextField";
  import Container from "@material-ui/core/Container";
  import InputLabel from "@material-ui/core/InputLabel";
  import FormHelperText from "@material-ui/core/FormHelperText";
  import FormControl from "@material-ui/core/FormControl";
  import Radio from "@material-ui/core/Radio";
  import RadioGroup from "@material-ui/core/RadioGroup";
  import FormControlLabel from "@material-ui/core/FormControlLabel";
  import { makeStyles } from '@material-ui/core/styles';


export default class FoodPage extends Component {
    defaultTreats = 0
    
    constructor(props) {
        super(props);

        var today = new Date(),
        defaultDate = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();

        this.state = {
            mealType: "",
            date: this.defaultDate,
            comment: "",
            treats: this.defaultTreats,
          };

        this.handleMealTypeChange = this.handleMealTypeChange.bind(this);
        this.handleDateChange = this.handleDateChange.bind(this);
        this.handleCommentChange = this.handleCommentChange.bind(this);
        this.handleTreatsChange = this.handleTreatsChange.bind(this);
        this.handleSubmitButtonPressed = this.handleSubmitButtonPressed.bind(this);
    }

    handleMealTypeChange(e) {
        this.setState({
          mealType: e.target.value,
        });
    }

    handleDateChange(e) {
        this.setState({
          date: e.target.value,
        });
    }

    handleCommentChange(e) {
        this.setState({
          comment: e.target.value,
        });
    }

    handleTreatsChange(e) {
        this.setState({
          treats: e.target.value,
        });
    }

    handleSubmitButtonPressed() {
        console.log("at the top");
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              meal_type: this.state.mealType,
              date: this.state.date,
              comment: this.state.comment,
              treats: this.state.treats,
            }),
          };
          console.log("hi");

          fetch("/api/add-food", requestOptions)
            .then((response) => response.json())
            .then((data) => console.log(data));

        
    }

    render() {
        return (
            <form>
              <Grid container spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Food Log
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                  <Grid container spacing={2}>
                    <Grid item xs={12}>
                      <TextField 
                      fullWidth 
                      label="Meal Type" 
                      name="MealType" 
                      size="small" 
                      variant="outlined" 
                      onChange={this.handleMealTypeChange} 
                      />
                    </Grid>
                    <Grid item xs={12}>
                      <TextField 
                      fullWidth 
                      type="date" 
                      size="small" 
                      variant="outlined" 
                      onChange={this.handleDateChange} 
                      defaultValue={this.defaultDate} 
                      />
                    </Grid>
                    <Grid item xs={12}>
                      <TextField 
                      fullWidth 
                      label="Comment" 
                      name="Comment" 
                      size="small" 
                      variant="outlined" 
                      onChange={this.handleCommentChange} 
                      />
                    </Grid>
                    <Grid item xs={12}>
                      <TextField 
                      fullWidth 
                      type="number" 
                      label="Treats" 
                      name="Treats" 
                      size="small" 
                      variant="outlined" 
                      onChange={this.handleTreatsChange} 
                      defaultValue={this.defaultTreats} 
                      />
                    </Grid>
                  </Grid>
                </Grid>
                <Grid item xs={12}>
                  <Button 
                  color="primary" 
                  fullWidth 
                  type="submit" 
                  variant="contained" 
                  onClick={this.handleSubmitButtonPressed}
                  >
                    Post
                  </Button>
                </Grid>
              </Grid>
            </form>
        );
    }
}