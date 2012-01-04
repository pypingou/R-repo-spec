%global packname  WhatIf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.5
Release:          1%{?dist}
Summary:          WhatIf: Software for Evaluating Counterfactuals

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-lpSolve 

%description
Inferences about counterfactuals are essential for prediction, answering
what if questions, and estimating causal effects. However, when the
counterfactuals posed are too far from the data at hand, conclusions drawn
from well-specified statistical analyses become based largely on
speculation hidden in convenient modeling assumptions that few would be
willing to defend.  Unfortunately, standard statistical approaches assume
the veracity of the model rather than revealing the degree of
model-dependence, which makes this problem hard to detect.  WhatIf offers
easy-to-apply methods to evaluate counterfactuals that do not require
sensitivity testing over specified classes of models.  If an analysis
fails the tests offered here, then we know that substantive inferences
will be sensitive to at least some modeling choices that are not based on
empirical evidence, no matter what method of inference one chooses to use.
 WhatIf implements the methods for evaluating counterfactuals discussed in
Gary King and Langche Zeng, 2006, "The Dangers of Extreme
Counterfactuals," Political Analysis 14 (2); and Gary King and Langche
Zeng, 2007, "When Can History Be Our Guide?  The Pitfalls of
Counterfactual Inference," International Studies Quarterly 51 (March).

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/WhatIf/html
%doc %{rlibdir}/WhatIf/DESCRIPTION
%doc %{rlibdir}/WhatIf/doc
RPM build errors:
%{rlibdir}/WhatIf/help
%{rlibdir}/WhatIf/INDEX
%{rlibdir}/WhatIf/NAMESPACE
%{rlibdir}/WhatIf/Meta
%{rlibdir}/WhatIf/data
%{rlibdir}/WhatIf/demo
%{rlibdir}/WhatIf/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.5-1
- initial package for Fedora