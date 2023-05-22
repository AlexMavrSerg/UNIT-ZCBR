import { useState } from 'react';
import '../Form/form.scss';
import { useEffect } from 'react';

const Form = () => {
const [email, setEmail] = useState('')
const [password, setPassword] = useState('')
const [emailDirty, setEmailDirty] = useState(false)
const [passwordDirty, setPasswordDirty] = useState(false)
const [emailError, setEmailError] = useState('Вы не ввели почту')
const [passwordError, setPasswordError] = useState('Вы не ввели пароль')
const [formValid, setFormValid] = useState(false)


 useEffect( () => {
if(emailError || passwordError) {
    setFormValid(false)
} else {
    setFormValid(true)
}
},
 [emailError, passwordError])

const blurHandler = (e) => {
    switch (e.target.name) {
        case 'email':
            setEmailDirty(true)
            break
        case 'password':
            setPasswordDirty(true)
        break

    }
}

const emailHandler = (e) => {
    setEmail(e.target.value)
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    if (!re.test(String(e.target.value).toLowerCase())) {
        setEmailError('Не корректный ввод почты')
        if(!e.target.value) {
            setEmailError('Вы не ввели почту')
        }
    } else {
        setEmailError('')
    }

};

const passwordHandler = (e) => {
    setPassword(e.target.value)
    
    if (e.target.value.length <= 4 || e.target.value.length >= 10) {
        setPasswordError('Пароль должен быть длинее 4 и меньше 10 символов')
        if (!e.target.value) {
            setPasswordError('Вы не ввели пароль')
        }
    } else {
        setPasswordError('')
    }

}

    return (
        <div className="form">
    <form>
        <h1 className="form_name">Регистрация</h1>
        <label className="form_label">Email</label>
        {(emailDirty && emailError) && <div style={{color:'red'}}>{emailError}</div>}
        <input value={email} onChange={e => emailHandler(e)} onBlur={blurHandler} className="form_input" name="email" type="text" placeholder="Введите почту"/>

        <label className="form_label">Пароль</label>
        {(passwordDirty && passwordError) && <div style={{color:'red'}}>{passwordError}</div>}
        <input value={password} onChange={e => passwordHandler(e)} onBlur= { blurHandler } className="form_input" name="password" type="text" placeholder="Введите пароль"/>
        <button disabled={!formValid} className="form_btn">Войти</button>
    </form>
</div>
    )
};

export default Form; 