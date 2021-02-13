import React, { useState, useEffect } from "react"
import { Segment, Form, Button, Container, Grid, Placeholder, PlaceholderHeader, Header } from "semantic-ui-react"
import { DateTimeInput } from "semantic-ui-calendar-react"
import axios from 'axios'
import adjectives from "./adjectives"
import animals from "./animals"


export default function Create(){

    const [isLoading, setIsLoading] = useState(true)
    const [university, setUniversity] = useState("")
    const [moduleCode, setModuleCode] = useState("")
    const [sessionType, setSessionType] = useState("")
    const [start, setStart] = useState("")
    const [finish, setFinish] = useState("")
    const [message, setMessage] = useState("")
    const [institutionList, setInstitutionList] = useState([{ key: "Placeholder", text: "Placeholder", value: "Placeholder"}])
    const [newt, setNewt] = useState("")
    const [newtComplete, setNewtComplete] = useState(false)

    useEffect(() => {
        // Get the list of institutions and parse them to the dropdown format.
        // TODO: Implement 2 tier country dropdown (not needed for a while!)

        axios.get('api/institutions')
        .then(res => {
            const data = res.data
            const parsedData = data.map((value, index) => {
                return {key: index, text: value.name, value: value.name}
            })
            setInstitutionList(parsedData)

            // Also generate a newt - we do this now for convenience really!
            setNewt(generateNewt())

            setIsLoading(false)
        })
        .catch((error) => {
            console.error('Error:', error)
        })
    }, [])

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const chooseRandom = array => {
        // Helper function for choosing a random element from a list
        return array[Math.floor(Math.random() * array.length)]
    }

    const capitalize = s => {
        return typeof(s) !== "string" ? '' : s.charAt(0).toUpperCase() + s.slice(1)
    }

    const generateNewt = () => {
        
        // Randomly select an adjective and animal
        
        let randAdj = capitalize(chooseRandom(adjectives));
        let randAnimal = capitalize(chooseRandom(animals));
        
        return `${randAdj} ${randAnimal}` 
    }

    // Function for handling the change of form entries using the above hooks.
    const handleChange = (e, { name, value }) => {
        switch(name){
            case "university":
                setUniversity(value)
                break
            case "session type":
                setSessionType(value)
                break
            case "module code":
                setModuleCode(value)
                break
            case "from":
                setStart(value)
                break
            case "to":
                setFinish(value)
                break
            case "message":
                setMessage(value)
                break
            default:
                // pass

        }
       
    }

    const validateInput = () => {
        // TODO: Make sure form is filled in properly!
        return true
    }

    // Function for handling the submission of data to the backend API. For now it's just an alert!    
    const handleSubmit = (e) => {
        e.preventDefault();



        if(validateInput()){

            // Generate new Newt code if the form is good

            
            // Format data for POST request
            const formData = {
                course: moduleCode,
                newt_code: newt,
                session_type: sessionType,
                start: start,
                finish: finish,
                message: message
            }

            console.log(formData)

            let csrftoken = getCookie('csrftoken')
            axios.post("api/newts/", formData, { headers : {"X-CSRFTOKEN": csrftoken } })
            .then(res => {
                setNewtComplete(true)
            })
            .catch(err => {
                console.log(err)
                console.log(err.message)

            })


        } else {
            alert("Uh oh - you didn't fill out the form correctly!")
        }
    }

    const temp_session_types = [
        {key: 0, text: "Lecture", value: 1},
        {key: 1, text: "Tutorial", value: 2}
    ]

    return (
        <Container>
            <Grid centered>
                { newtComplete ? 
                    (
                        <Grid.Column width={10}>
                            <Segment>
                                <br/>
                                <Header size='medium' textAlign='center'>Today's Attendence Code Is:</Header>
                                <Header size='huge' textAlign='center'>{newt}</Header>
                                <br/>
                            </Segment>
                        </Grid.Column>
                    )
                :
                    (
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
                                        <Form.Select label="University" options={institutionList} placeholder="Select University" name="university" onChange={handleChange}/>
                                        <Form.Input label="Module Code" placeholder="e.g LIFE113" name="module code" onChange={handleChange}/>
                                        <Form.Select label="Session Type" options={temp_session_types} placeholder="Session Type" name="session type" onChange={handleChange}/>
                                        <DateTimeInput label="From" placeholder="Date and Time From" onChange={handleChange} name="from" value={start}/>
                                        <DateTimeInput label="To" placeholder="Date and Time To" onChange={handleChange} name="to" value={finish}/>
                                        <Form.Input label="Message" placeholder="Message for administrators" name="message" onChange={handleChange}/>
                                        <Button type='submit' onClick={handleSubmit}>Create Newt!</Button>
                                    </Form>
                                )}
                            </Segment>
                        </Grid.Column>
                    )
                }
                
            </Grid>
        </Container>
    )
}