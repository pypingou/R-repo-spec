%global packname  stoichcalc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          R Functions for Solving Stoichiometric Equations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Given a list of substance compositions, a list of substances involved in a
process, and a list of constraints in addition to mass conservation of
elementary constituents, the package contains functions to build the
substance composition matrix, to analyze the uniqueness of process
stoichiometry, and to calculate stoichiometric coefficients if process
stoichiometry is unique (see Reichert, P. and Schuwirth, N., A generic
framework for deriving process stoichiometry in environmental models,
Environmental Modelling and Software, in review, 2010 for more details).

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
%doc %{rlibdir}/stoichcalc/CITATION
%doc %{rlibdir}/stoichcalc/DESCRIPTION
%doc %{rlibdir}/stoichcalc/html
%{rlibdir}/stoichcalc/NAMESPACE
%{rlibdir}/stoichcalc/demo
%{rlibdir}/stoichcalc/Meta
%{rlibdir}/stoichcalc/R
%{rlibdir}/stoichcalc/INDEX
%{rlibdir}/stoichcalc/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora