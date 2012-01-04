%global packname  BayesDA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Functions and Datasets for the book "Bayesian Data Analysis"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Functions for Bayesian Data Analysis, with datasets from the book
"Bayesian data Analysis (second edition)" by Gelman, Carlin, Stern and
Rubin. Not all datasets yet, hopefully completed soon.

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
%doc %{rlibdir}/BayesDA/DESCRIPTION
%doc %{rlibdir}/BayesDA/html
%{rlibdir}/BayesDA/Meta
%{rlibdir}/BayesDA/NAMESPACE
%{rlibdir}/BayesDA/INDEX
%{rlibdir}/BayesDA/help
%{rlibdir}/BayesDA/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora