import json

MAX_STEPS = 5

def log_start():
    print("[START]")

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward} done={done}")

def log_end(success, steps, score):
    print(f"[END] success={success} steps={steps} score={score}")

def get_action(step):
    # simple logic
    if step % 2 == 0:
        return {"classification": "real", "severity": 4, "action": "fine"}
    else:
        return {"classification": "unclear", "severity": 3, "action": "ignore"}

def main():
    log_start()
    
    total_reward = 0
    
    for step in range(1, MAX_STEPS + 1):
        action = get_action(step)
        
        # fake reward logic
        reward = 0.7 if action["action"] == "fine" else 0.0
        done = step == MAX_STEPS
        
        total_reward += reward
        
        log_step(step, json.dumps(action), reward, done)
    
    success = total_reward > 1
    log_end(success, MAX_STEPS, total_reward)

if __name__ == "__main__":
    main()