async function submitInstruction() {
  const input = document.getElementById("inputText").value.trim();
  const output = document.getElementById("outputCode");
  const loading = document.getElementById("loading");

  if (!input) {
    output.textContent = "// Please enter a valid instruction.";
    return;
  }

  output.textContent = "";
  loading.classList.remove("hidden");

  try {
    const response = await fetch("http://localhost:5000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ instruction: input })
    });

    const data = await response.json();
    output.textContent = data.generated_code || "// No code returned.";
    Prism.highlightElement(output);
  } catch (error) {
    output.textContent = `// Error: ${error.message}`;
  } finally {
    loading.classList.add("hidden");
  }
}
