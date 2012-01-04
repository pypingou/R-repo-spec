%global packname  effects
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Effect Displays for Linear, Generalized Linear, Multinomial-Logit, Proportional-Odds Logit Models and mixed-effects models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-grid R-nlme R-MASS R-nnet R-colorspace 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-nlme R-MASS R-nnet R-colorspace 

%description
Graphical and tabular effect displays, e.g., of interactions, for linear
generalized linear, multinomial-logit, and proportional-odds logit models.

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
%doc %{rlibdir}/effects/DESCRIPTION
%doc %{rlibdir}/effects/CITATION
%doc %{rlibdir}/effects/html
%{rlibdir}/effects/Meta
%{rlibdir}/effects/data
%{rlibdir}/effects/R
%{rlibdir}/effects/NAMESPACE
%{rlibdir}/effects/INDEX
%{rlibdir}/effects/CHANGES
%{rlibdir}/effects/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora