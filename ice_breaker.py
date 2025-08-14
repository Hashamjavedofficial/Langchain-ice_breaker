from dotenv import load_dotenv;
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os

load_dotenv()


information = """
 Hasham Javed: Technical Lead & Full Stack Developer at Systems Limited | Javascript, React, Vue, Nextjs, Nestjs, Nuxtjs

🚀 Hello and welcome! I’m a passionate technologist and a skilled Technical Lead at Systems Limited, where I blend clean design with cutting-edge engineering. My expertise spans React, Next.js, Vue, TypeScript, and Node.js, building intuitive, scalable, and AI-enhanced digital products that deliver real impact.

🌟 What I Bring to the Table 🌟

🎯 Frontend Engineering at the Core

I specialize in building responsive, scalable, and performance-driven user interfaces using React.js, Next.js, Vue.js, TypeScript, and Tailwind CSS. My focus is on crafting seamless, intuitive UI experiences that are visually polished and technically robust from design systems to real-time dashboards.

🚀 AI-Powered Product Development

At AutoMatoAI, I led both frontend and backend development for an AI-based Amazon listing optimization platform. I engineered features like:
Real-time keyword intelligence and competitor analysis
Generative AI content tailored to search intent
Conversion-focused listings and sales forecasting

🧩 Full-Stack Engineering with Depth

Beyond UI, I build secure, efficient, and scalable backend systems using Node.js, NestJS, Express, PostgreSQL, MongoDB, and Firebase. I design and maintain RESTful and GraphQL APIs, cloud-native systems, and DevOps workflows using Docker, CI/CD, AWS, GCP, and Azure.

🔧 Problem Solver: I thrive in challenging environments, where every bug is a puzzle waiting to be solved. My analytical mindset and troubleshooting skills are my secret weapons.

🚀 Continuous Learner: The tech world never stops evolving, and neither do I. I'm committed to staying at the forefront of industry trends and best practices.

👥 Team Player: Collaboration is key. I thrive in collaborative environments, where I can share my knowledge and learn from others.


💼Expanding possibilities

I’m currently open to opportunities where I can contribute to product growth, technical direction, and AI-enhanced user experiences. If you're scaling your frontend stack or building innovative platforms, let’s connect and build something great.


🔗 Let's Connect 🔗

I'm always eager to connect with fellow tech enthusiasts, industry experts, and potential collaborators. Whether you want to discuss a project, share insights, or just have a virtual coffee chat, feel free to connect with me.

Let's harness the power of code to create a better digital world together. Connect with me, and let's embark on this exciting journey! """

if __name__ == '__main__':
    print('Hello World')
    print(__name__)

    summary_template = """
         write me song about pizza
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(os.environ['COOL_API'],res)