
    const text = document.getElementById("text");
    const extra = document.getElementById("extra");
    const output = document.getElementById("output");
    const hoverText = document.getElementById("hoverText");
    const userInput = document.getElementById("userInput");

    
    document.getElementById("btnChange").addEventListener("click", () => {
      text.innerText = "You clicked the button!";
      extra.innerText = "The second paragraph changed too!";
      text.style.color = "blue";
      text.style.fontSize = "20px";
    });

    document.getElementById("btnReset").addEventListener("click", () => {
      text.innerText = "This is a paragraph.";
      extra.innerText = "Another paragraph.";
      text.style.color = "";
      text.style.fontSize = "";
    });

    document.getElementById("btnShow").addEventListener("click", () => {
      output.innerText = "You typed: " + userInput.value;
    });

    hoverText.addEventListener("mouseover", () => {
      hoverText.innerText = "Mouse is here!";
    });

    hoverText.addEventListener("mouseout", () => {
      hoverText.innerText = "Hover over me!";
    });
  