%global packname  abc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Tools for Approximate Bayesian Computation (ABC)

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-nnet R-quantreg R-locfit 


BuildRequires:    R-devel tex(latex) R-MASS R-nnet R-quantreg R-locfit



%description
The package implements several ABC algorithms for performing parameter
estimation and model selection. Cross-validation tools are also available
for measuring the accuracy of ABC estimates, and to calculate the
misclassification probabilities of different models.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora