import React from 'react';

const SelectCarM = () => {
  const modelliPerMarca = {
    bmw: ["Serie 1", "Serie 2", "Serie 3", "Serie 4", "Serie 5", "Serie 6", "Serie 7", "X1", "X2", "X3", "X4", "X5", "X6", "X7"],
    mercedes: ["Classe A", "Classe B", "Classe C", "Classe E", "Classe S", "GLA", "GLB", "GLE", "GLS"],
    audi: ["A1", "A3", "A4", "A5", "A6", "A7", "A8", "Q2", "Q3", "Q5", "Q7", "Q8"]
  };

  const [marca, setMarca] = React.useState('');
  const [modello, setModello] = React.useState('');

  const handleMarcaChange = (event) => {
    const selectedMarca = event.target.value;
    setMarca(selectedMarca);
    setModello(''); // Reset model when brand changes
  };

  const handleModelloChange = (event) => {
    setModello(event.target.value);
  };

  // Get available models based on selected brand
  const availableModels = marca ? modelliPerMarca[marca] : [];

  return (
    <div className="container mt-5">
      <div className="row mb-3">
        <div className="col">
          <label htmlFor="marca" className="form-label">
            Seleziona la marca:
          </label>
          <select 
            id="marca" 
            name="marca" 
            className="form-select" 
            value={marca}
            onChange={handleMarcaChange}
          >
            <option value="">Seleziona marca</option>
            <option value="bmw">BMW</option>
            <option value="mercedes">Mercedes</option>
            <option value="audi">Audi</option>
          </select>
        </div>
      </div>
      
      <div className="row">
        <div className="col">
          <label htmlFor="modello" className="form-label">
            Seleziona il modello:
          </label>
          <select 
            id="modello" 
            name="modello" 
            className="form-select"
            value={modello}
            onChange={handleModelloChange}
            disabled={!marca}
          >
            <option value="">Seleziona modello</option>
            {availableModels.map((model) => (
              <option 
                key={model} 
                value={model}
              >
                {model}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
};

export default SelectCarM;