%global packname  SemiPar
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Semiparametic Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster R-nlme R-MASS 

BuildRequires:    R-devel tex(latex) R-cluster R-nlme R-MASS 

%description
Functions for semiparametric regression analysis, to complement the book:
Ruppert, D., Wand, M.P. and Carroll, R.J. (2003). Semiparametric
Regression. Cambridge University Press.

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
%doc %{rlibdir}/SemiPar/html
%doc %{rlibdir}/SemiPar/DESCRIPTION
%{rlibdir}/SemiPar/Meta
%{rlibdir}/SemiPar/INDEX
%{rlibdir}/SemiPar/NAMESPACE
%{rlibdir}/SemiPar/help
%{rlibdir}/SemiPar/data
%{rlibdir}/SemiPar/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora