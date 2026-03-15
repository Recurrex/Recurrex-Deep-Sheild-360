import React, { useState } from 'react';

function App() {
  return (
    <div style={{ backgroundColor: '#000', color: '#fff', minHeight: '100vh', textAlign: 'center', paddingTop: '50px' }}>
      <h1 style={{ color: '#ff0000' }}>RECURREX // DEEP-SHIELD 360</h1>
      <p>Advanced Deepfake Detection System</p>
      <div style={{ border: '2px dashed #333', padding: '50px', margin: '20px auto', maxWidth: '500px' }}>
        <input type="file" />
        <br/><br/>
        <button style={{ backgroundColor: '#ff0000', color: '#fff', border: 'none', padding: '10px 20px', cursor: 'pointer' }}>
          SCAN VIDEO
        </button>
      </div>
    </div>
  );
}

export default App;

