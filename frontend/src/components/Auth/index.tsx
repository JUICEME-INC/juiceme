import { useEffect, useState } from "react";
import { NavLink, useLocation } from "react-router-dom"
import { Form, Button, Row, Col } from "react-bootstrap";
import './index.scss'
import CountryCodeSelect from "../CountryCodeSelect";

const SignIn = () => {
  const initialAuth = {
    reset: false,
    signIn: false,
    signUp: false
  }
  const [auth, setAuth] = useState(initialAuth)
  const location = useLocation()
  useEffect(() => {
    if (location.pathname === '/signin') {
      setAuth({...initialAuth, signIn:true})
     } else if (location.pathname === '/signup') {
      setAuth({...initialAuth, signUp:true})
    } else if (location.pathname === '/reset') {
      setAuth({...initialAuth, reset:true})
    }
  }, [location.pathname])

  const typographyInfo = {
    signUp: {
      "title": "Create your account",
      "description": "Let’s help you get started on Juiceme"
    },
    signIn: {
      "title": "Log in to your account",
      "description": "Welcome back to Juiceme"
    },
    reset: {
      "title": "Reset your password",
      "description": "Input your email or phone number to get a reset link."
    }
  }
  return (
    <div className="auth-container">
      <div>
      {auth.signIn && (
        <div>
          <h1 className="auth-header" >{typographyInfo.signIn.title}</h1>
          <p className="auth-paragraph">{typographyInfo.signIn.description}</p>
        </div>
      )}
      {auth.signUp && (
        <div>
          <h1 className="auth-header">{typographyInfo.signUp.title}</h1>
          <p className="auth-paragraph">{typographyInfo.signUp.description}</p>
        </div>
      )}
      {auth.reset && (
        <div>
        <h1 className="auth-header">{typographyInfo.reset.title}</h1>
        <p className="auth-paragraph">{typographyInfo.reset.description}</p>
      </div>
      )}
      <Form>
        {auth.signUp && (<Form.Group className="mb-3" controlId="fullName">
          <Form.Label>Full Name</Form.Label>
          <Form.Control type="text" placeholder="John Doe" />
        </Form.Group>)}
        {auth.signUp && (<Form.Group className="mb-3" controlId="phoneNumber">
          <Form.Label>Phone Number</Form.Label>
          <Row noGutters={true}>
            <Col xs={3}>
              <CountryCodeSelect />
            </Col>
            <Col xs={9}>
              <Form.Control type="tel" placeholder="8287938745" />
            </Col>
          </Row>
        </Form.Group>)}
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>{auth.signIn ? "Representative Email" : "Email"}</Form.Label>
          <Form.Control type="email" placeholder="example@gmail.com" />
        </Form.Group>
        {!auth.reset &&
        <Form.Group className="mb-3" controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="********" />
        </Form.Group>}

        {auth.signUp && (<Form.Group className="mb-3" controlId="confirmPassword">
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control type="password" placeholder="********" />
        </Form.Group>)}
        {auth.signIn && <Row className="auth-row">
          <Col md={5}>
            <Form.Check type='checkbox' id="rememberMe" label="Remember me" />
          </Col>
          <Col md={7}>
            <p className="auth-paragraph">Forgot password? <NavLink to="/reset">Reset</NavLink></p>
          </Col>
        </Row>}
        <Button variant="primary" >{auth.signIn ? "Sign In" : auth.reset? "Send": "Sign Up"}</Button>
        {auth.signIn && (<p className="auth-paragraph">Don't have an account? <NavLink to="/signup">Sign Up</NavLink></p>)}
        {!auth.signIn && (<p className="auth-paragraph">{auth.signUp? "Have an account?": "Remember password?"} <NavLink to="/signin">Sign In</NavLink></p>)}
      </Form>
      </div>
    </div>
  )

}

export default SignIn;