import React, { useState } from "react"
import { Segment, Form, Button, Container, Grid, Placeholder, PlaceholderHeader } from "semantic-ui-react"


export default function Create(){

    const [isLoading, setIsLoading] = useState(false)
    const [university, setUniversity] = useState("")
    const [moduleCode, setModuleCode] = useState("")

    // Function for handling the change of form entries using the above hooks.
    const handleChange = (e, { name, value }) => {
        if(name==="university"){
            setUniversity(value)
        } else {
            setModuleCode(value)
        }
       
    }

    // Function for handling the submission of data to the backend API. For now it's just an alert!    
    const handleSubmit = (e) => {
        alert(`Congratulations! You've created a new Newt for \n University: ${university}\n Module Code: ${moduleCode}`)
    }


    // Temporary button for toggling the loading animation before the API returns
    const toggleLoading = () => {
        isLoading ? setIsLoading(false) : setIsLoading(true)
    }

    // Temporary options for drop down
    const options = [
        { key: "uoliverpool", text: "University of Liverpool", value: "uoliverpool"},
        { key: "uomanchester", text: "University of Manchester", value: "uomanchester"}
    ]

    return (
        <Container>
            <Grid centered>
                <Grid.Column width={6}>
                <Segment>
                    { isLoading ?
                        (
                        <Placeholder>
                            <PlaceholderHeader>
                                <Placeholder.Line/>
                                <Placeholder.Line/>
                            </PlaceholderHeader>
                            <Placeholder.Header>
                                <Placeholder.Line/>
                                <Placeholder.Line/>
                            </Placeholder.Header>
                        </Placeholder>
                    )            
                    : (
                        <Form>
                            <Form.Select label="University" options={options} placeholder="Select University" name="university" onChange={handleChange}/>
                            <Form.Input label="Module Code" placeholder="e.g LIFE113" name="module code" onChange={handleChange}/>
                            <Button type='submit' onClick={handleSubmit}>Create Newt!</Button>
                        </Form>
                    )}
                </Segment>
                <Button onClick={toggleLoading}>Toggle Loading</Button>
                </Grid.Column>
            </Grid>
        </Container>
    )
}