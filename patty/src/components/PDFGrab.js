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

  // Event handler for file load
  const onFileLoad = ({ target: { result } }) => {
    setPdfData(result);
  };

  // Event handler for successful document load
  const onDocumentLoadSuccess = ({ numPages }) => {
    setNumPages(numPages);
  };

  //   const { pageNumber, numPages, pdfData } = this.state;
  return (
    <>
      <input
        type="file"
        accept=".pdf"
        onChange={(event) => this.onFileLoad(event)}
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
    </>
  );
}

export default PDFGrab;
