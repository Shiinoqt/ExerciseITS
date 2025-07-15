import React from 'react'

const LoginForm = () => {
    const [email, setEmail] = React.useState();
    const [password, setPassword] = React.useState();
    const [message, setMessage] = React.useState();

    const gestioneDati = (e) => {
        e.preventDefault();
        setMessage(email + " " + password);
    }

    return (
        <div>
            <h1>Login</h1>
            <h3>{message}</h3>
            <form>
                <div>
                    <label>Email: </label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password: </label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button onClick={gestioneDati} type="submit">Login</button>
            </form>
        </div>
    )
}

export default LoginForm
