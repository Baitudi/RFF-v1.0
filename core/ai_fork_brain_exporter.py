import torch
import torch.nn as nn

class AIForkBrain(nn.Module):
    def __init__(self):
        super(AIForkBrain, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(10, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 3)  # Outputs: [Up, Down, Wait]
        )

    def forward(self, x):
        return self.network(x)

if __name__ == "__main__":
    model = AIForkBrain()

    # Ensure the models/ directory exists
    import os
    os.makedirs("models", exist_ok=True)

    # Save model to models/
    model_path = "models/ai_fork_brain.pt"
    torch.save(model.state_dict(), model_path)

    print(f"✅ AI Fork Brain model exported to {model_path}")
