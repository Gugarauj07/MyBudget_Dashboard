import { useState, useEffect } from "react";

export const useAuthentication = () => {
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(null);

    // deal with memory leak
    const [cancelled, setCancelled] = useState(false);

    function checkIfIsCancelled() {
    if (cancelled) {
        return;
    }
}

const createUser = async (data) => {
checkIfIsCancelled();

setLoading(true);



setLoading(false);
};

const login = async (data) => {
checkIfIsCancelled();

setLoading(true);
setError(false);

try {
    await signInWithEmailAndPassword(auth, data.email, data.password);
} catch (error) {
    console.log(error.message);
    console.log(typeof error.message);
    console.log(error.message.includes("user-not"));

    let systemErrorMessage;

    if (error.message.includes("user-not-found")) {
    systemErrorMessage = "Usuário não encontrado.";
    } else if (error.message.includes("wrong-password")) {
    systemErrorMessage = "Senha incorreta.";
    } else {
    systemErrorMessage = "Ocorreu um erro, por favor tenta mais tarde.";
    }

    console.log(systemErrorMessage);

    setError(systemErrorMessage);
}

console.log(error);

setLoading(false);
};

useEffect(() => {
return () => setCancelled(true);
}, []);

return {
auth,
createUser,
error,
logout,
login,
loading,
};
};