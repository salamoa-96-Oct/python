import React, { useState } from 'react';

function UserForm() {
  const [formData, setFormData] = useState({
    email: '',
    full_name: '',
    password: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:8000/api/v1/users/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });
    if (response.ok) {
      alert('회원가입이 완료되었습니다.');
      setFormData({ email: '', full_name: '', password: '' });
    } else {
      const data = await response.json();
      alert(`에러: ${data.detail}`);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>이메일:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
      </div>
      <div>
        <label>이름:</label>
        <input type="text" name="full_name" value={formData.full_name} onChange={handleChange} />
      </div>
      <div>
        <label>비밀번호:</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} required />
      </div>
      <button type="submit">회원가입</button>
    </form>
  );
}

export default UserForm;