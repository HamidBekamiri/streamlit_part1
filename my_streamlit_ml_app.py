import streamlit as st
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('AI-Growth-Lab/PatentSBERTa')

# Two lists of sentences
sentences1 = st.text_input('Insert sentences 1:')


sentences2 = st.text_input('Insert sentences 2:')



if st.button('Submit'):
  st.write('sentences1 is: ', sentences1)
  st.write('sentences2 is: ', sentences2)

  #Compute embedding for both lists
  embeddings1 = model.encode(sentences1, convert_to_tensor=True)
  embeddings2 = model.encode(sentences2, convert_to_tensor=True)

  #Compute cosine-similarities
  cosine_scores = util.cos_sim(embeddings1, embeddings2)

  #Output the pairs with their score
  for i in range(len(sentences1)):
    st.write("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))
#     print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))
