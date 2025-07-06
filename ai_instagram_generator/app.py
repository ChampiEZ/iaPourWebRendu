from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import os
import random

app = Flask(__name__)
CORS(app)

# Charger le modèle
class InstagramHookGenerator:
    def __init__(self):
        self.hooks_templates = [
            "🔥 {topic} qui va changer votre {domain} !",
            "✨ Découvrez le secret de {topic}",
            "💡 Cette astuce {topic} va vous surprendre",
            "🚀 Prêt à maîtriser {topic} ?",
            "💎 Le guide ultime pour {topic}",
            "🌟 Pourquoi {topic} est si important",
            "⚡ {topic} : la méthode qui marche",
            "🎯 Attention : {topic} révélé !",
            "🔑 {topic} : voici comment faire",
            "💪 {topic} : relevez le défi !",
            "🎨 {topic} comme vous ne l'avez jamais vu",
            "🏆 Devenez expert en {topic}",
            "🔮 L'avenir de {topic} commence ici",
            "🌍 {topic} : la révolution est en marche",
            "⭐ {topic} : les secrets des pros"
        ]
        
        self.topics = ["fitness", "cuisine", "voyage", "mode", "tech", "lifestyle", "beauté", "business", "art", "musique", "sport", "santé"]
        self.domains = ["vie", "quotidien", "routine", "style", "approche", "vision", "stratégie", "mindset"]
    
    def generate_hook(self, topic=None, domain=None):
        if not topic:
            topic = random.choice(self.topics)
        if not domain:
            domain = random.choice(self.domains)
            
        template = random.choice(self.hooks_templates)
        
        try:
            return template.format(topic=topic, domain=domain)
        except:
            return template.replace("{topic}", topic).replace("{domain}", domain)
    
    def generate_multiple_hooks(self, count=5, topic=None):
        return [self.generate_hook(topic=topic) for _ in range(count)]

# Initialiser le générateur
generator = InstagramHookGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_hooks():
    data = request.get_json()
    topic = data.get('topic', '').strip()
    count = int(data.get('count', 5))
    
    if not topic:
        topic = None
    
    try:
        hooks = generator.generate_multiple_hooks(count=count, topic=topic)
        return jsonify({
            'success': True,
            'hooks': hooks,
            'topic': topic if topic else 'aléatoire'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)