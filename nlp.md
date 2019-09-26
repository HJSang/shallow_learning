# Summary for NLP Reading

## tf-idf
[TFIDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf): term frequency-Inverse document frequency
* Term frequency: the number of times a term occurs in a document is called its term frequency; The weight of a term that occurs in a document is simply proportional to the term frequency.
* Inverse document frequency: The specificity of a term can be quantified as an inverse function of the number of documents in which it occurs.


* **Definition**: 
  * The tf–idf is the product of two statistics, term frequency and inverse document frequency. There are various ways for determining the exact values of both statistics.
  * A formula that aims to define the importance of a keyword or phrase within a document or a web page.


* **Term frequency**:
  * the simplest choice is to use the raw count of a term in a document
  * Boolean "frequencies": tf(t,d) = 1 if t occurs in d and 0 otherwise
  * term frequency adjusted for document length : ft,d ÷ (number of words in d)
  * logarithmically scaled frequency: tf(t,d) = log (1 + ft,d)
  * augmented frequency, to prevent a bias towards longer documents, e.g. raw frequency divided by the raw frequency of the most occurring term in the document.


 * **Inverse document frequency**:
   * The inverse document frequency is a measure of how much information the word provides, i.e., if it's common or rare across all documents. 
   * It is the logarithmically scaled inverse fraction of the documents that contain the word. 
   * Obtained by dividing the total number of documents by the number of documents containing the term, and then taking the logarithm of that quotient.


 * **Term frequency–Inverse document frequency**:
   * **Term frequency** x **Inverse document frequency**


