export const submitFormData = (formData) => {
  // Check if any field is empty
  if (!formData.name.trim()) {
    console.error("Name is required");
    return false;
  }

  if (!formData.email.trim()) {
    console.error("Email is required");
    return false;
  }

  if (!formData.message.trim()) {
    console.error("Message is required");
    return false;
  }

  // All fields are filled
  console.log("Form submitted successfully:", formData);
  return true;
};