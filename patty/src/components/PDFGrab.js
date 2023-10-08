import { Document, Page } from "react-pdf";
import React, { useState } from "react";

function PDFGrab() {
  // Component state variables
  //   const state = {
  //     selectedFile: null,
  //     numPages: null,
  //     pageNumber: 1,
  //   };

  // Define state variables using useState
  const [selectedFile, setSelectedFile] = useState(null);
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);
  const [pdfData, setPdfData] = useState(null);
  const [file, setFile] = useState(null);

  // Event handler for file load
  //   const onFileLoad = ({ target: { result } }) => {
  //     setPdfData(result);
  //   };
  //
  // in close event we are sure that stream from child process is closed

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
  };

  // Event handler for successful document load
  const onDocumentLoadSuccess = ({ numPages }) => {
    setNumPages(numPages);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("pdfFile", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload-pdf", {
        method: "POST",
        body: formData,
      });

      // Check if the upload-pdf request was successful
      if (response.ok) {
        // If successful, proceed to send the generate-ics POST request
        const response2 = await fetch("http://127.0.0.1:8000/generate-ics", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (response2.ok) {
          // Handle the success response from the API
        } else {
          // Handle errors for the generate-ics request
        }
      } else {
        // Handle errors for the upload-pdf request
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  //   const { pageNumber, numPages, pdfData } = this.state;
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="file"
        accept=".pdf"
        // onChange={(event) => this.onFileLoad(event)}
        onChange={handleFileChange}
      />

      {pdfData && (
        <Document file={pdfData} onLoadSuccess={this.onDocumentLoadSuccess}>
          <Page pageNumber={pageNumber} />
        </Document>
      )}

      {pdfData && (
        <p>
          Page {pageNumber} of {numPages}
        </p>
      )}
      <button type="submit">Submit</button>
    </form>
  );
}

export default PDFGrab;
