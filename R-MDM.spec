%global packname  MDM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Multinomial Diversity Model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nnet 

BuildRequires:    R-devel tex(latex) R-nnet 

%description
The multinomial diversity model is a toolbox for relating diversity to
complex predictors. It is based on (1) Shannon diversity; (2) the
multinomial logit model, and (3) the link between Shannon diversity and
the log-likelihood of the MLM.

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
%doc %{rlibdir}/MDM/DESCRIPTION
%doc %{rlibdir}/MDM/html
%{rlibdir}/MDM/data
%{rlibdir}/MDM/INDEX
%{rlibdir}/MDM/R
%{rlibdir}/MDM/NAMESPACE
%{rlibdir}/MDM/help
%{rlibdir}/MDM/demo
%{rlibdir}/MDM/Meta

%changelog
* Sat Dec 03 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora